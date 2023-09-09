# -----------------------------------------------------------------------------------------------
#   Name:           Allowance Bot
#   Purpose:        To keep track of the clothing allowances of the three Ranui children
#   Version:        Version 32 -  make changes after user testing              
#   Author:         Micole Marquez
#   Date:           October 2021
# -----------------------------------------------------------------------------------------------
# imports
import tkinter as tk                # use to create Graphical User Interface (GUIs)
from tkinter import ttk             
from tkinter import *               
from csv import reader              # use to read flat file in csv format
import pandas as pd                 # use to parse multiple file formats to converting an entire data table into a NumPy matrix array
import time                         # use to add time
from tkcalendar import DateEntry    # use for tk date picker
from datetime import datetime       # setting the datetime to be a reference to the class and setting it to be a referenace to the module
import string                       # to create and customize the string formatting behaviors
import os                           # provides functions for interacting with the operating syst

# main AllowanceBot class 
class AllowanceBot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
       
        self.shared_data = {'{}Balance'.format(str.title(namelist[0])):tk.DoubleVar(),
                            '{}Balance'.format(str.title(namelist[1])):tk.DoubleVar(),
                            '{}Balance'.format(str.title(namelist[2])):tk.DoubleVar()}
        # Set default properties of AllowanceBot container
        self.nameofthechild=''
        self.endoftheyearflag=0
        self.currentbalanceoftheselectedchild=0
        self.fnc_setnameofthechild(namelist[0])
        self.fnc_setendoftheyearflag(0)
        self.fnc_setcurrentbalselectedchild(0)

        # Global so we can destroy and create ChildPage
        global container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
       
        # Create the Frames/Pages
        self.frames = {}
        for F in (StartPage, MenuPage, ChildPage, ResetPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location; the one on the top of the stacking order will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.fnc_showframe("StartPage")

    # Show the Frame/Pages desired with new Parameters
    def fnc_showframe(self, page_name, param1=None,param2=None):
        for frame in self.frames.values():
            frame.grid_remove()  
        frame = self.frames[page_name]
        # Show the Page!
        frame.grid()
        frame.tkraise()
        frame.update()

    # Destroys and reinitialises the Childpage
    def fnc_refreshChildPage(self):
        frame = self.frames['ChildPage']
        frame.destroy()
        frame = ChildPage(parent=container, controller=self)
        self.frames['ChildPage'] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.fnc_showframe("ChildPage")

    # Getters/setters of variables for AllowanceBot container
    def fnc_getlistofrows(self):
        return self.listofrows

    def fnc_setlistofrows(self,newlistofrows):
        self.listofrows = newlistofrows
   
    def fnc_getnameofthechild(self):
        return self.nameofthechild

    def fnc_setnameofthechild(self,newnameofthechild):
        self.nameofthechild = newnameofthechild
   
    def fnc_getendoftheyearflag(self):
        return self.endoftheyearflag

    def fnc_setendoftheyearflag(self,newendoftheyearflag):
        self.endoftheyearflag=newendoftheyearflag

    def fnc_getcurrentbalselectedchild(self):
        return self.currentbalanceoftheselectedchild

    def fnc_setcurrentbalselectedchild(self,newbalanceoftheselectedchild):
        self.currentbalanceoftheselectedchild=newbalanceoftheselectedchild

# class Page that contains the login 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#9FD745')
        self.controller = controller

        top_frame = Frame(self, bg="#408B20", height=33)

        # function to display time on the top of screeen
        def fnc_displaytime():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time, bg='#408B20', fg='white')
            time_label.after(200,fnc_displaytime)    
        time_label = tk.Label(top_frame,font=('orbitron',12))
        time_label.pack(side='right')

        fnc_displaytime()

        top_frame.pack(fill=X)
        top_frame.pack_propagate(0)
       
        head_frame = Frame(self, bg='white')

        self.photo = PhotoImage(file = r"images\logo1.png")
        heading_label = Label(head_frame, image = self.photo, borderwidth=0).pack(pady=(30,10))

        head_frame.pack(fill=X)

        label = tk.Label(self, text='Ranui Family', font=('calibri',22), fg='white', bg='#9FD745')
        label.pack(pady=(40,0))

        input_frame = Frame(self,bg='#9FD745')

        password_label = tk.Label(input_frame, text='Enter your password', font=('arial',11), bg='#9FD745', fg='white')
        password_label.grid(row=0, padx=75)
		
	# password entry box
        my_password = tk.StringVar()
        password_entry_box = tk.Entry(input_frame, textvariable=my_password, font=('arial',15), width=10)
        password_entry_box.focus_set()
        password_entry_box.grid(row=1, pady=10)

        def fnc_handlefocus(_):
            password_entry_box.configure(fg='black',show='*', justify=CENTER)
           
        password_entry_box.bind('<FocusIn>',fnc_handlefocus)

	# function to check the password
        def fnc_checkpassword():
           if my_password.get() == '1234':
               my_password.set('')
               incorrect_password_label['text']=''
               # Save the end of the year flag to Controller
               controller.fnc_setendoftheyearflag(endoftheyearflag.get())
               # Show the MenuPage
               controller.fnc_showframe('MenuPage')
           else:
               incorrect_password_label['text']='Incorrect Password\nPlease Try Again'
               
        self.loginphoto = PhotoImage(file=r"images\login.png")
        enter_button = tk.Button(input_frame, image=self.loginphoto, command=fnc_checkpassword, highlightthickness = 0, bd=0)
        enter_button.grid(row=3, column=0, pady=10)

        incorrect_password_label = tk.Label(input_frame, text='', font=('arial',10), fg='black', bg='#9FD745', anchor='n')
        incorrect_password_label.grid(row=4)
       
	# check button if its the end of year so that we can test the bonus. ideally this flag is not needed and should rely if current date is 31December
        def fnc_endyearflag(eoyflag):
            print('Checkbox-endoftheyearflag:')
            print(eoyflag.get())
           
        endoftheyearflag = IntVar(value=0)
        endyear_check = Checkbutton(input_frame, text="Today is 31 December", variable=endoftheyearflag, onvalue =1, offvalue =0, command=lambda: fnc_endyearflag(endoftheyearflag), selectcolor='#9FD745', bg='#9FD745', fg='white')   #, command=endyear
        endyear_check.grid(row=2)

        input_frame.pack(fill=BOTH,expand=True, padx=30)

