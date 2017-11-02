import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk




class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def addun(self, un):
        print("1")
        changeBuff(v='1')
        
    def adddeux(self, deux):
        print("2")
        changeBuff(v='2')
        
    def addtrois(self, trois):
        print("3")
        changeBuff(v='3')
        
    def addquatre(self, quatre):
        print("4")
        changeBuff(v='4')
        
    def addcinq(self, cinq):
        print("5")
        changeBuff(v='5')
        
    def addsix(self, six):
        print("6")
        changeBuff(v='6')
    
    def addsept(self, sept):
        print("7")
        changeBuff(v='7')
        
    def addhuit(self, huit):
        print("8")
        changeBuff(v='8')
        
    def addneuf(self, neuf):
        print("9")
        changeBuff(v='9')

        
    def onplus(self, plus):
        print("+")
        changeBuff(v='+')
        
    def onmoin(self, moin):
        print("-")
        changeBuff(v='-')
        
    def onfois(self, fois):
        print("*")
        changeBuff(v='*')
        
    def onsur(self, sur):
        print("/")
        changeBuff(v='/')
        
    def oncal(self, out):
        print("result")
        textv2 = builder.get_object("out")
        textv1 = builder.get_object("incal")
        textbuffer = textv1.get_buffer()
        textbuffer2 = textv2.get_buffer()
        start_iter = textbuffer.get_start_iter()
        end_iter = textbuffer.get_end_iter()
        text = textbuffer.get_text(start_iter, end_iter, True)
        res = eval(text)
        textbuffer2.set_text('=' + str(res))
    def onclean(self, clear):
        print("clean")
        textv2 = builder.get_object("out")
        textv1 = builder.get_object("incal")
        textbuffer = textv1.get_buffer()
        textbuffer2 = textv2.get_buffer()
        textbuffer2.set_text('')
        textbuffer.set_text('')
        
    
def changeBuff(v):
    textv1 = builder.get_object("incal")
    textbuffer = textv1.get_buffer()
    start_iter = textbuffer.get_start_iter()
    end_iter = textbuffer.get_end_iter()
    text = textbuffer.get_text(start_iter, end_iter, True)
    textbuffer.set_text(text + v)

builder = Gtk.Builder()
builder.add_from_file("layout-calculator.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()
window.connect("delete-event", Gtk.main_quit)

Gtk.main()
