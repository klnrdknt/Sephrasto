# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankMain.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 452)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.showTalente = QtWidgets.QCheckBox(Form)
        self.showTalente.setChecked(True)
        self.showTalente.setObjectName("showTalente")
        self.verticalLayout.addWidget(self.showTalente)
        self.showVorteile = QtWidgets.QCheckBox(Form)
        self.showVorteile.setChecked(True)
        self.showVorteile.setTristate(False)
        self.showVorteile.setObjectName("showVorteile")
        self.verticalLayout.addWidget(self.showVorteile)
        self.showFertigkeiten = QtWidgets.QCheckBox(Form)
        self.showFertigkeiten.setChecked(True)
        self.showFertigkeiten.setObjectName("showFertigkeiten")
        self.verticalLayout.addWidget(self.showFertigkeiten)
        self.showUebernatuerlicheFertigkeiten = QtWidgets.QCheckBox(Form)
        self.showUebernatuerlicheFertigkeiten.setChecked(True)
        self.showUebernatuerlicheFertigkeiten.setObjectName("showUebernatuerlicheFertigkeiten")
        self.verticalLayout.addWidget(self.showUebernatuerlicheFertigkeiten)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonLoadDB = QtWidgets.QPushButton(Form)
        self.buttonLoadDB.setObjectName("buttonLoadDB")
        self.verticalLayout.addWidget(self.buttonLoadDB)
        self.buttonSaveDB = QtWidgets.QPushButton(Form)
        self.buttonSaveDB.setObjectName("buttonSaveDB")
        self.verticalLayout.addWidget(self.buttonSaveDB)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listDatenbank = QtWidgets.QListView(Form)
        self.listDatenbank.setObjectName("listDatenbank")
        self.verticalLayout_2.addWidget(self.listDatenbank)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonHinzufuegen = QtWidgets.QPushButton(Form)
        self.buttonHinzufuegen.setObjectName("buttonHinzufuegen")
        self.horizontalLayout.addWidget(self.buttonHinzufuegen)
        self.buttonEditieren = QtWidgets.QPushButton(Form)
        self.buttonEditieren.setObjectName("buttonEditieren")
        self.horizontalLayout.addWidget(self.buttonEditieren)
        self.buttonLoeschen = QtWidgets.QPushButton(Form)
        self.buttonLoeschen.setObjectName("buttonLoeschen")
        self.horizontalLayout.addWidget(self.buttonLoeschen)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.showTalente, self.showVorteile)
        Form.setTabOrder(self.showVorteile, self.showFertigkeiten)
        Form.setTabOrder(self.showFertigkeiten, self.showUebernatuerlicheFertigkeiten)
        Form.setTabOrder(self.showUebernatuerlicheFertigkeiten, self.buttonHinzufuegen)
        Form.setTabOrder(self.buttonHinzufuegen, self.buttonEditieren)
        Form.setTabOrder(self.buttonEditieren, self.buttonLoeschen)
        Form.setTabOrder(self.buttonLoeschen, self.buttonLoadDB)
        Form.setTabOrder(self.buttonLoadDB, self.buttonSaveDB)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sephrasto - Datenbank-Editor"))
        self.showTalente.setText(_translate("Form", "Talente"))
        self.showVorteile.setText(_translate("Form", "Vorteile"))
        self.showFertigkeiten.setText(_translate("Form", "Profane Fertigkeiten"))
        self.showUebernatuerlicheFertigkeiten.setText(_translate("Form", "Übernatürliche Fertigkeiten"))
        self.buttonLoadDB.setText(_translate("Form", "Andere Regelbasis laden"))
        self.buttonSaveDB.setText(_translate("Form", "Regelbasis speichern"))
        self.buttonHinzufuegen.setText(_translate("Form", "Hinzufügen"))
        self.buttonEditieren.setText(_translate("Form", "Editieren"))
        self.buttonLoeschen.setText(_translate("Form", "Löschen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

