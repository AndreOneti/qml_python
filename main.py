#!/usr/bin/env python

import sys
from threading import Thread
from time import sleep

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtQml import *

import resources


class Person(QObject):
    def __init__(self, parent: None) -> None:
        super().__init__(parent)

        self._name = ''

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def run_qml():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qmlRegisterType(Person, 'People', 1, 0, 'Person')

    engine.load("qml:Main.qml")

    sys.exit(app.exec())


if __name__ == "__main__":
    run_qml()
