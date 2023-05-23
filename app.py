'''｡☆✼★━━━━━━━━━━━━★✼☆｡IMPORT｡☆✼★━━━━━━━━━━━━★✼☆｡'''



from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import mysql.connector as sq



'''｡☆✼★━━━━━━━━━━━━★✼☆｡CONNECTIONS｡☆✼★━━━━━━━━━━━━★✼☆｡'''



connect = sq.connect(host = 'localhost', user = 'root', passwd = 'Vinaya@2003', database = 'LumosLiving')

cursor = connect.cursor()



'''｡☆✼★━━━━━━━━━━━━★✼☆｡MAIN｡☆✼★━━━━━━━━━━━━★✼☆｡'''



main = Tk()
main.title('｡ﾟ★*･ﾟ☆LUMOS LIVING｡ﾟ★*･ﾟ☆')
main.iconbitmap('icon.ico')
main.geometry('800x800')



'''｡☆✼★━━━━━━━━━━━━★✼☆｡VARIABLES｡☆✼★━━━━━━━━━━━━★✼☆｡'''



person = ''
adminid_val = IntVar()
building_val = StringVar()
apartment_val = IntVar()
password_val = StringVar()
issueid = 0 
dateresolved_val = StringVar()
category_val = StringVar() 
status_val = StringVar()
expense_val = StringVar()
nmcategory_val = StringVar()
contact_val = IntVar()



'''｡☆✼★━━━━━━━━━━━━★✼☆｡IMAGES｡☆✼★━━━━━━━━━━━━★✼☆｡'''



main_image = PhotoImage(file = 'main.png')
login_image = PhotoImage(file = 'loginbutton.png')
outline_loginpage = PhotoImage(file = 'loginpageoutline.png')
resident_loginpage = PhotoImage(file = 'residentloginpage.png')
admin_loginpage = PhotoImage(file = 'adminloginpage.png')
show_pass = PhotoImage(file = 'show.png')
hide_pass = PhotoImage(file = 'hide.png') 
admin_image = PhotoImage(file = 'admin.png') 
resident_image = PhotoImage(file = 'resident.png')
home = PhotoImage(file = 'home.png')
welcome_image = PhotoImage(file = 'welcome.png')
issues_image = PhotoImage(file = 'issues_option.png')
nearme_image = PhotoImage(file = 'nearme_option.png')
logout_image = PhotoImage(file = 'logout_option.png')
issues_altimage = PhotoImage(file = 'issues_alt.png')
nearme_altimage = PhotoImage(file = 'nearme_alt.png')
logout_altimage = PhotoImage(file = 'logout_alt.png')
sort_image = PhotoImage(file = 'sort.png')
tools_image = PhotoImage(file = 'tools.png')
ModifyIssue_image = PhotoImage(file = 'modify.png')
details_image = PhotoImage(file = 'view_details.png')
AddIssue_image = PhotoImage(file = 'add_issue.png')
UpdateIssue_image = PhotoImage(file = 'update_issue.png')
vd_title = PhotoImage(file = 'vd_title.png')
ai_title = PhotoImage(file = 'ai_title.png')
ui_title = PhotoImage(file = 'ui_title.png')
blockframe_image = PhotoImage(file = 'blockframe.png')
back_image = PhotoImage(file = 'back.png')
confirm_image = PhotoImage(file = 'confirm.png')
category_image = PhotoImage(file = 'category.png')
store_image1 = PhotoImage(file = 'storedonut.png')
store_image2 = PhotoImage(file = 'storegrocery.png')
store_image3 = PhotoImage(file = 'storepizza.png')
store_image4 = PhotoImage(file = 'storegift.png')
AddStore_image = PhotoImage(file = 'add_store.png')
EditStore_image = PhotoImage(file = 'edit_store.png')
as_title = PhotoImage(file = 'as_title.png')
es_title = PhotoImage(file = 'es_title.png')



'''｡☆✼★━━━━━━━━━━━━★✼☆｡PRI. FUNCTIONS｡☆✼★━━━━━━━━━━━━★✼☆｡'''



# clear page:༅｡.｡༅:*･ﾟﾟ･⭑
def clean(*new):

    widgets = main.winfo_children()
    for widget in widgets:
        widget.place_forget()
        
    for nextpage in new:
        nextpage()
    
# first:༅｡.｡༅:*･ﾟﾟ･⭑
def first():
    
    background1.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    login_button.place(relx=0.78,rely=0.3)

# second:༅｡.｡༅:*･ﾟﾟ･⭑
def second():

    background2.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    admin_button.place(relx = 0.19, rely = 0.3)
    resident_button.place(relx = 0.62, rely = 0.3)

