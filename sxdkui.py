# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sxdk.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(615, 518)
        Main.setAutoFillBackground(True)
        Main.setStyleSheet(_fromUtf8("font: 12pt \"Monospace\";"))
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.NOPLabel = QtGui.QLabel(self.centralwidget)
        self.NOPLabel.setGeometry(QtCore.QRect(10, 40, 161, 31))
        self.NOPLabel.setObjectName(_fromUtf8("NOPLabel"))
        self.Nopslide = QtGui.QSpinBox(self.centralwidget)
	self.Nopslide.setGeometry(QtCore.QRect(190, 40, 61, 27))
        self.Nopslide.setMinimumSize(QtCore.QSize(51, 0))
        self.Nopslide.setMaximum(2147483647)
        self.Nopslide.setObjectName(_fromUtf8("Nopslide"))
        self.AddrszLabel = QtGui.QLabel(self.centralwidget)
        self.AddrszLabel.setGeometry(QtCore.QRect(11, 90, 141, 31))
        self.AddrszLabel.setObjectName(_fromUtf8("AddrszLabel"))
        self.OffsetLabel = QtGui.QLabel(self.centralwidget)
        self.OffsetLabel.setGeometry(QtCore.QRect(11, 140, 111, 31))
        self.OffsetLabel.setObjectName(_fromUtf8("OffsetLabel"))
        self.Addrsz = QtGui.QSpinBox(self.centralwidget)
        self.Addrsz.setGeometry(QtCore.QRect(190, 90, 61, 27))
        self.Addrsz.setMinimumSize(QtCore.QSize(51, 0))
        self.Addrsz.setMaximum(2147483647)
        self.Addrsz.setObjectName(_fromUtf8("Addrsz"))
        self.Saddr = QtGui.QLineEdit(self.centralwidget)
        self.Saddr.setGeometry(QtCore.QRect(450, 90, 151, 27))
        self.Saddr.setMaxLength(10)
        self.Saddr.setObjectName(_fromUtf8("Saddr"))
        self.SAddrLabel = QtGui.QLabel(self.centralwidget)
        self.SAddrLabel.setGeometry(QtCore.QRect(280, 90, 161, 31))
        self.SAddrLabel.setObjectName(_fromUtf8("SAddrLabel"))
        self.OS_CB = QtGui.QComboBox(self.centralwidget)
        self.OS_CB.setGeometry(QtCore.QRect(450, 40, 151, 27))
        self.OS_CB.setObjectName(_fromUtf8("OS_CB"))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OS_CB.addItem(_fromUtf8(""))
        self.OSLabel = QtGui.QLabel(self.centralwidget)
        self.OSLabel.setGeometry(QtCore.QRect(280, 40, 161, 21))
        self.OSLabel.setObjectName(_fromUtf8("OSLabel"))
        self.Clear = QtGui.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(20, 410, 98, 27))
        self.Clear.setObjectName(_fromUtf8("Clear"))
	self.Clear.clicked.connect(self.clear)
        self.Save = QtGui.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(490, 410, 98, 27))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(190, 140, 61, 27))
        self.spinBox.setMaximum(2147483647)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.radioButton64_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton64_2.setGeometry(QtCore.QRect(10, 190, 101, 21))
        self.radioButton64_2.setObjectName(_fromUtf8("radioButton64_2"))
        self.radioButton64_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton64_3.setGeometry(QtCore.QRect(150, 190, 101, 21))
        self.radioButton64_3.setObjectName(_fromUtf8("radioButton64_3"))
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Main)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Main.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Main)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(Main)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtGui.QToolBar(Main)
        self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtGui.QToolBar(Main)
        self.toolBar_4.setObjectName(_fromUtf8("toolBar_4"))
        Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)

        self.retranslateUi(Main)
        QtCore.QObject.connect(self.Clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Clear.click)
        QtCore.QObject.connect(Main, QtCore.SIGNAL(_fromUtf8("toolButtonStyleChanged(Qt::ToolButtonStyle)")), self.radioButton64_2.toggle)
        QtCore.QMetaObject.connectSlotsByName(Main)
	

    def clear(self):
	self.Nopslide.setValue(0)
	

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "Shell Exploit Development kit", None))
        self.NOPLabel.setText(_translate("Main", "NOP instructions", None))
        self.AddrszLabel.setText(_translate("Main", "Address blocks", None))
        self.OffsetLabel.setText(_translate("Main", "Offset size ", None))
        self.SAddrLabel.setText(_translate("Main", "Starting Address", None))
        self.OS_CB.setItemText(0, _translate("Main", "Linux", None))
        self.OS_CB.setItemText(1, _translate("Main", "Windows Xp, Vista, 7", None))
        self.OS_CB.setItemText(2, _translate("Main", "BSD", None))
        self.OS_CB.setItemText(3, _translate("Main", "FreeBSD", None))
        self.OS_CB.setItemText(4, _translate("Main", "NetBSD", None))
        self.OS_CB.setItemText(5, _translate("Main", "OpenBSD", None))
        self.OS_CB.setItemText(6, _translate("Main", "OSX", None))
        self.OS_CB.setItemText(7, _translate("Main", "OSX/PPC", None))
        self.OS_CB.setItemText(8, _translate("Main", "Hp-Ux", None))
        self.OS_CB.setItemText(9, _translate("Main", "Irix", None))
        self.OS_CB.setItemText(10, _translate("Main", "Linux/ARM", None))
        self.OS_CB.setItemText(11, _translate("Main", "Linux/Strong Arm", None))
        self.OS_CB.setItemText(12, _translate("Main", "Linux/Super-H", None))
        self.OS_CB.setItemText(13, _translate("Main", "Linux/MIPS", None))
        self.OS_CB.setItemText(14, _translate("Main", "Linux/PPc", None))
        self.OS_CB.setItemText(15, _translate("Main", "Linux/Sparc", None))
        self.OS_CB.setItemText(16, _translate("Main", "Linux/CRISv32", None))
        self.OS_CB.setItemText(17, _translate("Main", "Solaris/MIPS", None))
        self.OS_CB.setItemText(18, _translate("Main", "Solaris/SPARC", None))
        self.OS_CB.setItemText(19, _translate("Main", "Cisco IOS", None))
        self.OS_CB.setItemText(20, _translate("Main", "CSO", None))
        self.OS_CB.setItemText(21, _translate("Main", "Alpha", None))
        self.OS_CB.setItemText(22, _translate("Main", "AIX", None))
        self.OSLabel.setText(_translate("Main", "Operating System", None))
        self.Clear.setText(_translate("Main", "Clear", None))
        self.Save.setText(_translate("Main", "Save", None))
        self.radioButton64_2.setText(_translate("Main", "32-bit", None))
        self.radioButton64_3.setText(_translate("Main", "64-bit", None))
        self.toolBar.setWindowTitle(_translate("Main", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("Main", "toolBar_2", None))
        self.toolBar_3.setWindowTitle(_translate("Main", "toolBar_3", None))
        self.toolBar_4.setWindowTitle(_translate("Main", "toolBar_4", None))

	

#################################################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Main = QtGui.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

