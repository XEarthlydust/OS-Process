# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 110, 531, 234))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.pc_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.pc_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pc_gridLayout.setObjectName("pc_gridLayout")
        self.pc_label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pc_label_5.setObjectName("pc_label_5")
        self.pc_gridLayout.addWidget(self.pc_label_5, 4, 0, 1, 1)
        self.pc_label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pc_label_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pc_label_1.setObjectName("pc_label_1")
        self.pc_gridLayout.addWidget(self.pc_label_1, 0, 0, 1, 1)
        self.pc_bar_5 = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.pc_bar_5.setProperty("value", 0)
        self.pc_bar_5.setObjectName("pc_bar_5")
        self.pc_gridLayout.addWidget(self.pc_bar_5, 4, 1, 1, 1)
        self.pc_label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pc_label_3.setObjectName("pc_label_3")
        self.pc_gridLayout.addWidget(self.pc_label_3, 2, 0, 1, 1)
        self.pc_bar_3 = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.pc_bar_3.setMaximum(100)
        self.pc_bar_3.setProperty("value", 0)
        self.pc_bar_3.setTextVisible(True)
        self.pc_bar_3.setOrientation(QtCore.Qt.Horizontal)
        self.pc_bar_3.setObjectName("pc_bar_3")
        self.pc_gridLayout.addWidget(self.pc_bar_3, 2, 1, 1, 1)
        self.pc_label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pc_label_4.setObjectName("pc_label_4")
        self.pc_gridLayout.addWidget(self.pc_label_4, 3, 0, 1, 1)
        self.pc_bar_4 = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.pc_bar_4.setProperty("value", 0)
        self.pc_bar_4.setObjectName("pc_bar_4")
        self.pc_gridLayout.addWidget(self.pc_bar_4, 3, 1, 1, 1)
        self.pc_bar_1 = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.pc_bar_1.setProperty("value", 0)
        self.pc_bar_1.setObjectName("pc_bar_1")
        self.pc_gridLayout.addWidget(self.pc_bar_1, 0, 1, 1, 1)
        self.pc_label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pc_label_2.setObjectName("pc_label_2")
        self.pc_gridLayout.addWidget(self.pc_label_2, 1, 0, 1, 1)
        self.pc_bar_2 = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.pc_bar_2.setProperty("value", 0)
        self.pc_bar_2.setObjectName("pc_bar_2")
        self.pc_gridLayout.addWidget(self.pc_bar_2, 1, 1, 1, 1)
        self.pgdn_button = QtWidgets.QPushButton(self.centralwidget)
        self.pgdn_button.setGeometry(QtCore.QRect(380, 360, 93, 28))
        self.pgdn_button.setObjectName("pgdn_button")
        self.pgup_button = QtWidgets.QPushButton(self.centralwidget)
        self.pgup_button.setGeometry(QtCore.QRect(210, 360, 93, 28))
        self.pgup_button.setObjectName("pgup_button")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(110, 20, 471, 66))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.time_lay = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.time_lay.setContentsMargins(0, 0, 0, 0)
        self.time_lay.setObjectName("time_lay")
        self.time_lcd = QtWidgets.QLCDNumber(self.horizontalLayoutWidget_3)
        self.time_lcd.setObjectName("timr_lcd")
        self.time_lay.addWidget(self.time_lcd)
        self.button_lay = QtWidgets.QGridLayout()
        self.button_lay.setObjectName("button_lay")
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.start_button.setObjectName("start_button")
        self.button_lay.addWidget(self.start_button, 0, 1, 1, 1)
        self.null_lay_1 = QtWidgets.QHBoxLayout()
        self.null_lay_1.setObjectName("null_lay_1")
        self.button_lay.addLayout(self.null_lay_1, 0, 0, 1, 1)
        self.change_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.change_button.setObjectName("change_button")
        self.button_lay.addWidget(self.change_button, 1, 1, 1, 1)
        self.null_lay_2 = QtWidgets.QHBoxLayout()
        self.null_lay_2.setObjectName("null_lay_2")
        self.button_lay.addLayout(self.null_lay_2, 0, 2, 1, 1)
        self.time_lay.addLayout(self.button_lay)
        self.state_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.state_text.setGeometry(QtCore.QRect(20, 400, 651, 211))
        self.state_text.setObjectName("state_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menun = QtWidgets.QMenu(self.menubar)
        self.menun.setObjectName("menun")
        MainWindow.setMenuBar(self.menubar)
        self.actionFCFS = QtWidgets.QAction(MainWindow)
        self.actionFCFS.setObjectName("actionFCFS")
        self.actionSJF = QtWidgets.QAction(MainWindow)
        self.actionSJF.setObjectName("actionSJF")
        self.actionMFQ = QtWidgets.QAction(MainWindow)
        self.actionMFQ.setObjectName("actionMFQ")
        self.actionRR = QtWidgets.QAction(MainWindow)
        self.actionRR.setObjectName("actionRR")
        self.menun.addAction(self.actionFCFS)
        self.menun.addAction(self.actionSJF)
        self.menun.addAction(self.actionMFQ)
        self.menun.addAction(self.actionRR)
        self.menubar.addAction(self.menun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "进程调度模拟器"))
        self.pc_label_5.setText(_translate("MainWindow", "程序 5"))
        self.pc_label_1.setText(_translate("MainWindow", "程序 1"))
        self.pc_bar_5.setFormat(_translate("MainWindow", " %v/%m"))
        self.pc_label_3.setText(_translate("MainWindow", "程序 3"))
        self.pc_bar_3.setFormat(_translate("MainWindow", " %v/%m"))
        self.pc_label_4.setText(_translate("MainWindow", "程序 4"))
        self.pc_bar_4.setFormat(_translate("MainWindow", " %v/%m"))
        self.pc_bar_1.setFormat(_translate("MainWindow", " %v/%m"))
        self.pc_label_2.setText(_translate("MainWindow", "程序 2"))
        self.pc_bar_2.setFormat(_translate("MainWindow", " %v/%m"))
        self.pgdn_button.setText(_translate("MainWindow", "下一页"))
        self.pgup_button.setText(_translate("MainWindow", "上一页"))
        self.start_button.setText(_translate("MainWindow", "初始化"))
        self.change_button.setText(_translate("MainWindow", "下一状态"))
        self.menun.setTitle(_translate("MainWindow", "调整调度算法"))
        self.actionFCFS.setText(_translate("MainWindow", "FCFS"))
        self.actionSJF.setText(_translate("MainWindow", "SJF"))
        self.actionMFQ.setText(_translate("MainWindow", "MFQ"))
        self.actionRR.setText(_translate("MainWindow", "RR"))