# third:༅｡.｡༅:*･ﾟﾟ･⭑
def third():
    
    background3.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    issues_option.place(relx = 0.05, rely = 0.04)
    nearme_option.place(relx = 0.25, rely = 0.04)
    logout_option.place(relx = 0.45, rely = 0.04)
    welcome_label.place(relx = 0.09, rely = 0.2)
    
    global person
    
    if person == 'Resident':
        aprmnt_label.config(text = f'{building_val.get()} {apartment_val.get()}')
        
    elif person == 'Admin':
        aprmnt_label.config(text = 'ADMIN')

    aprmnt_label.place(relx = 0.25, rely = 0.4)
        

# fourth:༅｡.｡༅:*･ﾟﾟ･⭑
def fourth():
    
    issuestable.place(relx = 0.07, rely = 0.15, relwidth = 0.86, relheight = 0.4)
    sort_button.place(relx = 0.94, rely = 0.15)
    tools_label.place(relx = 0.18, rely = 0.65)
    details_button.place(relx = 0.6, rely = 0.65)
    AddIssue_button.place(relx = 0.6, rely = 0.75)
    UpdateIssue_button.place(relx = 0.6, rely = 0.85)
    
# fifth:༅｡.｡༅:*･ﾟﾟ･⭑
def fifth():

    background4.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    title_label.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)
    container.place(relx = 0.1, rely = 0.15, relwidth = 0.8, relheight = 0.7)
    blockframe.place(relx = 0, rely = 0, relwidth = 1, relheight =1)
    id_label.place(relx = 0.05, rely = 0.05)
    id_entry.place(relx = 0.3, rely = 0.05)
    raisedby_label.place(relx = 0.05, rely = 0.125)
    building_label.place(relx = 0.21, rely = 0.125)
    building_entry.place(relx = 0.35, rely = 0.125, relwidth = 0.2)
    apartment_label.place(relx = 0.56, rely = 0.125)
    apartment_entry.place(relx = 0.74, rely = 0.125, relwidth = 0.2)
    dateraised_label.place(relx = 0.05, rely = 0.2)
    dateraised_entry.place(relx = 0.3, rely = 0.2)
    dateresolved_label.place(relx = 0.05, rely = 0.275)
    dateresolved_entry.place(relx = 0.3, rely = 0.275)
    category_label.place(relx = 0.05, rely = 0.35)
    category_dropdown.place(relx = 0.3, rely = 0.35)
    description_label.place(relx = 0.05, rely = 0.425)
    description_text.place(relx = 0.3, rely = 0.425, relwidth = 0.6, relheight = 0.35)
    status_label.place(relx = 0.05, rely = 0.82)
    status1_radiobutton.place(relx = 0.3, rely = 0.82)
    status2_radiobutton.place(relx = 0.5, rely = 0.82)
    status3_radiobutton.place(relx = 0.74, rely = 0.82)
    expense_label.place(relx = 0.05, rely = 0.895)
    expense_entry.place(relx = 0.3, rely = 0.895)
    back_button.place(relx = 0.65, rely = 0.9)

#sixth:༅｡.｡༅:*･ﾟﾟ･⭑
def sixth():
    
    nmcategory_label.place(relx = 0.25, rely = 0.13)
    nearme_dropdown.place(relx = 0.45, rely = 0.13)
    store_imglabel1.place(relx = 0.04, rely = 0.75)
    store_imglabel2.place(relx = 0.3, rely = 0.75)
    store_imglabel3.place(relx = 0.55, rely = 0.75)
    store_imglabel4.place(relx = 0.78, rely = 0.75)

    global person

    if person == 'Resident':
        nearmetable.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.5)

    elif person == 'Admin':
        nearmetable.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.4)
        AddStore_button.place(relx = 0.2, rely = 0.65)
        EditStore_button.place(relx = 0.6, rely = 0.65)

#seventh:༅｡.｡༅:*･ﾟﾟ･⭑
def seventh():
    
    background4.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    title_label.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.1)
    container.place(relx = 0.1, rely = 0.15, relwidth = 0.8, relheight = 0.7)
    blockframe.place(relx = 0, rely = 0, relwidth = 1, relheight =1)
    name_label.place(relx = 0.05, rely = 0.1)
    name_entry.place(relx = 0.3, rely = 0.1)
    scategory_label.place(relx = 0.05, rely = 0.25)
    nearme_dropdown.place(relx = 0.34, rely = 0.32)
    timing_label.place(relx = 0.05, rely = 0.4)
    timing_entry.place(relx = 0.3, rely = 0.4)
    contact_label.place(relx = 0.05, rely = 0.55)
    contact_entry.place(relx = 0.3, rely = 0.55)
    address_label.place(relx = 0.05, rely = 0.7)
    address_text.place(relx = 0.3, rely = 0.7, relwidth = 0.4, relheight = 0.2 )
    confirm_button.place(relx = 0.15, rely = 0.9)
    back_button.place(relx = 0.65, rely = 0.9)


