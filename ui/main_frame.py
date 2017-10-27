from ui.wxform.gui import FrmMain

class MainFrame(FrmMain):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)
        self.Show()
        self.Maximize()
