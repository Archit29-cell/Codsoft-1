from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x600+0+0")
        self.root.attribute=("-fullscreen",True)
        self.root.title("TO DO LIST (TASK LIST)")
        self.root.configure(bg ='black')

        self.var_task = StringVar()
        self.var_id = StringVar()
        self.var_status = StringVar()

        title_label =Label(self.root, text="TO DO LIST / TASK LIST ", font=("Consolas",40, "bold"),bg = "red",fg = "black",bd =8)
        title_label.place(x= 0, y =0, width = 780,height = 150 )

        img1 = Image.open(r"download.jpeg")
        img1 = img1.resize((500,150))
        self.photoimg1 = ImageTk.PhotoImage(img1)


        f_lbl = Label(self.root, image=self.photoimg1,bd =4)
        f_lbl.place(x=780,y =0, width =500, height = 150)


        add_text =Label(self.root, text="TASK DETAILS", font=("Consolas",18, "bold"),bg = "blue",fg = "red",bd =8)
        add_text.place(x= 200, y =160+30,height = 40)

        # S.No. LABEL
        id_text =Label(self.root, text="S.No. ", font=("Consolas",15, "bold"),bg = "red",fg = "white",bd =8)
        id_text.place(x= 200, y =205+30,height = 20)

        # S.No. ENTRY
        id_entry = ttk.Entry(self.root,textvariable=self.var_id,font= ("times new roman", 15, "bold"),width = 8)
        id_entry.place(x=290,y =205+30,height = 20) 
        self.id_entry = id_entry 

        # TASK LABEL
        task =Label(self.root, text="TASK ", font=("Consolas",18, "bold"),bg = "red",fg = "white",bd =8)
        task.place(x= 200, y =230+30,height = 30,width = 180) 

        task_entry = ttk.Entry(self.root,textvariable=self.var_task,font= ("times new roman", 15, "bold"),width = 17)
        task_entry.grid(row = 1,column=0,padx = 200,pady = 265+30)
        self.task_entry = task_entry

              
        
        # STATUS LABEL
        status = Label(self.root, bd =4, font=("time new roman", "15","bold"),text="STATUS",bg ="red", fg = "white")
        status.place(x = 200,y =300+30 , width = 180,height =30)

        # STATUS DROPDOWN LIST
        status_combo = ttk.Combobox(self.root, textvariable=self.var_status,font=("times new roman", "15","bold"), state="readonly" )
        status_combo["values"] =("Incomplete", "Complete")
        status_combo.current(0)
        status_combo.place(x = 200,y =335+30, width = 180,height =40)




        # BUTTONS 
        #  ADD BUTTON TO ADD THE TASK INTO TABLE 
        add = Button(self.root,text = "ADD",command=self.add_data, font = ("Consolas",20, "bold","italic"), fg= "black", bg = "blue")
        add.place(x = 200,y =375+30, width = 180,height =40 )

        #  UPDATE BUTTON TO UPDATE THE TASK AND STATUS INTO THE TABLE 
        update = Button(self.root, text = "UPDATE",command=self.update_data, font = ("Consolas",20, "bold","italic"), fg= "black", bg = "blue")
        update.place(x = 200,y =420+30, width = 180,height =40 )

        #  DELETE BUTTON TO DELETE THE TASK FROM TABLE
        delete = Button(self.root, text = "DELETE", command=self.del_data, font = ("Consolas",20, "bold","italic"), fg= "black", bg = "blue")
        delete.place(x = 200,y =465+30, width = 180,height =40 )

        # EXIT BUTTON TO EXTI THE APPLICATION
        exit = Button(self.root, text = "EXIT", command=self.exit,font = ("Consolas",20, "bold","italic"), fg= "black", bg = "blue")
        exit.place(x = 200,y =510+30, width = 180,height =40 )


#============================= right frame ==========================================
#============================= Table Format =========================================
        right_frame = Frame(self.root, bd=8, relief= GROOVE,bg="white")
        right_frame.place(x =600,y =155, width=680,height=540 )

        scroll_x = ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame,orient=VERTICAL)

        self.table = ttk.Treeview(right_frame, columns=("S.NO.","TASK", "STATUS" ),xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)
        scroll_x.pack(side =BOTTOM, fill=X )
        scroll_y.pack(side =RIGHT, fill=Y )
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)
        
        self.table.heading("S.NO.", text ="S.NO.")
        self.table.heading("TASK", text= "TASK")
        self.table.heading("STATUS", text="STATUS")
        self.table["show"] = "headings"

        self.table.column("S.NO.", width= 50)
        self.table.column("STATUS", width = 100)
        self.table.pack(fill = BOTH, expand =1)
        self.table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()
        
# function to add the data in the list

    def add_data(self):
        if self.var_task.get() =="" :
            messagebox.showerror("Error","Insert Task", parent =self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username ="root", password = "root", database = "todolist")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into todolist values(%s,%s,%s)",(
                                  self.var_id.get().upper(),self.var_task.get().upper(),self.var_status.get().upper()))
                conn.commit()
                self.fetch_data()
                conn.close()

                self.var_id.set("")  # Clear S.No.
                self.var_task.set("")  # Clear Task
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}", parent = self.root)

# function to fetch the data from database todolist

    def fetch_data(self):
        conn = mysql.connector.connect(host= "localhost", username = "root", password = "root",database = "todolist")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from todolist")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data :
                self.table.insert("",END, values = i)
            conn.commit()
        conn.close()
    
    # fun to choose the item where the cursor

    def get_cursor(self,event =""):
        cursor_focus = self.table.focus()
        content = self.table.item(cursor_focus)
        data = content["values"]
        self.var_id.set(data[0])
        self.var_task.set(data[1])
        self.var_status.set(data[2])

    # function to update the task in list

    def update_data(self):
        if self.var_task.get() == "":
            messagebox.showerror("Error", "Select Task to Update", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update ?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="todolist")
                    my_cursor = conn.cursor()

                    my_cursor.execute("UPDATE todolist SET Task = %s, Status = %s WHERE `S.No.` = %s", 
                                      (self.var_task.get().upper(), self.var_status.get().upper(), self.var_id.get().upper()))

                    messagebox.showinfo("Success", "Updated successfully", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    self.var_id.set("")  # Clear S.No.
                    self.var_task.set("")  # Clear Task

                    
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # function to delete the task from list 

    def del_data(self):
        if self.var_task.get() == "":
            messagebox.showerror("Error", "Select Task to Delete", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="todolist")
                    my_cursor = conn.cursor()
                    sql ="delete from todolist where `S.No.` =%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                self.var_id.set("")  # Clear S.No.
                self.var_task.set("")  # Clear Task
                messagebox.showinfo("Delete","Deleted Successfully ", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    # function to exit the application

    def exit(self):
        exit = messagebox.askyesno("Exit", "Do You Want to Exit") 
        if exit >0:
            return root.destroy()
        else:
            return

    
#  Main Function    

if __name__  == "__main__":
    root = Tk()
    obj = ToDoList(root)
    root.mainloop()