'''｡☆✼★━━━━━━━━━━━━★✼☆｡SEC FUNCTIONS｡☆✼★━━━━━━━━━━━━★✼☆｡'''



# password:༅｡.｡༅:*･ﾟﾟ･⭑

def visible(event):
    print(event)

    password_entry.config(show = '')

    show_label.config(image = show_pass)
    show_label.bind('<Leave>', invisible)

def invisible(event):

    password_entry.config(show = '●')

    show_label.config(image = hide_pass)
    show_label.bind('<Enter>', visible)

# user:༅｡.｡༅:*･ﾟﾟ･⭑
def user(arg):

    login_button.place(relx = 0.4, rely = 0.8)
    password_entry.place(relx = 0.3, rely = 0.7, relwidth = 0.4, relheight = 0.03)
    show_label.place(relx = 0.73, rely = 0.705)

    widgets = [adminid_val, password_val, building_val, apartment_val]
    for widget in widgets:
        widget.set('')
     
    if arg == 'resident':
        background2.config(image = resident_loginpage)
        resident_button.config(state = 'disabled')
        admin_button.config(state = 'active')

        building_dropdown.place(relx = 0.3, rely = 0.435, relwidth = 0.4, relheight = 0.03)
        apartment_dropdown.place(relx = 0.3, rely = 0.56, relwidth = 0.4, relheight = 0.03) 

        for widget in admin:
            widget.place_forget()

        password_entry.bind('<Return>', VerifyResident)
        login_button.config(command = lambda: VerifyResident(None), bg = '#B5FFFB')

    else:
        background2.config(image = admin_loginpage)
        resident_button.config(state = 'active')
        admin_button.config(state = 'disabled')

        adminid_entry.place(relx = 0.3, rely = 0.54, relwidth = 0.4, relheight = 0.03)

        for widget in resident:
            widget.place_forget()

        password_entry.bind('<Return>', VerifyAdmin)
        login_button.config(command = lambda: VerifyAdmin(None), bg = '#B5FFFB')

# fetch apartment_dropdown data:༅｡.｡༅:*･ﾟﾟ･⭑
def fetchapartments(event):

    qry = f'SELECT apartments FROM building_info WHERE buildingname = "{building_val.get()}"'
    cursor.execute(qry)
    number = cursor.fetchone()

    apartment_options = [x for x in range(101, number[0]+100+1)]

    apartment_dropdown['value'] = apartment_options

# verfication:༅｡.｡༅:*･ﾟﾟ･⭑
def VerifyAdmin(event):

    try:
        adminid_val.get()

    except Exception:
        messagebox.showerror('LOGIN ERROR', 'Check your ID again. ID must contain digits (0-9) only')

    else:
        qry = f'SELECT password FROM admin_master WHERE adminid = {adminid_val.get()}'
        cursor.execute(qry)

        passwd = cursor.fetchone()

        if passwd:
            if password_val.get() == passwd[0]:
                global person
                person = 'Admin'
                clean(third)

            else:
                messagebox.showerror('LOGIN ERROR', 'You have entered the wrong password. Please try again.')
                password_val.set('')
                
        else:
            messagebox.showerror('LOGIN ERROR', 'You have entered the wrong ID. Please try again.')

            adminid_val.set('')
            password_val.set('')

def VerifyResident(event):
    
    if building_val.get() == '':
        messagebox.showerror('LOGIN ERROR', 'Please select the building you live in.')

#    elif apartment_val.get() == '': #elephant
#        messagebox.showerror('LOGIN ERROR', 'Please select the apartment you live in.')
    try:
        apartment_val.get()
    except TclError:
        messagebox.showerror('LOGIN ERROR', 'Please select the apartment you live in.')
        
    else:
        qry = f'SELECT password FROM apartment_master WHERE buildingname = "{building_val.get()}" AND apartment = {apartment_val.get()}'
        cursor.execute(qry)

        passwd = cursor.fetchone()

        if password_val.get() == passwd[0]:
            global person
            person = 'Resident'
            clean(third)
            
        else:
            messagebox.showerror('LOGIN ERROR', 'You have entered the wrong password. Please try again.')
            password_val.set('')

# confirm:༅｡.｡༅:*･ﾟﾟ･⭑

