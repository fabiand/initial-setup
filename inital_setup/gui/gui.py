from pyanaconda.ui.gui import QuitDialog, GUIObject, GraphicalUserInterface
#from .product import productName, productVersion
from .hubs import FirstbootHub
from pyanaconda.ui.gui.spokes import StandaloneSpoke
import pyanaconda.ui.gui.spokes
from pyanaconda.ui.common import collect, FirstbootSpokeMixIn
import os.path

productName = "Fedora"
productVersion = "rawhide"
isFinal = False

class FirstbootQuitDialog(QuitDialog):
    MESSAGE = "Are you sure you want to quit the configuration process?\nYou might end up with unusable system if you do."

class FirstbootGraphicalUserInterface(GraphicalUserInterface):
    """This is the main Gtk based firstboot interface. It inherits from
       anaconda to make the look & feel as similar as possible.
    """

    TITLE = "%(productName)s %(productVersion)s SETUP"
    
    def __init__(self, storage, payload, instclass):
        GraphicalUserInterface.__init__(self, storage, payload, instclass,
                                        productName, productVersion, isFinal,
                                        quitDialog = FirstbootQuitDialog)
    
    def _list_hubs(self):
        return [FirstbootHub]

    basemask = "firstboot.gui"
    basepath = os.path.dirname(__file__)
    paths = GraphicalUserInterface.paths + {
        "spokes": [(basemask + ".spokes.%s", os.path.join(basepath, "spokes"))],
        "categories": [(basemask + ".categories.%s", os.path.join(basepath, "categories"))],
        }
