# coding=utf-8

import wx

class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(None,title='the first wxpython procedure',size=(400,300),pos=(100,100))

app=wx.App()

frm=MyFrame

frm.Show()

app.MainLoop()