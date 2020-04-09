import QtQuick 2.7

Rectangle {
    color: "#ff243A55"
    property int count: 0

//    AnimatedImage {
//        width: 90
//        height: 90
//        source: "../webp/134.webp"
//    }

    function addModelData() {
        if (count >= 20){
            timer.stop()
            return
        }
        count += 1
        listModel.append({type: "time"})
        scrollToEnd()
    }

    function scrollToEnd() {
        listView.positionViewAtIndex(listView.count-1, ListView.Beginning)
    }

    Timer {
        id: timer
        interval: 300
        running: true
        repeat: true
        onTriggered: addModelData()
    }

    ListModel {
        id: listModel
        ListElement{
            type: "time"
        }
    }

    Component {
        id: listDelegate
        Row {
//            AnimatedImage {
//                width: 40
//                height: 50
//                source: "../webp/like.webp"
//            }
            Text {
                height: 30
                color: "#ffffff"
                font.family: "Microsoft YaHei"
                font.pixelSize: 18
                text: "大静静🌹宠爱娱乐厅11860晚上7.30拍卖会"
            }
        }
    }

    ListView {
        id: listView
        anchors.fill: parent
        orientation: ListView.Vertical
        model: listModel
        delegate: listDelegate
    }
}
