# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditRuestung.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_talentDialog(object):
    def setupUi(self, talentDialog):
        talentDialog.setObjectName("talentDialog")
        talentDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        talentDialog.resize(441, 434)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sbKopf = QtWidgets.QSpinBox(talentDialog)
        self.sbKopf.setMinimumSize(QtCore.QSize(50, 0))
        self.sbKopf.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbKopf.setMaximum(8)
        self.sbKopf.setObjectName("sbKopf")
        self.gridLayout.addWidget(self.sbKopf, 11, 2, 1, 1)
        self.sbBeine = QtWidgets.QSpinBox(talentDialog)
        self.sbBeine.setMinimumSize(QtCore.QSize(50, 0))
        self.sbBeine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbBeine.setMaximum(8)
        self.sbBeine.setObjectName("sbBeine")
        self.gridLayout.addWidget(self.sbBeine, 6, 2, 1, 1)
        self.warning = QtWidgets.QLabel(talentDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(talentDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 1, 1, 1)
        self.sbBauch = QtWidgets.QSpinBox(talentDialog)
        self.sbBauch.setMinimumSize(QtCore.QSize(50, 0))
        self.sbBauch.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbBauch.setMaximum(8)
        self.sbBauch.setObjectName("sbBauch")
        self.gridLayout.addWidget(self.sbBauch, 9, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.sbSchild = QtWidgets.QSpinBox(talentDialog)
        self.sbSchild.setMinimumSize(QtCore.QSize(50, 0))
        self.sbSchild.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbSchild.setMaximum(8)
        self.sbSchild.setObjectName("sbSchild")
        self.gridLayout.addWidget(self.sbSchild, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.leName = QtWidgets.QLineEdit(talentDialog)
        self.leName.setMinimumSize(QtCore.QSize(300, 0))
        self.leName.setObjectName("leName")
        self.gridLayout.addWidget(self.leName, 2, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 1, 1, 1)
        self.sbSchwert = QtWidgets.QSpinBox(talentDialog)
        self.sbSchwert.setMinimumSize(QtCore.QSize(50, 0))
        self.sbSchwert.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbSchwert.setMaximum(8)
        self.sbSchwert.setObjectName("sbSchwert")
        self.gridLayout.addWidget(self.sbSchwert, 8, 2, 1, 1)
        self.sbBrust = QtWidgets.QSpinBox(talentDialog)
        self.sbBrust.setMinimumSize(QtCore.QSize(50, 0))
        self.sbBrust.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sbBrust.setMaximum(8)
        self.sbBrust.setObjectName("sbBrust")
        self.gridLayout.addWidget(self.sbBrust, 10, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(talentDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(talentDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(talentDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        self.lblRS = QtWidgets.QLabel(talentDialog)
        self.lblRS.setObjectName("lblRS")
        self.gridLayout.addWidget(self.lblRS, 5, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(talentDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.cbTyp = QtWidgets.QComboBox(talentDialog)
        self.cbTyp.setObjectName("cbTyp")
        self.gridLayout.addWidget(self.cbTyp, 3, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(talentDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)
        self.teBeschreibung = QtWidgets.QTextEdit(talentDialog)
        self.teBeschreibung.setObjectName("teBeschreibung")
        self.gridLayout.addWidget(self.teBeschreibung, 12, 1, 1, 2)
        self.label_11 = QtWidgets.QLabel(talentDialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.cbSystem = QtWidgets.QComboBox(talentDialog)
        self.cbSystem.setObjectName("cbSystem")
        self.cbSystem.addItem("")
        self.cbSystem.addItem("")
        self.cbSystem.addItem("")
        self.gridLayout.addWidget(self.cbSystem, 4, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept)
        self.buttonBox.rejected.connect(talentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.leName, self.cbTyp)
        talentDialog.setTabOrder(self.cbTyp, self.cbSystem)
        talentDialog.setTabOrder(self.cbSystem, self.sbBeine)
        talentDialog.setTabOrder(self.sbBeine, self.sbSchild)
        talentDialog.setTabOrder(self.sbSchild, self.sbSchwert)
        talentDialog.setTabOrder(self.sbSchwert, self.sbBauch)
        talentDialog.setTabOrder(self.sbBauch, self.sbBrust)
        talentDialog.setTabOrder(self.sbBrust, self.sbKopf)
        talentDialog.setTabOrder(self.sbKopf, self.teBeschreibung)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(
            _translate("talentDialog", "Sephrasto - Rüstung bearbeiten...")
        )
        self.warning.setText(
            _translate(
                "talentDialog",
                "Dies ist eine Ilaris-Standardrüstung. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in der aktuellen User-Regelbasis gelöscht. Damit erhältst du für diese Rüstung keine automatischen Updates mehr mit neuen Sephrasto-Versionen.",
            )
        )
        self.label_7.setText(_translate("talentDialog", "Kopf"))
        self.label_3.setText(_translate("talentDialog", "Schildarm"))
        self.label.setText(_translate("talentDialog", "Name"))
        self.label_5.setText(_translate("talentDialog", "Bauch"))
        self.label_8.setText(_translate("talentDialog", "RS"))
        self.label_2.setText(_translate("talentDialog", "Beine"))
        self.label_9.setText(_translate("talentDialog", "Typ"))
        self.label_4.setText(_translate("talentDialog", "Schwertarm"))
        self.lblRS.setText(_translate("talentDialog", "0"))
        self.label_6.setText(_translate("talentDialog", "Brust"))
        self.label_10.setText(_translate("talentDialog", "Beschreibung"))
        self.label_11.setText(_translate("talentDialog", "Verfügbarkeit"))
        self.cbSystem.setItemText(
            0, _translate("talentDialog", "Beide Rüstungssysteme")
        )
        self.cbSystem.setItemText(
            1, _translate("talentDialog", "Einfaches Rüstungssystem")
        )
        self.cbSystem.setItemText(2, _translate("talentDialog", "Zonenrüstungssystem"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())
