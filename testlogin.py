class main:
    def __init__(self,master): 
  
        self.master = master
        
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_reg=StringVar()
        self.n_mobile=StringVar()
        self.mobile11=StringVar()
        self.widgets()


    
    def login(self):
  
        with sqlite3.connect('Akash5.db') as db:
            c = db.cursor()


        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        
        if result:
            self.track()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    
        
        with sqlite3.connect('Akash5.db') as db:
            c = db.cursor()
        if self.n_username.get()!=' ' and self.n_password.get()!=' ' and self.n_mobile.get()!=' ':
            find_user = ('SELECT * FROM user WHERE username = ?')
            c.execute(find_user,[(self.n_username.get())])        

            if c.fetchall():
                    ms.showerror('Error!','Username Taken Try a Diffrent One.')
            else:
                    insert = 'INSERT INTO user(username,password,mobile) VALUES(?,?,?)'
                    c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.n_mobile.get())])
                    db.commit()

                    ms.showinfo('Success!','Account Created!')
                    self.log()
        else:
             ms.showerror('Error!','Please Enter the details.')