# class use to call back the function triggered by the child buttons selection  
class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)

# class page that shows the Main Menu
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='white')
        self.controller = controller  
       
	# function to exit
        def fnc_exit():
            controller.fnc_showframe('StartPage')

        top_frame = Frame(self, bg="#408B20", height=33)

        # Creating a photoimage object to use image
        self.logoutimg = PhotoImage(file = r"images\logout.png")
        home_button = Button(top_frame, command=fnc_exit, image=self.logoutimg, bg="#408B20").pack(side = 'left', anchor=W)

	# function to display time on the top of screeen
        def fnc_displaytime():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time, bg='#408B20', fg='white')
            time_label.after(200,fnc_displaytime)    
        time_label = tk.Label(top_frame,font=('orbitron',12))
        time_label.pack(side='right')

        fnc_displaytime()

        top_frame.pack(fill=X)
        top_frame.pack_propagate(0)
       
        self.photo = PhotoImage(file = r"images\logo.png")
        heading_label = Label(self, image = self.photo, borderwidth=0)
        heading_label.pack(pady=(35,10))

        main_menu_label = tk.Label(self, text='Welcome Ranui Family!', font=('calibri',18), fg='black', bg='white')
        main_menu_label.pack()

        button_frame = tk.Frame(self,bg='#9FD745')

        selection_label = tk.Label(button_frame, text='Select an Account:', font=('calibri',15), fg='black', bg='#9FD745', anchor='n')
        selection_label.grid(row=0, pady=(20,0))

        # function to call Child page controller
        def fnc_childselected(childname):
            # Save the name of the child to the Controller
            controller.fnc_setnameofthechild(childname)
            # Refresh the ChildPage
            controller.fnc_refreshChildPage()
            controller.fnc_showframe('ChildPage')  # call common class named ChildPage
		
	# button to select 1st child  
        self.first_photo = PhotoImage(file=r"images\{}btn.png".format(namelist[0]))
        first_button = tk.Button(button_frame, image=self.first_photo, command=Callback(fnc_childselected, namelist[0]), highlightthickness = 0, bd=0)
        first_button.grid(row=1, column=0, pady=(20,10), padx=65)

        # button to select 2nd child  
        self.second_photo = PhotoImage(file=r"images\{}btn.png".format(namelist[1]))
        second_button = tk.Button(button_frame, image=self.second_photo, command=Callback(fnc_childselected,namelist[1]), highlightthickness = 0, bd=0)
        second_button.grid(row=2, column=0, pady=10)

        # button to select 3rd child  
        self.third_photo = PhotoImage(file=r"images\{}btn.png".format(namelist[2]))
        third_button = tk.Button(button_frame, image=self.third_photo, command=Callback(fnc_childselected,namelist[2]), highlightthickness = 0, bd=0)
        third_button.grid(row=3, column=0, pady=10)

        # function called by reset button
        def fnc_reset():
            controller.fnc_showframe('ResetPage')

        # button reset
        reset_button = tk.Button(button_frame, text='Reset All', command=fnc_reset, relief='flat', borderwidth=2, height=2, bg='black', fg='white')
        reset_button.grid(row=4, column=0, pady=8)
        button_frame.pack(fill='both',expand=True)
        button_frame.pack_propagate(0)

