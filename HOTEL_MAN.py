from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv
import sqlite3
from random import randint

db = sqlite3.connect("hotel.db")
cr = db.cursor()

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"Manager.ui"))

class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.add_guest_widget.hide()
        self.button_setup()

    def setupprice(self):
        self.room_type_box.clear()
        if self.room_view_box.currentText() == "Sea":
            self.room_type_box.addItem("Single-500LE")
            self.room_type_box.addItem("Double-700LE")
            self.room_type_box.addItem("Triple-900LE")
            self.room_type_box.addItem( "Quad-1150LE")
            self.room_type_box.addItem("Suite-1750LE")
        elif self.room_view_box.currentText() == "Pool":
            self.room_type_box.addItem("Single-400LE")
            self.room_type_box.addItem("Double-550LE")
            self.room_type_box.addItem("Triple-750LE")
            self.room_type_box.addItem( "Quad-900LE")
            self.room_type_box.addItem("Suite-1500LE")
        elif self.room_view_box.currentText() == "Street":
            self.room_type_box.addItem("Single-325LE")
            self.room_type_box.addItem("Double-475LE")
            self.room_type_box.addItem("Triple-600LE")
            self.room_type_box.addItem( "Quad-750LE")
            self.room_type_box.addItem("Suite-1250LE")

    def button_setup(self):
        self.add_guest_button.clicked.connect(self.add_guest_window)
        self.check_button.clicked.connect(self.check_room)
        self.reserve_button.clicked.connect(self.reserv)
        self.confirm_button.clicked.connect(self.confirmation)
    def add_guest_window(self):
        self.reserve_button.hide()
        self.confirm_button.hide()
        self.add_guest_widget.show()
        

    def check_room(self):
        self.reserve_button.show()
        self.no_of_adults = self.adults_box.value()
        self.no_of_children = self.children_box.value()
        self.no_of_nights = self.nights_box.value()
        self.guest_name = self.Guest_full_name.text()
        self.guest_number = self.guest_phone_number.text()
        self.guest_mail = self.guest_email.text()
        self.room_type_box.show()
        self.setupprice()

    def reserv(self):
        self.room_type = self.room_type_box.currentText()
        self.room_view = self.room_view_box.currentText()
        rom_typ = self.room_type.find("-")
        moh = cr.execute(f"select price , room_number from hotel_rooms where room_view = '{self.room_view}' and room_type = '{self.room_type[:rom_typ]}'")
        result = moh.fetchall()
        room_data = result[randint(0,len(result))]
        self.room_number = room_data[1]
        self.price = room_data[0]
        self.total_price_2.setText(f"Room Number : {self.room_number}")
        self.total_price.setText(f"Total price :  {int(self.price)*int(self.no_of_nights)}LE")
        self.confirm_button.show()
    
    def clear(self):
        self.Guest_full_name.setText("")
        self.guest_phone_number.setText("")
        self.guest_email.setText("")
        self.adults_box.setValue(0)
        self.children_box.setValue(0)
        self.nights_box.setValue(0)
        self.room_type_box.clear()
        self.total_price.setText("Total price : ")
        self.total_price_2.setText("Room Number: ")
        self.add_guest_window()




    def message_box(self):
        self.message = QMessageBox()
        self.message.setIcon(QMessageBox.Information)
        self.message.setText(f"Guest Name:{self.guest_name}\nRoom Number: {self.room_number}")
        self.message.setWindowTitle("Reservation Confirmation")
        self.message.setStandardButtons(QMessageBox.Ok)
        self.message.exec_()

    def confirmation(self):
        cr.execute("insert into guest (Name,Phone_number,Email,room_number,Nights,Adults,Children) VALUES (?,?,?,?,?,?,?)",(self.guest_name,self.guest_number,self.guest_mail,self.room_number,self.no_of_nights,self.no_of_adults,self.no_of_children))
        self.message_box()
        db.commit()
        self.clear()

if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = mainapp()
    window.show()
    app.exec()