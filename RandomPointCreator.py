"""
/***************************************************************************
Name			 	 : generowanie punktow
Description          : Generuje losowe punkty na mapie
Date                 : 10/Sep/11 
copyright            : (C) 2011 by Malgorzata Baron
email                : ggosia6@mat.umk.pl 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from RandomPointCreatorDialog import RandomPointCreatorDialog

class RandomPointCreator: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/plugins/RandomPointCreator/icon.png"), \
        "Random Point Creator", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&Random Point Creator", self.action)

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&Random Point Creator",self.action)
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self): 
    # create and show the dialog 
    dlg = RandomPointCreatorDialog() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    if result == 1: 
      # do something useful (delete the line containing pass and
      # substitute with your code
      pass 
