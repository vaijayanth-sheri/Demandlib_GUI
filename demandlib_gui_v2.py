import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import demandlib.bdew as bdew
import demandlib.particular_profiles as profiles
from PyQt5 import QtWidgets
import holidays
from datetime import time as settime

class Ui_Form(object):

    # defining the global variables
    input_country = None
    input_country_2 = None
    input_state = None
    input_state_2 = None
    input_year = None
    input_year_2 = None
    input_temp_column = None
    input_house_type = None
    input_annual_demand_heat = None
    input_annual_demand_elec = None
    input_building_class = None
    input_wind_class = None
    input_WWload = None
    input_profile_type = None
    dataframe = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 524)
        self.Demand = QtWidgets.QTabWidget(Form)
        self.Demand.setGeometry(QtCore.QRect(0, 0, 651, 521))
        self.Demand.setMinimumSize(QtCore.QSize(651, 521))
        self.Demand.setMaximumSize(QtCore.QSize(651, 521))
        self.Demand.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Demand.setObjectName("Demand")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_heat_simulate = QtWidgets.QPushButton(self.tab)
        self.pushButton_heat_simulate.setGeometry(QtCore.QRect(340, 440, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_heat_simulate.setFont(font)
        self.pushButton_heat_simulate.setObjectName("pushButton_heat_simulate")

        # connection to heat simulation button
        self.pushButton_heat_simulate.clicked.connect(self.solve_heat_demand)

        self.label_Heat_demand = QtWidgets.QLabel(self.tab)
        self.label_Heat_demand.setGeometry(QtCore.QRect(260, 11, 101, 19))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_Heat_demand.setFont(font)
        self.label_Heat_demand.setObjectName("label_Heat_demand")
        self.pushButton_heat_inputs = QtWidgets.QPushButton(self.tab)
        self.pushButton_heat_inputs.setGeometry(QtCore.QRect(130, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_heat_inputs.setFont(font)
        self.pushButton_heat_inputs.setObjectName("pushButton_heat_inputs")

        # connection to heat simulation button
        self.pushButton_heat_inputs.clicked.connect(self.country)
        self.pushButton_heat_inputs.clicked.connect(self.state)
        self.pushButton_heat_inputs.clicked.connect(self.year)
        self.pushButton_heat_inputs.clicked.connect(self.temp_column)
        self.pushButton_heat_inputs.clicked.connect(self.house_type)
        self.pushButton_heat_inputs.clicked.connect(self.demand_value_heat)
        self.pushButton_heat_inputs.clicked.connect(self.building_class)
        self.pushButton_heat_inputs.clicked.connect(self.wind_class)
        self.pushButton_heat_inputs.clicked.connect(self.ww_load)

        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(50, 50, 541, 371))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.label_country = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_country.setFont(font)
        self.label_country.setObjectName("label_country")
        self._2.addWidget(self.label_country)
        self.lineEdit_country = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_country.setFont(font)
        self.lineEdit_country.setObjectName("lineEdit_country")
        self._2.addWidget(self.lineEdit_country)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._2.addItem(spacerItem)
        self.label_subdivision = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_subdivision.setFont(font)
        self.label_subdivision.setObjectName("label_subdivision")
        self._2.addWidget(self.label_subdivision)
        self.lineEdit_state = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_state.setFont(font)
        self.lineEdit_state.setObjectName("lineEdit_state")
        self._2.addWidget(self.lineEdit_state)
        self.verticalLayout.addLayout(self._2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_year = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName("label_year")
        self.horizontalLayout_2.addWidget(self.label_year)
        self.lineEdit_year = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_year.sizePolicy().hasHeightForWidth())
        self.lineEdit_year.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_year.setFont(font)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.horizontalLayout_2.addWidget(self.lineEdit_year)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_temp_column = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_temp_column.setFont(font)
        self.label_temp_column.setObjectName("label_temp_column")
        self.horizontalLayout_3.addWidget(self.label_temp_column)
        self.lineEdit_temp_column = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_temp_column.setFont(font)
        self.lineEdit_temp_column.setObjectName("lineEdit_temp_column")
        self.horizontalLayout_3.addWidget(self.lineEdit_temp_column)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_house = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_house.setFont(font)
        self.label_house.setObjectName("label_house")
        self.horizontalLayout_4.addWidget(self.label_house)
        self.comboBox_house_type = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_house_type.setFont(font)
        self.comboBox_house_type.setEditable(True)
        self.comboBox_house_type.setObjectName("comboBox_house_type")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.comboBox_house_type.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_house_type)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_annual_heat = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_annual_heat.setFont(font)
        self.label_annual_heat.setObjectName("label_annual_heat")
        self.horizontalLayout_5.addWidget(self.label_annual_heat)
        self.lineEdit_heat_demand = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_heat_demand.setFont(font)
        self.lineEdit_heat_demand.setObjectName("lineEdit_heat_demand")
        self.horizontalLayout_5.addWidget(self.lineEdit_heat_demand)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_building = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_building.setFont(font)
        self.label_building.setObjectName("label_building")
        self.horizontalLayout_7.addWidget(self.label_building)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_wind = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_wind.setFont(font)
        self.label_wind.setObjectName("label_wind")
        self.horizontalLayout_6.addWidget(self.label_wind)
        self.comboBox_windclass = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_windclass.setFont(font)
        self.comboBox_windclass.setObjectName("comboBox_windclass")
        self.comboBox_windclass.addItem("")
        self.comboBox_windclass.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_windclass)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_ww = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ww.setFont(font)
        self.label_ww.setObjectName("label_ww")
        self.horizontalLayout_8.addWidget(self.label_ww)
        self.comboBox_ww_load = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_ww_load.setFont(font)
        self.comboBox_ww_load.setObjectName("comboBox_ww_load")
        self.comboBox_ww_load.addItem("")
        self.comboBox_ww_load.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_ww_load)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_weather = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.horizontalLayout_9.addWidget(self.label_weather)
        self.pushButton_upload = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upload.sizePolicy().hasHeightForWidth())
        self.pushButton_upload.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_upload.setFont(font)
        self.pushButton_upload.setObjectName("pushButton_upload")

        # connection to the upload button
        self.pushButton_upload.clicked.connect(self.upload_dataframe)

        self.horizontalLayout_9.addWidget(self.pushButton_upload)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.Demand.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_Elec_demand = QtWidgets.QLabel(self.tab_2)
        self.label_Elec_demand.setGeometry(QtCore.QRect(230, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_Elec_demand.setFont(font)
        self.label_Elec_demand.setObjectName("label_Elec_demand")
        self.pushButton_elec_simulate = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_elec_simulate.setGeometry(QtCore.QRect(330, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_elec_simulate.setFont(font)
        self.pushButton_elec_simulate.setObjectName("pushButton_elec_simulate")

        # connection to the electricity simulation button
        self.pushButton_elec_simulate.clicked.connect(self.solve_elec_demand)

        self.pushButton_elec_inputs = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_elec_inputs.setGeometry(QtCore.QRect(130, 390, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_elec_inputs.setFont(font)
        self.pushButton_elec_inputs.setObjectName("pushButton_elec_inputs")

        # connection to the electricity simulation button
        self.pushButton_elec_inputs.clicked.connect(self.country_2)
        self.pushButton_elec_inputs.clicked.connect(self.state_2)
        self.pushButton_elec_inputs.clicked.connect(self.year_2)
        self.pushButton_elec_inputs.clicked.connect(self.profile_type)
        self.pushButton_elec_inputs.clicked.connect(self.demand_value_elec)

        self.widget1 = QtWidgets.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(40, 90, 581, 241))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_country_code = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_country_code.setFont(font)
        self.label_country_code.setObjectName("label_country_code")
        self.horizontalLayout.addWidget(self.label_country_code)
        self.lineEdit_country_2 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_country_2.setFont(font)
        self.lineEdit_country_2.setObjectName("lineEdit_country_2")
        self.horizontalLayout.addWidget(self.lineEdit_country_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_state = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.horizontalLayout.addWidget(self.label_state)
        self.lineEdit_state_2 = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_state_2.setFont(font)
        self.lineEdit_state_2.setObjectName("lineEdit_state_2")
        self.horizontalLayout.addWidget(self.lineEdit_state_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_year_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_year_2.setFont(font)
        self.label_year_2.setObjectName("label_year_2")
        self.horizontalLayout_10.addWidget(self.label_year_2)
        self.lineEdit_year_2 = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_year_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_year_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_year_2.setFont(font)
        self.lineEdit_year_2.setObjectName("lineEdit_year_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_year_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_annual_elec = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_annual_elec.setFont(font)
        self.label_annual_elec.setObjectName("label_annual_elec")
        self.horizontalLayout_21.addWidget(self.label_annual_elec)
        self.lineEdit_elec_demand = QtWidgets.QLineEdit(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_elec_demand.sizePolicy().hasHeightForWidth())
        self.lineEdit_elec_demand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_elec_demand.setFont(font)
        self.lineEdit_elec_demand.setObjectName("lineEdit_elec_demand")
        self.horizontalLayout_21.addWidget(self.lineEdit_elec_demand)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_profile = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_profile.setFont(font)
        self.label_profile.setObjectName("label_profile")
        self.horizontalLayout_20.addWidget(self.label_profile)
        self.comboBox_profile_type = QtWidgets.QComboBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_profile_type.sizePolicy().hasHeightForWidth())
        self.comboBox_profile_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_profile_type.setFont(font)
        self.comboBox_profile_type.setEditable(True)
        self.comboBox_profile_type.setObjectName("comboBox_profile_type")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.comboBox_profile_type.addItem("")
        self.horizontalLayout_20.addWidget(self.comboBox_profile_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.Demand.addTab(self.tab_2, "")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(700, 90, 351, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        self.Demand.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_heat_simulate.setText(_translate("Form", "Simulate"))
        self.label_Heat_demand.setText(_translate("Form", "Heat Demand"))
        self.pushButton_heat_inputs.setText(_translate("Form", "Load inputs"))
        self.label_country.setText(_translate("Form", "Country Code:"))
        self.lineEdit_country.setPlaceholderText(_translate("Form", "Ex: DE"))
        self.label_subdivision.setText(_translate("Form", "Subdivision/State:"))
        self.lineEdit_state.setPlaceholderText(_translate("Form", "Ex: TH"))
        self.label_year.setText(_translate("Form", "Year: "))
        self.lineEdit_year.setPlaceholderText(_translate("Form", "Ex: 2023"))
        self.label_temp_column.setText(_translate("Form", "Temperature column name:"))
        self.lineEdit_temp_column.setPlaceholderText(_translate("Form", "Ex: Temperature"))
        self.label_house.setText(_translate("Form", "House Type:"))
        self.comboBox_house_type.setCurrentText(_translate("Form", "Please choose"))
        self.comboBox_house_type.setPlaceholderText(_translate("Form", "Please choose"))
        self.comboBox_house_type.setItemText(0, _translate("Form", "EFH (single family house)"))
        self.comboBox_house_type.setItemText(1, _translate("Form", "MFH (multi family house)"))
        self.comboBox_house_type.setItemText(2, _translate("Form", "GMK (metal and automotive)"))
        self.comboBox_house_type.setItemText(3, _translate("Form", "GHA (retail and wholesale)"))
        self.comboBox_house_type.setItemText(4, _translate("Form", "GKO (Local authorities, credit institutions and insurance companies)"))
        self.comboBox_house_type.setItemText(5, _translate("Form", "GBD (other operational services)"))
        self.comboBox_house_type.setItemText(6, _translate("Form", "GGA (restaurants)"))
        self.comboBox_house_type.setItemText(7, _translate("Form", "GBH (accommodation)"))
        self.comboBox_house_type.setItemText(8, _translate("Form", "GWA (laundries, dry cleaning)"))
        self.comboBox_house_type.setItemText(9, _translate("Form", "GGB (horticulture)"))
        self.comboBox_house_type.setItemText(10, _translate("Form", "GBA (bakery)"))
        self.comboBox_house_type.setItemText(11, _translate("Form", "GPD (paper and printing)"))
        self.comboBox_house_type.setItemText(12, _translate("Form", "GMF (household-like business enterprises)"))
        self.comboBox_house_type.setItemText(13, _translate("Form", "GHD (Total load profile Business/Commerce/Services)"))
        self.label_annual_heat.setText(_translate("Form", "Annual Heat Demand:"))
        self.lineEdit_heat_demand.setPlaceholderText(_translate("Form", "Heat demand/year in kWh (eg: 10000)"))
        self.label_building.setText(_translate("Form", "Building Class:"))
        self.comboBox.setItemText(0, _translate("Form", "11 (2010 -  present)"))
        self.comboBox.setItemText(1, _translate("Form", "10 (2002 - 2009)"))
        self.comboBox.setItemText(2, _translate("Form", "9 (1995 - 2001)"))
        self.comboBox.setItemText(3, _translate("Form", "8 (1984 - 1994)"))
        self.comboBox.setItemText(4, _translate("Form", "7 (1979 - 1983)"))
        self.comboBox.setItemText(5, _translate("Form", "6 (1969 - 1978)"))
        self.comboBox.setItemText(6, _translate("Form", "5 (1958 - 1968)"))
        self.comboBox.setItemText(7, _translate("Form", "4 (1949 - 1957)"))
        self.comboBox.setItemText(8, _translate("Form", "3 (1919 - 1948)"))
        self.comboBox.setItemText(9, _translate("Form", "2 (1860 - 1918)"))
        self.comboBox.setItemText(10, _translate("Form", "1 (         - 1859)"))
        self.label_wind.setText(_translate("Form", "Wind class:"))
        self.comboBox_windclass.setItemText(0, _translate("Form", "0 (not windy)"))
        self.comboBox_windclass.setItemText(1, _translate("Form", "1 (windy)"))
        self.label_ww.setText(_translate("Form", "Warm Water Load:"))
        self.comboBox_ww_load.setItemText(0, _translate("Form", "False"))
        self.comboBox_ww_load.setItemText(1, _translate("Form", "True"))
        self.label_weather.setText(_translate("Form", "Weather data file:"))
        self.pushButton_upload.setText(_translate("Form", "upload"))
        self.Demand.setTabText(self.Demand.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.label_Elec_demand.setText(_translate("Form", "Electricity Demand"))
        self.pushButton_elec_simulate.setText(_translate("Form", "Simulate"))
        self.pushButton_elec_inputs.setText(_translate("Form", "Load inputs"))
        self.label_country_code.setText(_translate("Form", "Country Code:"))
        self.lineEdit_country_2.setPlaceholderText(_translate("Form", "Ex: DE"))
        self.label_state.setText(_translate("Form", "Subdivision/State:"))
        self.lineEdit_state_2.setPlaceholderText(_translate("Form", "Ex: TH"))
        self.label_year_2.setText(_translate("Form", "Year:"))
        self.lineEdit_year_2.setPlaceholderText(_translate("Form", "Ex: 2023"))
        self.label_annual_elec.setText(_translate("Form", "Annual Electricity Demand:"))
        self.lineEdit_elec_demand.setPlaceholderText(_translate("Form", "Elec demand/year in kWh (eg: 10000)"))
        self.label_profile.setText(_translate("Form", "Profile Type:"))
        self.comboBox_profile_type.setCurrentText(_translate("Form", "Please choose"))
        self.comboBox_profile_type.setPlaceholderText(_translate("Form", "Please choose"))
        self.comboBox_profile_type.setItemText(0, _translate("Form", "G0-General trade/business/commerce"))
        self.comboBox_profile_type.setItemText(1, _translate("Form", "G1-Business on weekdays 8 a.m. - 6 p.m."))
        self.comboBox_profile_type.setItemText(2, _translate("Form", "G2-Businesses with heavy to predominant consumption in the evening hours"))
        self.comboBox_profile_type.setItemText(3, _translate("Form", "G3-Continuous business"))
        self.comboBox_profile_type.setItemText(4, _translate("Form", "G4-Shop/barber shop"))
        self.comboBox_profile_type.setItemText(5, _translate("Form", "G5-Bakery with bakery"))
        self.comboBox_profile_type.setItemText(6, _translate("Form", "G6-Weekend operation"))
        self.comboBox_profile_type.setItemText(7, _translate("Form", "G7-Mobile phone transmitter station"))
        self.comboBox_profile_type.setItemText(8, _translate("Form", "L0-General farms"))
        self.comboBox_profile_type.setItemText(9, _translate("Form", "L1-Farms with dairy farming/part-time livestock farming"))
        self.comboBox_profile_type.setItemText(10, _translate("Form", "L2-Other farms"))
        self.comboBox_profile_type.setItemText(11, _translate("Form", "H0/H0_dyn-Household/dynamic houshold"))
        self.Demand.setTabText(self.Demand.indexOf(self.tab_2), _translate("Form", "Tab 2"))


    # function for country
    def country(self):
        input_country = self.lineEdit_country.text()
        self.input_country = input_country
        # print(input_country)
        self.plainTextEdit.appendPlainText(f"Country :{input_country}")
        return input_country

    def country_2(self):
        input_country_2 = self.lineEdit_country_2.text()
        self.input_country_2 = input_country_2
        # print(input_country_2)
        self.plainTextEdit.appendPlainText(f"Country :{input_country_2}")
        return input_country_2

    def state(self):
        input_state = self.lineEdit_state.text()
        self.input_state = input_state
        # print(input_state)
        self.plainTextEdit.appendPlainText(f"State :{input_state}")
        return input_state

    def state_2(self):
        input_state_2 = self.lineEdit_state_2.text()
        self.input_state_2 = input_state_2
        # print(input_state_2)
        self.plainTextEdit.appendPlainText(f"State :{input_state_2}")
        return input_state_2

    def year(self):
        input_year = self.lineEdit_year.text()
        try:
            self.input_year = int(input_year)
            # print(input_year)
            self.plainTextEdit.appendPlainText(f"Year :{input_year}")
            return input_year
        except ValueError:
            #print("invalid value for year")
            self.plainTextEdit.appendPlainText("invalid value for year")

    def year_2(self):
        input_year_2 = self.lineEdit_year_2.text()
        try:
            self.input_year_2 = int(input_year_2)
            # print(input_year_2)
            self.plainTextEdit.appendPlainText(f"Year :{input_year_2}")
            return input_year_2
        except ValueError:
            #print("invalid value for year")
            self.plainTextEdit.appendPlainText("invalid value for year")

    def temp_column(self):
        input_temp_column = self.lineEdit_temp_column.text()
        self.input_temp_column = input_temp_column
        # print(input_temp_column)
        self.plainTextEdit.appendPlainText(f"Temp column :{input_temp_column}")
        return (input_temp_column)

    def house_type(self):
        house_type_selection = self.comboBox_house_type.currentText()

        if house_type_selection == 'EFH (single family house)':
            input_house_type = 'EFH'
        if house_type_selection == 'MFH (multi family house)':
            input_house_type = 'MFH'
        if house_type_selection == 'GMK (metal and automotive)':
            input_house_type = 'GMK'
        if house_type_selection == 'GHA (retail and wholesale)':
            input_house_type = 'GHA'
        if house_type_selection == 'GKO (Local authorities, credit institutions and insurance companies)':
            input_house_type = 'GKO'
        if house_type_selection == 'GBD (other operational services)':
            input_house_type = 'GBD'
        if house_type_selection == 'GGA (restaurants)':
            input_house_type = 'GGA'
        if house_type_selection == 'GBH (accommodation)':
            input_house_type = 'GBH'
        if house_type_selection == 'GWA (laundries, dry cleaning)':
            input_house_type = 'GWA'
        if house_type_selection == 'GGB (horticulture)':
            input_house_type = 'GGB'
        if house_type_selection == 'GBA (bakery)':
            input_house_type = 'GBA'
        if house_type_selection == 'GPD (paper and printing)':
            input_house_type = 'GPD'
        if house_type_selection == 'GMF (household-like business enterprises)':
            input_house_type = 'GMF'
        if house_type_selection == 'GHD (Total load profile Business/Commerce/Services)':
            input_house_type = 'GHD'

        # print(input_house_type)
        self.input_house_type = input_house_type
        self.plainTextEdit.appendPlainText(f"House type :{input_house_type}")
        return input_house_type

    def demand_value_heat(self):
        input_annual_demand_heat = self.lineEdit_heat_demand.text()

        try:
            input_annual_demand_heat = float(input_annual_demand_heat)
            self.input_annual_demand_heat = input_annual_demand_heat
            # print(input_annual_demand_heat)
            self.plainTextEdit.appendPlainText(f"Annual Heat Demand :{input_annual_demand_heat}")
            return input_annual_demand_heat

        except ValueError:
            #print("invalid value for annual heat demand")
            self.plainTextEdit.appendPlainText("invalid value for annual heat demand")

    def demand_value_elec(self):
        input_annual_demand_elec = self.lineEdit_elec_demand.text()

        try:
            input_annual_demand_elec = float(input_annual_demand_elec)
            self.input_annual_demand_elec = input_annual_demand_elec
            # print(input_annual_demand_elec)
            self.plainTextEdit.appendPlainText(f"Annual Electric Demand :{input_annual_demand_elec}")
            return input_annual_demand_elec

        except ValueError:
            #print("invalid value for annual elec demand")
            self.plainTextEdit.appendPlainText("invalid value for annual electric demand")

    def building_class(self):
        building_class_selection = self.comboBox.currentText()

        if building_class_selection == '11 (2010 -  present)':
            input_building_class = 11
        if building_class_selection == '10 (2002 - 2009)':
            input_building_class = 10
        if building_class_selection == '9 (1995 - 2001)':
            input_building_class = 9
        if building_class_selection == '8 (1984 - 1994)':
            input_building_class = 8
        if building_class_selection == '7 (1979 - 1983)':
            input_building_class = 7
        if building_class_selection == '6 (1969 - 1978)':
            input_building_class = 6
        if building_class_selection == '5 (1958 - 1968)':
            input_building_class = 5
        if building_class_selection == '4 (1949 - 1957)':
            input_building_class = 4
        if building_class_selection == '3 (1919 - 1948)':
            input_building_class = 3
        if building_class_selection == '2 (1860 - 1918)':
            input_building_class = 2
        if building_class_selection == '1 (until 1859)':
            input_building_class = 1

        self.input_building_class = input_building_class
        # print(input_building_class)
        self.plainTextEdit.appendPlainText(f"Building class :{input_building_class}")
        return input_building_class

    def wind_class(self):
        wind_class_selection = self.comboBox_windclass.currentText()
        if wind_class_selection == '0 (not windy)':
            input_wind_class = 0
        if wind_class_selection == '1 (windy)':
            input_wind_class = 1

        self.input_wind_class = input_wind_class
        # print(input_wind_class)
        self.plainTextEdit.appendPlainText(f"Wind class :{input_wind_class}")
        return input_wind_class

    def ww_load(self):
        input_WWload = self.comboBox_ww_load.currentText()
        self.input_WWload = input_WWload
        # print(input_WWload)
        self.plainTextEdit.appendPlainText(f"Include warm water load :{input_WWload}")
        return input_WWload

    def profile_type(self):
        profile_type_selection = self.comboBox_profile_type.currentText()

        if profile_type_selection == 'G0-General trade/business/commerce':
            input_profile_type = 'g0'
        if profile_type_selection == 'G1-Business on weekdays 8 a.m. - 6 p.m.':
            input_profile_type = 'g1'
        if profile_type_selection == 'G2-Businesses with heavy to predominant consumption in the evening hours':
            input_profile_type = 'g2'
        if profile_type_selection == 'G3-Continuous business':
            input_profile_type = 'g3'
        if profile_type_selection == 'G4-Shop/barber shop':
            input_profile_type = 'g4'
        if profile_type_selection == 'G5-Bakery with bakery':
            input_profile_type = 'g5'
        if profile_type_selection == 'G6-Weekend operation':
            input_profile_type = 'g6'
        if profile_type_selection == 'G7-Mobile phone transmitter station':
            input_profile_type = 'g7'
        if profile_type_selection == 'L0-General farms':
            input_profile_type = 'l0'
        if profile_type_selection == 'L1-Farms with dairy farming/part-time livestock farming':
            input_profile_type = 'l1'
        if profile_type_selection == 'L2-Other farms':
            input_profile_type = 'l2'
        if profile_type_selection == 'H0/H0_dyn-Household/dynamic houshold':
            input_profile_type = 'h0/h0_dyn'

        self.input_profile_type = input_profile_type
        # print(input_profile_type)
        self.plainTextEdit.appendPlainText(f"Profile type :{input_profile_type}")
        return input_profile_type

    # function for weather data
    def upload_dataframe(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)",
                                                       options=options)
        if file_name:
            # Read the CSV file into a DataFrame
            try:
                dataframe = pd.read_csv(file_name)
                self.dataframe = dataframe
                # print("weather data uploaded")
                self.plainTextEdit.appendPlainText("weather data uploaded")
                return dataframe
            except Exception as e:
                #print("error uploading the selected file")
                self.plainTextEdit.appendPlainText("Error uploading the selected file")

    def solve_heat_demand(self):

        country_name = self.input_country
        state = self.input_state
        year = self.input_year
        temperature_column = self.input_temp_column
        annual_demand_heat = self.input_annual_demand_heat
        house_type = self.input_house_type
        building_class = self.input_building_class
        wind_class = self.input_wind_class
        WW_load = self.input_WWload
        weather_data = self.dataframe

        holidays_list = holidays.country_holidays(country_name, subdiv=state, years=year)

        temperature_column = weather_data[
            temperature_column]  # column name from your dataset containing temperature data

        ann_demands_per_type = {house_type: annual_demand_heat}

        # dataframe creation for year
        demand = pd.DataFrame(index=pd.date_range(datetime.datetime(year, 1, 1, 0), periods=8760, freq="H"))

        # define your house type and other optional parameters
        demand[house_type] = bdew.HeatBuilding(demand.index,
                                               holidays=holidays_list,
                                               temperature=temperature_column,
                                               shlp_type=house_type,
                                               building_class=building_class,
                                               wind_class=wind_class,
                                               ww_incl=WW_load,
                                               annual_heat_demand=ann_demands_per_type[house_type],
                                               name=house_type).get_bdew_profile()

        # plot demand for building
        ax = demand.plot()
        ax.set_xlabel("Date")
        ax.set_ylabel("Heat demand in kW")
        plt.show()

        # exporting the output file
        file_path = "heat_demand.csv"
        demand[house_type].to_csv(file_path, index=True)
        #print("output heat demand is exported to current directory ")
        self.plainTextEdit.setPlainText("Output heat demand is saved to current directory")

        for key in ann_demands_per_type:
            assert np.isclose(demand[key].sum(), ann_demands_per_type[key], rtol=1e-4)

    def solve_elec_demand(self):

        country_name = self.input_country_2
        state = self.input_state_2
        year = self.input_year_2
        profile = self.input_profile_type
        annual_elec_demand = self.input_annual_demand_elec

        holidays_list = holidays.country_holidays(country_name, subdiv=state, years=year)

        ann_el_demand_per_sector = {
            profile: annual_elec_demand,
        }

        year = year

        # read standard load profiles
        e_slp = bdew.ElecSlp(year, holidays=holidays_list)

        # multiply given annual demand with timeseries
        elec_demand = e_slp.get_profile(ann_el_demand_per_sector)

        # add the slp for the industrial group (industrial electrical profile uses a step function)
        ilp = profiles.IndustrialLoadProfile(e_slp.date_time_index, holidays=holidays_list)

        # beginning and end of workday, weekdays, weekends and scaling factors by default
        elec_demand[profile] = ilp.simple_profile(ann_el_demand_per_sector[profile])

        # set beginning of workday
        elec_demand[profile] = ilp.simple_profile(ann_el_demand_per_sector[profile], am=settime(9, 0, 0))

        # change scaling factors
        elec_demand[profile] = ilp.simple_profile(
            ann_el_demand_per_sector[profile],
            profile_factors={
                "week": {"day": 1.0, "night": 0.8},
                "weekend": {"day": 0.8, "night": 0.6},
            }, )

        # resample 15-minute values to hourly values
        elec_demand_resampled = elec_demand.resample("H").mean()


        # plot elec demand
        ax = elec_demand_resampled.plot()
        ax.set_xlabel("date")
        ax.set_ylabel("power demand")
        plt.show()


        # exporting the output file
        file_path = "elec_demand.csv"
        elec_demand_resampled[profile].to_csv(file_path, index=True)
        self.plainTextEdit.setPlainText("Output electric demand is saved to current directory")

        for key in ann_el_demand_per_sector:
            assert np.isclose(
                elec_demand[key].sum() / 4, ann_el_demand_per_sector[key]
            )



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
