from datetime import datetime
user_data=[]
home_det=[]
veri_status=[]
verified_homes_list=[]
time_list=[]
class User :
    def __init__(self,userid=None,username=None,password=None,phone=None,mail=None,city=None,gender=None,role=None):
        
        self._userid=userid
        self.username=username
        self.__password=password
        self.phone=phone
        self.mail=mail
        self.city=city
        self.gender=gender
        self.role=role
        
    def hardcoded_data(self):
        user_data.append(users)
        #return user_data
        
    def validate_user(self,mail,password):
        for user in user_data:
            if (user.mail==mail and user.__password==password):
                return user
    def welcome(self):
        print("Successfull login!")
        print("Welcome",current_login.username+'!')
        print()

class Home_det(User):
    def __init__(self,home_detid=None,htype=None,rent=None,sq_feet=None,locality=None,city=None,userid=None):
        super().__init__(userid)
        self.home_detid=home_detid
        self.htype=htype
        self.rent=rent
        self.sq_feet=sq_feet
        self.locality=locality
        self.city=city
        
    def hardcoded_data(self):
        home_det.append(self)

    def add_home(self):
        hadd=Home_det(4,'3BHK','19,000/Month',2000,'Naavalur','chennai',2)
        home_det.append(hadd)
        print("Successfully added")

    def delete_home(self):
        delete_home=input("Enter home locality to delete : ")
        for i in home_det:
            if current_login._userid == i._userid:
                if delete_home==i.locality:
                    home_det.remove(i)
                    print("Removed")

class Verifiedhome(Home_det):
    def __init__(self,verify_hid=None,home_detid=None,status=None):
        super().__init__(home_detid)
        self.verify_hid=verify_hid
        self.status=status
        #self.veri_id=[]

    def add_status(self):
        print('--------------')
        a=Verifiedhome(1,1,'approved')
        veri_status.append(a)
        a=Verifiedhome(2,2,'approved')
        veri_status.append(a)
        a=Verifiedhome(3,3,'rejected')
        veri_status.append(a)
        a=Verifiedhome(4,4,'approved')
        veri_status.append(a)
        
        self.verified_homes()

    def verified_homes(self):
        for i in veri_status:
            for j in home_det:
                if i.home_detid == j.home_detid and i.status=='approved' :
                    verified_homes_list.append(i.verify_hid)
                    verified_homes_list.append(j)
        #print(verified_homes_list)
        self.display_verified_homes()
        

    def display_verified_homes(self):
        i=0
        while i<len(verified_homes_list):
            print("Verified home_id :",verified_homes_list[i])
            i+=1
            if i<len(verified_homes_list):
                print("Home type :",verified_homes_list[i].htype)
                print("Monthly Rent :",verified_homes_list[i].rent)
                print("Square feet :",verified_homes_list[i].sq_feet)
                print("Locality :",verified_homes_list[i].locality)
                print("Home city :",verified_homes_list[i].city)
                print("Owner id :",verified_homes_list[i]._userid)
            i+=1
            print('-------------------------------------------')

class Request(Verifiedhome):
    def __init__(self,verify_hid,Request_id,status):
        super().__init__(verify_hid)
        self.Request_id=Request_id
        self.status=status
    def approval(self):
        if self.status=='approved':
            print("Thanks for booking our home!")
            print("You may proceed to pay!")
            pay=Payment(1)
        
        else:
            print("Your request is rejected!")

class Payment:
    def __init__(self,paymentid,Request_id=None,card_no=None,cvv=None,exp_date=None):
        self.paymentid=paymentid
        self.a=input("Enter Payment method(card/cash) :")
        if self.a=='card':
            self.card_det()
        elif self.a=='cash':
            print("Payment Successfull!")
            print("Happy home!")
            time_list.append(self.paymentid)
            self.time()
    def card_det(self):
        self.card_no=int(input("Enter your card no : "))
        self.cvv=int(input("Enter your cvv : "))
        self.exp=input("Enter exp date(yy/mm) : ")
        print("Payment Successfull!")
        print("Happy home!")
        time_list.append(self.paymentid)
        self.time()
    def time(self):
        now=datetime.now()
        time=now.strftime('%y %m %d %H:%M:%S')
        time_list.append(time)
        
        
        
        
class History:
    def __init__(self,history_id,username=None):
        self.history_id=history_id

    def show_history(self):
        time_list.append(current_login.username)
        
        self.print_his()
    def print_his(self):
        print(time_list)


class Advertisement:
    def __init__(self,ad_id=None,ad_len=None,freq=None,verify_hid=None):
        self.ad_id=ad_id
        self.ad_len=ad_len
        self.freq=freq
        self.verify_hid=verify_hid
    def ad_det(self):
        advertisement=Advertisement(5,10,3,1)
        for i in verified_homes_list:
            if i==advertisement.verify_hid:
                print()
                print('ad_id ',advertisement.ad_id)
                print('ad_len ',advertisement.ad_len)
                print('freq',advertisement.freq)
                print('verify_hid',advertisement.verify_hid)

                print("Your add will be telecast!")
                
        
        
        

       
        
        
if __name__=='__main__':
    users=User(1,'Mohitha',1234,3754762357,'mohitha@gmail.com','chennai','female','owner')
    users.hardcoded_data()
    users=User(2,'priya',4333,2763562,'priya@gmail.com','chennai','female','tenent')
    users.hardcoded_data()
    users=User(3,'Vicky',1233,8973827,'vicky@gmail.com','goa','male','owner')
    users.hardcoded_data()
    current_login=users.validate_user('vicky@gmail.com',1233)
    
    users.welcome()
    h=Home_det(1,'2BHK','12,000/Month',1200,'Scholinganallor','chennai',1)
    h.hardcoded_data()
    h=Home_det(2,'3BHK','25,000/Month',4000,'sathy','Erode',2)
    h.hardcoded_data()
    h=Home_det(3,'4BHK','50,000/Month',5000,'Meenakshipuram','madurai',3)
    h.hardcoded_data()
    if current_login.role=='owner':
        choice=input("Enter your choice(add/remove) : ")
        if choice=='add':
            h.add_home()
        elif choice=='remove':
            h.delete_home()
        

    homes=input("Do you want to see the homes list(y/n) : ")
    
    if homes=='y':
        v=Verifiedhome()
        v.add_status()
        if current_login.role=='tenent':
            home_id=int(input("Enter your selected home id for request : "))
            for i in verified_homes_list:
                if home_id==i:
                    r=Request(1,4,'approved')
                    r.approval()
            his=input("Do you want to see the history(y/n) : ")
            if his=='y':
                h=History(10)
                h.show_history()
    if current_login.role=='owner':
        ad=input("do you want to show ad's(y/n) : ")
        if ad=='y':
            adv=Advertisement()
            adv.ad_det()
                
    elif  homes=='n':
        exit(0)
    
    
        
        

            
            
            
          
