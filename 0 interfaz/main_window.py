# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nike_main_windowIcGBZX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2extn.RoundProgressBar import roundProgressBar
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 684)
        MainWindow.setStyleSheet("alternate-background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMinimumSize(QtCore.QSize(0, 60))
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.main_header.setStyleSheet("QFrame{\n"
"    background-color: rgba(31,135,246,255);\n"
"    border-top-right-radius: 25px;\n"
"    border-top-left-radius: 25px;\n"
"\n"
"\n"
"\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(self.main_header)
        self.tittle_bar_container.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgba(31,135,246,255);\n"
"    border: none;\n"
"    border-top-left-radius: 25px;\n"
"\n"
"\n"
"}")
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(55, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"    /*background-color: #000;*/\n"
"    background-color: rgba(42,45,52,255);\n"
"    border-top-left-radius: 25px;\n"
"    border-top-right-radius: 0px;\n"
"\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_menu_toggle_btn = QtWidgets.QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.left_menu_toggle_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.left_menu_toggle_btn.setStyleSheet("border-top-left-radius: 25px;\n"
"background-color: rgba(42,45,52,255);")
        self.left_menu_toggle_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_menu_toggle_btn.setIcon(icon)
        self.left_menu_toggle_btn.setIconSize(QtCore.QSize(24, 24))
        self.left_menu_toggle_btn.setObjectName("left_menu_toggle_btn")
        self.horizontalLayout_4.addWidget(self.left_menu_toggle_btn)
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(self.tittle_bar_container)
        self.tittle_bar.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}\n"
