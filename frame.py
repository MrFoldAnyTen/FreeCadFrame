from PySide import QtCore, QtGui

import FreeCADGui

class MyTaskPanel(QtGui.QWidget):
    def __init__(self):
        super(MyTaskPanel, self).__init__()
        self.myspinbox = QtGui.QDoubleSpinBox(self)
        self.setLayout(QtGui.QGridLayout().addWidget(self.myspinbox, 1, 0))


mw = FreeCADGui.getMainWindow()
awidget = QtGui.QDockWidget("MyTaskPanel", mw)
awidget.setWidget(MyTaskPanel())
mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, awidget)



reply = QtGui.QInputDialog.getText(None, "Frame Size","Enter size W,H,T:", text="1000,2000,95")[0]
myTuple = tuple(reply.split(','))

frameWidth = float(myTuple[0])
frameHeight = float(myTuple[1])
frameThick = float(myTuple[2])

cillThick = 45
cillProject = 50


print("frameWidth = ", frameWidth)
print("frameHeight = ", frameHeight)
print("frameThick = ", frameThick)

App.newDocument("Cill")
partName = App.ActiveDocument.Name
print("partName = ", partName)
App.setActiveDocument(partName)
App.ActiveDocument=App.getDocument(partName)
Gui.ActiveDocument=Gui.getDocument(partName)

App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.ActiveObject.Label = "Cill"

#FreeCAD.getDocument(partName).getObject('Box').Length = width

# >>> from FreeCAD import Base
# >>> import Part,PartGui
App.getDocument(partName).Box.Length= frameWidth
App.getDocument(partName).Box.Width=(frameThick + cillProject)
App.getDocument(partName).Box.Height= cillThick
# >>> App.getDocument("new").Box.Placement=App.Placement(App.Vector(0.00,0.00,0.00),App.Rotation(App.Vector(0.00,0.00,1.00),0.00))
# >>> 
Gui.SendMsgToActiveView("ViewFit")