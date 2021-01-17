from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk 
from tkinter.ttk import Treeview 
from tkinter import messagebox
import os
import json

root = Tk()
root.configure(background='black')
root.geometry("1350x690+0+0")
header = Frame(root)
header.pack(fill=BOTH,pady=50)
header.configure(background='black',height=50)
main = Frame(root)
main.pack()
bottom = Frame(root)
bottom.pack(side = "bottom", fill=BOTH )
bottom.configure(background='black')
# --------------------------------defined Function---------------------------------
rollnos=[]
def save_record():
    global rollnos
    if os.path.isfile("student.json"):
        with open ("student.json","r") as f:
            student = json.load(f)
            stu_list = student['Students']
            for i in stu_list:
                rollnos.append('rollno')
    stu = {}
    stu1 = {}
    stu['Students'] = list()
    name = e1.get()
    rollno = e2.get()
    if rollno not in rollnos:
        address = e3.get()
        gender = v.get()
        phone = e4.get()
        batch = e5.get()
        hostel = True if Hostel == 1 else False
        stu1['Name'] = name
        stu1['Rollno'] = rollno
        stu1['address'] = address
        stu1['Gender'] = gender
        stu1['Phone'] = phone
        stu1['Batch'] = batch
        stu1['Hostel'] = hostel
        
        if os.path.isfile("student.json"):
            with open ("student.json","r") as f:
                stu = json.load(f)
                stu['Students'].append(stu1)
            with open ("student.json","w") as f:
                json.dump(stu,f)
                
        else:
            with open ("studen.json","w") as f:
                stu['Students'].append(stu1)
                json.dump(stu,f)
        messagebox.showinfo("Save","Your record has been saved")
    
    else:
        messagebox.showinfo("Error","Your roll no already exists")
          # clear funtion
def clear():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        checkbox1.deselect()

# function
def show_stundents():
    treev.delete(*treev.get_children())
    if os.path.isfile('student.json'):
        with open ('student.json') as f:
            stu = json.load(f)
        for i in stu ['Students']:
            treev.insert("",index=0,values=(i['Rollno'],i['Name'],i['Gender'],i['address'],i["Phone"],i['Batch'],i['Hostel']))
    else:
        messagebox.showinfo("Error","File doesn't exists")







           # function for course creation
c_id_list =[]
def save_course():
    global c_id_list
    if os.path.isfile("Courses.json"):
        with open ("Courses.json","r") as f:
            student = json.load(f)
            stu_list = student['Courses']
            for i in stu_list:
                c_id_list.append('CourseID')
    stu = {}
    stu1 = {}
    stu['CourseID'] = list()
    cid = c_id.get()
    Coursename = c_name.get()
    if cid not in c_id_list:

        stu1['CourseID'] = cid
        stu1['CourseName'] = Coursename
        
        if os.path.isfile("course.json"):
            with open ("course.json","r") as f:
                stu = json.load(f)
                stu['Courses'].append(stu1)
            with open ("course.json","w") as f:
                json.dump(stu,f)
                
        else:
            with open ("course.json","w") as f:
                stu['Courses'].append(stu1)
                json.dump(stu,f)
        messagebox.showinfo("Save","Course has been saved")
    
    else:
        messagebox.showinfo("Error","Course already exists")




def show_courses():
    treev2.delete(*treev2.get_children())
    if os.path.isfile('course.json'):
        with open ('course.json') as f:
            stu = json.load(f)
    course_list=[]
    for i in stu ['Courses']:
        treev2.insert("",index=0,values=(i['CourseID'],i['CourseName']))
        course_list.append(i['CourseName'])
    else:
        messagebox.showinfo("Error","File doesn't exists")

# Course allocatio
def return_courseID(cn):
        for i in stu['Courses']:
                if i['CourseName']==cn:
                        return i['CourseID']