def confirm(function, task):

    if function == 'issue':
        
        if task == 'ai':
            
            if not category_val.get() or description_text.get('1.0', 'end') == '\n':
                messagebox.showerror('INCOMPLETE', 'Please fill all fields before pressing confirm')

            else:
                qry = f'INSERT INTO issue VALUES({issueid}, "{category_val.get()}", "{description_text.get("1.0", "end")}", "{building_val.get()}", {apartment_val.get()}, "{date.today()}", NULL, "Pending", NULL)'
                issuestable.insert('', 'end', values = (issueid, building_val.get()+' '+str(apartment_val.get()), category_val.get(), status_val.get()))
                clean(third, fourth)
               
        elif task == 'ui':
            
            if person == 'Admin':

                if expense_entry.get() == 'N/A':
                    expense_val.set('')

                else:
                    expense_val.set(expense_entry.get())

                if dateresolved_entry.get() == 'N/A':
                    dateresolved_val.set('')

                else:
                    dateresolved_val.set(f'"{dateresolved_entry.get()}"')   

                qry = f'UPDATE issue SET dateresolved = {dateresolved_val.get() if dateresolved_val.get() else "NULL"}, status = "{status_val.get()}", expense = {expense_val.get() if expense_val.get() else "NULL"} WHERE issueid = {issueid}'

            else:
                qry = f'UPDATE issue SET issuecategory = "{category_val.get()}", issuedesc = "{description_text.get("1.0", "end")}" WHERE issueid = {issueid}'

            selected = issuestable.focus()
            issuestable.item(selected, text = '', values = (issueid, building_entry.get()+' '+apartment_entry.get(), category_val.get(), status_val.get()))
            clean(third, fourth)
        
    elif function == 'nearme':

        if not nmcategory_val.get() or not name_entry.get() or not timing_entry.get() or not contact_entry.get() or address_text.get('1.0', 'end') == '\n':
            messagebox.showerror('INCOMPLETE', 'Please fill all fields before pressing confirm')

        try:
            contact_val.get()

            if len(str(contact_val.get())) != 10 and len(str(contact_val.get())) != 8:
                messagebox.showerror('INVALID', 'Invalid contact number entered')

            else:

                if task == 'add':
                    qry = f'INSERT INTO nearme VALUES("{name_entry.get()}", "{nmcategory_val.get()}", "{timing_entry.get()}", {contact_val.get()}, "{address_text.get("1.0", "end")}")'
                    nearmetable.insert('', 'end', values = (name_entry.get(), timing_entry.get(), contact_val.get(), address_text.get("1.0", "end")))
                    clean(third, sixth)

                elif task == 'edit':
                    selected = nearmetable.focus()
                    record = nearmetable.item(selected, 'values')
                    qry = f'UPDATE nearme SET name = "{name_entry.get()}", category = "{nmcategory_val.get()}", timings = "{timing_entry.get()}", contact= {contact_val.get()}, address = "{address_text.get("1.0", "end")}" WHERE name = "{record[0]}"'
                    selected = nearmetable.focus()
                    nearmetable.item(selected, text = '', values = (name_entry.get(), timing_entry.get(), contact_val.get(), address_text.get("1.0", "end")))
                    clean(third, sixth)

        except Exception:
            messagebox.showerror('INVALID', 'Invalid contact number entered')   
  
    try:
        cursor.execute(qry)
        connect.commit()
    except UnboundLocalError:
        pass
    

# issue:༅｡.｡༅:*･ﾟﾟ･⭑

