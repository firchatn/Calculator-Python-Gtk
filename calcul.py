import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def addun(self, un):
        print("Hello World!")
        incal.set_buffer("1")
    def adddeux(self, deux):
        print("Hello World22!")
    def addtrois(self, un):
        print("Hello World!")
    def addquatre(self, un):
        print("Hello World!")
    def addciq(self, un):
        print("Hello World!")
    def addsix(self, un):
        print("Hello World!")
    def addsept(self, un):
        print("Hello World!")
    def addhuit(self, un):
        print("Hello World!")
    def addneuf(self, un):
        print("Hello World!")
        
    def onplus(self, un):
        print("Hello World!")
    def onmoin(self, un):
        print("Hello World!")
    def onfois(self, un):
        print("Hello World!")
    def onsur(self, un):
        print("Hello World!")
        
    def oncal(self, un):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("layout-calculator.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