def course_allocation():
        f1=strl.get()
        f2=course_name.get()
        f3=return_courseID(f2)
        r={"Rollno": f1, "CourseID": f3}

        with open('Allocation.json') as f:
                data3=json.load(f)
        data3["Stu_Course"].append(r)
        data_serialise=json.dumps(data3, indent=2)
        with open('Allocation.json','w') as f:
                json.dump(data3,f,indent=1)
        messagebox.showinfo("Saved","Course Allocated")


#header of the application
Label(root,text ="CHITKARA UNIVERSITY",font = ("Times New Roman",22),fg='white',bg='black').place(x=485,y=3)
Label(root,text ="STUDENT DATABASE",font = ("Times New Roman",22),fg='white',bg='black').place(x=505,y=103)
Label(root,text ="EXPLORE",font = ("Times New Roman",22),fg='red',bg='black').place(x=10,y=3)
Label(root,text ="YOUR",font = ("Times New Roman",22),fg='white',bg='black').place(x=10,y=33)
Label(root,text ="POTENTIAL",font = ("Times New Roman",22),fg='red',bg='black').place(x=10,y=63)
img = ImageTk.PhotoImage(Image.open("logo.png"))
panel = Label(root, image = img,bg='black')
panel.place(x=1090,y=3)


#main section
tabControl = ttk.Notebook(main) 

tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='New Student') 
tabControl.add(tab2, text ='Display')
tabControl.add(tab3, text ='Course Creation') 
tabControl.add(tab4, text ='Display Courses') 
tabControl.add(tab5, text ='Cousrse Allocation') 

tabControl.pack(expand = 1, fill ="both") 


ttk.Label(tab1 , text = "Enter Your Name").grid(column = 0, row = 0, columnspan=3,sticky="e",padx=10) 
e1 = ttk.Entry(tab1,width=50)
e1.grid(column = 5, row = 0, pady = 15, columnspan=3,padx=10)

ttk.Label(tab1 , text = "Enter Your Roll No.").grid(column = 0, row = 1, columnspan=3,sticky="e") 
e2 = ttk.Entry(tab1,width=50)
e2.grid(column = 5, row = 1, pady = 15, columnspan=3)

ttk.Label(tab1 , text = "Choose Your Gender").grid(column = 0, row = 2, columnspan=3,sticky="e") 
v = StringVar() 
Radiobutton(tab1, text='male', variable=v, value='Male').grid(column = 5, row = 2 )
Radiobutton(tab1, text='female', variable=v, value='Female').grid(column = 6, row = 2)


ttk.Label(tab1 , text = "Adress for Corrospondence").grid(column = 0, row = 3, columnspan=3,sticky="e",padx=10) 
e3 = ttk.Entry(tab1,width=50)
e3.grid(column = 5, row = 3, pady = 15, columnspan=3 )

ttk.Label(tab1 , text = "Phone No.").grid(column = 0, row = 4, columnspan=3,sticky="e") 
e4 = ttk.Entry(tab1,width=50)
e4.grid(column = 5, row = 4, pady = 15, columnspan=3)

ttk.Label(tab1 , text = "Your Batch").grid(column = 0, row = 5, columnspan=3,sticky="e") 
e5 = ttk.Combobox(tab1,state='readonly',width=47)
e5['values']=['2017','2018','2019','2020']
e5.grid(column = 5, row = 5, pady = 15, columnspan=3)

Hostel = IntVar()
ttk.Label(tab1 , text = "Hostel[Y/N]").grid(column = 0, row = 6, columnspan=3,sticky="e") 
ttk.Checkbutton(tab1, text='Check If You Need Hostel Facility' ,  onvalue=1, offvalue=0,variable="Hostel").grid(column = 5 , row=6, sticky="e")


save_button = ttk.Button(tab1, text='Save', width=25, command=save_record )
save_button.grid(column=3, row = 7,pady=30)

clear_button = ttk.Button(tab1, text='Clear', width=25 , command=clear )
clear_button.grid(column=4, row = 7,pady=30)
#Label(tab1).grid(column = 8)

#tab2
frame1 = Frame(tab2)
frame1.pack()
treev = Treeview(frame1,selectmode='browse')
treev.pack()

