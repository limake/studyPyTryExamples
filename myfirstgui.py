#-------------------------------------------------------------------------------
# Name:        myfirstgui
# Purpose:
#
# Author:      Administrator
#
# Created:     30/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import*
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit',command=self.quit)
        self.quitButton.pack()

app=Application()
app.master.title('Hello World')
app.mainloop()