from tkinter import *
from tkinter import messagebox
import pymysql


root = Tk()
root.geometry("1500x1500")
# root.configure(bg="silver")
root.title("gui using python")
f2 = Frame(root, width=600, height=600, relief=GROOVE,borderwidth=5)
f2.pack(side=LEFT)

def delete(id):
    x= messagebox.askquestion("Wait",'Delete User?')
    if x=='yes':
        con= pymysql.connect(host="localhost",user="root",passwd="",db="gui")
        mycursor= con.cursor()
        msg= "DELETE FROM users WHERE id = {}"
        query=msg.format(id)
        mycursor.execute(query)
        con.commit()
    messagebox.showinfo("success", "user deleted successfully")


global editor
def edit(id):
    editor = Tk()
    editor.geometry("1500x1000")
    editor.title("Update Users")
    # connect to database
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        db = "gui"
    )
    # create a cursor
    mycursor = conn.cursor()
    # write a query
    query = "SELECT * FROM users WHERE id={}"
    text = query.format(id)
    mycursor.execute(text)
    users = mycursor.fetchall()
    print(users)

    def save():
        connect = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="gui"
        )
        my_cursor = connect.cursor()
        query = "UPDATE users SET Fullname=%s, Email=%s, Password=%s, Gender=%s, About=%s WHERE id=%s"
        Fullname = lab_1.get()
        Email = lab_2.get()
        Password = lab_3.get()
        Gender = lab_4.get()
        About = lab_5.get("1.0", END)
        Id = lab_0.get()

        input=(Fullname, Email, Password, Gender, About, Id)
        my_cursor.execute(query, input)
        connect.commit()
        editor.destroy()

    lab = Label(editor, text="UPDATE USER", font=('sans-serif', 20), fg='red')
    lab.place(x=100, y=20)


    lab_0 = Entry(editor)
    lab_0.place(x=250, y=80)
    lab_0.insert(0,users[0][0])
    # entry 1
    
    lab_1 = Entry(editor)
    lab_1.place(x=250, y=130)
    lab_1.insert(0,users[0][1])
    # entry 2
    lab_2 = Entry(editor)
    lab_2.place(x=250, y=180)
    lab_2.insert(0,users[0][2])
    # entry 3
    lab_3 = Entry(editor, show="*")
    lab_3.place(x=250, y=230)
    lab_3.insert(0,users[0][3])
    # entry 4
    lab_4 = Entry(editor)
    lab_4.place(x=250, y=280)
    lab_4.insert(0,users[0][4])
    # text 6
    lab_5 = Text(editor,width=40, height=10)
    lab_5.place(x=250, y=330)
    lab_5.insert("end",users[0][5])

    label_0 = Label(editor, text="Id:", width=20, font=("bold",10))
    label_0.place(x=80, y=80)

    label_1 = Label(editor, text="FullName:", width=20, font=("bold",10))
    label_1.place(x=80, y=130)

    label_2 = Label(editor, text="Email:",width=20, font=("bold",10))
    label_2.place(x=68, y=180)

    label_3 = Label(editor, text="Password:", width=20, font=("bold",10))
    label_3.place(x=70, y=230)

    label_4 = Label(editor, text="Gender:", width=20, font=("bold",10))
    label_4.place(x=73, y=280)

    label_6 = Label(editor, text="About", font=("bold",10))
    label_6.place(x=120, y=330)

    save = Button(editor, text="Save", padx=10, pady=5, command=save, bg="blue", fg="white")
    save.place(x=200, y=550)

        # for widget in f2.winfo_children():
        #         widget.destroy()
