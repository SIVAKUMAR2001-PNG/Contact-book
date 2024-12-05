from tkinter import*
import pymysql
from tkinter import messagebox
from tkinter import ttk

top=Tk()
top.title("Main page")
top.geometry("800x600")
top.config()
top.resizable(False,False)

#database connection
connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="python_morning"
    )

def initialize_widgets():
    global entry1, entry2, entry3, entry4, entry5, ent1,page2,page3,page4,b1


    page2=Frame(top,bg="blue",height=50,width=800)
    page2.grid(row=0,column=0,padx=0,pady=1)

    page3=Frame(top,bg="white",height=250,width=800)
    page3.grid(row=1,column=0,padx=0,pady=1)

    page4=Frame(top,bg="white",height=400,width=800)
    page4.grid(row=2,column=0,padx=0,pady=1)

    lab1_up=Label(page2,text="CONTACT BOOK",
               font=('Graphique Pro',20,"bold"),fg="white",bg="blue")
    lab1_up.place(x=5,y=5)

    lab1_up=Label(page3,text="Enter First Name",
               font=('Graphique Pro',10,"bold"),fg="black",bg="white")
    lab1_up.place(x=20,y=20)

    entry1 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    entry1.place(x=170,y=20)

    lab1_up=Label(page3,text="Enter last Name",
               font=('Graphique Pro',10,"bold"),fg="black",bg="white")
    lab1_up.place(x=20,y=60)

    entry2 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    entry2.place(x=170,y=60)

    lab1_up=Label(page3,text="Enter Phone Number",
               font=('Graphique Pro',10,"bold"),fg="black",bg="white")
    lab1_up.place(x=20,y=100)

    entry3 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    entry3.place(x=170,y=100)

    lab1_up=Label(page3,text="Enter Email",
               font=('Graphique Pro',10,"bold"),fg="black",bg="white")
    lab1_up.place(x=20,y=140)

    entry4 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    entry4.place(x=170,y=140)

    lab1_up=Label(page3,text="Enter Address",
               font=('Graphique Pro',10,"bold"),fg="black",bg="white")
    lab1_up.place(x=20,y=180)

    entry5 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    entry5.place(x=170,y=180)

    

    b1 = Button(page3,text='search',command=search,bg="blue",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b1.place(x=450, y=20)

    ent1 = Entry(page3, font=('Century Gothic', 10),relief="solid")
    ent1.place(x=600,y=24)
    
    b2 = Button(page3,text='cancel',command=next,bg="blue",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b2.place(x=430, y=220)


    b3 = Button(page3,text='save',command= save,bg="blue",fg="white",
            font=("Consolas", 13, "bold"),height="1",width="13",bd=0)
    b3.place(x=300, y=220)
    

def save():

    a=entry1.get()
    b=entry2.get()
    c=entry3.get()
    d=entry4.get()
    e=entry5.get()
    if(entry1.get()=="" or entry2.get()=="" or entry3.get()=="" or entry4.get()=="" or entry5.get()==""):
        messagebox.showerror("Error","Enter all the details")
    else:
        cursor=connection.cursor()
        query = "INSERT INTO contact_book (f_name,l_name,p_number,email,address) VALUES (%s,%s,%s,%s,%s)"
        values = (a,b,c,d,e)
        cursor.execute(query,values)
        connection.commit()
    
    # Closing the cursor and connection
        cursor.close()
        messagebox.showinfo("Info","Successfully Saved..!")
        nex()

def nex():
    global page2, page3, page4

    page2.destroy()
    page3.destroy()
    page4.destroy()

    initialize_widgets()

def next():
     global page2,page3,page4
     
     messagebox.showinfo("Info","Successfully Canceled..!")
     page2.destroy()
     page3.destroy()
     page4.destroy()
    
     initialize_widgets()
     

def show(result):
    # Clear previous results
    for widget in page4.winfo_children():
        widget.destroy()

    if result:
        # Add column headers
        headers = ["First Name", "Last Name", "Phone Number", "Email", "Address"]
        for col, header in enumerate(headers):
            lbl_header = Label(page4, text=header, font=('Graphique Pro', 10, "bold"), fg="white", bg="blue")
            lbl_header.grid(row=0, column=col, padx=5, pady=5, sticky='w')

        # Display the results
        for idx, columns in enumerate(result, start=1):
            for col, value in enumerate(columns):
                lbl_result = Label(page4, text=value, font=('Century Gothic', 10, "bold"), fg="black", bg="white")
                lbl_result.grid(row=idx, column=col, padx=5, pady=5, sticky='w')

    else:
        lbl = Label(page4, text="No Results Found", font=('Graphique Pro', 10, "bold"), fg="black", bg="white")
        lbl.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

def search():
    query = ent1.get()
    if not query:
        messagebox.showerror("Error", "Enter a search query")
        return

    cursor = connection.cursor()
    sql = "SELECT f_name, l_name, p_number, email, address FROM contact_book WHERE f_name LIKE %s OR l_name LIKE %s"
    cursor.execute(sql, (f"%{query}%", f"%{query}%"))
    result = cursor.fetchall()
    show(result)
    cursor.close()

# Initialize the widgets
initialize_widgets()

# Start the main event loop
top.mainloop()



















