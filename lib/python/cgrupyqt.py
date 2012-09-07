QtCore = None
QtGui = 'QtGui'
QtNetwork = 'QtNetwork'
List = ['QtCore', 'QtGui', 'QtNetwork']
PythonQtType = None
PySide = True

try:
	PythonQt = __import__('PySide', globals(), locals(), List, -1)
	PythonQtType = 'PySide'
except:
	PythonQt = __import__('PyQt4', globals(), locals(), List, -1)
	PythonQtType = 'PyQt4'

QtCore = PythonQt.QtCore
QtGui = PythonQt.QtGui
QtNetwork = PythonQt.QtNetwork

print( PythonQtType + ' module imported.')
if PythonQtType == 'PyQt4':
	print('You can install PySide if interested in LGPL license.')
	PySide = False

def GetOpenFileName( i_qwidget, i_title, i_path):
	if PySide:
		afile, filter = QtGui.QFileDialog.getOpenFileName( i_qwidget, i_title, i_path)
		return afile
	return str( QtGui.QFileDialog.getOpenFileName( i_qwidget, i_title, i_path))

def GetSaveFileName( i_qwdget, i_title, i_path):
	if Pyside:
		afile, filter = QtGui.QFileDialog.getSaveFileName( i_qwdget, i_title, i_path)
		return afile
	return = str( QtGui.QFileDialog.getSaveFileName( i_qwdget, i_title, i_path)

def GetExistingDirectory( i_qwidget, i_title, i_path):
	if PySide:
		folder, filter = QtGui.QFileDialog.getExistingDirectory( i_qwidget, i_title, i_path)
		return folder
	return str( QtGui.QFileDialog.getExistingDirectory( i_qwidget, i_title, i_path))