# class page to Reset
class ResetPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='white')
        self.controller = controller
        self.var_feedback = tk.StringVar()

	# function to call menu controller 
        def fnc_menu():
            controller.fnc_showframe('MenuPage')
     
        top_frame = Frame(self, bg="#408B20", height=33)

        # Creating a photoimage object to use image
        self.homeimg = PhotoImage(file = r"images\home.png")
        home_button = Button(top_frame, command=fnc_menu, image=self.homeimg, bg="#408B20").pack(side = 'left', anchor=W)

        # function to display time on the top of screeen
        def fnc_displaytime():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time, bg='#408B20', fg='white')
            time_label.after(200,fnc_displaytime)    
        time_label = tk.Label(top_frame,font=('orbitron',12))
        time_label.pack(side='right')
        fnc_displaytime()

        top_frame.pack(fill=X)
        top_frame.pack_propagate(0)

        self.photo = PhotoImage(file = r"images\logo.png")
        heading_label = Label(self, image = self.photo, borderwidth=0)
        heading_label.pack(pady=(35,10))
       
        confirm_reset_label = tk.Label(self, text="Are you sure you would like\nto reset all the saved data of all accounts?\nThis action CANNOT be undone.",
                                       font=('arial',13), fg='#408B20', bg='white', anchor='n')
        confirm_reset_label.pack(fill='x')

        button_frame = tk.Frame(self,bg='white')
        button_frame.pack(fill='both',expand=True)
       
        # function to reset data
        def fnc_resetdata():
            for child in namelist:
                open('data/{}.txt'.format(child), 'w').close() # deletes everything in file
                with open('data/childtemplate.txt','r') as firstfile, open('data/{}.txt'.format(child),'a') as secondfile:
                    if os.stat('data/{}.txt'.format(child)).st_size == 0: # checks if file is now empty
                        for line in firstfile:
                                secondfile.write(line) # write content to second file
            self.var_feedback.set("Successfully reset all accounts!") # feedback to user that they have reset the file
       
        # function to reset data
        def fnc_no_resetdata():
            self.var_feedback.set("Did not reset all accounts")
            
        # button no reset
        no_reset_button = tk.Button(button_frame, command=fnc_no_resetdata, text='No', relief='raised', borderwidth=3, height=2, width=20)
        no_reset_button.grid(row=0,column=0,pady=20, padx=12)
        # button reset
        reset_button = tk.Button(button_frame, command=fnc_resetdata, text='Yes', relief='raised', borderwidth=3, height=2, bg='#9FD745', width=20)
        reset_button.grid(row=0,column=1,pady=20, padx=12)
       
        # set the feedback text to nothing to start with except a new line
        # this keeps spacing constant for messages that will come up later that take up two lines
        self.var_feedback.set("")        
        label_feedback = tk.Label(button_frame, textvariable = self.var_feedback, fg='#408B20', bg='white')
        label_feedback.grid(row=1, columnspan=2)
       
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(fill='x',side='bottom')

