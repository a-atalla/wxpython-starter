import wx
from ui.list_book import MainBook
from ui.main_frame import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None)
    notebook = MainBook(frame)
    app.MainLoop()
