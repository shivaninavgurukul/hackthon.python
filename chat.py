from tkinter import*
# " from tkinter import*:- it already imports all the module which we need for tkinter library"
# "tkinter is library of python"
# from turtle import width
root=Tk()
# "it manage all the complecatents and programmer of tkinter application"
def send():
    send=" "+e.get()
    txt.insert(END,"\n"+send)
    # "END is constant and literal"
    if(e.get()=="Hello"):
    # "get:- get the output or to write text"
        txt.insert(END,"\n"+"\t"*9+"Hi")
    elif(e.get()=="hi"):
        txt.insert(END,"\n"+"\t"*9+"Hello") 
    elif(e.get()=="How are you"):
        txt.insert(END,"\n"+"\t"*8+"Find and you")
    elif(e.get()=="fine"):
        txt.insert(END,"\n"+"\t"*8+"Nice to hear") 
    else:
        txt.insert(END,"\n"+"\t"*7+"Sorry i didnt get it") 
    e.delete(0,END)
    # "delete:- message delete karne ke liye ke use kiya jata h" 
txt=Text(root)
txt.grid(row=0,column=0)

e=Entry(root,width=200,bg='pink',fg='dark blue')
# "Entry:- it works as a form of user input"
# "GUI:- "graphical user interface":- it is allow dublicate application to communicate with computer . 
# "widgests:- it is gui ,which allows us to take user input"
send=Button(root,text="Send",command=send).grid(row=1,column=2)
# "Buttom :- are is a keyword"
# "command:- buttom functionality"
# "grid :- it gives us to geomatrically structure row and column ke liye"
e.grid(row=1,column=0)
root.title("CHAT BOT")
# root['bg']='pink'
root.mainloop()
# "mainloop:- without mainloop use your code is not working"


