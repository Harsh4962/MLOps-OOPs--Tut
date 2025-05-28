class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()



    def menu(self):
        user_input = input(""" Welcome to chatbook !! How would you like to proceed ?
                        1) Press 1 to sign-up
                        2) Press 2 to sign-in
                        3) Press 3 to write a post
                        4) Press 4 to message a friend
                        5) Press any other key to exit
                        ---> """)
        if (user_input == "1") :
            self.signup()
        elif (user_input == "2") :
            self.signin()
        elif (user_input == "3") :
            self.my_post()
        elif (user_input == "4") :
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Enter your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed-up successfully !! \n")
        self.menu()

    def signin(self):
        if(self.username == '' and self.password == ''):
            print("Please sign-up first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if(self.username == uname and self.password == pwd):
                print("You have signed-in successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials ...\n")

        self.menu()

    def my_post(self):
        if(self.loggedin == True):
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to sign-in first to post something ...\n")

        self.menu()
    
    def send_msg(self):
        if(self.loggedin == True):
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send your message ? -> ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to sign-in first to send a message ...\n")

        self.menu()
            
            


obj = chatbook()