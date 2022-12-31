// Creation Date: 2022-30-12
// Author: André Luiz Oneti Carvalho

import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

import People 1.0

ApplicationWindow {
    id: window
    width: 500
    height: 580
    visible: true
    title: qsTr("Python + QML")

    Shortcut {
        sequence: "esc"
        onActivated: {
            window.close();
        }
    }

    Text {
        id: txt
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }

    Person {
        id: andre
        name: "Andre"
        Component.onCompleted: {
            txt.text += ` ${andre.name}`;
        }
    }
}