"\n"
"QFrame{\n"
"    border-bottom: 1px solid #000;\n"
"    background-color: rgba(31,135,246,255);\n"
"    border: none;\n"
"\n"
"}")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.tittle_bar)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.top_right_btns = QtWidgets.QFrame(self.main_header)
        self.top_right_btns.setMaximumSize(QtCore.QSize(150, 16777215))
        self.top_right_btns.setStyleSheet("QFrame{\n"
"    padding-right: 30px;\n"
"    border-top-right-radius: 50px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.restoreButton = QtWidgets.QPushButton(self.top_right_btns)
        self.restoreButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restoreButton.setStyleSheet("")
        self.restoreButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setIconSize(QtCore.QSize(24, 24))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.minimizeButton = QtWidgets.QPushButton(self.top_right_btns)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cil-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeButton.setIcon(icon2)
        self.minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(self.top_right_btns)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setMinimumSize(QtCore.QSize(0, 0))
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(55, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-left: 2px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(0, 92, 157);\n"
"    border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_top_buttons = QtWidgets.QFrame(self.left_side_menu)
        self.left_menu_top_buttons.setStyleSheet("")
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.formLayout = QtWidgets.QFormLayout(self.left_menu_top_buttons)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.accounts_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.accounts_button.setMinimumSize(QtCore.QSize(100, 0))
        self.accounts_button.setStyleSheet("background-image: url(:/icons/icons/cil-user.png);\n"
"background-repeat: none;\n"
"padding-left: 70px;\n"
"background-position: center left;")
        self.accounts_button.setObjectName("accounts_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.accounts_button)
        self.home_button = QtWidgets.QPushButton(self.left_menu_top_buttons)
        self.home_button.setMinimumSize(QtCore.QSize(100, 0))
        self.home_button.setStyleSheet("background-image: url(:/icons/icons/cil-home.png);\n"
"background-repeat: none;\n"
"padding-left: 70px;\n"
"background-position: center left;\n"
"/*This is the default selected button style*/\n"
"border-left: 2px solid  rgb(0, 136, 255);\n"
"border-bottom: 2px solid  rgb(0, 136, 255);")
        self.home_button.setObjectName("home_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.home_button)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons, 0, QtCore.Qt.AlignHCenter)
        self.settings_button = QtWidgets.QPushButton(self.left_side_menu)
        self.settings_button.setMinimumSize(QtCore.QSize(100, 0))
        self.settings_button.setStyleSheet("background-image: url(:/icons/icons/cil-code.png);\n"
"background-repeat: none;\n"
"padding-left: 70px;\n"
"background-position: center left;")
        self.settings_button.setObjectName("settings_button")
        self.verticalLayout_3.addWidget(self.settings_button)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setStyleSheet("")
        self.home_page.setObjectName("home_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.home_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.title = QtWidgets.QPushButton(self.frame)
        self.title.setMinimumSize(QtCore.QSize(855, 500))
        self.title.setStyleSheet("image: url(:/images/images/logo2.png);")
        self.title.setText("")
        self.title.setObjectName("title")
        self.gridLayout_7.addWidget(self.title, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.frame)
        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QtWidgets.QWidget()
        self.accounts_page.setStyleSheet("")
        self.accounts_page.setObjectName("accounts_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.accounts_page)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.top_frame = QtWidgets.QFrame(self.accounts_page)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.loadWavFrame = QtWidgets.QFrame(self.top_frame)
        self.loadWavFrame.setMinimumSize(QtCore.QSize(250, 100))
        self.loadWavFrame.setMaximumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.loadWavFrame.setFont(font)
        self.loadWavFrame.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255,85,124 255);\n"
"    border: 4px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    /*background-color: rgb(0, 92, 157);*/\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.loadWavFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loadWavFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loadWavFrame.setObjectName("loadWavFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.loadWavFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.scoreGenerateButton = QtWidgets.QPushButton(self.loadWavFrame)
        self.scoreGenerateButton.setMinimumSize(QtCore.QSize(0, 40))
        self.scoreGenerateButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.scoreGenerateButton.setFont(font)
        self.scoreGenerateButton.setStyleSheet("\n"
"background-color: rgba(125,64,245,255);\n"
"\n"
"")
        self.scoreGenerateButton.setObjectName("scoreGenerateButton")
        self.gridLayout.addWidget(self.scoreGenerateButton, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.loadWavButton = QtWidgets.QPushButton(self.loadWavFrame)
        self.loadWavButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loadWavButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.loadWavButton.setFont(font)
        self.loadWavButton.setStyleSheet("")
        self.loadWavButton.setObjectName("loadWavButton")
        self.gridLayout.addWidget(self.loadWavButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.loadWavEditLine = QtWidgets.QLineEdit(self.loadWavFrame)
        self.loadWavEditLine.setEnabled(True)
        self.loadWavEditLine.setMinimumSize(QtCore.QSize(30, 30))
        self.loadWavEditLine.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.loadWavEditLine.setText("")
        self.loadWavEditLine.setObjectName("loadWavEditLine")
        self.gridLayout.addWidget(self.loadWavEditLine, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.loadWavFrame, 0, QtCore.Qt.AlignLeft)
        self.SettingsFrame = QtWidgets.QFrame(self.top_frame)
        self.SettingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SettingsFrame.setObjectName("SettingsFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.SettingsFrame)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.umbralFrame = QtWidgets.QFrame(self.SettingsFrame)
        self.umbralFrame.setMinimumSize(QtCore.QSize(200, 100))
        self.umbralFrame.setMaximumSize(QtCore.QSize(200, 300))
        self.umbralFrame.setStyleSheet("QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 69, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.umbralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.umbralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.umbralFrame.setObjectName("umbralFrame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.umbralFrame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.umbralSlider = QtWidgets.QSlider(self.umbralFrame)
        self.umbralSlider.setMinimumSize(QtCore.QSize(0, 40))
        self.umbralSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.umbralSlider.setStyleSheet("background-color: rgba(42,45,52,255)")
        self.umbralSlider.setOrientation(QtCore.Qt.Horizontal)
        self.umbralSlider.setObjectName("umbralSlider")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.umbralSlider)
        self.umbralLabel = QtWidgets.QLabel(self.umbralFrame)
        self.umbralLabel.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.umbralLabel.setFont(font)
        self.umbralLabel.setObjectName("umbralLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.umbralLabel)
        self.gridLayout_2.addWidget(self.umbralFrame, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.heuristicaFrame = QtWidgets.QFrame(self.SettingsFrame)
        self.heuristicaFrame.setMinimumSize(QtCore.QSize(200, 100))
        self.heuristicaFrame.setMaximumSize(QtCore.QSize(200, 300))
        self.heuristicaFrame.setStyleSheet("QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 69, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.heuristicaFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heuristicaFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.heuristicaFrame.setObjectName("heuristicaFrame")
        self.formLayout_4 = QtWidgets.QFormLayout(self.heuristicaFrame)
        self.formLayout_4.setObjectName("formLayout_4")
        self.heuristicaSlider = QtWidgets.QSlider(self.heuristicaFrame)
        self.heuristicaSlider.setMinimumSize(QtCore.QSize(0, 40))
        self.heuristicaSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.heuristicaSlider.setStyleSheet("background-color: rgba(42,45,52,255)")
        self.heuristicaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.heuristicaSlider.setObjectName("heuristicaSlider")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.heuristicaSlider)
        self.heuristicaLabel = QtWidgets.QLabel(self.heuristicaFrame)
        self.heuristicaLabel.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.heuristicaLabel.setFont(font)
        self.heuristicaLabel.setObjectName("heuristicaLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.heuristicaLabel)
        self.gridLayout_2.addWidget(self.heuristicaFrame, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_7.addWidget(self.SettingsFrame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusFrame = QtWidgets.QFrame(self.top_frame)
        self.statusFrame.setMinimumSize(QtCore.QSize(350, 0))
        self.statusFrame.setStyleSheet("QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 69, 116);\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.statusFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statusFrame.setObjectName("statusFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.statusFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.progress_cont = QtWidgets.QFrame(self.statusFrame)
        self.progress_cont.setMinimumSize(QtCore.QSize(225, 225))
        self.progress_cont.setMaximumSize(QtCore.QSize(225, 225))
        self.progress_cont.setStyleSheet("QFrame{        \n"
"    background-color: rgb(255, 255, 255,0);\n"
"    border: 3px solid rgb(255, 255, 255);\n"
"    border-radius: 100px;\n"
"}")
        self.progress_cont.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.progress_cont.setFrameShadow(QtWidgets.QFrame.Raised)
        self.progress_cont.setObjectName("progress_cont")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.progress_cont)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.progress = roundProgressBar(self.progress_cont)
        self.progress.setStyleSheet("border-radius: 0px;\n"
"background-color: rgba(255, 255, 255,0);")
        self.progress.setObjectName("progress")
        self.horizontalLayout_9.addWidget(self.progress)
        self.gridLayout_6.addWidget(self.progress_cont, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addWidget(self.statusFrame, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.top_frame, 0, QtCore.Qt.AlignLeft)
        self.bottom_frame = QtWidgets.QFrame(self.accounts_page)
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.bottom_frame)
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.login_response_frame_7 = QtWidgets.QFrame(self.bottom_frame)
        self.login_response_frame_7.setMinimumSize(QtCore.QSize(200, 100))
        self.login_response_frame_7.setMaximumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.login_response_frame_7.setFont(font)
        self.login_response_frame_7.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(255,85,124 255);\n"
"    border: 4px;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-top-right-radius: 50px;\n"
"}\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.login_response_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_response_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_response_frame_7.setObjectName("login_response_frame_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.login_response_frame_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.generarMIDIButton = QtWidgets.QPushButton(self.login_response_frame_7)
        self.generarMIDIButton.setMinimumSize(QtCore.QSize(0, 40))
        self.generarMIDIButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.generarMIDIButton.setFont(font)
        self.generarMIDIButton.setStyleSheet("")
        self.generarMIDIButton.setObjectName("generarMIDIButton")
        self.verticalLayout_10.addWidget(self.generarMIDIButton)
        self.generarPDFButton = QtWidgets.QPushButton(self.login_response_frame_7)
        self.generarPDFButton.setMinimumSize(QtCore.QSize(0, 40))
        self.generarPDFButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generarPDFButton.setFont(font)
        self.generarPDFButton.setStyleSheet("background-color: rgba(125,64,245,255);\n"
"\n"
"")
        self.generarPDFButton.setObjectName("generarPDFButton")
        self.verticalLayout_10.addWidget(self.generarPDFButton)
        self.gridLayout_3.addWidget(self.login_response_frame_7, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.music_player_frame = QtWidgets.QFrame(self.bottom_frame)
        self.music_player_frame.setMinimumSize(QtCore.QSize(300, 100))
        self.music_player_frame.setMaximumSize(QtCore.QSize(700, 300))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.music_player_frame.setFont(font)
        self.music_player_frame.setStyleSheet("QFrame{    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(42,45,52,255);\n"
"    border: 2px solid rgb(0, 69, 116);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"    padding: 10px;\n"
"    border: none;\n"
"}")
        self.music_player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.music_player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.music_player_frame.setObjectName("music_player_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.music_player_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.musicTitleLabel = QtWidgets.QLabel(self.music_player_frame)
        self.musicTitleLabel.setMaximumSize(QtCore.QSize(300, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.musicTitleLabel.setFont(font)
        self.musicTitleLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.musicTitleLabel.setObjectName("musicTitleLabel")
        self.gridLayout_4.addWidget(self.musicTitleLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.timestampLabel = QtWidgets.QLabel(self.music_player_frame)
        self.timestampLabel.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timestampLabel.setFont(font)
        self.timestampLabel.setObjectName("timestampLabel")
        self.gridLayout_4.addWidget(self.timestampLabel, 1, 0, 1, 1)
        self.timestampSlider = QtWidgets.QSlider(self.music_player_frame)
        self.timestampSlider.setMinimumSize(QtCore.QSize(400, 40))
        self.timestampSlider.setMaximumSize(QtCore.QSize(500, 16777215))
        self.timestampSlider.setStyleSheet("background-color: rgba(42,45,52,255)")
        self.timestampSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timestampSlider.setObjectName("timestampSlider")
        self.gridLayout_4.addWidget(self.timestampSlider, 1, 1, 1, 1)
        self.totaltimeLabel = QtWidgets.QLabel(self.music_player_frame)
        self.totaltimeLabel.setMaximumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.totaltimeLabel.setFont(font)
        self.totaltimeLabel.setObjectName("totaltimeLabel")
        self.gridLayout_4.addWidget(self.totaltimeLabel, 1, 2, 1, 1)
        self.button_music_player_frame = QtWidgets.QFrame(self.music_player_frame)
        self.button_music_player_frame.setStyleSheet("QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.button_music_player_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_music_player_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_music_player_frame.setObjectName("button_music_player_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.button_music_player_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.playButton = QtWidgets.QPushButton(self.button_music_player_frame)
        self.playButton.setMinimumSize(QtCore.QSize(50, 30))
        self.playButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.playButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/cil-media-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon4)
        self.playButton.setIconSize(QtCore.QSize(24, 24))
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_8.addWidget(self.playButton)
        self.pauseButton = QtWidgets.QPushButton(self.button_music_player_frame)
        self.pauseButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pauseButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/cil-media-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon5)
        self.pauseButton.setIconSize(QtCore.QSize(24, 24))
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_8.addWidget(self.pauseButton)
        self.stopButton = QtWidgets.QPushButton(self.button_music_player_frame)
        self.stopButton.setMinimumSize(QtCore.QSize(50, 30))
        self.stopButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/cil-media-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon6)
        self.stopButton.setIconSize(QtCore.QSize(24, 24))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_8.addWidget(self.stopButton)
        self.gridLayout_4.addWidget(self.button_music_player_frame, 2, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_3.addWidget(self.music_player_frame, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addWidget(self.bottom_frame, 0, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.accounts_page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setStyleSheet("")
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.informationFrame = QtWidgets.QFrame(self.settings_page)
        self.informationFrame.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel{\n"
"    color: #fff;\n"
"}")
        self.informationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.informationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.informationFrame.setObjectName("informationFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.informationFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.githubButton = QtWidgets.QPushButton(self.informationFrame)
        self.githubButton.setMinimumSize(QtCore.QSize(855, 300))
        self.githubButton.setStyleSheet("image: url(:/images/images/GitHub-LogoCeleste.png);")
        self.githubButton.setText("")
        self.githubButton.setObjectName("githubButton")
        self.gridLayout_5.addWidget(self.githubButton, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.informationFrame)
        self.stackedWidget.addWidget(self.settings_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMinimumSize(QtCore.QSize(0, 50))
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-top-color: solid 1px  rgb(0, 0, 0);\n"
"    border-bottom-left-radius: 25px;\n"
"    border-bottom-right-radius: 25px;\n"
"}\n"
"QLabel{\n"
"    color: #fff;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.main_footer)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.size_grip = QtWidgets.QFrame(self.main_footer)
        self.size_grip.setMinimumSize(QtCore.QSize(20, 20))
        self.size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.size_grip.setStyleSheet("")
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_6.addWidget(self.size_grip)
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "HARMONIC ALGORITHM PROGRAM"))
        self.accounts_button.setText(_translate("MainWindow", "PROGRAMA"))
        self.home_button.setText(_translate("MainWindow", "INICIO"))
        self.settings_button.setText(_translate("MainWindow", "CODIGO"))
        self.scoreGenerateButton.setText(_translate("MainWindow", "CONVERTIR PARTITURA"))
        self.loadWavButton.setText(_translate("MainWindow", "CARGAR PIEZA MUSICAL"))
        self.umbralLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">UMBRAL</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">COMPENSACI├ôN</span></p></body></html>"))
        self.heuristicaLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">HEURISTICA</span></p><p align=\"center\"><span style=\" font-size:10pt;\">FLEXIBILIDAD</span></p></body></html>"))
        self.generarMIDIButton.setText(_translate("MainWindow", "VER ARCHIVO MIDI"))
        self.generarPDFButton.setText(_translate("MainWindow", "VER PDF"))
        self.musicTitleLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">REPRODUCIR MIDI</span></p></body></html>"))
        self.timestampLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0:00</p></body></html>"))
        self.totaltimeLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">0:00</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "v 1.0"))
    # retranslateUi