def fetchdata(task):

    back_button.config(command = lambda: clean(third, fourth))
    
    widgets = container.winfo_children()
    for widget in widgets:
        widget.place_forget()

    widgets = [id_entry, building_entry, apartment_entry, dateraised_entry,
               dateresolved_entry, category_dropdown, description_text,
               status1_radiobutton, status2_radiobutton, status3_radiobutton,
               expense_entry]
    for widget in widgets:
        widget.config(state = NORMAL)
        try:    
            widget.delete(0, END)
        except Exception:
            pass
    description_text.delete('1.0', 'end')
    category_dropdown.set('')
    
    if task == 'ai':
        
        if person == 'Admin':
            messagebox.showinfo('INFO', 'Admins cannot perform this action')
            
        else:
            title_label.config(image = ai_title)
            clean(fifth)
            confirm_button.place(relx = 0.15, rely = 0.9)
            
            qry = 'SELECT MAX(issueid) FROM issue'
            cursor.execute(qry)
            global issueid
            issueid = cursor.fetchone()[0] + 1
            
            id_entry.insert(0, issueid)
            building_entry.insert(0, building_val.get())
            apartment_entry.insert(0, apartment_val.get())
            dateraised_entry.insert(0, date.today())
            dateresolved_entry.insert(0, 'N/A')
            status_val.set('Pending')
            expense_entry.insert(0, 'N/A')

            widgets = [id_entry, building_entry, apartment_entry,
                       dateraised_entry, dateresolved_entry, status1_radiobutton,
                       status2_radiobutton, status3_radiobutton, expense_entry]
            for widget in widgets:
                widget.config(state = DISABLED)
            category_dropdown.config(state = 'readonly')

            confirm_button.config(command = lambda: confirm('issue', task))
        
    else:
        selected = issuestable.focus()
        
        if selected:
            clean(fifth)
            record = issuestable.item(selected, 'values')
            qry = f'SELECT * FROM issue WHERE issueid = {int(record[0])}'
            cursor.execute(qry)
            detail = list(cursor.fetchone())

            for i in range(len(detail)):
                if detail[i] == None:
                    detail[i] = 'N/A'
                else:
                    pass

            issueid = detail[0]
                
            id_entry.insert(0, issueid)
            building_entry.insert(0, detail[3])
            apartment_entry.insert(0, detail[4])
            dateraised_entry.insert(0, detail[5])
            dateresolved_entry.insert(0, detail[6])
            category_dropdown.set(detail[1])
            description_text.insert('1.0', detail[2])
            status_val.set(detail[7])
            expense_entry.insert(0, detail[8])
            
            if task == 'ui':
                title_label.config(image = ui_title)
                
                confirm_button.config(command = lambda: confirm('issue', task))
                confirm_button.place(relx = 0.15, rely = 0.9)

                if person == 'Admin':
                    widgets = [id_entry, building_entry,
                               apartment_entry, category_dropdown,
                               description_text, dateraised_entry]
                    for widget in widgets:
                        widget.config(state = DISABLED)

                else:
                    
                    if detail[3] != building_val.get() or detail[4] != apartment_val.get():
                        clean(third, fourth)
                        messagebox.showinfo('INFO', 'Residents cannot update and/or edit issues not raised by them')
                        
                    else:
                        widgets = [id_entry, building_entry, apartment_entry,
                                   dateraised_entry, dateresolved_entry,
                                   status1_radiobutton,status2_radiobutton,
                                   status3_radiobutton, expense_entry]
                        for widget in widgets:
                            widget.config(state = DISABLED)
                        category_dropdown.config(state = 'readonly')
              
            elif task == 'vd':
                title_label.config(image = vd_title)

                for widget in widgets:
                    widget.config(state = DISABLED)
                

        else:

            if task == 'ui':
                messagebox.showinfo('No Record Selected', 'Please select a record to update and/or edit its details.')

            else:
                messagebox.showinfo('No Record Selected', 'Please select a record to view its details.')

# sort:༅｡.｡༅:*･ﾟﾟ･⭑

def sort(index, text, criteria, order):
    for record in issuestable.get_children():
        issuestable.delete(record)
    qry = f'SELECT * FROM issue ORDER BY {criteria} {order}'
    cursor.execute(qry)
    issues = cursor.fetchall()
    for issue in issues:
        issuestable.insert('', 'end', values = (issue[0], issue [3]+' '+str(issue[4]), issue[1], issue[7]))
    if order == 'ASC':
        sort_menu.entryconfig(index, label = 'Sort By: '+text+' ↓', command = lambda: sort(index, text, criteria,'DESC'))
    else:
        sort_menu.entryconfig(index, label = 'Sort By: '+text+' ↑', command = lambda: sort(index, text, criteria,'ASC'))
         
def menu():
    sort_menu.tk_popup(sort_button.winfo_rootx()-190, sort_button.winfo_rooty()+25)

# fetch store details:༅｡.｡༅:*･ﾟﾟ･⭑

def fetchstores(event):

    for store in nearmetable.get_children():
        nearmetable.delete(store)
    
    qry = f'SELECT * FROM nearme WHERE category = "{nmcategory_val.get()}"'
    cursor.execute(qry)
    stores = cursor.fetchall()
    for store in stores:
        nearmetable.insert('', 'end', values = (store[0], store[2], store[3], store[4]))

# add/ edit store details:༅｡.｡༅:*･ﾟﾟ･⭑

