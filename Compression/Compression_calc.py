from .model import *
from utilities.is800_2007 import IS800_2007
from utilities.other_standards import IS1363_part_1_2002, IS1363_part_3_2002, IS1367_Part3_2002
from utilities.common_calculation import *
import math
import logging
import sys
import sqlite3
flag = 1
logger = None
beam_d = 0
beam_B = 0

def module_setup():
    global logger
    logger = logging.getLogger("osdag.Tension_calc")


module_setup()

# Start of Main Program

def compression_design(uiObj):
    global logger
    global design_status
    design_status = True

    # if uiObj['Member']['Location'] == "Web":
    #     conn_type = "Web"
    # elif uiObj['Member']['Location'] == "Flange":
    #     conn_type = "Flange"
    # else:
    #     conn_type = "Leg"
    Member_type = uiObj['Member']['SectionType']
    # Member_type = "Angles"
    Member_size = uiObj['Member']['SectionSize']
    print(Member_size)
    # Member_size = "40 40 x 4"
    
    #*************************************************************
    #Cross_section    type****************************************
    #*************************************************************
    if (Member_type == "Angles" or Member_type == "Back to Back Angles" or Member_type == "Star Angles" or Member_type == "Channels" or Member_type == "Back to Back Channels"):
        Cross_section = 'Channel_Angle_T_Solid_Section'
    else:
        Cross_section = "Rolled_I_Section"
    #*************************************************************



    Member_fu = float(uiObj['Member']['fu (MPa)'])
    f_y = Member_fy = float(uiObj['Member']['fy (MPa)'])
    Member_length = float(uiObj["Member"]["Member_length"])
    P = Compression_load = float(uiObj["Load"]["AxialForce (kN)"])
    if Member_type == "Back to Back Web" or Member_type =="Star Angles" or Member_type == "Back to Back Angles":
        Plate_thickness = float(uiObj["Bolt"]["Platethickness"])
    end1_cond1 = uiObj["Support_Condition"]["end1_cond1"]
    end1_cond2 = uiObj["Support_Condition"]["end1_cond2"]
    end2_cond1 = uiObj["Support_Condition"]["end2_cond1"]
    end2_cond2 = uiObj["Support_Condition"]["end2_cond2"]
    boundary_conditions = [end1_cond1, end1_cond2, end2_cond1, end2_cond2]
    old_beam_section = get_oldbeamcombolist()
    old_column_section = get_oldcolumncombolist()

    if Member_size in old_beam_section or Member_size in old_column_section:
        logger.warning(": You are using a section (in red colour) that is not available in the latest version of IS 808")

    if Member_fu < 410 or Member_fy < 230:
        logger.warning(" : You are using a section of grade that is not available in the latest version of IS 2062")
    
    e = math.sqrt(250/f_y)
    E= 200000
    gamma_m0=1.1

    dictmemberdata = get_memberdata(Member_size,Member_type)
    print(dictmemberdata)

    if Member_type == "Angles" or Member_type == "Back to Back Angles" or Member_type == "Star Angles":
        member_leg = dictmemberdata["AXB"]
        leg = member_leg.split("x")
        leg1 = leg[0]
        leg2 = leg[1]
        t = float(dictmemberdata["t"])

        Member_Ag = float(dictmemberdata["Area"]) * 100
        r= float(dictmemberdata["ru(max)"]) *10
        ry = float(dictmemberdata["rv(min)"]) * 10
        buckling_axis = "v-v"  #(***needs checking)
    else:
        t= t_w = member_tw = float(dictmemberdata["tw"])
        t_f = member_tf = float(dictmemberdata["T"])
        h = member_d = float(dictmemberdata["D"])
        b = b_f = member_B = float(dictmemberdata["B"])
        member_R1= float(dictmemberdata["R1"])
        Member_Ag = float (dictmemberdata["Area"]) * 100
        #radius_gyration = min((float(dictmemberdata["rz"])),(float(dictmemberdata["ry"])))*10
        r= (float(dictmemberdata["rz"])*10)
        ry = radius_gyration = float(dictmemberdata["ry"])*10
        buckling_axis = "y-y"  #(***needs checking)

    if Member_type == "Back to Back Channels":
        Member_Izz = float(dictmemberdata["Iz"])
        Member_Iyy = float(dictmemberdata["Iy"])
        Member_Cy = float(dictmemberdata["Cy"])/10
        Iyy = (Member_Iyy + (Member_Ag/100* (Member_Cy+(Plate_thickness/20))* (Member_Cy+(Plate_thickness/20))))*2
        Izz = 2 * Member_Izz
        I = min(Iyy,Izz)
        radius_gyration = (math.sqrt(I / (Member_Ag/100* 2))) * 10

    if Member_type == "Back to Back Angles":
        Member_Izz = float(dictmemberdata["Iz"])
        Member_Iyy = float(dictmemberdata["Iy"])
        Member_Cy = float(dictmemberdata["Cy"])/10
        Iyy = (Member_Iyy + (Member_Ag/100 * (Member_Cy+(Plate_thickness/20)) *(Member_Cy+(Plate_thickness/20)))) * 2
        Izz = 2 * Member_Izz
        I = min(Iyy, Izz)
        radius_gyration = (math.sqrt(I / (Member_Ag/100* 2))) * 10

    if Member_type == "Star Angles":
        Member_Izz = float(dictmemberdata["Iz"])
        Member_Iyy = float(dictmemberdata["Iy"])
        Member_Cy = float(dictmemberdata["Cy"])/10
        Member_Cz = float(dictmemberdata["Cz"]) / 10
        Iyy = (Member_Iyy + (Member_Ag/100 * (Member_Cy+(Plate_thickness/20)) * (Member_Cy+(Plate_thickness/20)))) * 2
        Izz = (Member_Izz + (Member_Ag/100 * Member_Cz * Member_Cz)) * 2
        I = min(Iyy, Izz)
        radius_gyration = (math.sqrt(I / (Member_Ag/100* 2))) * 10

    # if Member_type == "Back to Back Leg" and Member_type == "Angles":
    #     Member_Izz = float(dictmemberdata["Iz"])
    #     Member_Iyy = float(dictmemberdata["Iy"])
    #     Member_Cy = float(dictmemberdata["Cy"])/10
    #     Iyy = (Member_Iyy + (Member_Ag/100 * Member_Cy * Member_Cy)) * 2
    #     Izz = 2 * Member_Izz
    #     I = min(Iyy, Izz)
    #     radius_gyration = (math.sqrt(I / (Member_Ag/100* 2))) * 10
    #
    # k = IS800_2007.effective_length_coefficeint(end1_cond1, end1_cond2, end2_cond1, end2_cond2)
    # tension_slenderness = IS800_2007.design_check_for_slenderness(k, Member_length, radius_gyration)
    # radius_gyration_min = k * (Member_length) / 400


    #********************************************************************
    #comp calc
    #********************************************************************
    def slenderness_classification (cl_3_7_Table_2,e,r1,b, t_f, d, t_w, t, D, compression_member):
        if cl_3_7_3_class(cl_3_7_Table_2, e, r1, b, t_f, d, t_w, t, D, compression_member)[0] == "class4":
            lamda_l3 = cl_3_7_3_class(cl_3_7_Table_2, e, r1, b, t_f, d, t_w, t, D, compression_member)[1]
            b_eff = lamda_l3*t*e
            print(b_eff)
            return b_eff
            
    #

    def effective_area (cl_3_7_Table_2,e,r1,b,t_f, d,t_w,t,D,compression_member):
        if compression_member[0] == "class4":
            area=slenderness_classification(cl_3_7_Table_2,e,r1,b, t_f, d,t_w,t,D,compression_member)*t
            print(area)
            return area
            
        else: area = Member_Ag


    def effective_length (Member_length,boundary_conditions):
        Leff = IS800_2007.cl_7_2_2_table11_effective_length_of_prismatic_compression_members(Member_length, boundary_conditions)
        print(Leff)
        return Leff
        

    def Buckling_class(Cross_section, t_f, t_w, h, b_f):
        """Return:
                Dictionary of Buckling axis and Buckling class with Buckling axis as key"""
        buckling_class = IS800_2007.cl_7_1_2_2_Table_10_Buckling_class_of_cross_section(Cross_section, t_f, t_w, h, b_f)
        print(buckling_class)
        return buckling_class
        

    def stress_reduction (Cross_section, t_f, t_w, h, b_f,buckling_axis):
        bucking_class = Buckling_class(Cross_section, t_f, t_w, h, b_f)
        alpha = IS800_2007.cl_7_1_Table_7_alpha[bucking_class[buckling_axis]]
        print(alpha)
        return alpha
        


    #   def radius_of_gyration(buckling_axis,dimensions):
    #      """from database """
    #   return r


    def calculate_f_cd (Member_length,Cross_section, t_f, t_w, h, b_f,buckling_axis, E, f_y, r, gamma_m0,boundary_conditions):
        alpha = stress_reduction(Cross_section, t_f, t_w, h, b_f,buckling_axis)
        K_L = effective_length(Member_length, boundary_conditions)
        f_cc = (math.pi ** 2 * E) / ((K_L / r) ** 2)
        f_cd = IS800_2007.cl_7_1_2_1_design_compressive_stress(alpha, f_y,f_cc, gamma_m0)
        print(f_cd)
        return f_cd


    f_cd_z = calculate_f_cd (Member_length, Cross_section, t_f, t_w, h, b_f,buckling_axis, E, f_y, r, gamma_m0,boundary_conditions)
    f_cd_y = calculate_f_cd (Member_length, Cross_section, t_f, t_w, h, b_f,buckling_axis, E, f_y, ry, gamma_m0,boundary_conditions)


    #def design_compressive_strength (cl_3_7_Table_2,e,r1,b, t_f, d,t_w,t,D,compression_member,f_cd):
    #   A_c= effective_area(cl_3_7_Table_2, e, r1, b, t_f, d, t_w, t, D, compression_member)
    #    p_d= A_c*f_cd
    #   return (p_d)

    """design_checks
    P= External Load P"""
    compression_design_zz = float(f_cd_z * Member_Ag  )
    compression_design_yy = float(f_cd_y * Member_Ag  )


    def design_check():
        if (f_cd*Member_Ag)> P:
            print("safe design")
        else:
            print("unsafe")


    def slenderness_check(L,boundary_conditions,r):
        slenderness_zz = effective_length(L,boundary_conditions)/r
        slenderness_yy = effective_length(L,boundary_conditions)/ry
        if max(slenderness_zz, slenderness_yy) > 180:
            return "TOO SLENDER SECTION"
        else:
            return
    #***********************************************************************








        # compression_design_zz = 100
        # compression_design_yy = 50
        # slenderness_zz = 100
        # slenderness_yy = 160
        utility_ratio_zz = float(P/compression_design_zz)
        utility_ratio_yy = float(P/compression_design_yy)

    # End of Calculation, SAMPLE Output dictionary
        outputobj = dict()

        # FOR OUTPUT DOCK
        outputobj['Compression_Force'] = {}

        outputobj['Compression_Force']['Capacity_zz'] = float(round(compression_design_zz,3))
        outputobj['Compression_Force']['Capacity_yy'] = float(round(compression_design_yy, 3))
        outputobj['Compression_Force']['Slenderness_zz'] = float(round(slenderness_zz,3))
        outputobj['Compression_Force']['Slenderness_yy'] = float(round((slenderness_yy),3))
        outputobj['Compression_Force']['Efficiency_zz'] = float(round(utility_ratio_zz,3))
        outputobj['Compression_Force']['Efficiency_yy'] = float(round(utility_ratio_yy,3))


        # for i,j in uiObj.items():
        #     if j == " ":
        #         logger.error(": Please enter all the inputs")
        #     else:
        #         pass

        if outputobj['Compression_Force']['Efficiency_zz']< 1 and outputobj['Compression_Force']['Slenderness_zz'] < 400:
            design_status = True
        elif outputobj['Compression_Force']['Efficiency_zz']> 1 and outputobj['Compression_Force']['Slenderness_zz'] < 400:
            design_status = False
            logger.error(": Chosen Member Section Size is not sufficient")
            logger.info(": Increase the size of Member ")
        elif outputobj['Compression_Force']['Efficiency_zz']< 1 and outputobj['Compression_Force']['Slenderness_zz']> 400:
            design_status = False
            logger.error(": Chosen Member Section Size is not sufficient")
            logger.warning(": Minimum Radius of Gyration of Member shall be {} mm ".format(radius_gyration_min))
            logger.info(": Increase the size of Member ")

        if outputobj['Compression_Force']['Efficiency_yy']< 1 and outputobj['Compression_Force']['Slenderness_yy'] < 400:
            design_status = True
        elif outputobj['Compression_Force']['Efficiency_yy']> 1 and outputobj['Compression_Force']['Slenderness_yy'] < 400:
            design_status = False
            logger.error(": Chosen Member Section Size is not sufficient")
            logger.info(": Increase the size of Member ")
        elif outputobj['Compression_Force']['Efficiency_yy']< 1 and outputobj['Compression_Force']['Slenderness_yy']> 400:
            design_status = False
            logger.error(": Chosen Member Section Size is not sufficient")
            logger.warning(": Minimum Radius of Gyration of Member shall be {} mm ".format(radius_gyration_min))
            logger.info(": Increase the size of Member ")

        if design_status is True:
            logger.info(":Member is safe for the applied tension load \n")
            logger.info(":In case of reversal load, Slenderness value shall be less than 180 \n")
            logger.debug(" :=========End Of design===========")
        else:
            logger.error(":Member fails for the applied tension load \n ")
            logger.debug(" :=========End Of design===========")

        return outputobj