treev['columns'] = ('Rollno','Name','Gender','Address','Phone','Batch','Hostel')
treev['show'] = 'headings'
treev.column("Rollno",width=100)
treev.column("Name",width=100)
treev.column("Gender",width=100)
treev.column("Address",width=100)
treev.column("Phone",width=100)
treev.column("Batch",width=100)
treev.column("Hostel",width=100)

treev.heading("Rollno",text='Rollno')
treev.heading("Name",text='Name')
treev.heading("Gender",text='Gender')
treev.heading("Address",text='Address')
treev.heading("Phone",text='PhoneNo')
treev.heading("Batch",text='Batch')
treev.heading("Hostel",text='Hostel')

if os.path.isfile('student.json'):
    with open ('student.json') as f:
        stu = json.load(f)
    for i in stu ['Students']:
        treev.insert("",index=0,values=(i['Rollno'],i['Name'],i['Gender'],i['address'],i["Phone"],i['Batch'],i['Hostel']))
else:
    messagebox.showinfo("Error","File doesn't exists")



frame2 = Frame(tab2)
frame2.pack(fill='both')
Button(frame2,text="Show Students",bg='black',fg='white',command=show_stundents).pack(side='bottom',pady=60)


# tab3
def clickme():
    
    if os.path.isfile("student.json"):
        with open ("student.json","r") as f:
            course = json.load(f)
            course_list = course['Students']
            for i in course_list:
                rollnos.append('rollno')





frame31 = Frame(tab3)
frame31.pack(pady='40')

Label(frame31,text='Course ID').grid(column=0,row=0,padx='70',pady='20',sticky='e')
c_id = Entry(frame31,width=50)
c_id.grid(column=1,row=0)

Label(frame31,text='Course Name').grid(column=0,row=1,padx='70',pady='20',sticky='e')
c_name = Entry(frame31,width=50)
c_name.grid(column = 1 , row=1)

frame32 = Frame(tab3)
frame32.pack()
def clear2():
    c_id.delete(0,END)
    c_name.delete(0,END)

Button(frame32,text='Save',command=save_course,width=30).grid(row =0,column='3')
Button(frame32,text='Clear',command="clear2",width=30).grid(row =0,column='5')

#   tab 4
frame41 = Frame(tab4)
frame41.pack()
treev2 = Treeview(frame41,selectmode='browse')
treev2.pack()

treev2['columns'] = ('CourseID','CourseName')
treev2['show'] = 'headings'
treev2.column("CourseID",width=100)
treev2.column("CourseName",width=300)
treev2.heading("CourseID",text='Course Id')
treev2.heading("CourseName",text='Course Name')









if os.path.isfile('course.json'):
    with open ('course.json') as f:
        stu = json.load(f)
    course_list=[]
    for i in stu ['Courses']:
        treev2.insert("",index=0,values=(i['CourseID'],i['CourseName']))
        course_list.append(i['CourseName'])
else:
    messagebox.showinfo("Error","File doesn't exists")

frame42 = Frame(tab4)
frame42.pack(fill='both')
Button(frame42,text="Display Courses",bg='black',fg='white').pack(side='bottom',pady=60)


#tab 5

frame51 = Frame(tab5)
frame51.pack(pady='40')

Label(frame51,text='Student Rollno').grid(column=0,row=0,padx='70',pady='20',sticky='e')
strl = Entry(frame51,width=50)
strl.grid(column=1,row=0)

Label(frame51,text='Course Name').grid(column=0,row=1,padx='70',pady='20',sticky='e')
course_name = ttk.Combobox(frame51,width=47)
course_name['values'] = course_list
course_name.grid(column = 1 , row=1)

frame52 = Frame(tab5)
frame52.pack()

Button(frame52,text='Allocate Course',command=course_allocation).grid(row =0,column='3')







Label(bottom,text='Department of Computer Science & Engineering',bg='black',fg='white',font = ("Times New Roman",20)).pack(pady='35')




root.mainloop()