def list_users():
    list_users = Tk()
    list_users.geometry("1000x1000")
    list_users.title("users")
    # connect to database
    connect = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="gui" 
    ) 
    # create a cursor
    my_cursor = connect.cursor()
    # create query
    query = "SELECT * FROM users"
    # execute query
    my_cursor.execute(query)
    # fetch data from the database
    users = my_cursor.fetchall()
    # create the heading
    Id = Label(list_users, text="Id", width=0, font=("bold", 10)).grid(row=0, column=0)
    Fullname = Label(list_users, text="Fullname", width=20, font=("bold", 10)).grid(row=0, column=1)
    Email = Label(list_users, text="Email", width=20, font=("bold", 10)).grid(row=0, column=2)
    Password = Label(list_users, text="Password", width=20, font=("bold", 10)).grid(row=0, column=3)
    Gender = Label(list_users, text="Gender", width=15, font=("bold", 10)).grid(row=0, column=4)
    About = Label(list_users, text="About", width=20, font=("bold", 10)).grid(row=0, column=5)
    Edit = Label(list_users, text="Edit", width=10, font=("bold", 10)).grid(row=0, column=6)
    Delete =Label(list_users, text="Delete", width=10, font=("bold", 10)).grid(row=0, column=7)

    row_count = 1
    column_count = 0

    for i in users:
        Id = Label(list_users, text=i[0], width=0, font=("bold", 10)).grid(row=row_count, column=column_count)
        Fullname = Label(list_users, text=i[1], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 1)
        Email = Label(list_users, text=i[2], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 2)
        Password = Label(list_users, text=i[3], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 3)
        Gender = Label(list_users, text=i[4], width=15, font=("bold", 10)).grid(row=row_count, column=column_count + 4)
        About = Label(list_users, text=i[5], width=20, font=("bold", 10)).grid(row=row_count, column=column_count + 5)
        Edit = Button(list_users, text="edit", width=10, font=("bold", 10), command=lambda id=i[0]: edit(id)).grid(row=row_count, column=column_count + 6)
        Delete = Button(list_users, text="delete", width=10, font=("bold", 10), command=lambda id=i[0]: delete(id)).grid(row=row_count, column=column_count + 7)

        row_count += 1
        connect.commit()

def register():
    x= messagebox.askquestion("Wait",'Create My Account?')
    if x == "yes":
        FullName= ent.get()
        Email= ent_1.get()
        Password= ent_2.get()
        Conf_password = ent_3.get()
        Gender= ent_4.get()
        About =ent_5.get("1.0", END)
       
        if FullName=="":
            messagebox.showerror("error","enter full name")
        elif Email=="":
            messagebox.showerror("error","enter email")
        elif Password=="":
            messagebox.showerror("error","enter password")
        elif len(Password) < 6 or len(Password)>12:
            messagebox.showerror("error","password should be between 6-12")
        elif Conf_password != Password:
            messagebox.showerror('error', 'password do not match')
        elif Gender=="":
            messagebox.showerror("error","enter gender")
        elif About=="":
            messagebox.showerror("error","enter about")
        else:    
        # connect to mysql
            connect = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="gui"
            )
            # create a cursor
            mycursor = connect.cursor()

            # create a query
            text = "INSERT INTO users VALUES('','{}','{}','{}','{}','{}')"
            query = text.format(FullName,Email,Password,Gender,About)

            # execute a query
            mycursor.execute(query)

            connect.commit()
            ent.delete(0, END)
            ent_1.delete(0,END)
            ent_2.delete(0, END)
            ent_3.delete(0, END)
            ent_4.delete(0, END)
            ent_5.delete('1.0', 'end')
            messagebox.showinfo('success', 'registration successful')


lab = Label(f2, text="REGISTRATION FORM", font=('sans-serif', 20), fg='red')
lab.place(x=100, y=20)


lab_1 = Label(f2, text='FULLNAME :',font=('sans-serif', 12))
lab_1.place(x=40, y=80)

ent=Entry(f2,width=50)
ent.place(x=240,y=80)

lab_1 = Label(f2, text='EMAIL :',font=('sans-serif', 12))
lab_1.place(x=40, y=120)

ent_1=Entry(f2,width=50)
ent_1.place(x=240,y=120)

lab_1 = Label(f2, text='PASSWORD :',font=('sans-serif', 12))
lab_1.place(x=40, y=160)

ent_2=Entry(f2,width=50,show='*')
ent_2.place(x=240,y=160)

lab_1 = Label(f2, text='CONFIRM PASSWORD :',font=('sans-serif', 12))
lab_1.place(x=40, y=200)

ent_3=Entry(f2,width=50,show='*')
ent_3.place(x=240,y=200)

lab_1 = Label(f2, text='GENDER :',font=('sans-serif', 12))
lab_1.place(x=40, y=240)

ent_4=Entry(f2,width=50)
ent_4.place(x=240,y=240)

lab_1 = Label(f2, text='ABOUT :',font=('sans-serif', 12))
lab_1.place(x=40, y=280)

ent_5=Text(f2,width=37, height=15)
ent_5.place(x=240,y=280)

reg=Button(f2,text='REGISTER',bg='blue',fg='white',padx=5,pady=3, command=register)
reg.place(x=150,y=550)

reg=Button(f2,text='LIST USERS',bg='blue',fg='white',padx=5,pady=3, command=list_users)
reg.place(x=250,y=550)

root.mainloop()


