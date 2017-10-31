import wx
from .home_page import HomePage


class MainBook(wx.Toolbook):
    def __init__(self, parent):
        super(MainBook, self).__init__(parent, -1, style=wx.BK_DEFAULT)
        home_page = HomePage(self)

        img1 = wx.Image('ui/icons/home.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        img2 = wx.Image('ui/icons/db.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        img3 = wx.Image('ui/icons/chart.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()

        imgs_list = wx.ImageList()
        imgs_list.Add(img1)
        imgs_list.Add(img2)
        imgs_list.Add(img3)

        self.AssignImageList(imgs_list)

        self.AddPage(home_page, 'Home', imageId=0)
        self.AddPage(home_page, 'Data', imageId=1)
        self.AddPage(home_page, 'Reports', imageId=2)
        self.AddPage(home_page, 'Home', imageId=0)
        self.AddPage(home_page, 'Data', imageId=1)
        self.AddPage(home_page, 'Reports', imageId=2)
        self.AddPage(home_page, 'Home', imageId=0)
        self.AddPage(home_page, 'Data', imageId=1)
        self.AddPage(home_page, 'Reports', imageId=2)


        self.Bind(wx.EVT_TOOLBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print("onChanging old:{}  new:{}  sel:{}".format(old, new, sel))
        event.Skip()