def modifystores(task):

    back_button.config(command = lambda: clean(third, sixth))

    widgets = container.winfo_children()
    for widget in widgets:
        widget.place_forget()

    widgets = [name_entry, timing_entry, contact_entry]
    for widget in widgets:
        widget.delete(0, END)
        
    address_text.delete('1.0', 'end')
    
    
    if task == 'add':

        nmcategory_val.set('')
        timing_entry.insert(0, 'ex. 10am - 10pm')        
        title_label.config(image = as_title)
        confirm_button.config(command = lambda: confirm('nearme', 'add'))

        clean(seventh)

    if task == 'edit':
        #'ex. 10am - 10pm'
        selected = nearmetable.focus()
        
        if selected:
            record = nearmetable.item(selected, 'values')

            name_entry.insert(0, record[0])
            timing_entry.insert(0, record[1])
            contact_entry.insert(0, record[2])
            address_text.insert('1.0', record[3])
            
            title_label.config(image = es_title)
            confirm_button.config(command = lambda: confirm('nearme', 'edit'))

            clean(seventh)

        else:
            messagebox.showinfo('No Store Selected', 'Please select a store to update and/or edit its details.')
        
# logout:༅｡.｡༅:*･ﾟﾟ･⭑

def logout():
    clean(first)
    widgets = [adminid_val, password_val, building_val, apartment_val]
    for widget in widgets:
        widget.set('')
    login_button.config(command = lambda: clean(second), bg = '#FEF2F2')
    background2.config(image = outline_loginpage)
    admin_button.config(state = 'active')
    resident_button.config(state = 'active')



'''｡☆✼★━━━━━━━━━━━━★✼☆｡WIDGETS｡☆✼★━━━━━━━━━━━━★✼☆｡'''



# backgrounds:༅｡.｡༅:*･ﾟﾟ･⭑

background1 = Label(main, image = main_image)

background2 = Label(main, image = outline_loginpage)

background3 = Label(main, image = home)

background4 = Label(main, image = ModifyIssue_image)

# first:༅｡.｡༅:*･ﾟﾟ･⭑ 

login_button = Button(main, image = login_image, bg = '#FEF2F2', borderwidth = 0,
                      cursor = 'hand2', command = lambda: clean(second))

# second:༅｡.｡༅:*･ﾟﾟ･⭑

admin_button = Button(main, image = admin_image, bg = '#DEE5FF', borderwidth = 0,
                      cursor = 'hand2', command = lambda: user('admin'))

resident_button = Button(main, image = resident_image, bg = '#DEE5FF', borderwidth = 0,
                         cursor = 'hand2', command = lambda: user('resident'))

adminid_entry = Entry(main, textvariable = adminid_val, font = 'Century\ Gothic',
                      justify = 'center', cursor = 'xterm')

building_options = []

qry = 'SELECT buildingname FROM building_info'
cursor.execute(qry)
for buildings in cursor.fetchall():
    for building in buildings:
        building_options.append(building)
           
building_dropdown = ttk.Combobox(main, textvariable = building_val, value = building_options,
                                 height = 5, justify = 'center', cursor = 'hand2', state = 'readonly')
building_dropdown.bind('<<ComboboxSelected>>', fetchapartments)


apartment_dropdown = ttk.Combobox(main, textvariable = apartment_val, height = 5,
                                  justify = 'center', cursor = 'hand2', state = 'readonly')

password_entry = Entry(main, textvariable = password_val, font = 'Century\ Gothic',
                       justify = 'center', cursor = 'xterm', show = '●')

show_label = Label(main, image = hide_pass, bg = '#B5FFFB', borderwidth = 0, cursor = 'hand2')
show_label.bind('<Enter>', visible)

resident = [building_dropdown, apartment_dropdown, ]
admin = [adminid_entry, ]

# third:༅｡.｡༅:*･ﾟﾟ･⭑

issues_option = Button(main, image = issues_image,  cursor = 'hand2',
                        borderwidth = 0, bg = '#FFFFFF', command = lambda: clean(third, fourth))
issues_option.bind('<Enter>', lambda x: issues_option.config(image = issues_altimage))
issues_option.bind('<Leave>', lambda x: issues_option.config(image = issues_image))

nearme_option = Button(main, image = nearme_image,  cursor = 'hand2',
                        borderwidth = 0, bg = '#FFFFFF', command = lambda: clean(third, sixth))
nearme_option.bind('<Enter>', lambda x: nearme_option.config(image = nearme_altimage))
nearme_option.bind('<Leave>', lambda x: nearme_option.config(image = nearme_image))

logout_option = Button(main, image = logout_image,  cursor = 'hand2',
                        borderwidth = 0, bg = '#FFFFFF', command = logout)
logout_option.bind('<Enter>', lambda x: logout_option.config(image = logout_altimage))
logout_option.bind('<Leave>', lambda x: logout_option.config(image = logout_image))

welcome_label = Label(main, image = welcome_image,
                 borderwidth = 0, bg = '#FEF2F2')

aprmnt_label = Label(main, bg = '#FEF2F2', fg = '#000000',
                     font = 'Goudy\ Stout 50')

# fourth:༅｡.｡༅:*･ﾟﾟ･⭑

