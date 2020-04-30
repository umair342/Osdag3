from design_type.connection.moment_connection import MomentConnection
from utils.common.component import *
from utils.common.is800_2007 import *
from Common import *
from design_report.reportGenerator_latex import CreateLatex
from Report_functions import *

from utils.common.load import Load
import yaml
import os
import shutil
import logging
from PyQt5.QtWidgets import QMainWindow, QDialog, QFontDialog, QApplication, QFileDialog, QColorDialog,QMessageBox





class ColumnCoverPlate(MomentConnection):

    def __init__(self):
        super(ColumnCoverPlate, self).__init__()
        self.design_status = False

    def set_osdaglogger(key):
        global logger
        logger = logging.getLogger('osdag')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler = OurLog(key)
        handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def input_values(self, existingvalues={}):

        options_list = []

        if KEY_CONN in existingvalues:
            existingvalue_key_conn = existingvalues[KEY_CONN]
        else:
            existingvalue_key_conn = ''

        if KEY_SECSIZE in existingvalues:
            existingvalue_key_secsize = existingvalues[KEY_SECSIZE]
        else:
            existingvalue_key_secsize = ''

        if KEY_MATERIAL in existingvalues:
            existingvalue_key_mtrl = existingvalues[KEY_MATERIAL]
        else:
            existingvalue_key_mtrl = ''

        if KEY_MOMENT in existingvalues:
            existingvalues_key_moment = existingvalues[KEY_MOMENT]
        else:
            existingvalues_key_moment = ''

        if KEY_SHEAR in existingvalues:
            existingvalue_key_versh = existingvalues[KEY_SHEAR]
        else:
            existingvalue_key_versh = ''

        if KEY_AXIAL in existingvalues:
            existingvalue_key_axial = existingvalues[KEY_AXIAL]
        else:
            existingvalue_key_axial = ''

        if KEY_D in existingvalues:
            existingvalue_key_d = existingvalues[KEY_D]
        else:
            existingvalue_key_d = ''

        if KEY_TYP in existingvalues:
            existingvalue_key_typ = existingvalues[KEY_TYP]
        else:
            existingvalue_key_typ = ''

        if KEY_GRD in existingvalues:
            existingvalue_key_grd = existingvalues[KEY_GRD]
        else:
            existingvalue_key_grd = ''

        if KEY_FLANGEPLATE_PREFERENCES in existingvalues:
            existingvalue_key_fplate_pref = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_pref = ''

        if KEY_FLANGEPLATE_THICKNESS in existingvalues:
            existingvalue_key_fplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_fplate_thk = ''

        if KEY_WEBPLATE_THICKNESS in existingvalues:
            existingvalue_key_wplate_thk = existingvalues[KEY_PLATETHK]
        else:
            existingvalue_key_wplate_thk = ''

        t16 = (KEY_MODULE, KEY_DISP_COLUMNCOVERPLATE, TYPE_MODULE, None, None)
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, None)
        options_list.append(t1)

        t4 = (KEY_SECSIZE, KEY_DISP_SECSIZE, TYPE_COMBOBOX, existingvalue_key_secsize, connectdb("Columns"))
        options_list.append(t4)

        t15 = (KEY_IMAGE, None, TYPE_IMAGE, None, None)
        options_list.append(t15)

        t5 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, existingvalue_key_mtrl, VALUES_MATERIAL)
        options_list.append(t5)

        t6 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, None)
        options_list.append(t6)

        t17 = (KEY_MOMENT, KEY_DISP_MOMENT, TYPE_TEXTBOX,existingvalues_key_moment,None)
        options_list.append(t17)

        t7 = (KEY_SHEAR, KEY_DISP_SHEAR, TYPE_TEXTBOX, existingvalue_key_versh, None)
        options_list.append(t7)

        t8 = (KEY_AXIAL, KEY_DISP_AXIAL, TYPE_TEXTBOX, existingvalue_key_axial, None)
        options_list.append(t8)

        t9 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None, None)
        options_list.append(t9)

        t10 = (KEY_D, KEY_DISP_D, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_d, VALUES_D)
        options_list.append(t10)

        t11 = (KEY_TYP, KEY_DISP_TYP, TYPE_COMBOBOX, existingvalue_key_typ, VALUES_TYP)
        options_list.append(t11)

        t12 = (KEY_GRD, KEY_DISP_GRD, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_grd, VALUES_GRD)
        options_list.append(t12)

        t18 = (None, DISP_TITLE_FLANGESPLICEPLATE, TYPE_TITLE, None, None)
        options_list.append(t18)

        t19 = (KEY_FLANGEPLATE_PREFERENCES, KEY_DISP_FLANGESPLATE_PREFERENCES, TYPE_COMBOBOX, existingvalue_key_fplate_pref, VALUES_FLANGEPLATE_PREFERENCES)
        options_list.append(t19)

        t20 = (KEY_FLANGEPLATE_THICKNESS, KEY_DISP_FLANGESPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_fplate_thk, VALUES_FLANGEPLATE_THICKNESS)
        options_list.append(t20)

        t21 = (None, DISP_TITLE_WEBSPLICEPLATE, TYPE_TITLE, None, None)
        options_list.append(t21)

        t22 = (KEY_WEBPLATE_THICKNESS, KEY_DISP_WEBPLATE_THICKNESS, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_wplate_thk, VALUES_WEBPLATE_THICKNESS)
        options_list.append(t22)


        # t13 = (None, DISP_TITLE_PLATE, TYPE_TITLE, None, None)
        # options_list.append(t13)
        #
        # t14 = (KEY_PLATETHK, KEY_DISP_PLATETHK, TYPE_COMBOBOX_CUSTOMIZED, existingvalue_key_platethk, VALUES_PLATETHK)
        # options_list.append(t14)

        return options_list

    def customized_input(self):

        list1 = []
        t1 = (KEY_GRD, self.grdval_customized)
        list1.append(t1)
        t3 = (KEY_D, self.diam_bolt_customized)
        list1.append(t3)
        t4 = (KEY_WEBPLATE_THICKNESS, self.plate_thick_customized)
        list1.append(t4)
        t5 = (KEY_FLANGEPLATE_THICKNESS, self.plate_thick_customized)
        list1.append(t5)

        return list1

    def flangespacing(self, flag):

        flangespacing = []

        t21 = (KEY_FLANGE_PITCH, KEY_DISP_FLANGE_PLATE_PITCH, TYPE_TEXTBOX,
               self.flange_plate.pitch_provided)
        flangespacing.append(t21)

        t22 = (KEY_ENDDIST_FLANGE, KEY_DISP_END_DIST_FLANGE, TYPE_TEXTBOX,
               self.flange_plate.end_dist_provided)
        flangespacing.append(t22)

        t23 = (KEY_FLANGE_PLATE_GAUGE, KEY_DISP_FLANGE_PLATE_GAUGE, TYPE_TEXTBOX,
               self.flange_plate.gauge_provided)
        flangespacing.append(t23)

        t24 = (KEY_EDGEDIST_FLANGE, KEY_DISP_EDGEDIST_FLANGE, TYPE_TEXTBOX,
               self.flange_plate.edge_dist_provided)
        flangespacing.append(t24)
        return flangespacing
        #

    def webspacing(self, flag):

        webspacing = []

        t8 = (KEY_WEB_PITCH, KEY_DISP_WEB_PLATE_PITCH, TYPE_TEXTBOX, self.web_plate.pitch_provided if flag else '')
        webspacing.append(t8)

        t9 = (KEY_ENDDIST_W, KEY_DISP_END_DIST_W, TYPE_TEXTBOX,
              self.web_plate.end_dist_provided if flag else '')
        webspacing.append(t9)

        t10 = (KEY_WEB_GAUGE, KEY_DISP_WEB_PLATE_GAUGE, TYPE_TEXTBOX, self.web_plate.gauge_provided if flag else '')
        webspacing.append(t10)

        t11 = (KEY_EDGEDIST_W, KEY_DISP_EDGEDIST_W, TYPE_TEXTBOX,
               self.web_plate.edge_dist_provided if flag else '')
        webspacing.append(t11)
        return webspacing
        #

    def flangecapacity(self, flag):

        flangecapacity = []

        t30 = (KEY_FLANGE_TEN_CAPACITY, KEY_DISP_FLANGE_TEN_CAPACITY, TYPE_TEXTBOX,
               round(self.section.tension_capacity_flange / 1000, 2) if flag else '')
        flangecapacity.append(t30)
        t30 = (KEY_FLANGE_PLATE_TEN_CAP, KEY_DISP_FLANGE_PLATE_TEN_CAP, TYPE_TEXTBOX,
               round(self.flange_plate.tension_capacity_flange_plate / 1000, 2) if flag else '')
        flangecapacity.append(t30)
        #
        # t30= (KEY_TENSIONYIELDINGCAP_FLANGE, KEY_DISP_TENSIONYIELDINGCAP_FLANGE, TYPE_TEXTBOX,
        #        round(self.flange_plate.tension_yielding_capacity/1000, 2) if flag else '')
        # flangecapacity.append(t30)
        #
        # t31 = (KEY_TENSIONRUPTURECAP_FLANGE,KEY_DISP_TENSIONRUPTURECAP_FLANGE , TYPE_TEXTBOX,
        #        round(self.flange_plate.tension_rupture_capacity/1000, 2) if flag else '')
        # flangecapacity.append(t31)
        #
        # # t25 = (KEY_SHEARYIELDINGCAP_FLANGE, KEY_DISP_SHEARYIELDINGCAP_FLANGE, TYPE_TEXTBOX,
        # #        round(self.flange_plate.shear_yielding_capacity/1000, 2) if flag else '')
        # # flangecapacity.append(t25)
        #
        # t26 = (KEY_BLOCKSHEARCAP_FLANGE, KEY_DISP_BLOCKSHEARCAP_FLANGE, TYPE_TEXTBOX,
        #        round(self.flange_plate.block_shear_capacity/1000, 2) if flag else '')
        # flangecapacity.append(t26)
        #
        # # t27 = ( KEY_SHEARRUPTURECAP_FLANGE,KEY_DISP_SHEARRUPTURECAP_FLANGE,TYPE_TEXTBOX,
        # #        round(self.flange_plate.shear_rupture_capacity/1000, 2) if flag else '')
        # # flangecapacity.append(t27)

        t28 = (KEY_FLANGE_PLATE_MOM_DEMAND, KEY_FLANGE_DISP_PLATE_MOM_DEMAND, TYPE_TEXTBOX,
               round(self.flange_plate.moment_demand / 1000000, 2) if flag else '')
        flangecapacity.append(t28)

        t29 = (KEY_FLANGE_PLATE_MOM_CAPACITY, KEY_FLANGE_DISP_PLATE_MOM_CAPACITY, TYPE_TEXTBOX,
               round(self.flange_plate.moment_capacity / 1000, 2) if flag else '')
        flangecapacity.append(t29)

        return flangecapacity

    def webcapacity(self, flag):

        webcapacity = []
        t30 = (KEY_WEB_TEN_CAPACITY, KEY_DISP_WEB_TEN_CAPACITY, TYPE_TEXTBOX,
               round(self.section.tension_capacity_web / 1000, 2) if flag else '')
        webcapacity.append(t30)
        t30 = (KEY_TEN_CAP_WEB_PLATE, KEY_DISP_TEN_CAP_WEB_PLATE, TYPE_TEXTBOX,
               round(self.web_plate.tension_capacity_web_plate / 1000, 2) if flag else '')
        webcapacity.append(t30)
        t30 = (KEY_WEBPLATE_SHEAR_CAPACITY, KEY_DISP_WEBPLATE_SHEAR_CAPACITY, TYPE_TEXTBOX,
               round(self.web_plate.shear_capacity_web_plate / 1000, 2) if flag else '')
        webcapacity.append(t30)

        # t30 = (KEY_TENSIONYIELDINGCAP_WEB, KEY_DISP_TENSIONYIELDINGCAP_WEB, TYPE_TEXTBOX,
        #        round(self.web_plate.tension_yielding_capacity / 1000, 2) if flag else '')
        # webcapacity.append(t30)
        #
        # t31 = (KEY_TENSIONRUPTURECAP_WEB, KEY_DISP_TENSIONRUPTURECAP_WEB, TYPE_TEXTBOX,
        #        round(self.web_plate.tension_rupture_capacity / 1000, 2) if flag else '')
        # webcapacity.append(t31)
        #
        # t12 = (KEY_SHEARYIELDINGCAP_WEB, KEY_DISP_SHEARYIELDINGCAP_WEB, TYPE_TEXTBOX,
        #        round(self.web_plate.shear_yielding_capacity/1000, 2) if flag else '')
        # webcapacity.append(t12)
        #
        # t13 = (KEY_BLOCKSHEARCAP_WEB, KEY_DISP_BLOCKSHEARCAP_WEB, TYPE_TEXTBOX,
        #        round(self.web_plate.block_shear_capacity/1000, 2) if flag else '')
        # webcapacity.append(t13)
        #
        # t14 = (KEY_SHEARRUPTURECAP_WEB, KEY_DISP_SHEARRUPTURECAP_WEB, TYPE_TEXTBOX,
        #        round(self.web_plate.shear_rupture_capacity/1000, 2) if flag else '')
        # webcapacity.append(t14)

        t15 = (KEY_WEB_PLATE_MOM_DEMAND, KEY_WEB_DISP_PLATE_MOM_DEMAND, TYPE_TEXTBOX,
               round(self.web_plate.moment_demand / 1000000, 2) if flag else '')
        webcapacity.append(t15)

        t16 = (KEY_WEB_PLATE_MOM_CAPACITY, KEY_WEB_DISP_PLATE_MOM_CAPACITY, TYPE_TEXTBOX,
               round(self.web_plate.moment_capacity / 1000, 2) if flag else '')
        webcapacity.append(t16)
        return webcapacity

    def Innerplate(self, flag):
        Innerplate = []

        # t17 = (None, DISP_TITLE_INNERFLANGESPLICEPLATE, TYPE_TITLE, None)
        # Innerplate.append(t17)

        t18 = (KEY_INNERFLANGE_PLATE_HEIGHT, KEY_DISP_INNERFLANGE_PLATE_HEIGHT, TYPE_TEXTBOX,
               self.flange_plate.Innerheight if flag else '')
        Innerplate.append(t18)

        t19 = (
            KEY_INNERFLANGE_PLATE_LENGTH, KEY_DISP_INNERFLANGE_PLATE_LENGTH, TYPE_TEXTBOX,
            self.flange_plate.Innerlength if flag else '')
        Innerplate.append(t19)

        t20 = (KEY_INNERFLANGEPLATE_THICKNESS, KEY_DISP_INNERFLANGESPLATE_THICKNESS, TYPE_TEXTBOX,
               self.flange_plate.thickness_provided if flag else '')
        Innerplate.append(t20)
        return Innerplate

    def boltdetails(self, flag):

        boltdetails = []
        t16 = (KEY_FLANGE_BOLT_LINE, KEY_FLANGE_DISP_BOLT_LINE, TYPE_TEXTBOX,
               round(self.flange_plate.bolt_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_FLANGE_BOLTS_ONE_LINE, KEY_FLANGE_DISP_BOLTS_ONE_LINE, TYPE_TEXTBOX,
               round(self.flange_plate.bolts_one_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_FLANGE_BOLTS_REQ, KEY_FLANGE_DISP_BOLTS_REQ, TYPE_TEXTBOX,
               round(self.flange_plate.bolts_required) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLT_LINE, KEY_WEB_DISP_BOLT_LINE, TYPE_TEXTBOX,
               round(self.web_plate.bolt_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLTS_ONE_LINE, KEY_WEB_DISP_BOLTS_ONE_LINE, TYPE_TEXTBOX,
               round(self.web_plate.bolts_one_line) if flag else '')
        boltdetails.append(t16)

        t16 = (KEY_WEB_BOLTS_REQ, KEY_WEB_DISP_BOLTS_REQ, TYPE_TEXTBOX,
               round(self.web_plate.bolts_required) if flag else '')
        boltdetails.append(t16)

        return boltdetails

    def output_values(self, flag):

        out_list = []

        t1 = (None, DISP_TITLE_BOLT, TYPE_TITLE, None)
        out_list.append(t1)

        t2 = (KEY_D, KEY_OUT_DISP_D_PROVIDED, TYPE_TEXTBOX,
              self.web_bolt.bolt_diameter_provided if flag else '')
        out_list.append(t2)

        t3 = (KEY_GRD, KEY_DISP_GRD, TYPE_TEXTBOX,
              self.web_bolt.bolt_grade_provided if flag else '')
        out_list.append(t3)

        t4 = (None, DISP_TITLE_BOLTDETAILS, TYPE_TITLE, None)
        out_list.append(t4)

        t21 = (
            KEY_BOLT_DETAILS, KEY_DISP_BOLT_DETAILS, TYPE_OUT_BUTTON, ['Bolt details', self.boltdetails])
        out_list.append(t21)

        t4 = (None, DISP_TITLE_WEBSPLICEPLATE, TYPE_TITLE, None)
        out_list.append(t4)

        t5 = (KEY_WEB_PLATE_HEIGHT, KEY_DISP_WEB_PLATE_HEIGHT, TYPE_TEXTBOX,
              self.web_plate.height if flag else '')
        out_list.append(t5)

        t6 = (KEY_WEB_PLATE_LENGTH, KEY_DISP_WEB_PLATE_LENGTH, TYPE_TEXTBOX,
              self.web_plate.length if flag else '')
        out_list.append(t6)

        t7 = (KEY_WEBPLATE_THICKNESS, KEY_DISP_WEBPLATE_THICKNESS, TYPE_TEXTBOX,
              self.web_plate.thickness_provided if flag else '')
        out_list.append(t7)

        t21 = (KEY_WEB_SPACING, KEY_DISP_WEB_SPACING, TYPE_OUT_BUTTON, ['Web Spacing Details (mm)', self.webspacing])
        out_list.append(t21)

        t21 = (KEY_WEB_CAPACITY, KEY_DISP_WEB_CAPACITY, TYPE_OUT_BUTTON, ['Web Capacity', self.webcapacity])
        out_list.append(t21)

        t17 = (None, DISP_TITLE_FLANGESPLICEPLATE, TYPE_TITLE, None)
        out_list.append(t17)

        t18 = (KEY_FLANGE_PLATE_HEIGHT, KEY_DISP_FLANGE_PLATE_HEIGHT, TYPE_TEXTBOX,
               self.flange_plate.height if flag else '')
        out_list.append(t18)

        t19 = (
            KEY_FLANGE_PLATE_LENGTH, KEY_DISP_FLANGE_PLATE_LENGTH, TYPE_TEXTBOX,
            self.flange_plate.length if flag else '')
        out_list.append(t19)

        t20 = (KEY_FLANGEPLATE_THICKNESS, KEY_DISP_FLANGESPLATE_THICKNESS, TYPE_TEXTBOX,
               self.flange_plate.thickness_provided if flag else '')
        out_list.append(t20)
        t21 = (
            KEY_FLANGE_SPACING, KEY_DISP_FLANGE_SPACING, TYPE_OUT_BUTTON,
            ['Flange Spacing Details', self.flangespacing])
        out_list.append(t21)

        t21 = (
            KEY_FLANGE_CAPACITY, KEY_DISP_FLANGE_CAPACITY, TYPE_OUT_BUTTON, ['Flange Capacity', self.flangecapacity])
        out_list.append(t21)
        t21 = (KEY_INNERPLATE, DISP_TITLE_INNERFLANGESPLICEPLATE, TYPE_OUT_BUTTON, ['Inner Plate Details (mm)', self.Innerplate])
        out_list.append(t21)

        # t21 = (
        #     KEY_BOLT_DETAILS, KEY_DISP_BOLT_DETAILS, TYPE_OUT_BUTTON, ['Bolt details', self.boltdetails])
        # out_list.append(t21)



        return out_list

    def func_for_validation(self, window, design_dictionary):
        self.design_status = False
        flag = False

        option_list = self.input_values(self)
        missing_fields_list = []
        for option in option_list:
            if option[2] == TYPE_TEXTBOX:
                if design_dictionary[option[0]] == '':
                    missing_fields_list.append(option[1])
            elif option[2] == TYPE_COMBOBOX and option[0] != KEY_CONN:
                val = option[4]
                if design_dictionary[option[0]] == val[0]:
                    missing_fields_list.append(option[1])

        if len(missing_fields_list) > 0:
            QMessageBox.information(window, "Information",
                                    self.generate_missing_fields_error_string(self, missing_fields_list))
            # flag = False
        else:
            flag = True

        if flag:
            self.set_input_values(self, design_dictionary)
        else:
            pass

    def warn_text(self):

        """
        Function to give logger warning when any old value is selected from Column and column table.
        """

        # @author Arsil Zunzunia
        global logger
        red_list = red_list_function()
        if self.section.designation in red_list or self.section.designation in red_list:
            logger.warning(
                " : You are using a section (in red color) that is not available in latest version of IS 808")
            logger.info(
                " : You are using a section (in red color) that is not available in latest version of IS 808")

        # for option in option_list:
        #     if option[0] == KEY_CONN:
        #         continue
        #     s = p.findChild(QtWidgets.QWidget, option[0])
        #
        #     if option[2] == TYPE_COMBOBOX:
        #         if option[0] in [KEY_D, KEY_GRD, KEY_PLATETHK]:
        #             continue
        #         if s.currentIndex() == 0:
        #             missing_fields_list.append(option[1])
        #
        #
        #     elif option[2] == TYPE_TEXTBOX:
        #         if s.text() == '':
        #             missing_fields_list.append(option[1])
        #     else:
        #         pass

    def generate_missing_fields_error_string(self, missing_fields_list):
        """
        Args:
            missing_fields_list: list of fields that are not selected or entered
        Returns:
            error string that has to be displayed
        """
        # The base string which should be displayed
        information = "Please input the following required field"
        if len(missing_fields_list) > 1:
            # Adds 's' to the above sentence if there are multiple missing input fields
            information += "s"
        information += ": "
        # Loops through the list of the missing fields and adds each field to the above sentence with a comma

        for item in missing_fields_list:
            information = information + item + ", "

        # Removes the last comma
        information = information[:-2]
        information += "."

        return information

    def module_name(self):

        return KEY_DISP_COLUMNCOVERPLATE

    def set_input_values(self, design_dictionary):
        super(ColumnCoverPlate, self).set_input_values(self, design_dictionary)
        # self.module = design_dictionary[KEY_MODULE]
        # global design_status
        # self.design_status = False # todo doubt of true or false
        #
        self.module = design_dictionary[KEY_MODULE]
        # self.connectivity = design_dictionary[KEY_CONN]
        self.preference = design_dictionary[KEY_FLANGEPLATE_PREFERENCES]

        self.section = Column(designation=design_dictionary[KEY_SECSIZE],
                            material_grade=design_dictionary[KEY_MATERIAL])
        print("anjali", design_dictionary[KEY_DP_DETAILING_EDGE_TYPE])
        self.web_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                             bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                             bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                             edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],

                             mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                             corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])

        self.bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                         bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                         bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                         edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                         mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                         corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])
        self.flange_bolt = Bolt(grade=design_dictionary[KEY_GRD], diameter=design_dictionary[KEY_D],
                                bolt_type=design_dictionary[KEY_TYP], material_grade=design_dictionary[KEY_MATERIAL],
                                bolt_hole_type=design_dictionary[KEY_DP_BOLT_HOLE_TYPE],
                                edge_type=design_dictionary[KEY_DP_DETAILING_EDGE_TYPE],
                                mu_f=design_dictionary[KEY_DP_BOLT_SLIP_FACTOR],
                                corrosive_influences=design_dictionary[KEY_DP_DETAILING_CORROSIVE_INFLUENCES])

        self.flange_plate = Plate(thickness=design_dictionary.get(KEY_FLANGEPLATE_THICKNESS, None),
                                  material_grade=design_dictionary[KEY_MATERIAL],
                                  gap=design_dictionary[KEY_DP_DETAILING_GAP])
        # self.plate = Plate(thickness=design_dictionary.get(KEY_FLANGEPLATE_THICKNESS, None),
        #                           material_grade=design_dictionary[KEY_MATERIAL],
        #                           gap=design_dictionary[KEY_DP_DETAILING_GAP])
        self.web_plate = Plate(thickness=design_dictionary.get(KEY_WEBPLATE_THICKNESS, None),
                               material_grade=design_dictionary[KEY_MATERIAL],
                               gap=design_dictionary[KEY_DP_DETAILING_GAP])
    

        self.member_capacity(self)
        # self.hard_values(self)

    def hard_values(self):
        #section HB 450* bearing outside-inside  material E 250 fe 450A bearing
        # flange bolt
        # load
        self.load.axial_force = 740.181  # KN
        self.load.shear_force = 345.886  # KN
        self.load.moment = 52.745157  # KNM
        self.section.fy = 230
        self.section.fu = 410
        self.flange_bolt.bolt_type = "Bearing Bolt"
        self.flange_bolt.connecting_plates_tk = None
        self.flange_bolt.bolt_grade_provided = 4.6
        self.flange_bolt.bolt_diameter_provided = 20
        self.flange_bolt.dia_hole = 22


        # web bolt
        self.web_bolt.bolt_type = "Bearing Bolt"
        self.web_bolt.connecting_plates_tk = None
        self.web_bolt.bolt_grade_provided = 4.6
        self.web_bolt.bolt_diameter_provided = 20
        self.web_bolt.dia_hole = 22


        # flange plate
        self.flange_plate.thickness_provided = 8
        self.flange_plate.height = 250
        self.flange_plate.length = 270
        self.flange_plate.bolt_line = 4
        self.flange_plate.bolts_one_line = 2
        self.flange_plate.bolts_required = 8
        self.flange_plate.pitch_provided = 50
        self.flange_plate.gauge_provided = 0.0
        self.flange_plate.edge_dist_provided = 40
        self.flange_plate.end_dist_provided =40

        # web plate
        self.web_plate.thickness_provided =12
        self.web_plate.height = 380
        self.web_plate.length = 270
        self.web_plate.bolt_line = 4
        self.web_plate.bolts_one_line = 5
        self.web_plate.bolts_required = 20
        self.web_plate.pitch_provided = 50
        self.web_plate.gauge_provided = 75
        self.web_plate.edge_dist_provided = 40
        self.web_plate.end_dist_provided = 40
        #  Inner Flange plate
        self.flange_plate.thickness_provided = 8
        self.flange_plate.Innerheight = 104.35
        self.flange_plate.Innerlength = 270
        self.flange_plate.gap = 10
        self.web_plate.gap = 10

        self.flange_plate.midgauge = 121.3
        self.web_plate.midpitch = 90
        self.flange_plate.midpitch = 90

        #
        # self.web_plate.moment_capacity = 0
        self.design_status = True

    def member_capacity(self):

        if self.section.type == "Rolled":
            length = self.section.depth
        else:
            length = self.section.depth - (
                    2 * self.section.flange_thickness)  # -(2*self.supported_section.root_radius)
        #     else:
        #         length = self.supported_section.depth - 50.0  # TODO: Subtract notch height for beam-beam connection

        gamma_m0 = 1.1
        # Axial Capacity
        self.axial_capacity = (self.section.area * self.section.fy) / gamma_m0  # N
        self.min_axial_load = 0.3 * self.axial_capacity
        self.factored_axial_load = max(self.load.axial_force * 1000, self.min_axial_load)  # N
        if self.factored_axial_load > self.axial_capacity:
            self.factored_axial_load = self.axial_capacity
        else:
            pass
        # self.load.axial_force = self.factored_axial_load #N
        print("self.factored_axial_load", self.factored_axial_load)

        # Shear Capacity  # N
        self.shear_capacity1 = ((self.section.depth - (
                    2 * self.section.flange_thickness)) * self.section.web_thickness * self.section.fy) / (
                                       math.sqrt(
                                           3) * gamma_m0)  # N # A_v: Total cross sectional area in shear in mm^2 (float)
        self.shear_load1 = 0.6 * self.shear_capacity1  # N
        self.fact_shear_load = max(self.shear_load1, self.load.shear_force * 1000)  # N
        if self.fact_shear_load > self.shear_capacity1:
            self.fact_shear_load = self.shear_capacity1
        else:
            pass
        # self.load.shear_force = self.fact_shear_load  #N
        print('shear_force', self.load.shear_force)

        self.Z_p = round(((self.section.web_thickness * (
                self.section.depth - 2 * (self.section.flange_thickness)) ** 2) / 4), )  # mm3
        self.Z_e = round(((self.section.web_thickness * (
                self.section.depth - 2 * (self.section.flange_thickness)) ** 2) / 6), 2)  # mm3
        if self.section.type == "Rolled":

            self.limitwidththkratio_flange = self.limiting_width_thk_ratio(column_f_t=self.section.flange_thickness,
                                                                           column_t_w=self.section.web_thickness,
                                                                           column_d=self.section.depth,
                                                                           column_b=self.section.flange_width,
                                                                           column_fy=self.section.fy,
                                                                           factored_axial_force=self.factored_axial_load,
                                                                           column_area=self.section.area,
                                                                           compression_element="External",
                                                                           section="Rolled")
            print("limitwidththkratio_flange", self.limitwidththkratio_flange)
        else:
            pass

        if self.section.type2 == "generally":

            self.limitwidththkratio_web = self.limiting_width_thk_ratio(column_f_t=self.section.flange_thickness,
                                                                        column_t_w=self.section.web_thickness,
                                                                        column_d=self.section.depth,
                                                                        column_b=self.section.flange_width,
                                                                        column_fy=self.section.fy,
                                                                        factored_axial_force=self.factored_axial_load,
                                                                        column_area=self.section.area,
                                                                        compression_element="Web of an I-H",
                                                                        section="generally")
        else:
            pass

        self.class_of_section = int(max(self.limitwidththkratio_flange, self.limitwidththkratio_web))
        if self.class_of_section == 1 or self.class_of_section == 2:
            Z_w = self.Z_p
        elif self.class_of_section == 3:
            Z_w = self.Z_e

        if self.class_of_section == 1 or self.class_of_section == 2:
            self.beta_b = 1
        elif self.class_of_section == 3:
            self.beta_b = self.Z_e / self.Z_p

        self.section.plastic_moment_capacty(beta_b=self.beta_b, Z_p=self.Z_p,
                                            fy=self.section.fy)  # N # for section #todo add in ddcl
        self.section.moment_d_deformation_criteria(fy=self.section.fy, Z_e=self.section.elast_sec_mod_z)
        # todo add in ddcl
        self.Pmc = self.section.plastic_moment_capactiy
        self.Mdc = self.section.moment_d_def_criteria
        self.section.moment_capacity = min(self.section.plastic_moment_capactiy, self.section.moment_d_def_criteria)
        print("moment_capacity", self.section.moment_capacity)
        self.load_moment_min = 0.5 * self.section.moment_capacity
        self.load_moment = max(self.load_moment_min, self.load.moment * 1000000)  # N
        if self.load_moment > self.section.moment_capacity:
            self.load_moment = self.section.moment_capacity
        else:
            pass
        # self.load.moment = load_moment # N
        print("design_bending_strength", self.load.moment)

        print("self.load_moment", self.load_moment)
        print("self.load_moment_min", self.load_moment_min)

        self.moment_web = (Z_w * self.load_moment / (
            self.section.plast_sec_mod_z))  # Nm todo add in ddcl # z_w of web & z_p  of section
        print('plast_sec_mod_z', self.section.plast_sec_mod_z)
        print("Z_W", Z_w)
        print("web moment", self.moment_web)
        self.moment_flange = ((self.load_moment) - self.moment_web)  # Nmm #Nmm todo add in ddcl
        print("moment_flange", self.moment_flange)

        ###WEB MENBER CAPACITY CHECK

        ###### # capacity Check for web in axial = min(block, yielding, rupture)
        self.axial_force_w = ((self.section.depth - (
                2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                 self.section.area)  # N

        # A_vn_web = ( self.section.depth - 2 * self.section.flange_thickness - self.web_plate.bolts_one_line * self.web_bolt.dia_hole) * self.section.web_thickness
        A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness
        self.tension_yielding_capacity_web = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web, fy=self.section.fy)

        print("tension_yielding_capacity_web", self.tension_yielding_capacity_web)

        if self.tension_yielding_capacity_web > self.axial_force_w:

            self.section.tension_yielding_capacity = self.tension_yielding_capacity_web
            # print("tension_yielding_capacity of web", self.section.tension_yielding_capacity)
            ### FLANGE MEMBER CAPACITY CHECK
            self.axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
                self.section.area)  # N
            self.flange_force = (
                    ((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
                self.axial_force_f))
            # A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole) * \
            #               self.section.flange_thickness
            A_v_flange = self.section.flange_thickness * self.section.flange_width

            self.tension_yielding_capacity_flange = self.tension_member_design_due_to_yielding_of_gross_section(
                A_v=A_v_flange,
                fy=self.flange_plate.fy)
            print("tension_yielding_capacity_flange", self.tension_yielding_capacity_flange)

            if self.tension_yielding_capacity_flange > self.flange_force:

                #             self.supported_section.tension_yielding_capacity > self.load.axial_force:
                # print("BBB flange member check is satisfactory. Doing bolt checks")
                self.web_plate_thickness_possible = [i for i in self.web_plate.thickness if
                                                     i >= (self.section.web_thickness / 2)]

                if self.preference == "Outside":
                    self.flange_plate_thickness_possible = [i for i in self.flange_plate.thickness if
                                                            i >= self.section.flange_thickness]
                else:
                    self.flange_plate_thickness_possible = [i for i in self.flange_plate.thickness if
                                                            i >= (self.section.flange_thickness / 2)]

                if len(self.flange_plate_thickness_possible) == 0 or self.web_plate_thickness_possible == 0:
                    logger.error(":aaaaWeb Plate thickness should be greater than section  thicknesss.")
                else:

                    # print("Selecting bolt diameter")
                    # self.select_bolt_dia(self)

                    self.flange_plate.thickness_provided = self.min_thick_based_on_area(self,
                                                                                        tk=self.section.flange_thickness,
                                                                                        width=self.section.flange_width,
                                                                                        list_of_pt_tk=self.flange_plate_thickness_possible,
                                                                                        t_w=self.section.web_thickness,
                                                                                        r_1=self.section.root_radius,
                                                                                        D=self.section.depth,
                                                                                        preference=self.preference)
                    self.web_plate.thickness_provided = self.min_thick_based_on_area(self,
                                                                                     tk=self.section.flange_thickness,
                                                                                     width=self.section.flange_width,
                                                                                     list_of_pt_tk=self.web_plate_thickness_possible,
                                                                                     t_w=self.section.web_thickness,
                                                                                     r_1=self.section.root_radius,
                                                                                     D=self.section.depth, )

                    if self.web_plate.thickness_provided == 0 or self.flange_plate.thickness_provided == 0:
                        self.design_status = False
                        logger.error("flange plate is not possible")
                    else:
                        self.design_status = True
            else:
                self.design_status = False
                logger.error(
                    " : tension_yielding_capacity  of flange is less than applied loads, Please select larger sections or decrease loads"
                    )
                print(" BBB failed in flange member checks. Select larger sections or decrease loads")
        else:
            self.design_status = False
            logger.error(
                " : tension_yielding_capacity of web  is less than applied loads, Please select larger sections or decrease loads")
            print("BBB failed in web member checks. Select larger sections or decrease loads")
        if self.design_status == True:
            print("Selecting bolt diameter")
            self.select_bolt_dia(self)
        else:
            logger.error(" : tension_yielding_capacity   is less "
                         "than applied loads, Please select larger sections or decrease loads")

    def module_name(self):
        return KEY_DISP_COLUMNCOVERPLATE

    def select_bolt_dia(self):
        self.min_plate_height = self.section.flange_width
        self.max_plate_height = self.section.flange_width

        axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
            self.section.area)

        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
            axial_force_f))  # todo added web moment -add in ddcl
        print("flange_force", self.flange_force)

        self.res_force = math.sqrt((self.fact_shear_load) ** 2 + (self.factored_axial_load) ** 2)  # N

        bolts_required_previous_1 = 2
        bolts_required_previous_2 = 2
        bolt_diameter_previous = self.bolt.bolt_diameter[-1]

        # res_force = math.sqrt(self.load.shear_force ** 2 + self.load.axial_force ** 2) * 1000
        self.bolt.bolt_grade_provided = self.bolt.bolt_grade[-1]
        count_1 = 0
        count_2 = 0
        bolts_one_line = 1
        # for flange plate thickness
        self.bolt_conn_plates_t_fu_fy = []
        if self.preference == "Outside":
            self.bolt_conn_plates_t_fu_fy.append(
                (self.flange_plate.thickness_provided, self.flange_plate.fu, self.flange_plate.fy))
            self.bolt_conn_plates_t_fu_fy.append(
                (self.section.flange_thickness, self.section.fu, self.section.fy))
        else:
            self.bolt_conn_plates_t_fu_fy.append(
                (2 * self.flange_plate.thickness_provided, self.flange_plate.fu, self.flange_plate.fy))
            self.bolt_conn_plates_t_fu_fy.append(
                (self.section.flange_thickness, self.section.fu, self.section.fy))

        # for web plate thickness
        self.bolt_conn_plates_web_t_fu_fy = []
        self.bolt_conn_plates_web_t_fu_fy.append(
            (2 * self.web_plate.thickness_provided, self.web_plate.fu, self.web_plate.fy))
        self.bolt_conn_plates_web_t_fu_fy.append(
            (self.section.web_thickness, self.section.fu, self.section.fy))
        bolt_design_status_1 = False
        bolt_design_status_2 = False
        for self.bolt.bolt_diameter_provided in reversed(self.bolt.bolt_diameter):
            # self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.flange_bolt.bolt_diameter[0],
            #                                                connecting_plates_tk=[self.flange_plate.thickness[0],
            #                                                                      self.section.flange_thickness])
            # self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.flange_bolt.bolt_diameter[0],
            #                                                connecting_plates_tk=[self.flange_plate.thickness[0],
            #                                                                      self.section.flange_thickness])

            self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                           conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)

            print(self.flange_bolt.min_edge_dist, self.flange_bolt.edge_type)

            if self.preference == "Outside":
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=1)
            else:
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=2)

            self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                        conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy)

            self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                  bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                  conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy,
                                                  n_planes=2)

            self.flange_plate.get_flange_plate_details(bolt_dia=self.flange_bolt.bolt_diameter_provided,
                                                       flange_plate_h_min=self.min_plate_height,
                                                       flange_plate_h_max=self.max_plate_height,
                                                       bolt_capacity=self.flange_bolt.bolt_capacity,
                                                       min_edge_dist=self.flange_bolt.min_edge_dist_round,
                                                       min_gauge=self.flange_bolt.min_gauge_round,
                                                       max_spacing=self.flange_bolt.max_spacing_round,
                                                       max_edge_dist=self.flange_bolt.max_edge_dist_round,
                                                       axial_load=self.flange_force, gap=self.flange_plate.gap / 2,
                                                       web_thickness=self.section.web_thickness,
                                                       root_radius=self.section.root_radius)

            self.min_web_plate_height = self.section.min_plate_height()
            self.max_web_plate_height = self.section.max_plate_height()
            axial_force_w = ((self.section.depth - (
                    2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                self.section.area)

            self.web_plate.get_web_plate_details(bolt_dia=self.bolt.bolt_diameter_provided,
                                                 web_plate_h_min=self.min_web_plate_height,
                                                 web_plate_h_max=self.max_web_plate_height,
                                                 bolt_capacity=self.web_bolt.bolt_capacity,
                                                 min_edge_dist=self.web_bolt.min_edge_dist_round,
                                                 min_gauge=self.web_bolt.min_gauge_round,
                                                 max_spacing=self.web_bolt.max_spacing_round,
                                                 max_edge_dist=self.web_bolt.max_edge_dist_round
                                                 , shear_load=self.fact_shear_load, axial_load=self.axial_force_w,
                                                 web_moment=self.moment_web,

                                                 gap=(self.web_plate.gap / 2), shear_ecc=True)

            if self.flange_plate.design_status is True and self.web_plate.design_status is True:
                if self.flange_plate.bolts_required > bolts_required_previous_1 and count_1 >= 1:
                    self.bolt.bolt_diameter_provided = bolt_diameter_previous
                    self.flange_plate.bolts_required = bolts_required_previous_1
                    self.flange_plate.bolt_force = bolt_force_previous_1
                    bolt_design_status_1 = self.flange_plate.design_status
                    break
                bolts_required_previous_1 = self.flange_plate.bolts_required
                bolt_diameter_previous = self.bolt.bolt_diameter_provided
                bolt_force_previous_1 = self.flange_plate.bolt_force
                count_1 += 1
                bolt_design_status_1 = self.flange_plate.design_status

                if self.web_plate.bolts_required > bolts_required_previous_2 and count_2 >= 1:
                    self.bolt.bolt_diameter_provided = bolt_diameter_previous
                    self.web_plate.bolts_required = bolts_required_previous_2
                    self.web_plate.bolt_force = bolt_force_previous_2
                    bolt_design_status_2 = self.web_plate.design_status
                    break
                bolts_required_previous_2 = self.web_plate.bolts_required
                bolt_diameter_previous = self.bolt.bolt_diameter_provided
                bolt_force_previous_2 = self.web_plate.bolt_force
                count_2 += 1
                print("self.flange_plate.bolts_required", self.flange_plate.bolts_required)
                bolt_design_status_2 = self.web_plate.design_status

                # else:
                #
                # # if self.bolt.bolt_diameter_provided == bolt_min:
                #
                # #     bolt_design_status_1 = self.plate.design_status
                #
                # #     bolt_design_status_2 = True
                #
                # pass

        bolt_capacity_req = self.bolt.bolt_capacity

        if (self.flange_plate.design_status == False and bolt_design_status_1 != True) or (
                self.web_plate.design_status == False and bolt_design_status_2 != True):
            self.design_status = False
        else:
            self.bolt.bolt_diameter_provided = bolt_diameter_previous
            self.flange_plate.bolts_required = bolts_required_previous_1
            self.flange_plate.bolt_force = bolt_force_previous_1
            self.web_plate.bolts_required = bolts_required_previous_2
            self.web_plate.bolt_force = bolt_force_previous_2

        if bolt_design_status_1 is True and bolt_design_status_2 is True:
            self.design_status = True
            self.get_bolt_grade(self)
        else:
            self.design_status = False
            logger.error("Bolt Not Possible")

    def get_bolt_grade(self):
        print(self.design_status, "Getting bolt grade")
        bolt_grade_previous = self.bolt.bolt_grade[-1]
        grade_status = False
        for self.bolt.bolt_grade_provided in reversed(self.bolt.bolt_grade):
            count = 1
            self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                           conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)

            if self.preference == "Outside":
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=1)
            else:
                self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                         bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                         conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                         n_planes=2)

            self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                        conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy)

            self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                  bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                  conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy,
                                                  n_planes=2)

            print(self.bolt.bolt_grade_provided, self.bolt.bolt_capacity, self.flange_plate.bolt_force)

            bolt_capacity_reduced_flange = self.flange_plate.get_bolt_red(self.flange_plate.bolts_one_line,
                                                                          self.flange_plate.gauge_provided,
                                                                          self.web_plate.bolt_line,
                                                                          self.web_plate.pitch_provided,
                                                                          self.flange_bolt.bolt_capacity,
                                                                          self.bolt.bolt_diameter_provided)
            bolt_capacity_reduced_web = self.web_plate.get_bolt_red(self.web_plate.bolts_one_line,
                                                                    self.web_plate.gauge_provided,
                                                                    self.web_plate.bolt_line,
                                                                    self.web_plate.pitch_provided,
                                                                    self.web_bolt.bolt_capacity,
                                                                    self.bolt.bolt_diameter_provided)
            if (bolt_capacity_reduced_flange < self.flange_plate.bolt_force) and (
                    bolt_capacity_reduced_web < self.web_plate.bolt_force) and (count >= 1):
                self.bolt.bolt_grade_provided = bolt_grade_previous
                # self.web_bolt.bolt_grade_provided = bolt_grade_previous
                grade_status = True
                break
            # bolts_required_previous_flange = self.flange_plate.bolts_required
            # bolts_required_previous_web =self.web_plate.bolts_required
            bolt_grade_previous = self.bolt.bolt_grade_provided
            grade_status = True
            count += 1

        if grade_status == False:
            self.design_status = False
        else:
            self.bolt.bolt_grade_provided = bolt_grade_previous
            # self.web_bolt.bolt_grade_provided = bolt_grade_previous

        self.get_plate_details(self)

    def get_plate_details(self):

        self.min_plate_height = self.section.flange_width
        self.max_plate_height = self.section.flange_width

        axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
            self.section.area)

        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
            axial_force_f))  # todo added web moment -add in ddcl
        self.flange_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                       conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy)

        if self.preference == "Outside":
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                     bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                     conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                     n_planes=1)
        else:
            self.flange_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                     bolt_grade_provided=self.bolt.bolt_grade_provided,
                                                     conn_plates_t_fu_fy=self.bolt_conn_plates_t_fu_fy,
                                                     n_planes=2)

        self.web_bolt.calculate_bolt_spacing_limits(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                                    conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy)

        self.web_bolt.calculate_bolt_capacity(bolt_diameter_provided=self.bolt.bolt_diameter_provided,
                                              bolt_grade_provided=self.bolt.bolt_grade_provided,
                                              conn_plates_t_fu_fy=self.bolt_conn_plates_web_t_fu_fy,
                                              n_planes=2)

        self.flange_plate.get_flange_plate_details(bolt_dia=self.flange_bolt.bolt_diameter_provided,
                                                   flange_plate_h_min=self.min_plate_height,
                                                   flange_plate_h_max=self.max_plate_height,
                                                   bolt_capacity=self.flange_bolt.bolt_capacity,
                                                   min_edge_dist=self.flange_bolt.min_edge_dist_round,
                                                   min_gauge=self.flange_bolt.min_gauge_round,
                                                   max_spacing=self.flange_bolt.max_spacing_round,
                                                   max_edge_dist=self.flange_bolt.max_edge_dist_round,
                                                   axial_load=self.flange_force, gap=self.flange_plate.gap / 2,
                                                   web_thickness=self.section.web_thickness,
                                                   root_radius=self.section.root_radius)

        self.min_web_plate_height = self.section.min_plate_height()
        self.max_web_plate_height = self.section.max_plate_height()
        axial_force_w = ((self.section.depth - (
                2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                            self.section.area)

        self.web_plate.get_web_plate_details(bolt_dia=self.web_bolt.bolt_diameter_provided,
                                             web_plate_h_min=self.min_web_plate_height,
                                             web_plate_h_max=self.max_web_plate_height,
                                             bolt_capacity=self.web_bolt.bolt_capacity,
                                             min_edge_dist=self.web_bolt.min_edge_dist_round,
                                             min_gauge=self.web_bolt.min_gauge_round,
                                             max_spacing=self.web_bolt.max_spacing_round,
                                             max_edge_dist=self.web_bolt.max_edge_dist_round
                                             , shear_load=self.fact_shear_load, axial_load=self.axial_force_w,
                                             web_moment=self.moment_web,

                                             gap=(self.web_plate.gap / 2), shear_ecc=True)

        possible_inner_plate = self.section.flange_width / 2 - self.section.web_thickness / 2 - self.section.root_radius
        self.flange_plate.edge_dist_provided = (possible_inner_plate - (
                    self.flange_plate.gauge_provided * (self.flange_plate.bolts_one_line - 1))) / 2

        if self.flange_plate.design_status is False or self.flange_plate.design_status is False:
            self.design_status = False
            logger.error("bolted connection not possible")

        else:
            self.member_check(self)

        ################################################################
        ##################################################################

    def member_check(self):
        block_shear_capactity = 0
        moment_capacity = 0

        ###### # capacity Check for flange = min(block, yielding, rupture)

        ###### # capacity Check for flange = min(block, yielding, rupture)

        #### Block shear capacity of  flange ### #todo comment out

        axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
            self.section.area)
        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
            axial_force_f))

        A_vn_flange = (self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole) * \
                      self.section.flange_thickness
        A_v_flange = self.section.flange_thickness * self.flange_plate.height

        self.section.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_flange,
            fy=self.flange_plate.fy)

        self.section.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_flange,
            fu=self.flange_plate.fu)
        #  Block shear strength for flange
        design_status_block_shear = False
        edge_dist = self.flange_plate.edge_dist_provided
        end_dist = self.flange_plate.end_dist_provided
        gauge = self.flange_plate.gauge_provided
        pitch = self.flange_plate.pitch_provided

        while design_status_block_shear == False:

            Avg = 2 * (end_dist + (
                    self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
                  * self.section.flange_thickness
            Avn = 2 * (self.flange_plate.end_dist_provided + (
                    self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                               self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                  self.section.flange_thickness
            Atg = 2 * ((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided +
                       self.flange_plate.edge_dist_provided) * \
                  self.section.flange_thickness
            # todo add in DDCl and diagram

            Atn = 2 * ((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided -
                       ((self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole) +
                       self.flange_plate.edge_dist_provided) * \
                  self.section.flange_thickness  # todo add in DDCl and diagram
            # print(Avg, Avn, Atg, Atn)
            # print(8, self.flange_plate.bolt_line, pitch, end_dist)

            self.section.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                  A_tn=Atn,
                                                                                  f_u=self.flange_plate.fu,
                                                                                  f_y=self.flange_plate.fy)
            # print(9,  self.flange_plate.block_shear_capacity, self.load.axial_force, self.flange_plate.pitch_provided)

            if self.section.block_shear_capacity < self.flange_force:

                if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.flange_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5

                else:
                    break

            else:
                design_status_block_shear = True
                break

            if design_status_block_shear is True:
                break
        if design_status_block_shear is True:

            # flange_force = flange_force

            self.section.tension_capacity_flange = min(self.section.tension_yielding_capacity,
                                                       self.section.tension_rupture_capacity,
                                                       self.section.block_shear_capacity)

            if self.section.tension_capacity_flange < self.flange_force:
                self.design_status = False
                logger.warning(
                    ": Tension capacity flange J is less than required flange force kN Select larger column section")

            else:
                pass
        else:
            self.design_status = False
            logger.warning(
                ": Tension capacity flange I is less than required web force kN Select larger column section")  #
        if self.design_status == True:
            self.flange_plate_check(self)
        else:
            self.design_status = False
        print("status of flange I", self.design_status)

    # todo anjali
    def flange_plate_check(self):
        # capacity Check for flange_outsite_plate =min(block, yielding, rupture)

        ####Capacity of flange cover plate for bolted Outside #
        axial_force_f = self.factored_axial_load * self.section.flange_width * self.section.flange_thickness / (
            self.section.area)

        self.flange_force = (((self.moment_flange) / (self.section.depth - self.section.flange_thickness)) + (
            axial_force_f))
        print(self.preference)
        if self.preference == "Outside":
            print(self.preference)

            #  Block shear strength for outside flange plate
            available_flange_thickness = list(
                [x for x in self.flange_plate.thickness if (self.flange_plate.thickness_provided <= x)])
            # print(111,self.flange_plate.pitch_provided)
            # print(available_flange_thickness,self.flange_plate.thickness)
            for self.flange_plate.thickness_provided in available_flange_thickness:
                design_status_block_shear = False
                edge_dist = self.flange_plate.edge_dist_provided
                end_dist = self.flange_plate.end_dist_provided
                gauge = self.flange_plate.gauge_provided
                pitch = self.flange_plate.pitch_provided
                # print(1)

                A_vn_flange = (
                                          self.section.flange_width - self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole) * \
                              self.flange_plate.thickness_provided
                A_v_flange = self.flange_plate.thickness_provided * self.flange_plate.height
                self.flange_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                    A_v=A_v_flange,
                    fy=self.flange_plate.fy)

                self.flange_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                    A_vn=A_vn_flange,
                    fu=self.flange_plate.fu)

                #### Block shear capacity of flange plate ###

                while design_status_block_shear == False:

                    Avg = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * self.flange_plate.thickness_provided
                    Avn = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                       self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                          self.flange_plate.thickness_provided

                    Atg = 2 * ((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) + (
                            self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2))
                               * self.flange_plate.thickness_provided)  # todo add in DDCl
                    Atn = 2 * (((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) - (
                            self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole)) + (
                                       self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2)) * self.flange_plate.thickness_provided
                    #                       # todo add in DDCl
                    # print(8, self.flange_plate.bolt_line, pitch, end_dist, self.flange_plate.thickness_provided)

                    self.flange_plate.block_shear_capacity = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                             A_tg=Atg,
                                                                                             A_tn=Atn,
                                                                                             f_u=self.flange_plate.fu,
                                                                                             f_y=self.flange_plate.fy)

                    # print(9, self.flange_plate.thickness_provided, self.flange_plate.block_shear_capacity, self.load.axial_force,
                    #       self.flange_plate.pitch_provided)

                    if self.flange_plate.block_shear_capacity < self.flange_force:

                        if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                            if self.flange_plate.bolt_line == 1:
                                end_dist += 5
                            else:
                                pitch += 5

                        else:
                            # design_status_block_shear = False
                            break

                        # print(Avg, Avn, Atg, Atn)
                    else:
                        design_status_block_shear = True
                        break
                # print(design_status_block_shear)
                if design_status_block_shear is True:
                    break

            if design_status_block_shear is True:
                self.flange_plate.tension_capacity_flange_plate = min(self.flange_plate.tension_yielding_capacity,
                                                                      self.flange_plate.tension_rupture_capacity,
                                                                      self.flange_plate.block_shear_capacity)

                if self.flange_plate.tension_capacity_flange_plate < self.flange_force:
                    self.design_status = False
                    logger.warning(": Tension capacity flange plate G is less than required flange force kN")
                    logger.info(": Increase the size of column section")

                else:
                    pass
            else:
                self.design_status = False
                logger.warning(
                    ": Tension capacity flange_plate E is less than required flange force kN Select larger column section")  #

        else:
            # capacity Check for flange_outsite_plate =min(block, yielding, rupture)

            #  Block shear strength for outside + inside flange plate

            # OUTSIDE-inside
            available_flange_thickness = list(
                [x for x in self.flange_plate.thickness if ((self.flange_plate.thickness_provided) <= x)])
            # print(111,self.flange_plate.pitch_provided)
            # print(available_flange_thickness,self.flange_plate.thickness)
            for self.flange_plate.thickness_provided in available_flange_thickness:
                design_status_block_shear = False
                edge_dist = self.flange_plate.edge_dist_provided
                end_dist = self.flange_plate.end_dist_provided
                gauge = self.flange_plate.gauge_provided
                pitch = self.flange_plate.pitch_provided
                # print(11)

                #  yielding,rupture  for  inside flange plate
                self.flange_plate.Innerheight = (self.section.flange_width - self.section.web_thickness - (
                            self.section.root_radius * 2)) / 2
                flange_plate_height_outside = self.flange_plate.height
                self.flange_plate.Innerlength = self.flange_plate.length

                A_vn_flange = (((2 * self.flange_plate.Innerheight) + self.section.flange_width) - (
                            self.flange_plate.bolts_one_line * self.flange_bolt.dia_hole)) * self.flange_plate.thickness_provided
                A_v_flange = ((
                                          2 * self.flange_plate.Innerheight) + self.section.flange_width) * self.flange_plate.thickness_provided
                self.flange_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
                    A_v=A_v_flange,
                    fy=self.flange_plate.fy)

                self.flange_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
                    A_vn=A_vn_flange,
                    fu=self.flange_plate.fu)
                #### Block shear capacity of flange plate ###

                while design_status_block_shear == False:

                    Avg = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) * self.flange_plate.thickness_provided
                    Avn = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                       self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                          self.flange_plate.thickness_provided
                    Atg = 2 * ((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) + (
                                self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2))
                               * self.flange_plate.thickness_provided)  # todo add in DDCl
                    Atn = 2 * (((((self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided) - (
                            self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole)) +
                               (
                                           self.flange_plate.edge_dist_provided + self.section.root_radius + self.section.web_thickness / 2)) * self.flange_plate.thickness_provided
                    # todo add in DDCl

                    # print(12, self.flange_plate.bolt_line, pitch, end_dist, self.flange_plate.thickness_provided)

                    flange_plate_block_shear_capactity_outside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                                 A_tg=Atg,
                                                                                                 A_tn=Atn,
                                                                                                 f_u=self.flange_plate.fu,
                                                                                                 f_y=self.flange_plate.fy)

                    #  Block shear strength for inside flange plate under AXIAL
                    Avg = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided) \
                          * self.flange_plate.thickness_provided
                    Avn = 2 * (self.flange_plate.end_dist_provided + (
                            self.flange_plate.bolt_line - 1) * self.flange_plate.pitch_provided - (
                                       self.flange_plate.bolt_line - 0.5) * self.flange_bolt.dia_hole) * \
                          self.flange_plate.thickness_provided

                    Atg = 2 * ((
                                           self.flange_plate.bolts_one_line / 2 - 1) * self.flange_plate.gauge_provided + self.flange_plate.edge_dist_provided) * \
                          self.flange_plate.thickness_provided
                    # todo add in DDCl and diagram
                    Atn = 2 * ((self.flange_plate.bolts_one_line / 2 - 1) *
                               self.flange_plate.gauge_provided - ((
                                                                               self.flange_plate.bolts_one_line / 2 - 0.5) * self.flange_bolt.dia_hole) + self.flange_plate.edge_dist_provided) * \
                          self.flange_plate.thickness_provided
                    # todo add in DDCl
                    flange_plate_block_shear_capacity_inside = self.block_shear_strength_plate(A_vg=Avg, A_vn=Avn,
                                                                                               A_tg=Atg,
                                                                                               A_tn=Atn,
                                                                                               f_u=self.flange_plate.fu,
                                                                                               f_y=self.flange_plate.fy)
                    self.flange_plate.block_shear_capacity = flange_plate_block_shear_capactity_outside + flange_plate_block_shear_capacity_inside

                    # print(14, self.flange_plate.thickness_provided, self.flange_plate.block_shear_capacity,
                    #       self.load.axial_force,
                    #       self.flange_plate.pitch_provided)
                    if self.flange_plate.block_shear_capacity < self.flange_force:

                        if self.flange_bolt.max_spacing_round >= pitch + 5 and self.flange_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                            if self.flange_plate.bolt_line == 1:
                                end_dist += 5
                            else:
                                pitch += 5

                        else:
                            # design_status_block_shear = True
                            break

                        # print(Avg, Avn, Atg, Atn)
                        # logger.error(": flange_plate_t is less than min_thk_flange_plate:")
                        # logger.warning(": Minimum flange_plate_t required is %2.2f mm" % (min_thk_flange_plate))
                    else:
                        design_status_block_shear = True
                        break
                # print(design_status_block_shear)
                if design_status_block_shear is True:
                    break

            if design_status_block_shear is True:
                self.flange_plate.tension_capacity_flange_plate = min(self.flange_plate.tension_yielding_capacity,
                                                                      self.flange_plate.tension_rupture_capacity,
                                                                      self.flange_plate.block_shear_capacity)
                print("flange_force", self.flange_force)
                print(self.flange_plate.tension_capacity_flange_plate, "tension_capacity_flange_plate")
                if self.flange_plate.tension_capacity_flange_plate < self.flange_force:
                    self.design_status = False
                    logger.warning(": Tension capacity flange plate H is less than required flange force kN")
                    logger.info(": Increase the size of column section")

                else:
                    self.design_status = True
                    pass
            else:
                self.design_status = False

        if self.design_status == True:
            # pass
            self.web_axial_check(self)
        else:
            self.design_status = False
        print("status of flange E & H", self.design_status)

        # self.flange_plate.get_moment_cacacity(self.flange_plate.fy, self.flange_plate.thickness_provided,
        #                                       self.flange_plate.length)
        # print(300, design_status)

        ######################################################################### ##
        # Design of web splice plate

    ################################ CAPACITY CHECK FOR WEB #####################################################################################

    def web_axial_check(self):
        self.axial_force_w = ((self.section.depth - (
                    2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                 self.section.area)
        block_shear_capacity = 0
        moment_capacity = 0

        ###### # capacity Check for web in axial = min(block, yielding, rupture)

        A_vn_web = ((self.section.depth - (2 * self.section.flange_thickness) - (
                    self.web_plate.bolts_one_line * self.web_bolt.dia_hole))) \
                   * self.section.web_thickness
        A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness
        self.section.tension_yielding_capacity_web = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web, fy=self.web_plate.fy)
        self.section.tension_rupture_capacity_web = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_web, fu=self.web_plate.fu)

        # print(111,self.web_plate.pitch_provided)
        # print(available_web_thickness,self.web_plate.thickness)
        design_status_block_shear = False
        edge_dist = self.web_plate.edge_dist_provided
        end_dist = self.web_plate.end_dist_provided
        gauge = self.web_plate.gauge_provided
        pitch = self.web_plate.pitch_provided
        # print(1)

        #### Block shear capacity of web in axial ###
        #### Block shear capacity of web in axial ###

        while design_status_block_shear == False:
            # print(design_status_block_shear)
            # print(0, self.web_plate.max_end_dist, self.web_plate.end_dist_provided, self.web_plate.max_spacing_round, self.web_plate.pitch_provided)
            Avg = 2 * ((self.web_plate.bolt_line - 1) * pitch + end_dist) * \
                  self.section.web_thickness
            Avn = 2 * ((self.web_plate.bolt_line - 1) * pitch + (
                    self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole + end_dist) * \
                  self.section.web_thickness
            Atg = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge) * self.section.web_thickness
            Atn = (self.web_plate.edge_dist_provided + (
                    self.web_plate.bolts_one_line - 1) * gauge - (
                           self.web_plate.bolts_one_line - 1) * self.web_bolt.dia_hole) * self.section.web_thickness

            # print(17,self.web_plate.bolt_line, self.web_plate.pitch_provided, self.web_plate.bolt_line,
            #      self.web_bolt.dia_hole, self.web_plate.end_dist_provided, self.web_plate.thickness_provided)
            # print(18, self.web_plate.bolt_line, pitch, end_dist, self.section.web_thickness)

            self.section.block_shear_capacity_web = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn, A_tg=Atg,
                                                                                      A_tn=Atn,
                                                                                      f_u=self.web_plate.fu,
                                                                                      f_y=self.web_plate.fy)
            # print(19, self.web_plate.thickness_provided, self.web_plate.block_shear_capacity, self.load.axial_force, self.web_plate.pitch_provided)

            if self.section.block_shear_capacity_web < self.axial_force_w:

                if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                    if self.web_plate.bolt_line == 1:
                        end_dist += 5
                    else:
                        pitch += 5

                else:
                    # design_status_block_shear = False
                    break

            else:
                design_status_block_shear = True
                break
        if design_status_block_shear == True:
            self.section.tension_capacity_web = min(self.section.tension_yielding_capacity_web,
                                                    self.section.tension_rupture_capacity_web,
                                                    self.section.block_shear_capacity_web)

            self.axial_force_w = ((self.section.depth - (
                        2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                     self.section.area)
            if self.section.tension_capacity_web < self.axial_force_w:

                self.design_status = False
                logger.warning(
                    ": Tension capacity web_ is less than required web force kN Select larger column section")  # todo

            else:
                self.design_status = True
                pass
        else:
            self.design_status = False
            logger.warning(
                ": Tension capacity web_K is less than required web force kN Select larger column section")  #
        if self.design_status == True:
            self.web_plate_axial_check(self)
        else:
            self.design_status = False
        print("status of flange K", self.design_status)

    #         ###### # capacity Check for web plate in axial = min(block, yielding, rupture)
    def web_plate_axial_check(self):
        self.axial_force_w = ((self.section.depth - (
                2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
                                 self.section.area)

        A_vn_web = 2 * (self.web_plate.height - (
                self.web_plate.bolts_one_line * self.web_bolt.dia_hole)) * self.web_plate.thickness_provided
        A_v_web = 2 * self.web_plate.height * self.web_plate.thickness_provided
        self.web_plate.tension_yielding_capacity = self.tension_member_design_due_to_yielding_of_gross_section(
            A_v=A_v_web, fy=self.web_plate.fy)
        self.web_plate.tension_rupture_capacity = self.tension_member_design_due_to_rupture_of_critical_section(
            A_vn=A_vn_web, fu=self.web_plate.fu)

        available_web_thickness = list(
            [x for x in self.web_plate.thickness if ((self.web_plate.thickness_provided) <= x)])
        # print(111,self.web_plate.pitch_provided)
        # print(available_web_thickness,self.web_plate.thickness)
        for self.web_plate.thickness_provided in available_web_thickness:
            design_status_block_shear = False
            edge_dist = self.web_plate.edge_dist_provided
            end_dist = self.web_plate.end_dist_provided
            gauge = self.web_plate.gauge_provided
            pitch = self.web_plate.pitch_provided
            # print(1)

            #### Block shear capacity of web plate in axial ###

            while design_status_block_shear == False:
                # print(design_status_block_shear)
                # print(0, self.web_plate.max_end_dist, self.web_plate.end_dist_provided, self.web_plate.max_spacing_round, self.web_plate.pitch_provided)
                Avg = 2 * ((self.web_plate.bolt_line - 1) * pitch + end_dist) * \
                      self.web_plate.thickness_provided
                Avn = 2 * ((self.web_plate.bolt_line - 1) * pitch + (
                        self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole + end_dist) * \
                      self.web_plate.thickness_provided
                Atg = (self.web_plate.edge_dist_provided + (
                        self.web_plate.bolts_one_line - 1) * gauge) * self.web_plate.thickness_provided
                Atn = (self.web_plate.edge_dist_provided + (
                        self.web_plate.bolts_one_line - 1) * gauge - (
                               self.web_plate.bolts_one_line - 1) * self.web_bolt.dia_hole) * self.web_plate.thickness_provided

                # print(self.web_plate.bolt_line, self.web_plate.pitch_provided, self.web_plate.bolt_line,
                # self.web_plate.dia_hole, self.web_plate.end_dist_provided, self.web_plate.thickness_provided)
                # print(1, self.web_plate.bolt_line, pitch, end_dist, self.web_plate.thickness_provided)

                self.web_plate.block_shear_capacity = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn,
                                                                                        A_tg=Atg,
                                                                                        A_tn=Atn,
                                                                                        f_u=self.web_plate.fu,
                                                                                        f_y=self.web_plate.fy)
                # print(2, self.web_plate.thickness_provided, self.web_plate.block_shear_capacity, self.load.axial_force, self.web_plate.pitch_provided)

                self.web_plate.block_shear_capacity = 2 * self.web_plate.block_shear_capacity

                if self.web_plate.block_shear_capacity < self.axial_force_w:

                    if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                        if self.web_plate.bolt_line == 1:
                            end_dist += 5
                        else:
                            pitch += 5

                    else:
                        break

                else:
                    design_status_block_shear = True
                    break

            if design_status_block_shear == True:
                break
        if design_status_block_shear == True:

            self.web_plate.tension_capacity_web_plate = min(self.web_plate.tension_yielding_capacity,
                                                            self.web_plate.tension_rupture_capacity,
                                                            self.web_plate.block_shear_capacity)
            if self.web_plate.tension_capacity_web_plate < self.axial_force_w:
                self.design_status = False
                logger.warning(
                    ": Tension capacity web_plate A is less than required web force kN Select larger column section")  # todo

            else:
                self.design_status = True
                pass
        else:
            self.design_status = False
            logger.warning(
                ": Tension capacity web_plate B is less than required web force kN Select larger column section")  # todo
        if self.design_status == True:
            self.web_shear_plate_check(self)
        else:
            self.design_status = False
        print("status of flange L", self.design_status)

    def web_shear_plate_check(self):
        ###### # capacity Check for web plate  in shear = min(block, yielding, rupture)
        # self.axial_force_w = ((self.section.depth - (
        #         2 * self.section.flange_thickness)) * self.section.web_thickness * self.factored_axial_load) / (
        #                     self.section.area)

        # A_vn_web = 2*(self.web_plate.length - (self.web_plate.bolt_line * self.web_bolt.dia_hole)) * \
        #            self.web_plate.thickness_provided
        # A_v_web = 2*self.web_plate.length * self.web_plate.thickness_provided
        A_vn_web = 2 * (self.web_plate.height - (self.web_plate.bolts_one_line * self.web_bolt.dia_hole)) * \
                   self.web_plate.thickness_provided
        A_v_web = 2 * self.web_plate.height * self.web_plate.thickness_provided
        self.web_plate.shear_yielding_capacity = self.shear_yielding(
            A_v=A_v_web, fy=self.web_plate.fy)
        self.web_plate.shear_rupture_capacity = self.shear_rupture_(
            A_vn=A_vn_web, fu=self.web_plate.fu)

        available_web_thickness = list(
            [x for x in self.web_plate.thickness if ((self.web_plate.thickness_provided) <= x)])
        # print(111,self.web_plate.pitch_provided)
        # print(available_web_thickness,self.web_plate.thickness)
        for self.web_plate.thickness_provided in available_web_thickness:  #
            design_status_block_shear = False
            edge_dist = self.web_plate.edge_dist_provided
            end_dist = self.web_plate.end_dist_provided
            gauge = self.web_plate.gauge_provided
            pitch = self.web_plate.pitch_provided
            # print(1)

            #### Block shear capacity of web plate ###

            while design_status_block_shear == False:
                Atg = (((
                                    self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided) + self.web_plate.end_dist_provided) * self.web_plate.thickness_provided
                Atn = (((self.web_plate.bolt_line - 1) * self.web_plate.pitch_provided) + ((
                                                                                                   self.web_plate.bolt_line - 0.5) * self.web_bolt.dia_hole) + self.web_plate.end_dist_provided) * self.web_plate.thickness_provided
                Avg = (self.web_plate.edge_dist_provided + (
                        self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided) * self.web_plate.thickness_provided
                Avn = ((((self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided)
                        + self.web_plate.edge_dist_provided) - ((self.web_plate.bolts_one_line - 0.5)
                                                                * self.web_bolt.dia_hole)) * self.web_plate.thickness_provided

                # (self.web_plate.edge_dist_provided + ((self.web_plate.bolts_one_line - 1) * self.web_plate.gauge_provided) - ((
                #            self.web_plate.bolts_one_line - 0.5) * self.web_bolt.dia_hole)) * self.web_plate.thickness_provided
                self.web_plate.block_shear_capacity_shear = self.block_shear_strength_section(A_vg=Avg, A_vn=Avn,
                                                                                              A_tg=Atg,
                                                                                              A_tn=Atn,
                                                                                              f_u=self.web_plate.fu,
                                                                                              f_y=self.web_plate.fy)
                self.web_plate.block_shear_capacity_shear = 2 * self.web_plate.block_shear_capacity_shear
                # print(2, self.web_plate.thickness_provided, self.web_plate.block_shear_capacity, self.load.axial_force, self.web_plate.pitch_provided)

                if self.web_plate.block_shear_capacity_shear < self.fact_shear_load:
                    #
                    if self.web_bolt.max_spacing_round >= pitch + 5 and self.web_bolt.max_end_dist_round >= end_dist + 5:  # increase thickness todo
                        if self.web_plate.bolt_line == 1:
                            end_dist += 5
                        else:
                            pitch += 5

                    else:
                        # design_status_block_shear = False
                        break

                    # print(Avg, Avn, Atg, Atn)
                    # logger.error(": flange_plate_t is less than min_thk_flange_plate:")
                    # logger.warning(": Minimum flange_plate_t required is %2.2f mm" % (min_thk_flange_plate))
                else:
                    design_status_block_shear = True
                    break
                # print(design_status_block_shear)
            if design_status_block_shear is True:
                break

        if design_status_block_shear is True:
            self.web_plate.shear_capacity_web_plate = min(self.web_plate.shear_yielding_capacity,
                                                          self.web_plate.shear_rupture_capacity,
                                                          self.web_plate.block_shear_capacity_shear)

            if self.web_plate.shear_capacity_web_plate < self.fact_shear_load:
                self.design_status = False
                logger.warning(
                    ": Shear capacity web_plate C is less than required web force kN Select larger column section")  # todo
            else:
                self.design_status = True
                pass
        else:
            self.design_status = False
            logger.warning(
                ": Shear capacity web_plate D is less than required web force kN Select larger column section")  #
        if self.design_status == True:
            pass
        else:
            self.design_status = False
            logger.warning(
                ": Shear capacity web_plate L is less than required web force kN Select larger column section")
        print("status of flange M", self.design_status)

        ####todo comment out

        self.flange_plate.length = self.flange_plate.length * 2
        self.web_plate.length = self.web_plate.length * 2
        self.flange_plate.bolt_line = 2 * self.flange_plate.bolt_line
        self.flange_plate.bolts_one_line = self.flange_plate.bolts_one_line
        self.flange_plate.bolts_required = self.flange_plate.bolt_line * self.flange_plate.bolts_one_line
        self.flange_plate.midgauge = 2 * (
                    self.flange_plate.edge_dist_provided + self.section.root_radius) + self.section.web_thickness
        self.web_plate.midpitch = (2 * self.web_plate.end_dist_provided) + self.web_plate.gap
        self.flange_plate.midpitch = (2 * self.flange_plate.end_dist_provided) + self.flange_plate.gap

        self.web_plate.bolts_one_line = self.web_plate.bolts_one_line
        self.web_plate.bolt_line = 2 * self.web_plate.bolt_line
        self.web_plate.bolts_required = self.web_plate.bolt_line * self.web_plate.bolts_one_line
        self.flange_plate.Innerlength = self.flange_plate.length

        self.min_plate_length = (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))
        print("self.min_plate_length", self.min_plate_length)
        # print(600, design_status)
        #     print("self.section.tension_capacity_flange",self.section.tension_capacity_flange)
        #     print("self.section.tension_capacity_web", self.section.tension_capacity_web)
        #     print("self.flange_plate.tension_capacity_flange_plate",self.flange_plate.tension_capacity_flange_plate)
        #     # print("self.flange_plate.shear_capacity_flange_plate", self.flange_plate.shear_capacity_flange_plate)
        #
        #     print("self.web_plate.tension_capacity_web_plate", self.web_plate.tension_capacity_web_plate)
        #     print("self.web_plate.shear_capacity_web_plate",self.web_plate.shear_capacity_web_plate)

        # print(
        #     self.flange_plate.length *2)
        # print(
        #     self.web_plate.length *2)
        # print(
        #     self.flange_plate.bolts_required * 2)
        # print(
        #     self.web_plate.bolts_required * 2)

        # print("anjali", self.anjali)
        print(self.section)
        print(self.load)
        print(self.flange_bolt)
        print(self.flange_plate)
        print(self.web_bolt)
        print(self.web_plate)
        print(self.web_plate.thickness_provided)
        print(self.flange_plate.thickness_provided)
        # print(design_status)
        print(
            self.flange_plate.length)
        print(
            self.web_plate.length)
        print(
            self.flange_plate.bolts_required)
        print(
            self.web_plate.bolts_required)
        print("bolt dia", self.flange_bolt.bolt_diameter_provided)
        print("flange_plate.Innerlength", self.flange_plate.Innerlength)
        print("flange_plate.Innerheight", self.flange_plate.Innerheight)
        print("flange_plate.gap", self.flange_plate.gap)
        print(
            self.web_plate.length)
        print("webplategap", self.web_plate.gap)

        print("self.flange_plate.midgauge", self.flange_plate.midgauge)
        print("self.web_plate.midpitch", self.web_plate.midpitch)
        print("self.flange_plate.midpitch", self.flange_plate.midpitch)

        if self.design_status == True:

            logger.error(": Overall bolted cover plate splice connection design is safe \n")
            logger.debug(" :=========End Of design===========")
        else:
            logger.error(": Design is not safe \n ")
            logger.debug(" :=========End Of design===========")

    ################################ Design Report #####################################################################################

    # def beam_design_report(self, popup_summary):
    #     # bolt_list = str(*self.bolt.bolt_diameter, sep=", ")
    #     self.report_input = \
    #         {KEY_MODULE: self.module,
    #          KEY_MAIN_MODULE: self.mainmodule,
    #          KEY_CONN: self.connectivity,
    #          KEY_DISP_SHEAR: self.load.shear_force,
    #          KEY_DISP_AXIAL:self.load.axial_force,
    #          KEY_DISP_MOMENT:self.load.moment,
    #              "Section Details": "TITLE",
    #          "Beam Details": r'/ResourceFiles/images/coverplate".png',
    #          "Supported Section Details": "TITLE",
    #          KEY_DISP_D: str(self.bolt.bolt_diameter),
    #          KEY_DISP_GRD: str(self.bolt.bolt_grade),
    #          KEY_DISP_TYP: self.bolt.bolt_type,
    #          KEY_DISP_DP_BOLT_HOLE_TYPE: self.bolt.bolt_hole_type,
    #          KEY_DISP_DP_BOLT_SLIP_FACTOR: self.bolt.mu_f,
    #          KEY_DISP_DP_DETAILING_EDGE_TYPE: self.bolt.edge_type,
    #          KEY_DISP_DP_DETAILING_GAP: self.plate.gap,
    #          KEY_DISP_DP_DETAILING_CORROSIVE_INFLUENCES: self.bolt.corrosive_influences

    ################################ CAPACITY CHECK #####################################################################################

    @staticmethod
    def block_shear_strength_plate(A_vg, A_vn, A_tg, A_tn, f_u, f_y):  # for flange plate
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb, 3)
        return Tdb

        # Function for block shear capacity calculation

    @staticmethod
    def block_shear_strength_section(A_vg, A_vn, A_tg, A_tn, f_u, f_y):
        """Calculate the block shear strength of bolted connections as per cl. 6.4.1

        Args:
            A_vg: Minimum gross area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_vn: Minimum net area in shear along bolt line parallel to external force [in sq. mm] (float)
            A_tg: Minimum gross area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            A_tn: Minimum net area in tension from the bolt hole to the toe of the angle,
                           end bolt line, perpendicular to the line of force, respectively [in sq. mm] (float)
            f_u: Ultimate stress of the plate material in MPa (float)
            f_y: Yield stress of the plate material in MPa (float)

        Return:
            block shear strength of bolted connection in N (float)

        Note:
            Reference:
            IS 800:2007, cl. 6.4.1

        """
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        T_db1 = A_vg * f_y / (math.sqrt(3) * gamma_m0) + 0.9 * A_tn * f_u / gamma_m1
        T_db2 = 0.9 * A_vn * f_u / (math.sqrt(3) * gamma_m1) + A_tg * f_y / gamma_m0
        Tdb = min(T_db1, T_db2)
        Tdb = round(Tdb, 3)
        return Tdb
        # cl 6.2 Design Strength Due to Yielding of Gross Section

    @staticmethod
    def tension_member_design_due_to_yielding_of_gross_section(A_v, fy):
        '''
             Args:
                 A_v (float) Area under shear
                 column_fy (float) Yield stress of column material
             Returns:
                 Capacity of column web in shear yielding
             '''
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        # A_v = height * thickness
        tdg = (A_v * fy) / (gamma_m0)
        return tdg

    @staticmethod
    def tension_member_design_due_to_rupture_of_critical_section(A_vn, fu):
        '''
               Args:
                   A_vn (float) Net area under shear
                   column_fu (float) Ultimate stress of column material
               Returns:
                   Capacity of column web in shear rupture
               '''

        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        # A_vn = (height- bolts_one_line * dia_hole) * thickness
        T_dn = 0.9 * A_vn * fu / (gamma_m1)
        return T_dn

    @staticmethod
    def shear_yielding(A_v, fy):
        '''
        Args:
            length (float) length of member in direction of shear load
            thickness(float) thickness of member resisting shear
            column_fy (float) Yeild stress of section material
        Returns:
            Capacity of section in shear yeiding
        '''

        # A_v = length * thickness
        gamma_m0 = 1.1
        # print(length, thickness, fy, gamma_m0)
        # V_p = (0.6 * A_v * fy) / (math.sqrt(3) * gamma_m0 * 1000)  # kN
        V_p = (A_v * fy) / (math.sqrt(3) * gamma_m0)  # N
        return V_p

    @staticmethod
    def shear_rupture_(A_vn, fu):
        '''
               Args:
                   A_vn (float) Net area under shear
                   column_fu (float) Ultimate stress of column material
               Returns:
                   Capacity of column web in shear rupture
               '''

        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        # A_vn = (height- bolts_one_line * dia_hole) * thickness
        T_dn = 0.9 * A_vn * fu / (math.sqrt(3) * gamma_m1)
        return T_dn

    #
    # def web_force(column_d, column_f_t, column_t_w, axial_force, column_area):
    #     """
    #     Args:
    #        c_d: Overall depth of the column section in mm (float)
    #        column_f_t: Thickness of flange in mm (float)
    #        column_t_w: Thickness of flange in mm (float)
    #        axial_force: Factored axial force in kN (float)
    #
    #     Returns:
    #         Force in flange in kN (float)
    #     """
    #     axial_force_w = int(
    #         ((column_d - 2 * (column_f_t)) * column_t_w * axial_force ) / column_area)   # N
    #     return round(axial_force_w)

    @staticmethod
    def limiting_width_thk_ratio(column_f_t, column_t_w, column_d, column_b, column_fy, factored_axial_force,
                                 column_area, compression_element, section):

        epsilon = float(math.sqrt(250 / column_fy))
        axial_force_w = int(
            ((column_d - 2 * (column_f_t)) * column_t_w * factored_axial_force) / (column_area))  # N

        des_comp_stress_web = column_fy
        des_comp_stress_section = column_fy
        avg_axial_comp_stress = axial_force_w / ((column_d - 2 * column_f_t) * column_t_w)
        r1 = avg_axial_comp_stress / des_comp_stress_web
        r2 = avg_axial_comp_stress / des_comp_stress_section
        a = column_b / column_f_t
        # compression_element=["External","Internal","Web of an I-H" ,"box section" ]
        # section=["rolled","welded","compression due to bending","generally", "Axial compression" ]
        # section = "rolled"
        if compression_element == "External" or compression_element == "Internal":
            if section == "Rolled":
                if column_b * 0.5 / column_f_t <= 9.4 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 10.5 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 15.7 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
                # print("class_of_section", class_of_section )
            elif section == "welded":
                if column_b * 0.5 / column_f_t <= 8.4 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 9.4 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 13.6 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
            elif section == "compression due to bending":
                if column_b * 0.5 / column_f_t <= 29.3 * epsilon:
                    class_of_section1 = "plastic"
                elif column_b * 0.5 / column_f_t <= 33.5 * epsilon:
                    class_of_section1 = "compact"
                elif column_b * 0.5 / column_f_t <= 42 * epsilon:
                    class_of_section1 = "semi-compact"
                # else:
                #     print('fail')
            # else:
            #     pass

        elif compression_element == "Web of an I-H" or compression_element == "box section":
            if section == "generally":
                if r1 < 0:
                    if column_d / column_t_w <= max((84 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "plastic"
                    elif column_d / column_t_w <= (max(105 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "compact"
                    elif column_d / column_t_w <= max((126 * epsilon / (1 + 2 * r1)), column_d / column_t_w >= (
                            42 * epsilon)):
                        class_of_section1 = "semi-compact"
                    # else:
                    #     print('fail')
                    # print("class_of_section3", class_of_section)
                elif r1 > 0:
                    if column_d / column_t_w <= max((84 * epsilon / (1 + r1)), (42 * epsilon)):
                        class_of_section1 = "plastic"
                    elif column_d / column_t_w <= max((105 * epsilon / (1 + (r1 * 1.5))), (
                            42 * epsilon)):
                        class_of_section1 = "compact"
                    elif column_d / column_t_w <= max((126 * epsilon / (1 + 2 * r1)), (
                            42 * epsilon)):
                        class_of_section1 = "semi-compact"
                    # else:
                    #     self.design_status ==False
                    #     # print(self.design_status,"reduce Axial Force")
                    #     logger.warning(
                    #         ": Reduce Axial Force, web is slender under given forces")
                    # else:
                    #     print('fail')
                    # print("class_of_section4", class_of_section)
            elif section == "Axial compression":
                if column_d / column_t_w <= (42 * epsilon):
                    class_of_section1 = "semi-compact"
                else:
                    class_of_section1 = "N/A"
        #     else:
        #         print('fail')
        # else:
        #     pass
        print("class_of_section", class_of_section1)
        if class_of_section1 == "plastic":
            class_of_section1 = 1
        elif class_of_section1 == "compact":
            class_of_section1 = 2
        elif class_of_section1 == "semi-compact":
            class_of_section1 = 3
        # else:
        #     print('fail')
        print("class_of_section2", class_of_section1)

        return class_of_section1

        print("class_of_section1", class_of_section1)

    def min_thick_based_on_area(self, tk, width, list_of_pt_tk, t_w, r_1, D,
                                preference=None):  # area of flange plate should be greater than 1.05 times area of flange
        # 20 is the maximum spacing either side of the plate
        flange_crs_sec_area = tk * width
        self.design_status = True
        for y in list_of_pt_tk:
            if preference != None:
                if preference == "Outside":
                    outerwidth = width
                    flange_plate_crs_sec_area = y * width
                elif preference == "Outside + Inside":
                    outerwidth = width
                    innerwidth = (width - t_w - (2 * r_1)) / 2
                    if innerwidth < 50:
                        # logger.error(":Inner Plate not possible")
                        self.design_status = False
                    else:
                        self.design_status = True
                        flange_plate_crs_sec_area = (outerwidth + (2 * innerwidth)) * y
                if flange_plate_crs_sec_area >= flange_crs_sec_area * 1.05:
                    thickness = y
                    self.design_status = True
                    break
                else:
                    thickness = 0
                    self.design_status = False

            else:
                webwidth = D - (2 * tk) - (2 * r_1)
                web_crs_area = t_w * webwidth
                web_plate_crs_sec_area = 2 * webwidth * y
                if web_plate_crs_sec_area >= web_crs_area * 1.05:
                    thickness = y
                    self.design_status = True
                    break
                else:
                    thickness = 0
                    self.design_status = False
                # logger.error(":Inner Plate not possible")

        return thickness

    #     def web_force(column_d, column_f_t, column_t_w, axial_force, column_area):
    #         """
    #         Args:
    #            c_d: Overall depth of the column section in mm (float)
    #            column_f_t: Thickness of flange in mm (float)
    #            column_t_w: Thickness of flange in mm (float)
    #            axial_force: Factored axial force in kN (float)
    #
    #         Returns:
    #             Force in flange in kN (float)
    #         """
    #         axial_force_w = int(
    #             ((column_d - 2 * (column_f_t)) * column_t_w * axial_force * 10) / column_area)   # N
    #         return round(axial_force_w)

    # >>>>>>> 6cf73de1eccd9984a7eabbebc260495068a10335
    # def flange_force(column_d, column_f_t, column_b, column_area, factored_axial_force, moment_load):
    #     """
    #     Args:
    #        Column_d: Overall depth of the column section in mm (float)
    #        Column_b: width of the column section in mm (float)
    #        Column_f_t: Thickness of flange in mm (float)
    #        axial_force: Factored axial force in kN (float)
    #        moment_load: Factored bending moment in kN-m (float)
    #     Returns:
    #         Force in flange in kN (float)
    #     """
    #
    #     area_f = column_b * column_f_t
    #     axial_force_f = ((area_f * factored_axial_force * 1000 / (100 * column_area))) / 1000  # KN
    #     f_f = (((moment_load * 1000000) / (column_d - column_f_t)) + (axial_force_f * 1000)) / 1000  # KN
    #     # print(f_f)
    #     return (f_f)

    # print(self.web_bolt)
    # print(self.web_plate)
    # print(self.Tension_capacity_flange_plate)
    # print(self.Tension_capacity_flange)

    def call_3DModel(self, ui, bgcolor):
        # Call to calculate/create the BB Cover Plate Bolted CAD model
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.createBBCoverPlateBoltedCAD()
        #     self.ui.btn3D.setChecked(Qt.Checked)
        if ui.btn3D.isChecked():
            ui.chkBxCol.setChecked(Qt.Unchecked)
            ui.chkBxFinplate.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)

        # Call to display the BB Cover Plate Bolted CAD model
        #     ui.Commondisplay_3DModel("Model", bgcolor)  # "gradient_bg")
        ui.commLogicObj.display_3DModel("Model", bgcolor)

        # else:
        #     self.display.EraseAll()

    def call_3DColumn(self, ui, bgcolor):
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.ui.chkBx_beamSec1.setChecked(Qt.Checked)
        if ui.chkBxCol.isChecked():
            ui.btn3D.setChecked(Qt.Unchecked)
            ui.chkBxCol.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)
        # self.display_3DModel("Beam", bgcolor)
        ui.commLogicObj.display_3DModel("Column", bgcolor)

    def call_3DConnector(self, ui, bgcolor):
        # status = self.resultObj['Bolt']['status']
        # if status is True:
        #     self.ui.chkBx_extndPlate.setChecked(Qt.Checked)
        if ui.chkBxFinplate.isChecked():
            ui.btn3D.setChecked(Qt.Unchecked)
            ui.chkBxCol.setChecked(Qt.Unchecked)
            ui.mytabWidget.setCurrentIndex(0)
        # self.display_3DModel("Connector", bgcolor)
        ui.commLogicObj.display_3DModel("Connector", bgcolor)

    def tab_list(self):

        tabs = []

        t1 = (KEY_DISP_COLSEC, TYPE_TAB_1, self.tab_column_section)
        tabs.append(t1)

        t2 = ("Bolt", TYPE_TAB_2, self.bolt_values)
        tabs.append(t2)

        t3 = ("Weld", TYPE_TAB_2, self.weld_values)
        tabs.append(t3)

        t4 = ("Detailing", TYPE_TAB_2, self.detailing_values)
        tabs.append(t4)

        t5 = ("Design", TYPE_TAB_2, self.design_values)
        tabs.append(t5)

        t6 = ("Connector", TYPE_TAB_2, self.connector_values)
        tabs.append(t6)

        return tabs

    ################################ Design Report #####################################################################################

    def save_design(self, popup_summary):
        # bolt_list = str(*self.bolt.bolt_diameter, sep=", ")
        self.report_supporting = {KEY_DISP_SEC_PROFILE: "ISection",
                                  KEY_DISP_COLSEC: self.section.designation,
                                  KEY_DISP_MATERIAL: self.section.material,
                                  KEY_DISP_FU: self.section.fu,
                                  KEY_DISP_FY: self.section.fy,
                                  'Mass': self.section.mass,
                                  'Area(mm2) - A': self.section.area,
                                  'D(mm)': self.section.depth,
                                  'B(mm)': self.section.flange_width,
                                  't(mm)': self.section.web_thickness,
                                  'T(mm)': self.section.flange_thickness,
                                  'FlangeSlope': self.section.flange_slope,
                                  'R1(mm)': self.section.root_radius,
                                  'R2(mm)': self.section.toe_radius,
                                  'Iz(mm4)': self.section.mom_inertia_z,
                                  'Iy(mm4)': self.section.mom_inertia_y,
                                  'rz(mm)': self.section.rad_of_gy_z,
                                  'ry(mm)': self.section.rad_of_gy_y,
                                  'Zz(mm3)': self.section.elast_sec_mod_z,
                                  'Zy(mm3)': self.section.elast_sec_mod_y,
                                  'Zpz(mm3)': self.section.plast_sec_mod_z,
                                  'Zpy(mm3)': self.section.elast_sec_mod_y}

        self.report_input = \
            {KEY_MODULE: self.module,
             KEY_MAIN_MODULE: self.mainmodule,
             # KEY_CONN: self.connectivity,
             KEY_DISP_MOMENT: self.load.moment,
             KEY_DISP_SHEAR: self.load.shear_force,
             KEY_DISP_AXIAL: self.load.axial_force,

             # KEY_DISP_FAC_SHEAR_LOAD :round(self.fact_shear_load/1000,2),
             # KEY_DISP_FAC_AXIAL_FORCE : round(self.factored_axial_load/1000,2),
             # KEY_DISP_FAC_MOMENT_LOAD :round(self.load_moment/1000000.2),

             "Section": "TITLE",
             "Section Details": self.report_supporting,

             "Bolt Details": "TITLE",
             KEY_DISP_D: str(self.bolt.bolt_diameter),
             KEY_DISP_GRD: str(self.bolt.bolt_grade),
             KEY_DISP_TYP: self.bolt.bolt_type,
             KEY_DISP_DP_BOLT_HOLE_TYPE: self.bolt.bolt_hole_type,
             KEY_DISP_DP_BOLT_SLIP_FACTOR: self.bolt.mu_f,
             KEY_DISP_DP_DETAILING_EDGE_TYPE: self.bolt.edge_type,
             KEY_DISP_DP_DETAILING_GAP: self.flange_plate.gap,
             KEY_DISP_DP_DETAILING_CORROSIVE_INFLUENCES: self.bolt.corrosive_influences}

        self.report_check = []
        #####Outer plate#####
        flange_connecting_plates = [self.flange_plate.thickness_provided, self.section.flange_thickness]

        flange_bolt_shear_capacity_kn = round(self.flange_bolt.bolt_shear_capacity / 1000, 2)
        flange_bolt_bearing_capacity_kn = round(self.flange_bolt.bolt_bearing_capacity / 1000, 2)
        flange_bolt_capacity_kn = round(self.flange_bolt.bolt_capacity / 1000, 2)
        flange_kb_disp = round(self.flange_bolt.kb, 2)
        flange_kh_disp = round(self.flange_bolt.kh, 2)
        flange_bolt_force_kn = round(self.flange_plate.bolt_force, 2)
        flange_bolt_capacity_red_kn = round(self.flange_plate.bolt_capacity_red, 2)
        ########Inner plate#####
        innerflange_connecting_plates = [self.flange_plate.thickness_provided, self.section.flange_thickness]

        innerflange_bolt_shear_capacity_kn = round(self.flange_bolt.bolt_shear_capacity / 1000, 2)
        innerflange_bolt_bearing_capacity_kn = round(self.flange_bolt.bolt_bearing_capacity / 1000, 2)
        innerflange_bolt_capacity_kn = round(self.flange_bolt.bolt_capacity / 1000, 2)
        innerflange_kb_disp = round(self.flange_bolt.kb, 2)
        innerflange_kh_disp = round(self.flange_bolt.kh, 2)
        innerflange_bolt_force_kn = round(self.flange_plate.bolt_force, 2)
        innerflange_bolt_capacity_red_kn = round(self.flange_plate.bolt_capacity_red, 2)
        min_plate_length = (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

        t1 = ('SubSection', 'Member Capacity', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        t1 = (KEY_OUT_DISP_AXIAL_CAPACITY, '', axial_capacity(area=self.section.area, fy=self.section.fy,
                                                              gamma_m0=gamma_m0,
                                                              axial_capacity=round(self.axial_capacity / 1000, 2)),
              '')
        self.report_check.append(t1)
        h = self.section.depth - (2 * self.section.flange_thickness)
        self.shear_capacity1 = round(((self.section.depth - (
                2 * self.section.flange_thickness)) * self.section.web_thickness * self.section.fy) / (
                                             math.sqrt(3) * gamma_m0), 2)
        t1 = (KEY_OUT_DISP_SHEAR_CAPACITY, '',
              shear_capacity(h=h, t=self.section.web_thickness, f_y=self.section.fy, gamma_m0=gamma_m0,
                             shear_capacity=self.shear_capacity1 / 1000),
              '')
        self.Pmc = self.section.plastic_moment_capactiy
        self.report_check.append(t1)
        t1 = (KEY_OUT_DISP_PLASTIC_MOMENT_CAPACITY, '',
              plastic_moment_capacty(beta_b=self.beta_b, Z_p=self.Z_p, f_y=self.section.fy, gamma_m0=gamma_m0,
                                     Pmc=round(self.Pmc / 1000000, 2)), '')
        self.report_check.append(t1)
        self.Mdc = self.section.moment_d_def_criteria
        t1 = (KEY_OUT_DISP_MOMENT_D_DEFORMATION, '',
              moment_d_deformation_criteria(fy=self.section.fy, Z_e=self.section.elast_sec_mod_z,
                                            Mdc=round(self.Mdc / 1000000, 2)), '')
        self.report_check.append(t1)

        t1 = (KEY_OUT_DISP_MOMENT_CAPACITY, '',
              moment_capacity(Pmc=round(self.Pmc / 1000000, 2), Mdc=round(self.Mdc / 1000000, 2),
                              M_c=round(self.section.moment_capacity / 1000000, 2)), '')
        self.report_check.append(t1)

        t1 = ('SubSection', 'Load Considered', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        t1 = (KEY_DISP_APPLIED_AXIAL_FORCE, min_axial_capacity(axial_capacity=round(self.axial_capacity / 1000, 2),
                                                               min_ac=round(self.min_axial_load / 1000, 2)),
              prov_axial_load(axial_input=self.load.axial_force, min_ac=round(self.min_axial_load / 1000, 2),
                              app_axial_load=round(self.factored_axial_load / 1000, 2)),
              get_pass_fail(self.min_axial_load / 1000, self.factored_axial_load / 1000, relation='lesser'))
        self.report_check.append(t1)
        t1 = (KEY_DISP_APPLIED_SHEAR_LOAD, min_shear_capacity(shear_capacity=round(self.shear_capacity1 / 1000, 2),
                                                              min_sc=round(self.shear_load1 / 1000, 2)),
              prov_shear_load(shear_input=self.load.shear_force,
                              min_sc=round(self.shear_load1 / 1000, 2),
                              app_shear_load=round(self.fact_shear_load / 1000, 2)),
              get_pass_fail(self.shear_load1 / 1000, self.fact_shear_load / 1000, relation='lesser'))
        self.report_check.append(t1)

        t1 = (KEY_DISP_APPLIED_MOMENT_LOAD,
              min_moment_capacity(moment_capacity=round(self.section.moment_capacity / 1000000, 2),
                                  min_mc=round(self.load_moment_min / 1000000, 2)),
              prov_moment_load(moment_input=self.load.moment, min_mc=round(self.load_moment_min / 1000000, 2),
                               app_moment_load=round(self.load_moment / 1000000, 2)),
              get_pass_fail(round(self.load_moment_min / 1000000, 2), self.load_moment / 1000000,
                            relation="lesser"))
        self.report_check.append(t1)

        # "Flange plate Details": "TITLE"

        t1 = ('SubSection', 'Flange Bolt Checks', '|p{4cm}|p{5cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)

        if self.preference == "Outside":
            if self.flange_bolt.bolt_type == TYP_BEARING:
                t1 = (KEY_OUT_DISP_FLANGE_BOLT_SHEAR, '',
                      bolt_shear_prov(self.flange_bolt.bolt_fu, 1, self.flange_bolt.bolt_net_area,
                                      self.flange_bolt.gamma_mb, flange_bolt_shear_capacity_kn), '')
                self.report_check.append(t1)
                t2 = (KEY_OUT_DISP_FLANGE_BOLT_BEARING, '',
                      bolt_bearing_prov(flange_kb_disp, self.bolt.bolt_diameter_provided,
                                        self.bolt_conn_plates_t_fu_fy, self.flange_bolt.gamma_mb,
                                        flange_bolt_bearing_capacity_kn), '')
                self.report_check.append(t2)
                t3 = (KEY_OUT_DISP_FLANGE_BOLT_CAPACITY, '',
                      bolt_capacity_prov(flange_bolt_shear_capacity_kn, flange_bolt_bearing_capacity_kn,
                                         flange_bolt_capacity_kn),
                      '')
                self.report_check.append(t3)
            else:

                t4 = (KEY_OUT_DISP_FLANGE_BOLT_SLIP, '',
                      HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1, K_h=flange_kh_disp,
                                              fub=self.flange_bolt.bolt_fu,
                                              Anb=self.bolt.bolt_net_area, gamma_mf=self.web_bolt.gamma_mf,
                                              capacity=flange_bolt_capacity_kn), '')
                self.report_check.append(t4)
            t5 = (DISP_NUM_OF_BOLTS, get_trial_bolts(V_u=0.0, A_u=(round(self.flange_force / 1000, 2)),
                                                     bolt_capacity=flange_bolt_capacity_kn, multiple=2),
                  self.flange_plate.bolts_required, '')
            self.report_check.append(t5)
            t6 = (DISP_NUM_OF_COLUMNS, '', self.flange_plate.bolt_line, '')
            self.report_check.append(t6)
            t7 = (DISP_NUM_OF_ROWS, '', self.flange_plate.bolts_one_line, '')
            self.report_check.append(t7)
            t1 = (DISP_MIN_PITCH, min_pitch(self.bolt.bolt_diameter_provided),
                  self.flange_plate.pitch_provided,
                  get_pass_fail(self.flange_bolt.min_pitch, self.flange_plate.pitch_provided, relation='lesser'))
            self.report_check.append(t1)
            t1 = (DISP_MAX_PITCH, max_pitch(flange_connecting_plates),
                  self.flange_plate.pitch_provided,
                  get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.pitch_provided, relation='greater'))
            self.report_check.append(t1)
            t2 = (DISP_MIN_GAUGE, min_pitch(self.bolt.bolt_diameter_provided),
                  self.flange_plate.gauge_provided,
                  get_pass_fail(self.flange_bolt.min_gauge, self.flange_plate.gauge_provided, relation="lesser"))
            self.report_check.append(t2)
            t2 = (DISP_MAX_GAUGE, max_pitch(flange_connecting_plates),
                  self.flange_plate.gauge_provided,
                  get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.gauge_provided, relation="greater"))
            self.report_check.append(t2)
            t3 = (DISP_MIN_END, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
                  self.flange_plate.end_dist_provided,
                  get_pass_fail(self.flange_bolt.min_end_dist, self.flange_plate.end_dist_provided,
                                relation='lesser'))
            self.report_check.append(t3)
            t4 = (DISP_MAX_END, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
                  self.flange_plate.end_dist_provided,
                  get_pass_fail(self.flange_bolt.max_end_dist, self.flange_plate.end_dist_provided,
                                relation='greater'))
            self.report_check.append(t4)
            t3 = (DISP_MIN_EDGE, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
                  self.flange_plate.edge_dist_provided,
                  get_pass_fail(self.flange_bolt.min_edge_dist, self.flange_plate.edge_dist_provided,
                                relation='lesser'))
            self.report_check.append(t3)
            t4 = (DISP_MAX_EDGE, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
                  self.flange_plate.edge_dist_provided,
                  get_pass_fail(self.flange_bolt.max_edge_dist, self.flange_plate.edge_dist_provided,
                                relation="greater"))
            self.report_check.append(t4)
        else:
            if self.flange_bolt.bolt_type == TYP_BEARING:
                t1 = (KEY_OUT_DISP_FLANGE_BOLT_SHEAR, '',
                      bolt_shear_prov(self.flange_bolt.bolt_fu, 2, self.flange_bolt.bolt_net_area,
                                      self.flange_bolt.gamma_mb, innerflange_bolt_shear_capacity_kn), '')
                self.report_check.append(t1)
                t2 = (KEY_OUT_DISP_FLANGE_BOLT_BEARING, '',
                      bolt_bearing_prov(innerflange_kb_disp, self.bolt.bolt_diameter_provided,
                                        self.bolt_conn_plates_t_fu_fy, self.flange_bolt.gamma_mb,
                                        innerflange_bolt_bearing_capacity_kn), '')
                self.report_check.append(t2)
                t3 = (KEY_OUT_DISP_FLANGE_BOLT_CAPACITY, '',
                      bolt_capacity_prov(innerflange_bolt_shear_capacity_kn, innerflange_bolt_bearing_capacity_kn,
                                         innerflange_bolt_capacity_kn),
                      '')
                self.report_check.append(t3)
            else:

                t4 = (KEY_OUT_DISP_FLANGE_BOLT_SLIP, '',
                      HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1, K_h=innerflange_kh_disp,
                                              fub=self.flange_bolt.bolt_fu,
                                              Anb=self.bolt.bolt_net_area, gamma_mf=self.web_bolt.gamma_mf,
                                              capacity=innerflange_bolt_capacity_kn), '')
                self.report_check.append(t4)
            t5 = (DISP_NUM_OF_BOLTS, get_trial_bolts(V_u=0.0, A_u=(round(self.flange_force / 1000, 2)),
                                                     bolt_capacity=flange_bolt_capacity_kn, multiple=2),
                  self.flange_plate.bolts_required, '')
            self.report_check.append(t5)
            t6 = (DISP_NUM_OF_COLUMNS, '', self.flange_plate.bolt_line, '')
            self.report_check.append(t6)
            t7 = (DISP_NUM_OF_ROWS, '', self.flange_plate.bolts_one_line, '')
            self.report_check.append(t7)
            t1 = (DISP_MIN_PITCH, min_pitch(self.bolt.bolt_diameter_provided),
                  self.flange_plate.pitch_provided,
                  get_pass_fail(self.flange_bolt.min_pitch, self.flange_plate.pitch_provided, relation='lesser'))
            self.report_check.append(t1)
            t1 = (DISP_MAX_PITCH, max_pitch(innerflange_connecting_plates),
                  self.flange_plate.pitch_provided,
                  get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.pitch_provided,
                                relation='greater'))
            self.report_check.append(t1)
            t2 = (DISP_MIN_GAUGE, min_pitch(self.bolt.bolt_diameter_provided),
                  self.flange_plate.gauge_provided,
                  get_pass_fail(self.flange_bolt.min_gauge, self.flange_plate.gauge_provided, relation="lesser"))
            self.report_check.append(t2)
            t2 = (DISP_MAX_GAUGE, max_pitch(innerflange_connecting_plates),
                  self.flange_plate.gauge_provided,
                  get_pass_fail(self.flange_bolt.max_spacing, self.flange_plate.gauge_provided,
                                relation="greater"))
            self.report_check.append(t2)
            t3 = (DISP_MIN_END, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
                  self.flange_plate.end_dist_provided,
                  get_pass_fail(self.flange_bolt.min_end_dist, self.flange_plate.end_dist_provided,
                                relation='lesser'))
            self.report_check.append(t3)
            t4 = (DISP_MAX_END, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
                  self.flange_plate.end_dist_provided,
                  get_pass_fail(self.flange_bolt.max_end_dist, self.flange_plate.end_dist_provided,
                                relation='greater'))
            self.report_check.append(t4)
            t3 = (DISP_MIN_EDGE, min_edge_end(self.flange_bolt.dia_hole, self.bolt.edge_type),
                  self.flange_plate.edge_dist_provided,
                  get_pass_fail(self.flange_bolt.min_edge_dist, self.flange_plate.edge_dist_provided,
                                relation='lesser'))
            self.report_check.append(t3)
            t4 = (DISP_MAX_EDGE, max_edge_end(self.flange_plate.fy, self.flange_plate.thickness_provided),
                  self.flange_plate.edge_dist_provided,
                  get_pass_fail(self.flange_bolt.max_edge_dist, self.flange_plate.edge_dist_provided,
                                relation="greater"))
            self.report_check.append(t4)

        web_connecting_plates = [self.web_plate.thickness_provided, self.section.web_thickness]

        web_bolt_shear_capacity_kn = round(self.web_bolt.bolt_shear_capacity / 1000, 2)
        web_bolt_bearing_capacity_kn = round(self.web_bolt.bolt_bearing_capacity / 1000, 2)
        web_bolt_capacity_kn = round(self.web_bolt.bolt_capacity / 1000, 2)
        web_kb_disp = round(self.web_bolt.kb, 2)
        web_kh_disp = round(self.web_bolt.kh, 2)
        web_bolt_force_kn = round(self.web_plate.bolt_force / 1000, 2)
        web_bolt_capacity_red_kn = round(self.web_plate.bolt_capacity_red, 2)
        res_force = self.web_plate.bolt_force * self.web_plate.bolt_line * self.web_plate.bolts_one_line
        print("res_focce", res_force)

        t1 = ('SubSection', 'Web Bolt Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        if self.flange_bolt.bolt_type == TYP_BEARING:
            t1 = (
            KEY_OUT_DISP_WEB_BOLT_SHEAR, '', bolt_shear_prov(self.web_bolt.bolt_fu, 2, self.web_bolt.bolt_net_area,
                                                             self.web_bolt.gamma_mb, web_bolt_shear_capacity_kn),
            '')
            self.report_check.append(t1)
            t2 = (
            KEY_OUT_DISP_WEB_BOLT_BEARING, '', bolt_bearing_prov(web_kb_disp, self.bolt.bolt_diameter_provided,
                                                                 self.bolt_conn_plates_web_t_fu_fy,
                                                                 self.web_bolt.gamma_mb,
                                                                 web_bolt_bearing_capacity_kn), '')
            self.report_check.append(t2)
            t3 = (KEY_OUT_DISP_WEB_BOLT_CAPACITY, '',
                  bolt_capacity_prov(web_bolt_shear_capacity_kn, web_bolt_bearing_capacity_kn,
                                     web_bolt_capacity_kn),
                  '')
            self.report_check.append(t3)
        else:

            t4 = (KEY_OUT_DISP_WEB_BOLT_SLIP, '',
                  HSFG_bolt_capacity_prov(mu_f=self.bolt.mu_f, n_e=1, K_h=web_kh_disp, fub=self.web_bolt.bolt_fu,
                                          Anb=self.web_bolt.bolt_net_area, gamma_mf=self.web_bolt.gamma_mf,
                                          capacity=web_bolt_capacity_kn), '')
            self.report_check.append(t4)
        t5 = (DISP_NUM_OF_BOLTS,
              get_trial_bolts(V_u=round(self.fact_shear_load / 1000, 2), A_u=(round(self.axial_force_w / 1000, 2)),
                              bolt_capacity=web_bolt_capacity_kn,
                              multiple=2),
              self.web_plate.bolts_required, '')
        self.report_check.append(t5)  # todo no of bolts

        t6 = (DISP_NUM_OF_COLUMNS, '', self.web_plate.bolt_line, '')
        self.report_check.append(t6)

        t7 = (DISP_NUM_OF_ROWS, '', self.web_plate.bolts_one_line, '')
        self.report_check.append(t7)
        t1 = (DISP_MIN_PITCH, min_pitch(self.bolt.bolt_diameter_provided),
              self.web_plate.pitch_provided,
              get_pass_fail(self.web_bolt.min_pitch, self.web_plate.pitch_provided, relation='lesser'))
        self.report_check.append(t1)
        t1 = (DISP_MAX_PITCH, max_pitch(web_connecting_plates),
              self.web_plate.pitch_provided,
              get_pass_fail(self.web_bolt.max_spacing, self.web_plate.pitch_provided,
                            relation='greater'))
        self.report_check.append(t1)
        t2 = (DISP_MIN_GAUGE, min_pitch(self.bolt.bolt_diameter_provided),
              self.web_plate.gauge_provided,
              get_pass_fail(self.web_bolt.min_gauge, self.web_plate.gauge_provided, relation="lesser"))
        self.report_check.append(t2)
        t2 = (DISP_MAX_GAUGE, max_pitch(web_connecting_plates),
              self.web_plate.gauge_provided,
              get_pass_fail(self.flange_bolt.max_spacing, self.web_plate.gauge_provided,
                            relation="greater"))
        self.report_check.append(t2)
        t3 = (DISP_MIN_END, min_edge_end(self.web_bolt.dia_hole, self.bolt.edge_type),
              self.web_plate.end_dist_provided,
              get_pass_fail(self.web_bolt.min_end_dist, self.web_plate.end_dist_provided,
                            relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_END, max_edge_end(self.web_plate.fy, self.web_plate.thickness_provided),
              self.web_plate.end_dist_provided,
              get_pass_fail(self.web_bolt.max_end_dist, self.web_plate.end_dist_provided,
                            relation='greater'))
        self.report_check.append(t4)
        t3 = (DISP_MIN_EDGE, min_edge_end(self.web_bolt.dia_hole, self.bolt.edge_type),
              self.web_plate.edge_dist_provided,
              get_pass_fail(self.web_bolt.min_edge_dist, self.web_plate.edge_dist_provided,
                            relation='lesser'))
        self.report_check.append(t3)
        t4 = (DISP_MAX_EDGE, max_edge_end(self.web_plate.fy, self.web_plate.thickness_provided),
              self.web_plate.edge_dist_provided,
              get_pass_fail(self.web_bolt.max_edge_dist, self.web_plate.edge_dist_provided,
                            relation="greater"))
        self.report_check.append(t4)
        ######Flange plate check####
        if self.preference == "Outside":
            t1 = ('SubSection', 'Outer flange plate Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)

            t1 = (DISP_MIN_PLATE_HEIGHT, min_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                 min_flange_plate_ht=self.min_plate_height),
                  self.flange_plate.height,
                  get_pass_fail(self.min_plate_height, self.flange_plate.height, relation="lesser"))
            self.report_check.append(t1)

            min_plate_length = 2 * (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                        2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

            t1 = (DISP_MIN_PLATE_LENGTH, min_flange_plate_length_req(min_pitch=self.flange_bolt.min_pitch,
                                                                     min_end_dist=self.flange_bolt.min_end_dist,
                                                                     bolt_line=self.flange_plate.bolt_line,
                                                                     min_length=min_plate_length,
                                                                     gap=self.flange_plate.gap),
                  self.flange_plate.length,
                  get_pass_fail(min_plate_length, self.flange_plate.length, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MIN_PLATE_THICK, min_plate_thk_req(self.section.flange_thickness),
                  self.flange_plate.thickness_provided,
                  get_pass_fail(self.section.flange_thickness, self.flange_plate.thickness_provided,
                                relation="lesser"))
            self.report_check.append(t1)
        else:
            t1 = ('SubSection', 'Inner and Outer flange plate Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)

            t1 = (DISP_MIN_PLATE_HEIGHT, min_inner_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                       web_thickness=self.section.web_thickness,
                                                                       root_radius=self.section.root_radius,
                                                                       min_inner_flange_plate_ht=self.flange_plate.Innerheight),
                  self.flange_plate.Innerheight,
                  get_pass_fail(self.flange_plate.Innerheight, self.flange_plate.Innerheight, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MAX_PLATE_HEIGHT, min_inner_flange_plate_ht_req(beam_width=self.section.flange_width,
                                                                       web_thickness=self.section.web_thickness,
                                                                       root_radius=self.section.root_radius,
                                                                       min_inner_flange_plate_ht=self.flange_plate.Innerheight),
                  self.flange_plate.Innerheight,
                  get_pass_fail(self.flange_plate.Innerheight, self.flange_plate.Innerheight, relation="lesser"))
            self.report_check.append(t1)

            min_plate_length = 2 * (((self.flange_plate.bolt_line / 2 - 1) * self.flange_bolt.min_pitch) + (
                    2 * self.flange_bolt.min_end_dist) + (self.flange_plate.gap / 2))

            t1 = (DISP_MIN_PLATE_LENGTH, min_flange_plate_length_req(min_pitch=self.flange_bolt.min_pitch,
                                                                     min_end_dist=self.flange_bolt.min_end_dist,
                                                                     bolt_line=self.flange_plate.bolt_line,
                                                                     min_length=min_plate_length,
                                                                     gap=self.flange_plate.gap),
                  self.flange_plate.length,
                  get_pass_fail(min_plate_length, self.flange_plate.length, relation="lesser"))
            self.report_check.append(t1)
            t1 = (DISP_MIN_PLATE_THICK, min_plate_thk_req(self.section.flange_thickness / 2),
                  self.flange_plate.thickness_provided,
                  get_pass_fail(self.section.flange_thickness / 2, self.flange_plate.thickness_provided,
                                relation="lesser"))
            self.report_check.append(t1)

        ###################
        # Member Capacities
        ###################
        ### Flange Check ###
        t1 = ('SubSection', 'Member Checks', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

        t1 = (KEY_DISP_TENSIONYIELDINGCAP_FLANGE, '',
              tension_yield_prov(self.flange_plate.height, self.section.flange_thickness, self.section.fy, gamma_m0,
                                 round(self.section.tension_yielding_capacity / 1000, 2)), '')
        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        t1 = (
            KEY_DISP_TENSIONRUPTURECAP_FLANGE, '',
            tension_rupture_prov(self.flange_plate.height, self.section.flange_thickness,
                                 self.flange_plate.bolts_one_line, self.flange_bolt.dia_hole,
                                 self.section.fu, gamma_m1,
                                 round(self.section.tension_rupture_capacity / 1000,
                                       2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_BLOCKSHEARCAP_FLANGE, '', round(self.section.block_shear_capacity / 1000, 2), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_FLANGE_TEN_CAPACITY, round(self.flange_force / 1000, 2),
              tensile_capacity_prov(round(self.section.tension_yielding_capacity / 1000, 2),
                                    round(self.section.tension_rupture_capacity / 1000, 2),
                                    round(self.section.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.flange_force / 1000, 2),
                            round(self.section.tension_capacity_flange / 1000, 2), relation="lesser"))
        self.report_check.append(t1)

        ### web Check ###
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        # A_v_web = (self.section.depth - 2 * self.section.flange_thickness) * self.section.web_thickness
        webheight = (self.section.depth - 2 * self.section.flange_thickness)
        t1 = (KEY_DISP_TENSIONYIELDINGCAP_WEB, '',
              tension_yield_prov(webheight, self.section.web_thickness, self.section.fy, gamma_m0,
                                 round(self.section.tension_yielding_capacity_web / 1000, 2)), '')
        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        t1 = (KEY_DISP_TENSIONRUPTURECAP_WEB, '',
              tension_rupture_prov(webheight, self.section.web_thickness,
                                   self.web_plate.bolts_one_line, self.web_bolt.dia_hole,
                                   self.section.fu, gamma_m1,
                                   round(self.section.tension_rupture_capacity_web / 1000,
                                         2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_BLOCKSHEARCAP_WEB, '', round(self.section.block_shear_capacity_web / 1000, 2), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_WEB_TEN_CAPACITY, round(self.axial_force_w / 1000, 2),
              tensile_capacity_prov(round(self.section.tension_yielding_capacity_web / 1000, 2),
                                    round(self.section.tension_rupture_capacity_web / 1000, 2),
                                    round(self.section.block_shear_capacity_web / 1000, 2)),
              get_pass_fail(round(self.axial_force_w / 1000, 2), round(self.section.tension_capacity_web / 1000, 2),
                            relation="lesser"))
        self.report_check.append(t1)
        ###################
        # Flange plate Capacities check
        ###################
        if self.preference == "Outside":

            t1 = (
            'SubSection', 'Flange Plate Capacity Checks in axial-Outside ', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)
            gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

            t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '',
                  tension_yield_prov(self.flange_plate.height, self.flange_plate.thickness_provided,
                                     self.flange_plate.fy, gamma_m0,
                                     round(self.flange_plate.tension_yielding_capacity / 1000, 2)), '')
            self.report_check.append(t1)
            gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
            t1 = (
                KEY_DISP_TENSION_RUPTURECAPACITY, '',
                tension_rupture_prov(self.flange_plate.height, self.flange_plate.thickness_provided,
                                     self.flange_plate.bolts_one_line, self.flange_bolt.dia_hole,
                                     self.flange_plate.fu, gamma_m1,
                                     round(self.flange_plate.tension_rupture_capacity / 1000,
                                           2)), '')
            self.report_check.append(t1)

            t1 = (
            KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '', round(self.flange_plate.block_shear_capacity / 1000, 2), '')
            self.report_check.append(t1)

            t1 = (KEY_DISP_FLANGE_PLATE_TEN_CAP, round(self.flange_force / 1000, 2),
                  tensile_capacity_prov(round(self.flange_plate.tension_yielding_capacity / 1000, 2),
                                        round(self.flange_plate.tension_rupture_capacity / 1000, 2),
                                        round(self.flange_plate.block_shear_capacity / 1000, 2)),
                  get_pass_fail(round(self.flange_force / 1000, 2),
                                round(self.flange_plate.tension_capacity_flange_plate / 1000, 2),
                                relation="lesser"))
            self.report_check.append(t1)
        else:
            t1 = ('SubSection', 'Flange Plate Capacity Checks in axial-Outside/Inside ',
                  '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
            self.report_check.append(t1)
            gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
            total_height = self.flange_plate.height + (2 * self.flange_plate.Innerheight)
            t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '',
                  tension_yield_prov(total_height, self.flange_plate.thickness_provided,
                                     self.flange_plate.fy, gamma_m0,
                                     round(self.flange_plate.tension_yielding_capacity / 1000, 2)), '')
            self.report_check.append(t1)
            gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
            t1 = (KEY_DISP_TENSION_RUPTURECAPACITY, '',
                  tension_rupture_prov(total_height, self.flange_plate.thickness_provided,
                                       self.flange_plate.bolts_one_line, self.flange_bolt.dia_hole,
                                       self.flange_plate.fu, gamma_m1,
                                       round(self.flange_plate.tension_rupture_capacity / 1000,
                                             2)), '')
            self.report_check.append(t1)
            t1 = (
            KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '', round(self.flange_plate.block_shear_capacity / 1000, 2), '')
            self.report_check.append(t1)

            t1 = (KEY_DISP_FLANGE_PLATE_TEN_CAP, round(self.flange_force / 1000, 2),
                  tensile_capacity_prov(round(self.flange_plate.tension_yielding_capacity / 1000, 2),
                                        round(self.flange_plate.tension_rupture_capacity / 1000, 2),
                                        round(self.flange_plate.block_shear_capacity / 1000, 2)),
                  get_pass_fail(round(self.flange_force / 1000, 2),
                                round(self.flange_plate.tension_capacity_flange_plate / 1000, 2),
                                relation="lesser"))
            self.report_check.append(t1)

        ###################
        # Web plate Capacities check axial
        ###################
        t1 = ('SubSection', 'Web Plate Capacity Checks in Axial', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

        t1 = (KEY_DISP_TENSION_YIELDCAPACITY, '',
              tension_yield_prov(self.web_plate.height, self.web_plate.thickness_provided, self.web_plate.fy,
                                 gamma_m0,
                                 round(self.web_plate.tension_yielding_capacity / 1000, 2)), '')
        self.report_check.append(t1)
        gamma_m1 = IS800_2007.cl_5_4_1_Table_5["gamma_m1"]['ultimate_stress']
        t1 = (KEY_DISP_TENSION_RUPTURECAPACITY, '',
              tension_rupture_prov(self.web_plate.height, self.web_plate.thickness_provided,
                                   self.web_plate.bolts_one_line, self.web_bolt.dia_hole,
                                   self.web_bolt.fu, gamma_m1,
                                   round(self.web_plate.tension_rupture_capacity / 1000,
                                         2)), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_TENSION_BLOCKSHEARCAPACITY, '', round(self.web_plate.block_shear_capacity / 1000, 2), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_TEN_CAP_WEB_PLATE, round(self.axial_force_w / 1000, 2),
              tensile_capacity_prov(round(self.web_plate.tension_yielding_capacity / 1000, 2),
                                    round(self.web_plate.tension_rupture_capacity / 1000, 2),
                                    round(self.web_plate.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.axial_force_w / 1000, 2),
                            round(self.web_plate.tension_capacity_web_plate / 1000, 2),
                            relation="lesser"))
        self.report_check.append(t1)

        ###################
        # Web plate Capacities check Shear
        ###################
        t1 = ('SubSection', 'Web Plate Capacity Checks in Shear', '|p{4cm}|p{6cm}|p{5.5cm}|p{1.5cm}|')
        self.report_check.append(t1)

        t1 = (KEY_DISP_SHEAR_YLD, '', shear_yield_prov(self.web_plate.height, self.web_plate.thickness_provided,
                                                       self.web_plate.fy, gamma_m0,
                                                       round(self.web_plate.shear_yielding_capacity / 1000, 2)),
              '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_SHEAR_RUP, '', shear_rupture_prov(self.web_plate.height, self.web_plate.thickness_provided,
                                                         self.web_plate.bolt_line / 2, self.web_bolt.dia_hole,
                                                         self.web_plate.fu,
                                                         round(self.web_plate.shear_rupture_capacity / 1000, 2),
                                                         multiple=0.9),
              '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_PLATE_BLK_SHEAR_SHEAR, '', round(self.web_plate.block_shear_capacity_shear / 1000, 2), '')
        self.report_check.append(t1)

        t1 = (KEY_DISP_WEBPLATE_SHEAR_CAPACITY, round(self.fact_shear_load / 1000, 2),
              shear_capacity_prov(round(self.web_plate.shear_yielding_capacity / 1000, 2),
                                  round(self.web_plate.shear_rupture_capacity / 1000, 2),
                                  round(self.web_plate.block_shear_capacity / 1000, 2)),
              get_pass_fail(round(self.fact_shear_load / 1000, 2),
                            round(self.web_plate.shear_capacity_web_plate / 1000, 2), relation="lesser"))
        self.report_check.append(t1)

        Disp_3D_image = "./ResourceFiles/images/3d.png"

        config = configparser.ConfigParser()
        config.read_file(open(r'Osdag.config'))
        desktop_path = config.get("desktop_path", "path1")
        print("desk:", desktop_path)
        print(sys.path[0])
        rel_path = str(sys.path[0])
        rel_path = rel_path.replace("\\", "/")

        file_type = "PDF (*.pdf)"
        filename = QFileDialog.getSaveFileName(QFileDialog(), "Save File As",
                                               os.path.join(str(' '), "untitled.pdf"), file_type)
        print(filename, "hhhhhhhhhhhhhhhhhhhhhhhhhhh")
        # filename = os.path.join(str(folder), "images_html", "TexReport")
        file_name = str(filename)
        print(file_name, "hhhhhhhhhhhhhhhhhhhhhhhhhhh")
        fname_no_ext = filename[0].split(".")[0]
        print(fname_no_ext, "hhhhhhhhhhhhhhhhhhhhhhhhhhh")
        CreateLatex.save_latex(CreateLatex(), self.report_input, self.report_check, popup_summary, fname_no_ext,
                               rel_path, Disp_3D_image)

