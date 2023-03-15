from tkinter import *
from funkcijas import *
from tkinter import messagebox

root = Tk()
root.title("Astoņbumba")
root.geometry("350x350")
root.config(bg='#D1D1D1')

def loginScreen():           #Login logs
    for widgets in root.winfo_children():
        widgets.destroy()
    nameEntry = Entry(root)
    password = Label(root, text="Password")
    passField = Entry(root)
    login = Button(root, text="Ienākt", command=lambda: loginCheck(nameEntry, passField))
    name = Label(root, text="Vārds")
    back5 = Button(root, text="Atpakaļ", command=lambda: startup())

    back5.grid(row=4, column=0, pady=10)
    name.grid(row=0, column=0, padx=(80, 10), pady=(100, 10))
    nameEntry.grid(row=0, column=1, pady=(100, 10))
    password.grid(row=1, column=0, padx=(80, 10), pady=10)
    passField.grid(row=1, column=1)
    login.grid(row=2, column=0, columnspan=2, padx=(80, 10), pady=10)

def signUpScreen():                 #Reģistrācijas logs
    for widgets in root.winfo_children():
        widgets.destroy()
    name = Label(root, text="Vārds")
    nameEntry = Entry(root)
    surname = Label(root, text="Uzvārds")
    surnameEntry = Entry(root)
    username = Label(root, text="Lietotājvārds")
    usernameEntry = Entry(root)
    email = Label(root, text="Epasts")
    emailEntry = Entry(root)
    password = Label(root, text="Password")
    passField = Entry(root)
    register = Button(root, text="Reģistrējies", command=lambda: registerCheck(nameEntry, surnameEntry, usernameEntry, emailEntry, passField))
    back4 = Button(root, text="Atpakaļ", command=lambda: startup())

    back4.grid(row=7, column=0, pady=10)
    name.grid(row=0, column=0, padx=(80, 10), pady=(50, 10))
    nameEntry.grid(row=0, column=1, pady=(50, 10))
    surname.grid(row=1, column=0, padx=(80, 10), pady=10)
    surnameEntry.grid(row=1, column=1)
    username.grid(row=2, column=0, padx=(80, 10), pady=10)
    usernameEntry.grid(row=2, column=1)
    email.grid(row=3, column=0, padx=(80, 10), pady=10)
    emailEntry.grid(row=3, column=1)
    password.grid(row=4, column=0, padx=(80, 10), pady=10)
    passField.grid(row=4, column=1)
    register.grid(row=5, column=0, columnspan=2, padx=(80, 10), pady=10)



def userSpace(userID):
    for widgets in root.winfo_children():
        widgets.destroy()
    history = Button(root, text="Apskati vēsturi", command=lambda : historyWindow(userID))
    askQuestion = Button(root, text="Uzdod jautājumu", command= lambda : questionsWindow(userID))
    logout = Button(root, text="Izrakstīties", command=lambda : startup())

    history.grid(row=0, column=0, padx=(120, 10), pady=(100, 10))
    askQuestion.grid(row=1, column=0, padx=(120, 10), pady=10)
    logout.grid(row=2, column=0,padx=(120, 10), pady=10)



def historyWindow(userID):                      #Pārbauda vēsturi
    for widgets in root.winfo_children():
        widgets.destroy()
    history_questions = checkHistory(userID)

    if history_questions != "Empty":
        num = 0
        for i in history_questions:
            x = Label(root, text=i[0]+ i[1])
            x.grid(row=num, column=0)
            num+=1
        back2 = Button(root, text="Atpakaļ", command=lambda: userSpace(userID))
        back2.grid(row=num, column=0, pady=10)
    else:
        back3 = Button(root, text="Atpakaļ", command=lambda: userSpace(userID))
        back3.grid(row=0, column=0, pady=10)
        messagebox.showinfo("Nohistory", "Nohistory")


def askedQuestion(question, userID, ans):          #Izdod atbildi
    q = question.get()
    if len(q) != 0:
        question.delete(0, END)
        answer = answers()
        ans.config(text=answer)
        addToHistory(q, answer, userID)


def questionsWindow(userID):                   #Jautājumu logs
    for widgets in root.winfo_children():
        widgets.destroy()
    questionLabel = Label(root, text="Uzdod savu jautājumu: ")
    questionsEntry = Entry(root)
    answerLabel = Label(root, text="")
    askBtn = Button(root, text="Jautāt!", command= lambda :askedQuestion(questionsEntry, userID, answerLabel))
    back1 = Button(root, text="Atpakaļ", command=lambda:userSpace())

    questionLabel.grid(row=0, column=0, padx=(50, 10), pady=10)
    questionsEntry.grid(row=0, column=1)
    answerLabel.grid(row=1,column=0, columnspan=2, padx=(50, 10), pady=10)
    askBtn.grid(row=2,column=0, columnspan=2, padx=(50, 10), pady=10)
    back1.grid(row=3, column=0)


def loginCheck(vards, parole):          #Pārbauda vai ir pareizi ierakstits lietotājvāŗds
    x = vards.get()
    y = parole.get()
    sucess = loginIntoAccount(x, y)
    vards.delete(0,END)
    parole.delete(0,END)

    if sucess:
        userSpace(sucess.rstrip())


def registerCheck(vards, uzvards, username, email, password):                      #pārbauda vai tāds lietotājs eksistē
    userID = createAccount(vards.get(), uzvards.get(), username.get(), email.get(), password.get())
    x = [vards, uzvards, username, email, password]
    for i in x:
        i.delete(0, END)
    if userID != -1:
        userSpace(userID.rstrip())
    else:
        messagebox.showinfo("Lietotājvārds", "Lietotājvārds jau eksistē")


def startup():
    for widgets in root.winfo_children():
        widgets.destroy()
    pieslegties = Button(root, text="Pieslēdzies", command=loginScreen)
    registreties = Button(root, text="Reģistrējies", command=signUpScreen)
    pieslegties.grid(row=0, column=0, padx=125, pady=50)
    registreties.grid(row=1, column=0, padx=125, pady=50)

startup()
root.mainloop()