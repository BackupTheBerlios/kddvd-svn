# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/data/programming/python/kddvd/kddvd.ui'
#
# Created: Út dub 25 17:21:47 2006
#      by: The PyQt User Interface Compiler (pyuic) 3.16
#
# WARNING! All changes made in this file will be lost!


import sys,commands
from qt import *


class frm_hlavni(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("frm_hlavni")



        self.btn_init = QPushButton(self,"btn_init")
        self.btn_init.setGeometry(QRect(5,90,590,26))
        self.btn_init.setFlat(1)

        self.lst_info = QListView(self,"lst_info")
        self.lst_info.addColumn(self.__tr("Name"))
        self.lst_info.addColumn(self.__tr("Device"))
        self.lst_info.addColumn(self.__tr("Medium"))
        self.lst_info.addColumn(self.__tr("Burning speed"))
        self.lst_info.setGeometry(QRect(5,5,590,80))

        self.pb_progress = QProgressBar(self,"pb_progress")
        self.pb_progress.setGeometry(QRect(5,365,590,25))

        self.lbl_progress = QLabel(self,"lbl_progress")
        self.lbl_progress.setGeometry(QRect(5,345,69,17))

        self.btn_stop = QPushButton(self,"btn_stop")
        self.btn_stop.setGeometry(QRect(5,395,590,26))
        self.btn_stop.setFlat(1)

        self.tab = QTabWidget(self,"tab")
        self.tab.setGeometry(QRect(5,125,590,205))

        self.tab_iso = QWidget(self.tab,"tab_iso")

        self.lbl_ciso = QLabel(self.tab_iso,"lbl_ciso")
        self.lbl_ciso.setGeometry(QRect(6,6,28,26))

        self.lne_cselect = QLineEdit(self.tab_iso,"lne_cselect")
        self.lne_cselect.setGeometry(QRect(40,7,490,24))
        self.lne_cselect.setMinimumSize(QSize(0,24))
        self.lne_cselect.setMaximumSize(QSize(32767,32767))

        self.btn_cselect = QPushButton(self.tab_iso,"btn_cselect")
        self.btn_cselect.setGeometry(QRect(536,6,43,26))
        self.btn_cselect.setMaximumSize(QSize(32767,32767))

        self.lne_params = QLineEdit(self.tab_iso,"lne_params")
        self.lne_params.setGeometry(QRect(134,41,445,24))
        self.lne_params.setMinimumSize(QSize(0,24))

        self.lbl_params = QLabel(self.tab_iso,"lbl_params")
        self.lbl_params.setGeometry(QRect(6,41,122,24))

        self.btn_ciso = QPushButton(self.tab_iso,"btn_ciso")
        self.btn_ciso.setGeometry(QRect(5,75,575,40))
        self.btn_ciso.setFlat(1)
        self.tab.insertTab(self.tab_iso,QString.fromLatin1(""))

        self.tab_burn = QWidget(self.tab,"tab_burn")
        self.tab.insertTab(self.tab_burn,QString.fromLatin1(""))

        self.languageChange()

        self.resize(QSize(600,426).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.btn_ciso,SIGNAL("clicked()"),self.createISO)
        self.connect(self.btn_init,SIGNAL("clicked()"),self.initialization)
        self.connect(self.btn_cselect,SIGNAL("clicked()"),self.selectISO)


    def languageChange(self):
        self.setCaption(self.__tr("KDDVD"))
        self.btn_init.setText(self.__tr("Initialization"))
        self.lst_info.header().setLabel(0,self.__tr("Name"))
        self.lst_info.header().setLabel(1,self.__tr("Device"))
        self.lst_info.header().setLabel(2,self.__tr("Medium"))
        self.lst_info.header().setLabel(3,self.__tr("Burning speed"))
        self.lbl_progress.setText(self.__tr("Progress"))
        self.btn_stop.setText(self.__tr("STOP"))
        self.lbl_ciso.setText(self.__tr("ISO:"))
        self.btn_cselect.setText(self.__tr("..."))
        self.lbl_params.setText(self.__tr("Parameters for dd:"))
        self.btn_ciso.setText(self.__tr("Create ISO"))
        self.tab.changeTab(self.tab_iso,self.__tr("Create ISO"))
        self.tab.changeTab(self.tab_burn,self.__tr("Burn ISO"))


    def initialization(self):
        UDIs = str(commands.getoutput("hal-find-by-capability --capability storage.cdrom")).split("\n")
        for UDI in UDIs:
            NAM = commands.getoutput("hal-get-property --udi "+UDI+" --key info.product")
            DEV = commands.getoutput("hal-get-property --udi "+UDI+" --key block.device")
            MED = commands.getoutput("hal-get-property --udi "+UDI+" --key storage.cdrom.cdr | sed -e s/true/CD/ -e s/false//")+" "+commands.getoutput("hal-get-property --udi "+UDI+" --key storage.cdrom.dvd | sed -e s/true/DVD/ -e s/false//")
            SPE = commands.getoutput("mount | grep -q "+DEV+" && dvd+rw-mediainfo "+DEV+" | grep 'Current Write Speed' | cut -d: -f2 | sed 's: ::g'")
            self.lst_info.insertItem(QListViewItem(self.lst_info, NAM, DEV, MED, SPE))
        

    def createISO(self):
        print "frm_hlavni.createISO(): Not implemented yet"
        ##print str("dd if="+self.lne_cselect.text()+" of="+"/dev/hdc"+" "+self.lne_params.text())
        ##print str(self.lst_info.item[0,2])

    def burnISO(self):
        print "frm_hlavni.burnISO(): Not implemented yet"

    def selectISO(self):
        self.lne_cselect.setText(str(QFileDialog.getSaveFileName(".iso", "*.iso", self, "FileDialog")))
        

    def selectBURN(self):
        print "frm_hlavni.selectBURN(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("frm_hlavni",s,c)

if __name__ == "__main__":
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL("lastWindowClosed()"),a,SLOT("quit()"))
    w = frm_hlavni()
    a.setMainWidget(w)
    w.show()
    a.exec_loop()
