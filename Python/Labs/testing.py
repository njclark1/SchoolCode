import tkinter as tk
from tkinter import ttk,messagebox, Frame, Button, Radiobutton, StringVar,Label, Entry, Tk, IntVar, simpledialog, Canvas
import hashlib
import tkinter.ttk as ttk
#cred enter
#validate cred
#return info
#format info



def main():
    window = Tk()
    #window.state('zoomed') #fullscreen
    work(window)
    window.geometry("600x400") #change window size here
    window.protocol("WM_DELETE_WINDOW", lambda: quit_me(window))
    window.title("PassBase")
    window.mainloop()

def quit_me(window):
    print('quit')
    window.quit()
    window.destroy()

def work(window):
    Mainframe= Frame(window)
    Mainframe.pack(fill="both",expand="True")
    
    #topframeplaceholder
    topframeplaceholder = tk.Frame(Mainframe)
    topframeplaceholder.pack(side="top",fill="both",expand="True")
    #topframe
    topframe = tk.Frame(Mainframe)
    topframe.pack(side="top",fill="both",expand="True")
    #botframe
    botframe = tk.Frame(Mainframe)
    botframe.pack(side="top",fill="both",expand="True")
    #botframeplaceholder
    botframeplaceholder = tk.Frame(Mainframe)
    botframeplaceholder.pack(side="top",fill="both",expand="True")

    # username label
    userLabel = Label(topframe,text="Username").pack(side= "top")
    # username text box
    userEntry= Entry(topframe)
    userEntry.pack(side="top")
    userEntry.tag_add("start", background="black", foreground="yellow")
    # password label
    passLabel = Label(topframe, text = "Password").pack(side = "top")
    # password text box
    passEntry = Entry(topframe)
    passEntry.pack(side = "top")
    
    #botframe container
    b1 = Button(botframe,text="Login",command=lambda:SQL(userEntry.get(),passEntry.get())).pack(side="top")
    b2 = Button(botframe,text="Exit",command=lambda:quit_me(window)).pack(side="top")
    b3 = Button(botframe, text = "New User", command = lambda:newUser(Mainframe)).pack(side = "top")
def newUser(Mainframe):
    wind = Mainframe.winfo_children()#get current widget names then destroy to clear window
    for win in wind:
        win.pack_forget()
    Mainframe.pack_forget()
    newUserFrame = Frame(Mainframe)
    newUserFrame.pack(fill = "both", expand = "True")
#testing testing please dear god work why dear god why
    #top placeholder
    newTopPlaceHolder = tk.Frame(newUserFrame)
    newTopPlaceHolder.pack(side = "top", fill = "both", expand = "True")
    #top frame
    newTopFrame = tk.Frame(newUserFrame)
    newTopFrame.pack(side = "top", fill = "both", expand = "True")
    # bottom frame
    newBotFrame = tk.Frame(newUserFrame)
    newBotFrame.pack(side = "top", fill = "both", expand = "True")

    # new user login labels
    firstNameLabel = Label(newTopFrame, text = "First name").pack(side = "top")
    lastNameLabel = Label(newTopFrame, text = "Last name").pack(side = "top")
    emailLabel = Label(newTopFrame, text = "Email address").pack(side = "top")
    newUsernameLabel = Label(newTopFrame, text = "Username").pack(side = "top")
    newPasswordLabel = Label(newTopFrame, text = "Password").pack(side = "top")

    # new user text box
    firstNameEntry = Entry(newTopFrame)
    firstNameEntry.pack(side = "top")
    lastNameEntry = Entry(newTopFrame)
    lastNameEntry.pack(side = "top")
    emailLabel = Entry(newTopFrame)
    emailLabel.pack(side = "top")
    newUsername = Entry(newTopFrame)
    newUsername.pack(side = "top")
    newPassword = Entry(newTopFrame)
    newPassword.pack(side = "top")

def hashingCompare(realshow,password):
    realshow = str(realshow)
    result = hashlib.sha256(password.encode())
    result2 = hashlib.sha256(realshow.encode())
    print(result,result2)
    if result == result2:
        #yes authenticate
        pass
    else:
        #no auth
        pass
def newUserSQL():
    sterile_execute ="Select master_password from [user] WHERE master_username = '" + username + "';"#code to send to database 
    server = 'hopper.ws.edu' 
    database = 'naburke' 
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    #executing string with cursor
    print(sterile_execute)
    cursor = conn.cursor()
    cursor.execute(sterile_execute)
    conn.commit()#need to commit
    realshow = pandas.read_sql(sterile_execute,conn)
def SQL(username,password):
    sterile_execute ="Select master_password from [user] WHERE master_username = '" + username + "';"#code to send to database 
    server = 'hopper.ws.edu' 
    database = 'naburke' 
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    #executing string with cursor
    print(sterile_execute)
    cursor = conn.cursor()
    cursor.execute(sterile_execute)
    conn.commit()#need to commit
    realshow = pandas.read_sql(sterile_execute,conn)
    hashingCompare(password,realshow)

main()