# class page to Child
class ChildPage(tk.Frame): # class for child page (only one page for all three kids instead of repetitive code)
    def __init__(self, parent, controller, attr=1):
        tk.Frame.__init__(self, parent,bg='white')
        self.controller = controller
        # set initial values
        endyearflag = controller.fnc_getendoftheyearflag()
        child = controller.fnc_getnameofthechild()
        name = child.capitalize() # capitalises the first letter of the name
        allowed_alpha = string.ascii_letters + string.whitespace + '-'
        now_balance = 0
        # Reset the new balance to the Controller
        controller.fnc_setcurrentbalselectedchild(now_balance)

	# function to retrieve data 
        def fnc_retrievedata(current_balance):
            # Create a dataframe from csv
            df = pd.read_csv('data/{}.txt'.format(child), delimiter=',')
            # User list comprehension to create a list of lists from Dataframe rows
            list_of_rows = [list(row) for row in df.values]
            disp_list_of_rows = []
            controller.fnc_setlistofrows(disp_list_of_rows)
            for line in list_of_rows:
                disp_balance = str("${:.2f}".format(line[0]))
                disp_amount = str("${:.2f}".format(line[1]))
                disp_line = [disp_balance, disp_amount, line[2], line[3]]
                disp_list_of_rows.append(disp_line)
            disp_list_of_rows.reverse()
            controller.fnc_setlistofrows(disp_list_of_rows)
            recent_data = list_of_rows[-1]
            current_balance = recent_data[0]
            controller.shared_data['{}Balance'.format(name)].set("${:.2f}".format(current_balance))

            return(current_balance)

        now_balance  = fnc_retrievedata(now_balance)
        # Save the new balance to the Controller
        controller.fnc_setcurrentbalselectedchild(now_balance)
           
        # function to call menu controller 
        def fnc_menu():
            controller.fnc_showframe('MenuPage', endyearflag)
     
        top_frame = Frame(self, bg="#408B20", height=33)

        # Creating a photoimage object to use image
        self.homeimg = PhotoImage(file = r"images\home.png")
        home_button = Button(top_frame, command=fnc_menu, image=self.homeimg, bg="#408B20").pack(side = 'left', anchor=W)

        # function to display time on the top of screeen
        def fnc_displaytime():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time, bg='#408B20', fg='white')
            time_label.after(200,fnc_displaytime)    
        time_label = tk.Label(top_frame,font=('orbitron',12))
        time_label.pack(side='right')

        fnc_displaytime()

        top_frame.pack(fill=X)
        top_frame.pack_propagate(0)
       
        self.photo = PhotoImage(file = r"images\logo2.png")
        heading_label = Label(self, image = self.photo, borderwidth=0)
        heading_label.pack(pady=(25,0))
        welcome_label = tk.Label(self,text='{} Ranui'.format(name),font=('arial block',18),fg='#408B20',bg='white')
        welcome_label.pack()
       
        balance_label = tk.Label(self, text="Balance: ", font=('arial', 10), fg='#408B20', bg='white').pack()
       
        balancenum_label = tk.Label(self, textvariable=controller.shared_data['{}Balance'.format(name)], font=('arial block',15), fg='#408B20', bg='white', anchor='n')
        balancenum_label.pack(fill='x')

        bonus = tk.StringVar()
        mid_frame = tk.Frame(self, bg='#408B20')
        mid_frame.pack(fill='x')
        mid_frame.pack_propagate(0)

        bonus_feedback = tk.StringVar()
        bonus_feedback.set("\n")

        # function to call no bonus message
        def fnc_nobcreateframe():
            mid_frame.config(bg="#FFB65E")
            bonus_feedback.set('You have less than $50 left over this year\nUnfortunately you did not receive a bonus')
            nobonus_label = tk.Label(mid_frame, textvariable=bonus_feedback, fg='black', bg='#FFB65E')
            nobonus_label.grid(row=0, column=0, padx=60)

        # function to call check bonus
        def fnc_checkbonus():
            current_balance = controller.fnc_getcurrentbalselectedchild()
            if endyearflag == 1 and current_balance >= 50:
                mid_frame.config(bg="#B591C2")
                bonus_feedback.set('Congratulations {}\nEnter your chosen bonus activity'.format(name))
               
                # UI elements are create here
                bonus_label = tk.Label(mid_frame, textvariable=bonus_feedback, fg='white', bg='#B591C2')
                bonus_label.grid(row=0, column=0)

                bonus_enter = tk.Entry(mid_frame, textvariable=bonus)
                bonus_enter.grid(row=0, column=1, padx=(20,10))

                bonusactivity_label = tk.Label(mid_frame, text="", fg='white', bg='#B591C2')
                bonusactivity_label.grid(row=1, column=0, columnspan = 2, pady=3)

		# funciton to get child bonus 
                def fnc_childbonus():
                    bonusactivity = bonus.get()
                    bonusactivity_label["text"] = "Your bonus is: {}".format(bonusactivity)
                
		# button for bonus   
                bonus_enter_button = tk.Button(mid_frame, text='->', command=fnc_childbonus, fg='white', bg='#532C61')
                bonus_enter_button.grid(row=0, column=2)
                   
            elif endyearflag == 1 and current_balance < 50:
                fnc_nobcreateframe()
               
            else:
                bonus_feedback.set('Whoops! It is not yet the end of the year!')
                feedback = tk.Label(mid_frame, textvariable=bonus_feedback, fg='white', bg='#408B20')
                feedback.grid(row=0, column=1)

        # button to check bonus
        self.bonusbtn = PhotoImage(file = r"images\bonusbtn.png")
        buttonbonus = tk.Button(mid_frame, image = self.bonusbtn, command=fnc_checkbonus, highlightthickness = 0, bd=0)
        buttonbonus.grid(row=0, column=0)
               
        enter_frame = tk.Frame(self,bg='#9FD745')
        enter_frame.pack(fill=X)

        amt = tk.DoubleVar()
        item = tk.StringVar()
        date = tk.StringVar()

        fnc_spendamount_label = Label(enter_frame, text="Enter Amount:", bg="#9FD745", fg="black").grid(row=3, column=0, padx=(50,50))
        fnc_spendamount_entry_label = Label(enter_frame, text="$", bg="#9FD745", fg="black").grid(row=3, column=0, padx=(180,0))
        fnc_spendamount_entry = tk.Entry(enter_frame, textvariable=amt, width=20, justify='left')
        fnc_spendamount_entry.grid(row=3,column=1,pady=5,ipady=2)
        amt.set('0.00')

        fnc_spenditem_label = Label(enter_frame, text="Enter Clothing Item:", bg="#9FD745", fg="black").grid(row=4, column=0, padx=(30,0))
       
        item_entry = tk.Entry(enter_frame, textvariable=item, width=20, justify='left')
        item_entry.grid(row=4,column=1,pady=5,ipady=2)
        item.set(' ')

        fnc_spenddate_label = Label(enter_frame, text="Enter Date:", bg="#9FD745", fg="black").grid(row=5, column=0, padx=(0,20))
       

        date_entry = DateEntry(enter_frame, locale='en_NZ', date_pattern='dd/mm/y', textvariable=date, width=17, background='#408B20',
                              foreground='white', justify='left', borderwidth=2)
        date_entry.grid(row=5, column=1, pady=5,ipady=2)

        # create variable and label for feedback - held in frame_right
        self.var_feedback = tk.StringVar()
        # set the feedback text to nothing to start with except a new line
        # this keeps spacing constant for messages that will come up later that take up two lines
        self.var_feedback.set(" ")        
        label_feedback = tk.Label(enter_frame, textvariable = self.var_feedback,bg='#9FD745')
        label_feedback.grid(row=7, column=0, pady=5, ipady=4, columnspan=2, padx=(50,0))
       
        # function to write the spend amount to database file (text file)
        def fnc_spendcheck(current_balance, datee, spend_amt, clothing_itm):
            print('possible spend current_balance {}'.format(current_balance))
            new_data = '"{}","{}","{}","{}"'.format(current_balance, spend_amt, datee, clothing_itm)
            f = open('data/{}.txt'.format(child), 'a') #open the text file of the child who has their page currently open
            # export data into text file
            f.write('\n{}'.format(new_data))
            f.close()
            last_balance=fnc_retrievedata(current_balance)

        # function to check spend amount
        def fnc_spendamount(current_balance, datee, clothing_itm):
            current_balance_float = current_balance # declare value so that it returns at the end eventhough string entered
            try:
                spend_amt = round(float(amt.get()),2)
                print(spend_amt)
                # Convert spend_amt, current_balance into local float variable
                spend_amt_float = float(spend_amt)
                current_balance_float = float(current_balance)
                if 0 < spend_amt_float <= current_balance_float:
                    current_balance_float -= spend_amt_float
                    spend_amt = str("{:.2f}".format(spend_amt)) #make to string so it always has 2dp, even if 2 zeros
                    self.var_feedback.set('You spent ${}'.format(spend_amt))
                    fnc_spendcheck(current_balance_float, datee, spend_amt, clothing_itm)
                elif spend_amt_float  > current_balance_float:
                    self.var_feedback.set('Please make sure you have enough money left')
                else:
                    self.var_feedback.set('Please enter an amount greater than 0')
                    controller.shared_data['{}Balance'.format(name)].set("${:.2f}".format(current_balance_float))
            except Exception as error:                
                self.var_feedback.set('Please enter a numerical amount')
            amt.set('0.00')
            # Whatever happens, return the current_balance_float
            return(current_balance_float)

        # function to spend item
        def fnc_spenditem(current_balance, datee):
            try:
                clothing_itm = str(item.get().title())
                if(not (clothing_itm and not clothing_itm.isspace())):
                    self.var_feedback.set('Please enter the clothing item you bought')
                elif all(c in allowed_alpha for c in clothing_itm):
                    current_balance = fnc_spendamount(current_balance, datee, clothing_itm) #encapsulate new current_balance after spending
            except:
                self.var_feedback.set('Please enter a valid clothing item')
            item.set(' ') # after spends successfully it will clear entry box automatically
            # Whatever happens, return the current_balance_float
            return(current_balance)        
           
        # function to check spend date
        def fnc_spenddate(current_balance):
            datee = str(date.get())
            get_year = datetime.strptime(date.get(),'%d/%m/%Y')
            spend_year = get_year.year
            thisyear = datetime.now().year
            if spend_year == thisyear:
                current_balance = fnc_spenditem(current_balance, datee) # calls second spend function which is the spend item
            else:
                self.var_feedback.set('Please enter a date from this year')
            # Always return the current_balance_float
            return(current_balance)

        # function triggered by spend button to update the spending list
        def fnc_spendbtn(current_balance): # function called when spend button clicked
            current_balance = controller.fnc_getcurrentbalselectedchild()
            current_balance = fnc_spenddate(current_balance) # calls first spend function which is the date
            listbox.pack(pady=5)
            my_list = controller.fnc_getlistofrows()
            for dxy in listbox.get_children():
                listbox.delete(dxy)
            for xy in my_list:
                listbox.insert('', tk.END,values=xy)
            # Save the new balance to the Controller
            controller.fnc_setcurrentbalselectedchild(current_balance)
            return(current_balance)
        # sets now_balance variable to what current balance is for selected child to hold the value in the button
        now_balance = controller.fnc_getcurrentbalselectedchild()
        
	# button for spend
        self.spendbtn = PhotoImage(file = r"images\spendbtn.png")
        spend_button = tk.Button(enter_frame, image=self.spendbtn, command=Callback(fnc_spendbtn, now_balance), highlightthickness = 0, bd=0)
        spend_button.grid(row=6, column=0, pady=5, columnspan=2, padx=(47,0))
        
        # Create frame and scrollbar for past spendings
        purchases_frame = tk.Frame(self, bg='#408B20')
        listbox = ttk.Treeview(purchases_frame, column=("#1","#2","#3","#4"), show='headings', height=5)
        listbox.column("#1", anchor=CENTER, stretch=NO, width=75)
        listbox.heading("#1", text='Balance')
        listbox.column("#2", anchor=CENTER, stretch=NO, width=85)
        listbox.heading("#2", text='Amount Spent')
        listbox.column("#3", anchor=CENTER, stretch=NO, width=80)
        listbox.heading("#3", text='Date')
        listbox.column("#4", anchor=W, stretch=YES, width=120)
        listbox.heading("#4", text='Item')
        my_scrollbar = Scrollbar(purchases_frame, orient=VERTICAL)
        my_scrollbar.config(command=listbox.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        fnc_spendbtn(now_balance) # so that listbox displays, even without spending any money yet
        purchases_frame.pack()
# ## main script ## #
if __name__ == "__main__":  
    namelist = ["nikau", "hana", "tia"] # list of all kids names
    for child in namelist:
        with open('data/childtemplate.txt','r') as firstfile, open('data/{}.txt'.format(child),'a') as secondfile:
            print("size of {}'s file {}".format(child, os.stat('data/{}.txt'.format(child)).st_size)) # debugging purposes
            if os.stat('data/{}.txt'.format(child)).st_size == 0: # check if text file is empty
                for line in firstfile:
                        secondfile.write(line) # write content to second file if found empty      
    app = AllowanceBot()
    app.title('Ranui Family AllowanceBot')
    app.geometry('{}x{}'.format(355, 600))
    app.mainloop()
