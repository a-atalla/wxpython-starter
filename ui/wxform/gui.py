# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class LoginDialog
###########################################################################

class LoginDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"User Login", pos = wx.DefaultPosition, size = wx.Size( 350,250 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"icons/lock.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer3.Add( self.m_textCtrl2, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PnlHome
###########################################################################

class PnlHome ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 635,352 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer71.Add( self.m_staticText3, 1, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_textCtrl3, 1, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer71.Add( self.m_staticText7, 1, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_textCtrl7, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer71, 0, wx.EXPAND, 0 )
		
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer711.Add( self.m_staticText31, 1, wx.ALL, 5 )
		
		self.m_textCtrl31 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_textCtrl31, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer711, 0, wx.EXPAND, 0 )
		
		bSizer712 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer712.Add( self.m_staticText32, 1, wx.ALL, 5 )
		
		self.m_textCtrl32 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer712.Add( self.m_textCtrl32, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer712, 0, wx.EXPAND, 0 )
		
		bSizer7111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText311 = wx.StaticText( self, wx.ID_ANY, u"Confirm Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		bSizer7111.Add( self.m_staticText311, 1, wx.ALL, 5 )
		
		self.m_textCtrl311 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer7111.Add( self.m_textCtrl311, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7111, 1, wx.EXPAND, 5 )
		
		bSizer713 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button4 = wx.Button( self, wx.ID_SAVE, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer713.Add( self.m_button4, 1, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer713.Add( self.m_button5, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer713, 0, wx.EXPAND, 0 )
		
		
		bSizer7.Add( bSizer6, 0, 0, 0 )
		
		self.users_view = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.users_view, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Smart Rig", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu4 = wx.Menu()
		self.m_menu1 = wx.Menu()
		self.m_menu4.AppendSubMenu( self.m_menu1, u"MyMenu" )
		
		self.m_menubar2.Append( self.m_menu4, u"MyMenu" ) 
		
		self.m_menu7 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.AppendItem( self.m_menuItem1 )
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.AppendItem( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu7, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu7.AppendItem( self.m_menuItem3 )
		
		self.m_menubar2.Append( self.m_menu7, u"MyMenu" ) 
		
		self.m_menu6 = wx.Menu()
		self.m_menubar2.Append( self.m_menu6, u"MyMenu" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

