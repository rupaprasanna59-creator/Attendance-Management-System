import tkinter as tk
root=tk.Tk()
root.geometry("530x530")
def add_student():
    name = e1.get()
    if name != "":
         text_box.insert(tk.END, name)
         e1.delete(0, tk.END)
def mark_present():
    selected = text_box.curselection()

    if selected:
        student = text_box.get(selected[0])
        attendance_box.insert(tk.END, student + " - Present\n")

def mark_absent():
    selected = text_box.curselection()

    if selected:
        student = text_box.get(selected[0])
        attendance_box.insert(tk.END, student + " - Absent\n")
def save_attendance():
    data = attendance_box.get("1.0", tk.END)

    file = open("attendance.txt", "w")
    file.write(data)
    file.close()
    status_label.configure(text='Attendence Saved Successfully')
def show_record():
    name = es.get().lower()
    data = attendance_box.get("1.0", tk.END)
    for line in data.split("\n"):
        if line.lower().startswith(name):
            result_label.config(text=line)
            return
    result_label.config(text="Student Record Not Found")
root.title("Attendence Management System")
l=tk.Label(root,text="ATTENDANCE MANAGEMENT SYSTEM", font=("Arial", 10, "bold"), fg="blue").grid(row=0,column=1,columnspan=4)
l2=tk.Label(root,text="Enter Student Name",fg="blue").grid(row=1,column=0)
e1=tk.Entry(root)
e1.grid(row=1,column=1)
button=tk.Button(root,text="Add Student",command=add_student,bg="green",fg="white")
button.grid(row=1,column=2)
name=tk.Label(root,text="Student list").grid(row=2,column=0)
text_box = tk.Listbox(root, width=10, height=5)
text_box.grid(row=3,column=0)
b=tk.Button(root,text="Present",command=mark_present, bg="green", fg="white")
b.grid(row=4,column=0)
b1=tk.Button(root,text="Absent",command=mark_absent,bg="red",fg="white")
b1.grid(row=4,column=1)
tk.Label(root,text="Attendance Records",font=("Arial", 10, "bold"), fg="blue").grid(row=5,column=1)
attendance_box = tk.Text(root,width=25,height=10)
attendance_box.grid(row=6,column=1,rowspan=4)
save_btn = tk.Button(root, text="Save Attendance", command=save_attendance,bg="green",fg="white")
save_btn.grid(row=10, column=1, pady=10)
status_label = tk.Label(root, text="")
status_label.grid(row=12, column=1)
s=tk.Label(root,text="Enter Name",fg="blue").grid(row=13,column=0)
es=tk.Entry(root)
es.grid(row=13,column=1)
bb=tk.Button(root,text="show",command=show_record,bg="green",fg="white")
bb.grid(row=14,column=1)
result_label = tk.Label(root, text="")
result_label.grid(row=15, column=1)
root.mainloop()
