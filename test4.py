# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smithchart
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from Ui_test4 import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Gamma_converter import *
import math

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.checkBox.setChecked(True)
        #self.smithchart_key
        self.mags=[]
        self.phases=[]
        self.Reflectance_reals=[]
        self.Reflectance_imags=[]
        self.colour='blue'
        self.colours=[]
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.lineEdit_7.setText('50')
        self.Z0=50
        self.lineEdit_8.setText('0.001')
        self.lineEdit_9.setText('0')
        self.dBm=0
        self.Watts=0.001
        self.textBrowser.append('Impedance=50.0+0.0j ohm\nGamma=0.0+0.0j\nmag:0.0\nphase:0.0')
    @pyqtSlot(bool)
    def on_checkBox_clicked(self, checked):
        """
        Slot documentation goes here.
        
        @param checked DESCRIPTION
        @type bool
        """
        #if self.checkBox.isChecked():
        
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.textBrowser.setPlainText("")
        Real=self.lineEdit_2.text()
        Imag=self.lineEdit_4.text()
        if bool(Real)and bool(Imag):
            Reflectance=Impedance_to_Reflectance(float(Real),float(Imag), self.Z0)
            Reflectance_real=Reflectance.real
            Reflectance_imag=Reflectance.imag
            mag=round(xy_to_Magphase_Mag(Reflectance_real,Reflectance_imag),8)
            phase=round(xy_to_Magphase_phase(Reflectance_real,Reflectance_imag),8)
            self.textBrowser.append('Impedance='+Real+'+'+Imag+'j ohm')
            self.textBrowser.append('Gamma='+str(round(Reflectance.real,8))+'+'+str(round(Reflectance.imag,8))+'j')
            self.textBrowser.append('mag:' + str(mag) + '\nphase:' + str(phase))
            self.mags.append(mag)
            self.phases.append(phase)
            self.Reflectance_reals.append(Reflectance_real)
            self.Reflectance_imags.append(Reflectance_imag)
            self.colours.append(self.colour)
            #if self.checkBox.isChecked():
                #smithchart.displaysmithchart(self.Reflectance_reals,self.Reflectance_imags, self.colours)
            self.smithwidget.mpl.point_on_smithchart_plot(self.Reflectance_reals,self.Reflectance_imags, self.colours)
            #self.smithwidget.mpl.clear_chart()
        #self.label.setText("ENTER")
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textBrowser.setPlainText("")
        mag=self.lineEdit_3.text()
        phase=self.lineEdit_5.text()
        if bool(mag) and bool(phase):
            mag=float(mag)
            phase=float(phase)
            phase=phase%360
            Reflectance_real=Magphase_to_xy_X(mag,phase)
            Reflectance_imag=Magphase_to_xy_Y(mag,phase)
            Impedance=Reflectance_to_Impedance(Reflectance_real,Reflectance_imag, self.Z0)
            Real=round(Impedance.real,8)
            Imag=round(Impedance.imag,8)
            self.textBrowser.append('Impedance=' + str(Real) + '+' + str(Imag) + 'j ohm')
            self.textBrowser.append('Gamma='+str(round(Reflectance_real,8))+'+'+str(round(Reflectance_imag,8))+'j')
            self.textBrowser.append('mag:' + str(mag) + '\nphase:' + str(phase))
            self.mags.append(mag)
            self.phases.append(phase)
            self.Reflectance_reals.append(Reflectance_real)
            self.Reflectance_imags.append(Reflectance_imag)
            self.colours.append(self.colour)
            #if self.checkBox.isChecked():
                #smithchart.displaysmithchart(self.Reflectance_reals,self.Reflectance_imags, self.colours)
            self.smithwidget.mpl.point_on_smithchart_plot(self.Reflectance_reals,self.Reflectance_imags, self.colours)
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.textBrowser.setPlainText("")
        Reflectance_real=self.lineEdit.text()
        Reflectance_imag=self.lineEdit_6.text()
        if bool(Reflectance_imag) and bool(Reflectance_real):
            Reflectance_real=float(Reflectance_real)
            Reflectance_imag=float(Reflectance_imag)
            mag=xy_to_Magphase_Mag(Reflectance_real,Reflectance_imag)
            phase=xy_to_Magphase_phase(Reflectance_real,Reflectance_imag)
            Impedance=Reflectance_to_Impedance(Reflectance_real,Reflectance_imag, self.Z0)
            Real=round(Impedance.real,8)
            Imag=round(Impedance.imag,8)
            self.textBrowser.append('Impedance=' + str(Real) + '+' + str(Imag) + 'j ohm')
            self.textBrowser.append('Gamma='+str(round(Reflectance_real,8))+'+'+str(round(Reflectance_imag,8))+'j')
            self.textBrowser.append('mag:' + str(mag) + '\nphase:' + str(phase))
            self.mags.append(mag)
            self.phases.append(phase)
            self.Reflectance_reals.append(Reflectance_real)
            self.Reflectance_imags.append(Reflectance_imag)
            self.colours.append(self.colour)
            #print(self.mags)
            #if self.checkBox.isChecked():
                #smithchart.displaysmithchart(self.Reflectance_reals,self.Reflectance_imags, self.colours)
            self.smithwidget.mpl.point_on_smithchart_plot(self.Reflectance_reals,self.Reflectance_imags, self.colours)
    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        a=len(self.Reflectance_reals)
        if a!=0:
            self.Reflectance_reals.pop()
            self.Reflectance_imags.pop()
            self.colours.pop()
            #if self.checkBox.isChecked():
                #smithchart.displaysmithchart(self.Reflectance_reals,self.Reflectance_imags, self.colours)
            self.smithwidget.mpl.point_on_smithchart_plot(self.Reflectance_reals,self.Reflectance_imags, self.colours)
    def selectionchange(self,i):
        self.colour=self.comboBox.currentText()
        print(self.colours)
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        Z0_old=self.Z0
        self.Z0=float(self.lineEdit_7.text())
        #print(Z0_old)
        i=0
        for real in self.Reflectance_reals:
            Reflectance_new=old_Reflectance_to_new_Reflectance(real, self.Reflectance_imags[i], Z0_old, self.Z0)
            self.Reflectance_reals[i]=Reflectance_new.real
            self.Reflectance_imags[i]=Reflectance_new.imag
            i=i+1
        #if self.checkBox.isChecked():
            #smithchart.displaysmithchart(self.Reflectance_reals,self.Reflectance_imags, self.colours)
        self.smithwidget.mpl.point_on_smithchart_plot(self.Reflectance_reals,self.Reflectance_imags, self.colours)
        #print(self.Z0)
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        DB=float(self.lineEdit_9.text())
        WA=float(self.lineEdit_8.text())
        if WA!=self.Watts:
            self.Watts=WA
            self.dBm=round(10*math.log10(WA/0.001), 8)
            self.lineEdit_9.setText(str(self.dBm))
            self.lineEdit_8.setText(str(self.Watts))
            DB=float(self.lineEdit_9.text())
        
        if DB!=self.dBm:
            self.dBm=DB
            self.Watts=round((math.pow(10, DB/10))/1000, 8)
            self.lineEdit_9.setText(str(self.dBm))
            self.lineEdit_8.setText(str(self.Watts))
         
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
    