issuestable = ttk.Treeview(main, columns = (1,2,3,4), show = 'headings',
                           height = 20, selectmode = 'browse')
issuestable.column(1, width = 110, minwidth = 20, anchor = CENTER)
issuestable.column(2, width = 110, minwidth = 20, anchor = CENTER)
issuestable.column(3, width = 110, minwidth = 20, anchor = CENTER)
issuestable.column(4, width = 110, minwidth = 20, anchor = CENTER)
issuestable.heading(1, text = 'ID')
issuestable.heading(2, text = 'Apartment')
issuestable.heading(3, text = 'Category')
issuestable.heading(4, text = 'Status')

qry = 'SELECT * FROM issue'
cursor.execute(qry)
issues = cursor.fetchall()
for issue in issues:
    issuestable.insert('', 'end', values = (issue[0], issue [3]+' '+str(issue[4]), issue[1], issue[7]))

sort_button = Button(main, image = sort_image, cursor = 'hand2',
                     borderwidth = 0, bg = '#FEF2F2', command = menu)

sort_menu = Menu(main, tearoff = False, font = ('Century\ Gothic',15), bg = '#F8F8FF')
sort_menu.add_command(label = 'Sort By: Issue ID ↓', command = lambda: sort(0, 'Issue ID' ,'issueid', 'DESC'))
sort_menu.add_command(label = 'Sort By: Apartment ↑', command = lambda: sort(1, 'Apartment', 'buildingname, apartment', 'ASC'))
sort_menu.add_command(label = 'Sort By: Category ↑', command = lambda: sort(2, 'Category', 'issuecategory', 'ASC'))
sort_menu.add_command(label = 'Sort By: Status ↑', command = lambda: sort(3, 'Status', 'FIELD (status, "Pending", "Under Way", "Resolved")', 'ASC'))

tools_label = Label(main, image = tools_image,
                    borderwidth = 0, bg = '#FEF2F2')

details_button = Button(main, image = details_image, cursor = 'hand2',
                        borderwidth = 0, bg = '#FEF2F2', command = lambda: fetchdata('vd'))

AddIssue_button = Button(main, image = AddIssue_image, cursor = 'hand2',
                         borderwidth = 0, bg = '#FEF2F2', command = lambda: fetchdata('ai'))

UpdateIssue_button = Button(main, image = UpdateIssue_image, cursor = 'hand2',
                            borderwidth = 0, bg = '#FEF2F2', command = lambda: fetchdata('ui'))

#fifth:༅｡.｡༅:*･ﾟﾟ･⭑

title_label = Label(main, borderwidth = 0, bg = '#FEF2F2')

container = Frame(main)

blockframe = Label(container, image = blockframe_image,
                   borderwidth = 0, bg = '#FEF2F2')

id_label = Label(container, text = 'Issue ID:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

id_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                 disabledforeground = '#000000', justify = CENTER)

raisedby_label = Label(container, text = 'Raised By:',
                          font = ('Century\ Gothic',15, 'underline'), bg = 'white')

building_label = Label(container, text = 'Building:',
                          font = ('Century\ Gothic',15, 'underline'), bg = 'white')

building_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                       disabledforeground = '#000000', justify = CENTER)


apartment_label = Label(container, text = 'Apartment:',
                          font = ('Century\ Gothic',15, 'underline'), bg = 'white')

apartment_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                        disabledforeground = '#000000', justify = CENTER)

dateraised_label = Label(container, text = 'Date Raised:',
                            font = ('Century\ Gothic',15, 'underline'), bg = 'white')

dateraised_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                         disabledforeground = '#000000', justify = CENTER)

dateresolved_label = Label(container, text = 'Date Resolved:',
                              font = ('Century\ Gothic',15, 'underline'), bg = 'white')

dateresolved_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                           disabledforeground = '#000000', justify = CENTER)

category_label = Label(container, text = 'Category:',
                       font = ('Century\ Gothic',15, 'underline'), bg = 'white')

category_dropdown = ttk.Combobox(container, font = ('Century\ Gothic',15),
                                 textvariable = category_val, foreground = '#000000', justify = CENTER, state = 'readonly')
category_options = ['Electrical', 'Plumbing', 'Sewage', 'Waste Management', 'Other']
category_dropdown['value'] = category_options

description_label = Label(container, text = 'Description:',
                       font = ('Century\ Gothic',15, 'underline'), bg = 'white')

description_text = ScrolledText(container, font = ('Century\ Gothic',15), cursor = 'xterm')

status_label = Label(container, text = 'Status:',
                       font = ('Century\ Gothic',15, 'underline'), bg = 'white')

