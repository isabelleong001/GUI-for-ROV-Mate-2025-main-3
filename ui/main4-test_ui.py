# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main4-test.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 814)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buttonsPanel = QWidget(self.centralwidget)
        self.buttonsPanel.setObjectName(u"buttonsPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.buttonsPanel.sizePolicy().hasHeightForWidth())
        self.buttonsPanel.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.buttonsPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(334, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.controlPanelButton = QPushButton(self.buttonsPanel)
        self.controlPanelButton.setObjectName(u"controlPanelButton")
        self.controlPanelButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.controlPanelButton.sizePolicy().hasHeightForWidth())
        self.controlPanelButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.controlPanelButton)

        self.dataButton = QPushButton(self.buttonsPanel)
        self.dataButton.setObjectName(u"dataButton")

        self.horizontalLayout.addWidget(self.dataButton)

        self.mappingButton = QPushButton(self.buttonsPanel)
        self.mappingButton.setObjectName(u"mappingButton")

        self.horizontalLayout.addWidget(self.mappingButton)

        self.thrustersButton = QPushButton(self.buttonsPanel)
        self.thrustersButton.setObjectName(u"thrustersButton")

        self.horizontalLayout.addWidget(self.thrustersButton)

        self.horizontalSpacer_3 = QSpacerItem(336, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addWidget(self.buttonsPanel, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.control_panel_page = QWidget()
        self.control_panel_page.setObjectName(u"control_panel_page")
        sizePolicy.setHeightForWidth(self.control_panel_page.sizePolicy().hasHeightForWidth())
        self.control_panel_page.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.control_panel_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.control_panel_tab = QWidget(self.control_panel_page)
        self.control_panel_tab.setObjectName(u"control_panel_tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.control_panel_tab.sizePolicy().hasHeightForWidth())
        self.control_panel_tab.setSizePolicy(sizePolicy2)
        self.horizontalLayout_3 = QHBoxLayout(self.control_panel_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.control_panel_camera_widget = QWidget(self.control_panel_tab)
        self.control_panel_camera_widget.setObjectName(u"control_panel_camera_widget")
        self.control_panel_camera_widget.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.control_panel_camera_widget.sizePolicy().hasHeightForWidth())
        self.control_panel_camera_widget.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.control_panel_camera_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.secondary_camera_feeds = QWidget(self.control_panel_camera_widget)
        self.secondary_camera_feeds.setObjectName(u"secondary_camera_feeds")
        sizePolicy1.setHeightForWidth(self.secondary_camera_feeds.sizePolicy().hasHeightForWidth())
        self.secondary_camera_feeds.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.secondary_camera_feeds)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.camera_feeds = QGridLayout()
        self.camera_feeds.setObjectName(u"camera_feeds")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.camera_feeds.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.camera_feeds.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.camera_feed_2 = QLabel(self.secondary_camera_feeds)
        self.camera_feed_2.setObjectName(u"camera_feed_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.camera_feed_2.sizePolicy().hasHeightForWidth())
        self.camera_feed_2.setSizePolicy(sizePolicy4)
        self.camera_feed_2.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.camera_feeds.addWidget(self.camera_feed_2, 0, 1, 1, 1)

        self.camera_feed_3 = QLabel(self.secondary_camera_feeds)
        self.camera_feed_3.setObjectName(u"camera_feed_3")
        sizePolicy4.setHeightForWidth(self.camera_feed_3.sizePolicy().hasHeightForWidth())
        self.camera_feed_3.setSizePolicy(sizePolicy4)
        self.camera_feed_3.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.camera_feeds.addWidget(self.camera_feed_3, 0, 2, 1, 1)

        self.camera_feeds.setColumnStretch(0, 20)
        self.camera_feeds.setColumnStretch(1, 20)
        self.camera_feeds.setColumnStretch(2, 20)
        self.camera_feeds.setColumnStretch(3, 20)

        self.gridLayout_2.addLayout(self.camera_feeds, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.secondary_camera_feeds, 0, 0, 1, 1)

        self.primary_camera_feed = QWidget(self.control_panel_camera_widget)
        self.primary_camera_feed.setObjectName(u"primary_camera_feed")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.primary_camera_feed.sizePolicy().hasHeightForWidth())
        self.primary_camera_feed.setSizePolicy(sizePolicy5)
        self.gridLayout_15 = QGridLayout(self.primary_camera_feed)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.camera_feed_1 = QLabel(self.primary_camera_feed)
        self.camera_feed_1.setObjectName(u"camera_feed_1")
        sizePolicy.setHeightForWidth(self.camera_feed_1.sizePolicy().hasHeightForWidth())
        self.camera_feed_1.setSizePolicy(sizePolicy)
        self.camera_feed_1.setFrameShape(QFrame.Shape.NoFrame)
        self.camera_feed_1.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_15.addWidget(self.camera_feed_1, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.primary_camera_feed, 1, 0, 1, 1)

        self.gridLayout_24.setRowStretch(0, 20)
        self.gridLayout_24.setRowStretch(1, 80)

        self.gridLayout_6.addLayout(self.gridLayout_24, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.control_panel_camera_widget)

        self.control_panel_functions_widget = QWidget(self.control_panel_tab)
        self.control_panel_functions_widget.setObjectName(u"control_panel_functions_widget")
        self.gridLayout_5 = QGridLayout(self.control_panel_functions_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CreditWidget = QHBoxLayout()
        self.CreditWidget.setObjectName(u"CreditWidget")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.CreditWidget.addItem(self.horizontalSpacer_8)

        self.label_14 = QLabel(self.control_panel_functions_widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.CreditWidget.addWidget(self.label_14)

        self.program_exit = QPushButton(self.control_panel_functions_widget)
        self.program_exit.setObjectName(u"program_exit")

        self.CreditWidget.addWidget(self.program_exit)


        self.gridLayout_5.addLayout(self.CreditWidget, 1, 0, 1, 2)

        self.control_panel_scroll = QScrollArea(self.control_panel_functions_widget)
        self.control_panel_scroll.setObjectName(u"control_panel_scroll")
        self.control_panel_scroll.setFrameShape(QFrame.Shape.NoFrame)
        self.control_panel_scroll.setLineWidth(0)
        self.control_panel_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.control_panel_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 319, 586))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_box_comms_connect = QGroupBox(self.scrollAreaWidgetContents_3)
        self.group_box_comms_connect.setObjectName(u"group_box_comms_connect")
        self.group_box_comms_connect.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_8 = QGridLayout(self.group_box_comms_connect)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.control_rov_connect = QPushButton(self.group_box_comms_connect)
        self.control_rov_connect.setObjectName(u"control_rov_connect")
        sizePolicy1.setHeightForWidth(self.control_rov_connect.sizePolicy().hasHeightForWidth())
        self.control_rov_connect.setSizePolicy(sizePolicy1)
        self.control_rov_connect.setMinimumSize(QSize(0, 0))
        self.control_rov_connect.setCheckable(True)

        self.gridLayout_8.addWidget(self.control_rov_connect, 0, 1, 1, 1)

        self.control_controller_connect = QPushButton(self.group_box_comms_connect)
        self.control_controller_connect.setObjectName(u"control_controller_connect")
        sizePolicy1.setHeightForWidth(self.control_controller_connect.sizePolicy().hasHeightForWidth())
        self.control_controller_connect.setSizePolicy(sizePolicy1)
        self.control_controller_connect.setMinimumSize(QSize(0, 0))
        self.control_controller_connect.setCheckable(True)

        self.gridLayout_8.addWidget(self.control_controller_connect, 1, 1, 1, 1)

        self.rov_label = QLabel(self.group_box_comms_connect)
        self.rov_label.setObjectName(u"rov_label")
        self.rov_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.rov_label, 0, 0, 1, 1)

        self.controller_label = QLabel(self.group_box_comms_connect)
        self.controller_label.setObjectName(u"controller_label")
        self.controller_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.controller_label, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.group_box_comms_connect)

        self.digital_cameras_menu = QGroupBox(self.scrollAreaWidgetContents_3)
        self.digital_cameras_menu.setObjectName(u"digital_cameras_menu")
        self.digital_cameras_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout = QGridLayout(self.digital_cameras_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.camera_controls = QWidget(self.digital_cameras_menu)
        self.camera_controls.setObjectName(u"camera_controls")
        self.gridLayout_7 = QGridLayout(self.camera_controls)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.secondaryCamera_2_ToggleButton = QPushButton(self.camera_controls)
        self.secondaryCamera_2_ToggleButton.setObjectName(u"secondaryCamera_2_ToggleButton")

        self.gridLayout_7.addWidget(self.secondaryCamera_2_ToggleButton, 2, 0, 1, 1)

        self.primaryCameraToggleButton = QPushButton(self.camera_controls)
        self.primaryCameraToggleButton.setObjectName(u"primaryCameraToggleButton")

        self.gridLayout_7.addWidget(self.primaryCameraToggleButton, 0, 0, 1, 1)

        self.secondaryCamera_1_ToggleButton = QPushButton(self.camera_controls)
        self.secondaryCamera_1_ToggleButton.setObjectName(u"secondaryCamera_1_ToggleButton")

        self.gridLayout_7.addWidget(self.secondaryCamera_1_ToggleButton, 1, 0, 1, 1)

        self.camera_feed_1_menu = QComboBox(self.camera_controls)
        self.camera_feed_1_menu.setObjectName(u"camera_feed_1_menu")
        self.camera_feed_1_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_1_menu, 0, 1, 1, 1)

        self.camera_feed_2_menu = QComboBox(self.camera_controls)
        self.camera_feed_2_menu.setObjectName(u"camera_feed_2_menu")
        self.camera_feed_2_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_2_menu, 1, 1, 1, 1)

        self.camera_feed_3_menu = QComboBox(self.camera_controls)
        self.camera_feed_3_menu.setObjectName(u"camera_feed_3_menu")
        self.camera_feed_3_menu.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)

        self.gridLayout_7.addWidget(self.camera_feed_3_menu, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.camera_controls, 0, 0, 1, 1)

        self.toggleViewButton = QPushButton(self.digital_cameras_menu)
        self.toggleViewButton.setObjectName(u"toggleViewButton")

        self.gridLayout.addWidget(self.toggleViewButton, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.digital_cameras_menu)

        self.sensor_control = QGroupBox(self.scrollAreaWidgetContents_3)
        self.sensor_control.setObjectName(u"sensor_control")
        self.sensor_control.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.sensor_control)

        self.analog_cameras_menu = QGroupBox(self.scrollAreaWidgetContents_3)
        self.analog_cameras_menu.setObjectName(u"analog_cameras_menu")
        self.analog_cameras_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.analog_cameras_menu)

        self.timer_control = QGroupBox(self.scrollAreaWidgetContents_3)
        self.timer_control.setObjectName(u"timer_control")
        self.timer_control.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.timer_control)


        self.gridLayout_10.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.control_panel_scroll.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_5.addWidget(self.control_panel_scroll, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.control_panel_functions_widget)

        self.horizontalLayout_3.setStretch(0, 95)
        self.horizontalLayout_3.setStretch(1, 5)

        self.gridLayout_3.addWidget(self.control_panel_tab, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.control_panel_page)
        self.data_panel_page = QWidget()
        self.data_panel_page.setObjectName(u"data_panel_page")
        self.label = QLabel(self.data_panel_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 250, 201, 71))
        self.stackedWidget.addWidget(self.data_panel_page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 240, 201, 71))
        self.stackedWidget.addWidget(self.page_3)
        self.mapping_panel_page = QWidget()
        self.mapping_panel_page.setObjectName(u"mapping_panel_page")
        self.verticalLayoutWidget = QWidget(self.mapping_panel_page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 1091, 691))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.thruster1_label = QLabel(self.verticalLayoutWidget)
        self.thruster1_label.setObjectName(u"thruster1_label")
        self.thruster1_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_11.addWidget(self.thruster1_label)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.angle1_label = QLabel(self.verticalLayoutWidget)
        self.angle1_label.setObjectName(u"angle1_label")
        self.angle1_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_33.addWidget(self.angle1_label)

        self.formLayout_20 = QFormLayout()
        self.formLayout_20.setObjectName(u"formLayout_20")
        self.label_93 = QLabel(self.verticalLayoutWidget)
        self.label_93.setObjectName(u"label_93")

        self.formLayout_20.setWidget(0, QFormLayout.LabelRole, self.label_93)

        self.angleX1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX1_lineedit.setObjectName(u"angleX1_lineedit")
        self.angleX1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_20.setWidget(0, QFormLayout.FieldRole, self.angleX1_lineedit)

        self.label_94 = QLabel(self.verticalLayoutWidget)
        self.label_94.setObjectName(u"label_94")

        self.formLayout_20.setWidget(1, QFormLayout.LabelRole, self.label_94)

        self.angleY1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY1_lineedit.setObjectName(u"angleY1_lineedit")
        self.angleY1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_20.setWidget(1, QFormLayout.FieldRole, self.angleY1_lineedit)

        self.label_95 = QLabel(self.verticalLayoutWidget)
        self.label_95.setObjectName(u"label_95")

        self.formLayout_20.setWidget(2, QFormLayout.LabelRole, self.label_95)

        self.angleZ1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ1_lineedit.setObjectName(u"angleZ1_lineedit")
        self.angleZ1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_20.setWidget(2, QFormLayout.FieldRole, self.angleZ1_lineedit)


        self.horizontalLayout_33.addLayout(self.formLayout_20)


        self.verticalLayout_11.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.position1_label = QLabel(self.verticalLayoutWidget)
        self.position1_label.setObjectName(u"position1_label")
        self.position1_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_34.addWidget(self.position1_label)

        self.formLayout_21 = QFormLayout()
        self.formLayout_21.setObjectName(u"formLayout_21")
        self.label_97 = QLabel(self.verticalLayoutWidget)
        self.label_97.setObjectName(u"label_97")

        self.formLayout_21.setWidget(0, QFormLayout.LabelRole, self.label_97)

        self.positionX1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX1_lineedit.setObjectName(u"positionX1_lineedit")
        self.positionX1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_21.setWidget(0, QFormLayout.FieldRole, self.positionX1_lineedit)

        self.label_98 = QLabel(self.verticalLayoutWidget)
        self.label_98.setObjectName(u"label_98")

        self.formLayout_21.setWidget(1, QFormLayout.LabelRole, self.label_98)

        self.positionY1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY1_lineedit.setObjectName(u"positionY1_lineedit")
        self.positionY1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_21.setWidget(1, QFormLayout.FieldRole, self.positionY1_lineedit)

        self.label_99 = QLabel(self.verticalLayoutWidget)
        self.label_99.setObjectName(u"label_99")

        self.formLayout_21.setWidget(2, QFormLayout.LabelRole, self.label_99)

        self.positionZ1_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ1_lineedit.setObjectName(u"positionZ1_lineedit")
        self.positionZ1_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_21.setWidget(2, QFormLayout.FieldRole, self.positionZ1_lineedit)


        self.horizontalLayout_34.addLayout(self.formLayout_21)


        self.verticalLayout_11.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.maxpower1_label = QLabel(self.verticalLayoutWidget)
        self.maxpower1_label.setObjectName(u"maxpower1_label")
        self.maxpower1_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_35.addWidget(self.maxpower1_label)

        self.maxPower_spinbox_1 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_1.setObjectName(u"maxPower_spinbox_1")
        self.maxPower_spinbox_1.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_35.addWidget(self.maxPower_spinbox_1)


        self.verticalLayout_11.addLayout(self.horizontalLayout_35)

        self.thrusterStatus_1 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_1.setObjectName(u"thrusterStatus_1")
        self.thrusterStatus_1.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.thrusterStatus_1)


        self.horizontalLayout_32.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.thruster2_label = QLabel(self.verticalLayoutWidget)
        self.thruster2_label.setObjectName(u"thruster2_label")
        self.thruster2_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_12.addWidget(self.thruster2_label)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.angle2_label = QLabel(self.verticalLayoutWidget)
        self.angle2_label.setObjectName(u"angle2_label")
        self.angle2_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_36.addWidget(self.angle2_label)

        self.formLayout_22 = QFormLayout()
        self.formLayout_22.setObjectName(u"formLayout_22")
        self.label_101 = QLabel(self.verticalLayoutWidget)
        self.label_101.setObjectName(u"label_101")

        self.formLayout_22.setWidget(0, QFormLayout.LabelRole, self.label_101)

        self.angleX2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX2_lineedit.setObjectName(u"angleX2_lineedit")
        self.angleX2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_22.setWidget(0, QFormLayout.FieldRole, self.angleX2_lineedit)

        self.label_102 = QLabel(self.verticalLayoutWidget)
        self.label_102.setObjectName(u"label_102")

        self.formLayout_22.setWidget(1, QFormLayout.LabelRole, self.label_102)

        self.angleY2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY2_lineedit.setObjectName(u"angleY2_lineedit")
        self.angleY2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_22.setWidget(1, QFormLayout.FieldRole, self.angleY2_lineedit)

        self.label_103 = QLabel(self.verticalLayoutWidget)
        self.label_103.setObjectName(u"label_103")

        self.formLayout_22.setWidget(2, QFormLayout.LabelRole, self.label_103)

        self.angleZ2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ2_lineedit.setObjectName(u"angleZ2_lineedit")
        self.angleZ2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_22.setWidget(2, QFormLayout.FieldRole, self.angleZ2_lineedit)


        self.horizontalLayout_36.addLayout(self.formLayout_22)


        self.verticalLayout_12.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.position2_label = QLabel(self.verticalLayoutWidget)
        self.position2_label.setObjectName(u"position2_label")
        self.position2_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_37.addWidget(self.position2_label)

        self.formLayout_23 = QFormLayout()
        self.formLayout_23.setObjectName(u"formLayout_23")
        self.label_105 = QLabel(self.verticalLayoutWidget)
        self.label_105.setObjectName(u"label_105")

        self.formLayout_23.setWidget(0, QFormLayout.LabelRole, self.label_105)

        self.positionX2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX2_lineedit.setObjectName(u"positionX2_lineedit")
        self.positionX2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_23.setWidget(0, QFormLayout.FieldRole, self.positionX2_lineedit)

        self.label_106 = QLabel(self.verticalLayoutWidget)
        self.label_106.setObjectName(u"label_106")

        self.formLayout_23.setWidget(1, QFormLayout.LabelRole, self.label_106)

        self.positionY2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY2_lineedit.setObjectName(u"positionY2_lineedit")
        self.positionY2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_23.setWidget(1, QFormLayout.FieldRole, self.positionY2_lineedit)

        self.label_107 = QLabel(self.verticalLayoutWidget)
        self.label_107.setObjectName(u"label_107")

        self.formLayout_23.setWidget(2, QFormLayout.LabelRole, self.label_107)

        self.positionZ2_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ2_lineedit.setObjectName(u"positionZ2_lineedit")
        self.positionZ2_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_23.setWidget(2, QFormLayout.FieldRole, self.positionZ2_lineedit)


        self.horizontalLayout_37.addLayout(self.formLayout_23)


        self.verticalLayout_12.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.maxpower2_label = QLabel(self.verticalLayoutWidget)
        self.maxpower2_label.setObjectName(u"maxpower2_label")
        self.maxpower2_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_38.addWidget(self.maxpower2_label)

        self.maxPower_spinbox_2 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_2.setObjectName(u"maxPower_spinbox_2")
        self.maxPower_spinbox_2.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_38.addWidget(self.maxPower_spinbox_2)


        self.verticalLayout_12.addLayout(self.horizontalLayout_38)

        self.thrusterStatus_2 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_2.setObjectName(u"thrusterStatus_2")
        self.thrusterStatus_2.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.thrusterStatus_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.thruster3_label = QLabel(self.verticalLayoutWidget)
        self.thruster3_label.setObjectName(u"thruster3_label")
        self.thruster3_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_13.addWidget(self.thruster3_label)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.angle3_label = QLabel(self.verticalLayoutWidget)
        self.angle3_label.setObjectName(u"angle3_label")
        self.angle3_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_39.addWidget(self.angle3_label)

        self.formLayout_24 = QFormLayout()
        self.formLayout_24.setObjectName(u"formLayout_24")
        self.label_111 = QLabel(self.verticalLayoutWidget)
        self.label_111.setObjectName(u"label_111")

        self.formLayout_24.setWidget(0, QFormLayout.LabelRole, self.label_111)

        self.angleX3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX3_lineedit.setObjectName(u"angleX3_lineedit")
        self.angleX3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_24.setWidget(0, QFormLayout.FieldRole, self.angleX3_lineedit)

        self.label_112 = QLabel(self.verticalLayoutWidget)
        self.label_112.setObjectName(u"label_112")

        self.formLayout_24.setWidget(1, QFormLayout.LabelRole, self.label_112)

        self.angleY3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY3_lineedit.setObjectName(u"angleY3_lineedit")
        self.angleY3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_24.setWidget(1, QFormLayout.FieldRole, self.angleY3_lineedit)

        self.label_113 = QLabel(self.verticalLayoutWidget)
        self.label_113.setObjectName(u"label_113")

        self.formLayout_24.setWidget(2, QFormLayout.LabelRole, self.label_113)

        self.angleZ3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ3_lineedit.setObjectName(u"angleZ3_lineedit")
        self.angleZ3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_24.setWidget(2, QFormLayout.FieldRole, self.angleZ3_lineedit)


        self.horizontalLayout_39.addLayout(self.formLayout_24)


        self.verticalLayout_13.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.position3_label = QLabel(self.verticalLayoutWidget)
        self.position3_label.setObjectName(u"position3_label")
        self.position3_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_40.addWidget(self.position3_label)

        self.formLayout_25 = QFormLayout()
        self.formLayout_25.setObjectName(u"formLayout_25")
        self.label_115 = QLabel(self.verticalLayoutWidget)
        self.label_115.setObjectName(u"label_115")

        self.formLayout_25.setWidget(0, QFormLayout.LabelRole, self.label_115)

        self.positionX3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX3_lineedit.setObjectName(u"positionX3_lineedit")
        self.positionX3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_25.setWidget(0, QFormLayout.FieldRole, self.positionX3_lineedit)

        self.label_116 = QLabel(self.verticalLayoutWidget)
        self.label_116.setObjectName(u"label_116")

        self.formLayout_25.setWidget(1, QFormLayout.LabelRole, self.label_116)

        self.positionY3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY3_lineedit.setObjectName(u"positionY3_lineedit")
        self.positionY3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_25.setWidget(1, QFormLayout.FieldRole, self.positionY3_lineedit)

        self.label_117 = QLabel(self.verticalLayoutWidget)
        self.label_117.setObjectName(u"label_117")

        self.formLayout_25.setWidget(2, QFormLayout.LabelRole, self.label_117)

        self.positionZ3_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ3_lineedit.setObjectName(u"positionZ3_lineedit")
        self.positionZ3_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_25.setWidget(2, QFormLayout.FieldRole, self.positionZ3_lineedit)


        self.horizontalLayout_40.addLayout(self.formLayout_25)


        self.verticalLayout_13.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.maxpower3_label = QLabel(self.verticalLayoutWidget)
        self.maxpower3_label.setObjectName(u"maxpower3_label")
        self.maxpower3_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_41.addWidget(self.maxpower3_label)

        self.maxPower_spinbox_3 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_3.setObjectName(u"maxPower_spinbox_3")
        self.maxPower_spinbox_3.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_41.addWidget(self.maxPower_spinbox_3)


        self.verticalLayout_13.addLayout(self.horizontalLayout_41)

        self.thrusterStatus_3 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_3.setObjectName(u"thrusterStatus_3")
        self.thrusterStatus_3.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.thrusterStatus_3)


        self.horizontalLayout_32.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.thruster4_label = QLabel(self.verticalLayoutWidget)
        self.thruster4_label.setObjectName(u"thruster4_label")
        self.thruster4_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_14.addWidget(self.thruster4_label)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.angle4_label = QLabel(self.verticalLayoutWidget)
        self.angle4_label.setObjectName(u"angle4_label")
        self.angle4_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_42.addWidget(self.angle4_label)

        self.formLayout_26 = QFormLayout()
        self.formLayout_26.setObjectName(u"formLayout_26")
        self.label_121 = QLabel(self.verticalLayoutWidget)
        self.label_121.setObjectName(u"label_121")

        self.formLayout_26.setWidget(0, QFormLayout.LabelRole, self.label_121)

        self.angleX4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX4_lineedit.setObjectName(u"angleX4_lineedit")
        self.angleX4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_26.setWidget(0, QFormLayout.FieldRole, self.angleX4_lineedit)

        self.label_122 = QLabel(self.verticalLayoutWidget)
        self.label_122.setObjectName(u"label_122")

        self.formLayout_26.setWidget(1, QFormLayout.LabelRole, self.label_122)

        self.angleY4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY4_lineedit.setObjectName(u"angleY4_lineedit")
        self.angleY4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_26.setWidget(1, QFormLayout.FieldRole, self.angleY4_lineedit)

        self.label_123 = QLabel(self.verticalLayoutWidget)
        self.label_123.setObjectName(u"label_123")

        self.formLayout_26.setWidget(2, QFormLayout.LabelRole, self.label_123)

        self.angleZ4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ4_lineedit.setObjectName(u"angleZ4_lineedit")
        self.angleZ4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_26.setWidget(2, QFormLayout.FieldRole, self.angleZ4_lineedit)


        self.horizontalLayout_42.addLayout(self.formLayout_26)


        self.verticalLayout_14.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.position4_label = QLabel(self.verticalLayoutWidget)
        self.position4_label.setObjectName(u"position4_label")
        self.position4_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_43.addWidget(self.position4_label)

        self.formLayout_27 = QFormLayout()
        self.formLayout_27.setObjectName(u"formLayout_27")
        self.label_125 = QLabel(self.verticalLayoutWidget)
        self.label_125.setObjectName(u"label_125")

        self.formLayout_27.setWidget(0, QFormLayout.LabelRole, self.label_125)

        self.positionX4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX4_lineedit.setObjectName(u"positionX4_lineedit")
        self.positionX4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_27.setWidget(0, QFormLayout.FieldRole, self.positionX4_lineedit)

        self.label_126 = QLabel(self.verticalLayoutWidget)
        self.label_126.setObjectName(u"label_126")

        self.formLayout_27.setWidget(1, QFormLayout.LabelRole, self.label_126)

        self.positionY4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY4_lineedit.setObjectName(u"positionY4_lineedit")
        self.positionY4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_27.setWidget(1, QFormLayout.FieldRole, self.positionY4_lineedit)

        self.label_127 = QLabel(self.verticalLayoutWidget)
        self.label_127.setObjectName(u"label_127")

        self.formLayout_27.setWidget(2, QFormLayout.LabelRole, self.label_127)

        self.positionZ4_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ4_lineedit.setObjectName(u"positionZ4_lineedit")
        self.positionZ4_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_27.setWidget(2, QFormLayout.FieldRole, self.positionZ4_lineedit)


        self.horizontalLayout_43.addLayout(self.formLayout_27)


        self.verticalLayout_14.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.maxpower4_label = QLabel(self.verticalLayoutWidget)
        self.maxpower4_label.setObjectName(u"maxpower4_label")
        self.maxpower4_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_44.addWidget(self.maxpower4_label)

        self.maxPower_spinbox_4 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_4.setObjectName(u"maxPower_spinbox_4")
        self.maxPower_spinbox_4.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_44.addWidget(self.maxPower_spinbox_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_44)

        self.thrusterStatus_4 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_4.setObjectName(u"thrusterStatus_4")
        self.thrusterStatus_4.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.thrusterStatus_4)


        self.horizontalLayout_32.addLayout(self.verticalLayout_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.thruster5_label = QLabel(self.verticalLayoutWidget)
        self.thruster5_label.setObjectName(u"thruster5_label")
        self.thruster5_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_3.addWidget(self.thruster5_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.angle5_label = QLabel(self.verticalLayoutWidget)
        self.angle5_label.setObjectName(u"angle5_label")
        self.angle5_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_7.addWidget(self.angle5_label)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.angleX5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX5_lineedit.setObjectName(u"angleX5_lineedit")
        self.angleX5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.angleX5_lineedit)

        self.label_20 = QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.angleY5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY5_lineedit.setObjectName(u"angleY5_lineedit")
        self.angleY5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.angleY5_lineedit)

        self.label_21 = QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.angleZ5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ5_lineedit.setObjectName(u"angleZ5_lineedit")
        self.angleZ5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.angleZ5_lineedit)


        self.horizontalLayout_7.addLayout(self.formLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.position5_label = QLabel(self.verticalLayoutWidget)
        self.position5_label.setObjectName(u"position5_label")
        self.position5_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_8.addWidget(self.position5_label)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_23 = QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.positionX5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX5_lineedit.setObjectName(u"positionX5_lineedit")
        self.positionX5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.positionX5_lineedit)

        self.label_24 = QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.positionY5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY5_lineedit.setObjectName(u"positionY5_lineedit")
        self.positionY5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.positionY5_lineedit)

        self.label_25 = QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_25)

        self.positionZ5_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ5_lineedit.setObjectName(u"positionZ5_lineedit")
        self.positionZ5_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.positionZ5_lineedit)


        self.horizontalLayout_8.addLayout(self.formLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.maxpower5_label = QLabel(self.verticalLayoutWidget)
        self.maxpower5_label.setObjectName(u"maxpower5_label")
        self.maxpower5_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_9.addWidget(self.maxpower5_label)

        self.maxPower_spinbox_5 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_5.setObjectName(u"maxPower_spinbox_5")
        self.maxPower_spinbox_5.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_9.addWidget(self.maxPower_spinbox_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.thrusterStatus_5 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_5.setObjectName(u"thrusterStatus_5")
        self.thrusterStatus_5.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.thrusterStatus_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.thruster6_label = QLabel(self.verticalLayoutWidget)
        self.thruster6_label.setObjectName(u"thruster6_label")
        self.thruster6_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_4.addWidget(self.thruster6_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.angle6_label = QLabel(self.verticalLayoutWidget)
        self.angle6_label.setObjectName(u"angle6_label")
        self.angle6_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_10.addWidget(self.angle6_label)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_27 = QLabel(self.verticalLayoutWidget)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.angleX6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX6_lineedit.setObjectName(u"angleX6_lineedit")
        self.angleX6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.angleX6_lineedit)

        self.label_28 = QLabel(self.verticalLayoutWidget)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.angleY6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY6_lineedit.setObjectName(u"angleY6_lineedit")
        self.angleY6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.angleY6_lineedit)

        self.label_29 = QLabel(self.verticalLayoutWidget)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.angleZ6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ6_lineedit.setObjectName(u"angleZ6_lineedit")
        self.angleZ6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.angleZ6_lineedit)


        self.horizontalLayout_10.addLayout(self.formLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.position6_label = QLabel(self.verticalLayoutWidget)
        self.position6_label.setObjectName(u"position6_label")
        self.position6_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_11.addWidget(self.position6_label)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_31 = QLabel(self.verticalLayoutWidget)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_31)

        self.positionX6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX6_lineedit.setObjectName(u"positionX6_lineedit")
        self.positionX6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.positionX6_lineedit)

        self.label_32 = QLabel(self.verticalLayoutWidget)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_32)

        self.positionY6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY6_lineedit.setObjectName(u"positionY6_lineedit")
        self.positionY6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.positionY6_lineedit)

        self.label_33 = QLabel(self.verticalLayoutWidget)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_33)

        self.positionZ6_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ6_lineedit.setObjectName(u"positionZ6_lineedit")
        self.positionZ6_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.positionZ6_lineedit)


        self.horizontalLayout_11.addLayout(self.formLayout_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.maxpower6_label = QLabel(self.verticalLayoutWidget)
        self.maxpower6_label.setObjectName(u"maxpower6_label")
        self.maxpower6_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_12.addWidget(self.maxpower6_label)

        self.maxPower_spinbox_6 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_6.setObjectName(u"maxPower_spinbox_6")
        self.maxPower_spinbox_6.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_12.addWidget(self.maxPower_spinbox_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.thrusterStatus_6 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_6.setObjectName(u"thrusterStatus_6")
        self.thrusterStatus_6.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.thrusterStatus_6)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.thruster7_label = QLabel(self.verticalLayoutWidget)
        self.thruster7_label.setObjectName(u"thruster7_label")
        self.thruster7_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_5.addWidget(self.thruster7_label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.angle7_label = QLabel(self.verticalLayoutWidget)
        self.angle7_label.setObjectName(u"angle7_label")
        self.angle7_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_13.addWidget(self.angle7_label)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_37 = QLabel(self.verticalLayoutWidget)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_37)

        self.angleX7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX7_lineedit.setObjectName(u"angleX7_lineedit")
        self.angleX7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.angleX7_lineedit)

        self.label_38 = QLabel(self.verticalLayoutWidget)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_38)

        self.angleY7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY7_lineedit.setObjectName(u"angleY7_lineedit")
        self.angleY7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.angleY7_lineedit)

        self.label_39 = QLabel(self.verticalLayoutWidget)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_39)

        self.angleZ7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ7_lineedit.setObjectName(u"angleZ7_lineedit")
        self.angleZ7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.angleZ7_lineedit)


        self.horizontalLayout_13.addLayout(self.formLayout_8)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.position7_label = QLabel(self.verticalLayoutWidget)
        self.position7_label.setObjectName(u"position7_label")
        self.position7_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_14.addWidget(self.position7_label)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_41 = QLabel(self.verticalLayoutWidget)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_41)

        self.positionX7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionX7_lineedit.setObjectName(u"positionX7_lineedit")
        self.positionX7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.positionX7_lineedit)

        self.label_42 = QLabel(self.verticalLayoutWidget)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_42)

        self.positionY7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY7_lineedit.setObjectName(u"positionY7_lineedit")
        self.positionY7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.positionY7_lineedit)

        self.label_43 = QLabel(self.verticalLayoutWidget)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_43)

        self.positionZ7_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ7_lineedit.setObjectName(u"positionZ7_lineedit")
        self.positionZ7_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.positionZ7_lineedit)


        self.horizontalLayout_14.addLayout(self.formLayout_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.maxpower7_label = QLabel(self.verticalLayoutWidget)
        self.maxpower7_label.setObjectName(u"maxpower7_label")
        self.maxpower7_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_15.addWidget(self.maxpower7_label)

        self.maxPower_spinbox_7 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_7.setObjectName(u"maxPower_spinbox_7")
        self.maxPower_spinbox_7.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_15.addWidget(self.maxPower_spinbox_7)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.thrusterStatus_7 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_7.setObjectName(u"thrusterStatus_7")
        self.thrusterStatus_7.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.thrusterStatus_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.thruster8_label = QLabel(self.verticalLayoutWidget)
        self.thruster8_label.setObjectName(u"thruster8_label")
        self.thruster8_label.setStyleSheet(u"font: 26pt;")

        self.verticalLayout_6.addWidget(self.thruster8_label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.angle7_label_2 = QLabel(self.verticalLayoutWidget)
        self.angle7_label_2.setObjectName(u"angle7_label_2")
        self.angle7_label_2.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_16.addWidget(self.angle7_label_2)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_47 = QLabel(self.verticalLayoutWidget)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_47)

        self.angleX8_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleX8_lineedit.setObjectName(u"angleX8_lineedit")
        self.angleX8_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.angleX8_lineedit)

        self.label_48 = QLabel(self.verticalLayoutWidget)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_48)

        self.angleY8_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleY8_lineedit.setObjectName(u"angleY8_lineedit")
        self.angleY8_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.angleY8_lineedit)

        self.label_49 = QLabel(self.verticalLayoutWidget)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_49)

        self.angleZ8_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.angleZ8_lineedit.setObjectName(u"angleZ8_lineedit")
        self.angleZ8_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.angleZ8_lineedit)


        self.horizontalLayout_16.addLayout(self.formLayout_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.position8_label = QLabel(self.verticalLayoutWidget)
        self.position8_label.setObjectName(u"position8_label")
        self.position8_label.setStyleSheet(u"font: 20pt;")

        self.horizontalLayout_17.addWidget(self.position8_label)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.label_51 = QLabel(self.verticalLayoutWidget)
        self.label_51.setObjectName(u"label_51")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_51)

        self.positionX7_lineedit_2 = QLineEdit(self.verticalLayoutWidget)
        self.positionX7_lineedit_2.setObjectName(u"positionX7_lineedit_2")
        self.positionX7_lineedit_2.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.positionX7_lineedit_2)

        self.label_52 = QLabel(self.verticalLayoutWidget)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_52)

        self.positionY8_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionY8_lineedit.setObjectName(u"positionY8_lineedit")
        self.positionY8_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.positionY8_lineedit)

        self.label_53 = QLabel(self.verticalLayoutWidget)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_11.setWidget(2, QFormLayout.LabelRole, self.label_53)

        self.positionZ8_lineedit = QLineEdit(self.verticalLayoutWidget)
        self.positionZ8_lineedit.setObjectName(u"positionZ8_lineedit")
        self.positionZ8_lineedit.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.formLayout_11.setWidget(2, QFormLayout.FieldRole, self.positionZ8_lineedit)


        self.horizontalLayout_17.addLayout(self.formLayout_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.maxpower8_label = QLabel(self.verticalLayoutWidget)
        self.maxpower8_label.setObjectName(u"maxpower8_label")
        self.maxpower8_label.setStyleSheet(u"font: 16pt;")

        self.horizontalLayout_18.addWidget(self.maxpower8_label)

        self.maxPower_spinbox_8 = QSpinBox(self.verticalLayoutWidget)
        self.maxPower_spinbox_8.setObjectName(u"maxPower_spinbox_8")
        self.maxPower_spinbox_8.setStyleSheet(u"color: black;\n"
"background-color: white;")

        self.horizontalLayout_18.addWidget(self.maxPower_spinbox_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.thrusterStatus_8 = QCheckBox(self.verticalLayoutWidget)
        self.thrusterStatus_8.setObjectName(u"thrusterStatus_8")
        self.thrusterStatus_8.setStyleSheet(u"QCheckBox::indicator:unchecked\n"
"{\n"
"background-color : red;\n"
"}\n"
"QCheckBox::indicator:checked\n"
"{\n"
"background-color : green;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.thrusterStatus_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.mapping_panel_page)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1129, 36))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.controlPanelButton.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.dataButton.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.mappingButton.setText(QCoreApplication.translate("MainWindow", u"Mapping", None))
        self.thrustersButton.setText(QCoreApplication.translate("MainWindow", u"Thrusters", None))
        self.camera_feed_2.setText("")
        self.camera_feed_3.setText("")
        self.camera_feed_1.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Developed by Crush Depth Team", None))
        self.program_exit.setText(QCoreApplication.translate("MainWindow", u"Exit Program", None))
        self.group_box_comms_connect.setTitle(QCoreApplication.translate("MainWindow", u"Communication Setup", None))
        self.control_rov_connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.control_controller_connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.rov_label.setText(QCoreApplication.translate("MainWindow", u"ROV", None))
        self.controller_label.setText(QCoreApplication.translate("MainWindow", u"Controller", None))
        self.digital_cameras_menu.setTitle(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.secondaryCamera_2_ToggleButton.setText(QCoreApplication.translate("MainWindow", u"2nd - 2", None))
        self.primaryCameraToggleButton.setText(QCoreApplication.translate("MainWindow", u"1st", None))
        self.secondaryCamera_1_ToggleButton.setText(QCoreApplication.translate("MainWindow", u"2nd - 1", None))
        self.toggleViewButton.setText(QCoreApplication.translate("MainWindow", u"Toggle Camera View", None))
        self.sensor_control.setTitle(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.analog_cameras_menu.setTitle(QCoreApplication.translate("MainWindow", u"External Camera Feed", None))
        self.timer_control.setTitle(QCoreApplication.translate("MainWindow", u"Competition Time", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"DATA PAGE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MAPPING PAGE", None))
        self.thruster1_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 1", None))
        self.angle1_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position1_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower1_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_1.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster2_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 2", None))
        self.angle2_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position2_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower2_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_2.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster3_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 3", None))
        self.angle3_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position3_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower3_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_3.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster4_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 4", None))
        self.angle4_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position4_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower4_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_4.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster5_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 5", None))
        self.angle5_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position5_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower5_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_5.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster6_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 6", None))
        self.angle6_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position6_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower6_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_6.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster7_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 7", None))
        self.angle7_label.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position7_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower7_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_7.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.thruster8_label.setText(QCoreApplication.translate("MainWindow", u"Thruster 8", None))
        self.angle7_label_2.setText(QCoreApplication.translate("MainWindow", u"      Angle:    ", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.position8_label.setText(QCoreApplication.translate("MainWindow", u"   Position:   ", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"x:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"y:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"z:", None))
        self.maxpower8_label.setText(QCoreApplication.translate("MainWindow", u"      Max Power:", None))
        self.thrusterStatus_8.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

