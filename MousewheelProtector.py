# Adapted from Violet Giraffes answer at
# https://stackoverflow.com/questions/5821802/qspinbox-inside-a-qscrollarea-how-to-prevent-spin-box-from-stealing-focus-when
from PyQt5 import QtCore, QtGui, QtWidgets


class MousewheelProtector(QtCore.QObject):
    def eventFilter(self, obje, even):
        if (
            type(even) == QtGui.QWheelEvent
            and type(obje) == QtWidgets.QSpinBox
            and not obje.hasFocus()
        ):
            even.ignore()
            return True
        try:
            return obje.eventFilter(obje, even)
        except Exception:
            return False