status1_radiobutton = Radiobutton(container, text = 'Pending', font = ('Century\ Gothic',15),
                                  variable = status_val, value = 'Pending', disabledforeground = '#000000')

status2_radiobutton = Radiobutton(container, text = 'Under Way', font = ('Century\ Gothic',15),
                                  variable = status_val, value = 'Under Way', disabledforeground = '#000000')

status3_radiobutton = Radiobutton(container, text = 'Resolved', font = ('Century\ Gothic',15),
                                  variable = status_val, value = 'Resolved', disabledforeground = '#000000')

expense_label = Label(container, text = 'Expense:',
                       font = ('Century\ Gothic',15, 'underline'), bg = 'white')

expense_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                      disabledforeground = '#000000', justify = CENTER)

back_button = Button(main,image = back_image, cursor = 'hand2',
                     borderwidth = 0, bg = '#FEF2F2', command = lambda: clean(third, fourth))

confirm_button = Button(main, image = confirm_image, cursor = 'hand2',
                        borderwidth = 0, bg = '#FEF2F2')

#sixth:༅｡.｡༅:*･ﾟﾟ･⭑

nmcategory_label = Label(main, image = category_image,
                         borderwidth = 0, bg = '#FEF2F2')

nmcategory_val.set('')
nearme_dropdown = ttk.Combobox(main, font = ('Century\ Gothic',15),
                               textvariable = nmcategory_val, foreground = '#000000',
                               justify = CENTER, state = 'readonly')
nearme_options = ['Medical', 'Grocery Store', 'Restaurant', 'Petrol Pump', 'Stationary/ Xerox Store', 'Hospital/ Clinic']
nearme_dropdown['value'] = nearme_options
nearme_dropdown.bind('<<ComboboxSelected>>', fetchstores)

nearmetable = ttk.Treeview(main, columns = (1,2,3,4), show = 'headings',
                           height = 20, selectmode = 'browse')
nearmetable.column(1, width = 110, minwidth = 20, anchor = CENTER)
nearmetable.column(2, width = 110, minwidth = 20, anchor = CENTER)
nearmetable.column(3, width = 110, minwidth = 20, anchor = CENTER)
nearmetable.column(4, width = 110, minwidth = 20, anchor = CENTER)
nearmetable.heading(1, text = 'Name')
nearmetable.heading(2, text = 'Timings')
nearmetable.heading(3, text = 'Contact')
nearmetable.heading(4, text = 'Address')

store_imglabel1 = Label(main, image = store_image1,
                        borderwidth = 0, bg = '#FEF2F2')

store_imglabel2 = Label(main, image = store_image2,
                        borderwidth = 0, bg = '#FEF2F2')

store_imglabel3 = Label(main, image = store_image3,
                        borderwidth = 0, bg = '#FEF2F2')

store_imglabel4 = Label(main, image = store_image4,
                        borderwidth = 0, bg = '#FEF2F2')

AddStore_button = Button(main, image = AddStore_image, cursor = 'hand2',
                        borderwidth = 0, bg = '#FEF2F2', command = lambda: modifystores('add'))

EditStore_button = Button(main, image = EditStore_image, cursor = 'hand2',
                        borderwidth = 0, bg = '#FEF2F2', command = lambda: modifystores('edit'))

#seventh:༅｡.｡༅:*･ﾟﾟ･⭑
name_label = Label(container, text = 'Store Name:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

name_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                 disabledforeground = '#000000', justify = CENTER)

scategory_label = Label(container, text = 'Store Category:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

timing_label = Label(container, text = 'Store Timings:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

timing_entry = Entry(container, font = ('Century\ Gothic',15), cursor = 'xterm',
                 disabledforeground = '#000000', justify = CENTER)

contact_label = Label(container, text = 'Contact No.:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

contact_entry = Entry(container, font = ('Century\ Gothic',15), textvariable = contact_val,
                      cursor = 'xterm', disabledforeground = '#000000', justify = CENTER)

address_label = Label(container, text = 'Store Address:',
                 font = ('Century\ Gothic',15, 'underline'), bg = 'white')

address_text = ScrolledText(container, font = ('Century\ Gothic',15), cursor = 'xterm')



'''｡☆✼★━━━━━━━━━━━━★✼☆｡BEGIN｡☆✼★━━━━━━━━━━━━★✼☆｡'''



first()
main.mainloop()



'''｡☆✼★━━━━━━━━━━━━★✼☆｡CLOSE｡☆✼★━━━━━━━━━━━━★✼☆｡'''



connect.close()



'''｡☆✼★━━━━━━━━━━━━★✼☆｡THANK YOU, NEXT｡☆✼★━━━━━━━━━━━━★✼☆｡'''



