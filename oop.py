# oop.py
# create a class with just few attributes (1)
class Book:
    title = ""          # as a string placeholder
    author = ""
    pages=0             # as an integer placeholder

# use the class to create an object
book1=Book() # now we have a copy of the class Book

# set the attributes of the object....
book1.title="origin"
book1.author="dan brown"
book1.pages=542

# if we want to access the attributes of the object we can do it like this
# name of the object then . the attribute we want to access
print(book1.title) # origin
print(book1.author) # dan brown
print(f"pages: {book1.pages}") # if we want to type something.

# another object of the class Book
book2=Book()
book2.title="Dark whole"
book2.author="Nourhan Younis"
book2.pages=300
print(f"\nTitle: {book2.title}, Author: {book2.author}, Pages: {book2.pages}")

# third object of the class Book
book3=Book()
book3.title="into the water"
book3.author="jack finney"
book3.pages=455
print(book3.title)

# creat a class with attributes and method (2)
class Book:
# def init to send the object itself not anyothere objects and send the name of it with attributes
    def __init__(self,title,author,pages): # the method and init to praper it.
        self.title= title  
        self.author= author
        self.pages= pages
# the object (first_book) and the attribute (title) and = the argument ("Red Eyes")

# instead of whrightin many lines this is easier way.. 
first_book=Book("Red Eyes","Nourhan",470) # in order to goes step by step to enter the data and not forget it.
second_book=Book("dark world","jack",600)
third_book=Book("great things","younis",437)
# print from the data
print(f"the first book title is: {first_book.title}")
print(f"the second book title is: {second_book.title}")
print(f"the third book title is: {third_book.title}")

# another exampel
class Cars:
    def __init__(self,model,speed,color):
        self.model=model
        self.speed=speed
        self.color=color
# now use the class to make objects
BMW=Cars("X7",280,"black")
honda=Cars("DS67",300,"gray")
tyota=Cars("Tyota V3",450,"white")
# acses to the data
print(f"BMW model: {BMW.model}\nHonda model: {honda.model}\nTyota model: {tyota.model}")

# my homework..........>
# project 1
class Profile:
    def __init__(self,name,email,language):
        self.name=name
        self.email=email
        self.language=language

profile_1=Profile("nour ali","nourblack@gmail.com","english language")
profile_2=Profile("malik ahmed","malikso@gmail.com","french language")
profile_3=Profile("sara ali","saratota212@gmail.com","german language")
print(profile_1.name, profile_1.email, profile_1.language)

# project 2
class Telegram:
    def __init__(self,sender_name,futur_name,content_massage,sent_date):
        self.sender_name=sender_name
        self.futur_name=futur_name
        self.content_massage=content_massage
        self.sent_date=sent_date

message1=Telegram("ali moomen","nour younis","hey nour how are you","2026/9/17")
message2=Telegram("khalid ashraf","yousif ashraf","come home soon","2026/9/18")
message3=Telegram("omnia yehya","amira moustafa","where is my hat?","2026/9/17")
print(message1.sent_date)
print(message3.content_massage)

# project 3
class Amazon:
    def __init__(self,name_product,price,descript,evaluation):
        self.name_product=name_product
        self.price=price
        self.descript=descript
        self.evaluation=evaluation
product_1=Amazon("Dress",700,"black drees with yellow flowers","7/10")
profile_2=Amazon("Hat",300,"greet hat for beach","6/10")
profile_3=Amazon("T-Shirt",400,"blue T-Shirt for sport","9/10")
print(profile_3.name_product,profile_3.price)

# class with many methods (3)..
class Task:
    def __init__(self,title,description,due_date,status):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status=status  
    def dispaly_task(self): # smart way as shorcut.
        print(f"title: {self.title}\ndescription: {self.description}\ndue date: {self.due_date}")
        print(f"status: {self.status}\n")
    def mark_as_complete(self):
        self.status="complete" # to replace the argument

task1=Task("review syntax","review how to creat a class","2026-9-20","incomplete")
task2=Task("honda car","buy a new honda car","2030-1-20","incomplete")
# shoud call the name of function that i've made to print objects.
task1.dispaly_task()
task2.dispaly_task()
# now call mark_as_complete method to change the status
task1.mark_as_complete()
# now i need to recall the object again to display it with the change.
task1.dispaly_task() # now gonna show it with the change..

# homework changing diffrent argument (4)...>
print("_________Movies list_________\n")
class Movies:
    def __init__(self,title,director,release_year,genre):
        self.title=title
        self.director=director
        self.release_year=release_year
        self.genre=genre
    def display(self):
        print(f"title: {self.title}\ndirector: {self.director}")
        print(f"release year: {self.release_year}\ngenre: {self.genre}\n")

mavie1=Movies("inception","christpher nolan","2010","sci-fi")
mavie2=Movies("the godfather","francis ford","1972","crime")
mavie3=Movies("parasite","bong joon-ho","2019","thriller")
# now show them
mavie1.display()
mavie2.display()
mavie3.display()
print("\n\nchanging movie directors ...\n\n")
mavie1.director="Nourhan Younis"
mavie2.director="Malik Ahmed"
mavie3.director="Moustaf Yousif"
mavie1.display()
mavie2.display()
mavie3.display()

# class with return and defult value (5).....>
class Acount:
    def __init__(self,name,email,password,status="inactive"):
        self.name=name
        self.email=email
        self.password=password
        self.status=status

def creat_user(): # this for taking input from the user & shoud have same attributes.
    name=input("enter your name: ")
    email=input("enter your email: ")
    password=input("enter your password: ")
    return Acount(name,email,password) # after making same attributes return in the class those attributes.

user1=creat_user()
print(user1.email)

# a project on it
# register an order
class Product:
    def __init__(self,name_product,price,quantity,category="general"):
        self.name_product=name_product
        self.price=price
        self.quantity=quantity
        self.category=category

def creat_product():
    print("to register an order you need to follow these steps...")
    name_product=input("enter your chosen product: ")
    price=float(input("enter the price of th product: "))
    quantity=int(input("enter the quantity: "))
    return Product(name_product,price,quantity)

item1= creat_product()

print(f"""
your order has been submitted...
details of the order:
name product: {item1.name_product}
category: {item1.category}
total: ${item1.price * item1.quantity}
""")

# class with while loop (6)......>
class User:
    def __init__(self, first_name, last_name, email, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status

    def display_user(self):
        print(f"first_name: {self.first_name}\nlast_name: {self.last_name}\nemail: {self.email}\nstatus: {self.status}\n" + "-"*25)


# القائمة برة الـ while عشان تفضل محتفظة بالبيانات وما تتصفّرش
user_list = []

while True:
    ask = int(input("\nwelcome to user management\nchoose an action:\n1. Add new user\n2. Display all users\n3. Exit\nenter your choice: "))

    if ask == 1:
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        email = input("enter your email: ")
        new_user = User(first_name, last_name, email)
        
        user_list.append(new_user)
        print("\nUser added successfully!")

    elif ask == 2:
        if len(user_list) == 0:
            print("\nNo users found in the list!")
        else:
            print("\nDisplaying all users..\n")
            for z in user_list:
                z.display_user()  # ✅ ملحوظة: تصحيح حرف הـ i بدل e (display_user)

    elif ask == 3:
        print("\nGoodbye!")
        break  # الخروج من الـ loop وإغلاق البرنامج


# class with while loop (7)......> 
# car management system
print("Welcome to car management system\n")
class Car:
    def __init__(self,model,brand,year,price,status="available"):
        self.model=model
        self.brand=brand
        self.year=year
        self.price=price
        self.status=status

ask= int(input("Choose an action:\n1. Add a new car\n2. Display all cars\n3. Exit\nEnter your choice: "))
car_list = []

while ask != 3:
    if ask==1:
        model=input("Enter the car model: ")
        brand=input("Enter the car brand: ")
        year=int(input("Enter the car year: "))
        price=float(input("Enter the car price: "))
        
        car=Car(model,brand,year,price)
        car_list.append(car)
        print("Car added successfully!\n")
    elif ask==2:
        print("\nDisplaying all cars...\n")
        if not car_list:
            print("No cars found yet!\n")
        else:
            for car in car_list:
                print(f"Model: {car.model}\nBrand: {car.brand}\nYear: {car.year}\nPrice: ${car.price}\nStatus: {car.status}\n" + "-"*30)
    else:
        print("Invalid choice! Please try again.\n")
    ask= int(input("Choose an action:\n1. Add a new car\n2. Display all cars\n3. Exit\nEnter your choice: "))

print("Thank you for using the car management system. Goodbye!")
exit()

# Class drinks management system (8)......>
print ("Welcome to management system")
class Drinks:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

drinks_list = []
ask = int(input("Choose an action:\n1. Add a new drink\n2. Display all drinks\n3. Exit\nEnter your choice: "))

while ask !=3:
    if ask==1:
        name=input("\nenter the drink name: ")
        price=float(input("enter the drink price: "))
        quantity=int(input("enter the drink quantity: "))
        drink=Drinks(name,price,quantity)
        drinks_list.append(drink)
        print("\nDrink added successfully!\n")
    elif ask==2:
        print("\nDisplaying all drinks...\n")
        if not drinks_list:
            print("No drinks found yet!\n")
        else:
            for d in drinks_list:
                print("_"*25 +f"\ndrink name: {d.name}\nprice: ${d.price}\nquantity: {d.quantity}\ntotal: ${d.price * d.quantity:.2f}\n" + "_"*25)
    else:
        print("Invalid choice, please try again.\n")
    ask = int(input("Choose an action:\n1. Add a new drink\n2. Display all drinks\n3. Exit\nEnter your choice: "))

print("Exiting program. Goodbye!")

# class in advanced way (9)......>
import os
import time
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class User:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Status: {self.status}")
        print("-"*30)

def create_user():
    first_name=input("Enter First Name: ")
    last_name=input("Enter Last Name: ")
    email=input("Enter Email: ")
    password=input("Enter Password: ")
    return User(first_name,last_name,email,password)

users_list=[]
while True:
    print("User Management System")
    print("1. Create User")
    print("2. Display Users")
    print("3. Exit\n")
    choice=input("Enter your choice: ")
    if choice=="1":
        users_list.append(create_user())
        print("\nUser created successfully!\n")
        time.sleep(2)
    elif choice=="2":
        clear_screen()
        if users_list:
            print("\nDisplaying  all Users.....\n")
            time.sleep(1)
            for user in users_list:
                user.display_info()
            time.sleep(2)
        else:
            print("Sorry, no users found to display.\n")
            time.sleep(2)
    elif choice=="3":
        print("Exiting....")
        time.sleep(3)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(1)

# My own project on it
import os
import time
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Car:
    def __init__(self,name,model,year,color,status="Available"):
        self.name=name
        self.model=model
        self.year=year
        self.color=color
        self.status=status
    def display_cars(self):
        print(f"\nCar Name: {self.name}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        print(f"Car Color: {self.color}")
        print(f"Car Status: {self.status}")
        print("-"*30)

def create_car():
    name=input("Enter the Car Name: ")
    model=input("Enter the Car Model: ")
    year=int(input("Enter the Car Year: "))
    color=input("Enter the Car Color: ")
    return Car(name,model,year,color)

cars_list=[]
while True:
    print("*** Car Management System ***")
    print("1. Create Car")
    print("2. Display Cars")
    print("3. Exit\n")
    choice=input("Enter your choice: ")
    if choice =="1":
        cars_list.append(create_car())
        print("\nCar created successfully!\n")
        time.sleep(2)
    elif choice=="2":
        clear_screen()
        if cars_list:
            print("\nDisplaying all Cars.....\n")
            time.sleep(1)
            for car in cars_list:
                car.display_cars()
            time.sleep(1)
        else:
            print("Sorry, no cars found to display.\n")
            time.sleep(1)
    elif choice=="3":
        print("Exiting....")
        time.sleep(3)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(1)

# # class in advanced way (10)......>
import os
import time

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Member:
    def __init__(self,first_name,last_name,id,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.status=status
    def display(self):
        print(f"""
First Name: {self.first_name}
Last Name: {self.last_name}
Membership ID: {self.id}
Membership Status: {self.status}
        """)
        print("_"*30)

def create_member():
    clear_screen()
    first_name=input("Enter the first name: ")
    last_name=input("Enter the last name: ")
    id=input("Enter the ID: ")
    status=input("Enter membership status or click Enter: ")
    if not status:
        status="inactive"
    return Member(first_name,last_name,id,status)

members_list=[]

# making a funcation to search for a member.....
def search_member(members_list):
    print("\nSearch by: ")
    print("""
1. Membership ID
2. First Name
3. Membership Status
    """)
    search_choice=int(input("Enter your choice: "))
    found_member=[]

    if search_choice==1:
        search_id=input("Enter the membership ID to search: ")
        for x in members_list:
            if x.id == search_id:
                found_member.append(x)
                break
    elif search_choice==2:
        first_name=input("Enter the first name to srarch: ").lower()
        for v in members_list:
            if v.first_name.lower() in first_name:
                found_member.append(v)
    elif search_choice==3:
        status=input("Enter membership status to search (Active - Inactive): ").lower()
        for c in members_list:
            if c.status.lower() == status:
                found_member.append(c)
    else:
        print("Invalid choice Please try again.\n")

    if found_member:
        clear_screen()
        for x in found_member:
            x.display()
    else:
        print("There is no member yet!")

while True:
    print("""
*** Welcome to GYM membership management ***

Choose an action: 
1. Add a new member
2. Display all members
3. Search for a member
4. Exit
    """)
    choice=int(input("Enter here your choice: "))
    if choice==1:
        members_list.append(create_member())
        print("\nMembner added successfully!\n")
        time.sleep(1)
    elif choice==2:
        clear_screen()
        print("\nDisplaying all Members.....\n")
        time.sleep(2)
        if members_list:
            for member in members_list:
                member.display()
                
        else:
            print("Sorry, no members found to display.\n")
            time.sleep(1)
    elif choice==3:
        if members_list:
            search_member(members_list)
            time.sleep(2)
        else:
            print("There is no members to search!")
            time.sleep(1)

    elif choice==4:
        print("Exiting...")
        time.sleep(2)
        break
    else:
        print("Invalid choice. Please try again.\n")
        time.sleep(1)

#(10) My work on this code
import os
import time
import random

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

class Drinks:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.id=random.randint(1000,9000)
    def display_info(self):
        print(f"""
Drink Name: {self.name}
Quantity: {self.quantity}
Price: ${self.price}
total: ${self.price*self.quantity}
The TD: {self.id}
"""+"_"*30)

drinks_list=[]
def add_drink():
    name=input("Enter the name of the drink: ")
    price=float(input("Enter the price: "))
    quantity=int(input("Enter the quantity: "))
    drink=Drinks(name,price,quantity)
    drinks_list.append(drink)
    return drink

def search(drinks_list):
    found_list=[]
    choice=int(input("Search By...\n1. Id\n2. Name Drink\nEnter your choice: "))
    if choice==1:
        ask=int(input("Enter the ID number to search: "))
        for x in drinks_list:
            if x.id == ask:
                found_list.append(x)
                break
    elif choice==2:
        ask=input("Enter the name of the drink to search: ").lower()
        for x in drinks_list:
            if x.name.lower() == ask:
                found_list.append(x)
    else:
        print("Invalid choice, please try again.\n")

    if found_list:
        clear_screen()
        for g in found_list:
            g.display_info()
    else:
        print("There are no drinks to be found!")

while True:
    print("""
*** Welcome to Drinks management ***
choose an action:
1. Add Drink
2. Display Drinks
3. Search for an invoice
4.Exit
    """)
    user=int(input("Enter your choice: "))
    if user==1:
        clear_screen()
        add_drink()
        print("\nThe drink added successfully!\n")
        time.sleep(2)
    elif user==2:
        clear_screen()
        print("\nDisplaying all drinks.....\n")
        time.sleep(2)
        if drinks_list:
            for z in drinks_list:
                z.display_info()
        else:
            print("There are no drinks yet!")
            time.sleep(1)
    elif user==3:
        clear_screen()
        if drinks_list:
            search(drinks_list)
            time.sleep(2)
        else:
            print("You haven't added anything to search.")
            time.sleep(1)
    elif user==4:
        print("Exiting...")
        time(2)
        break
    else:
        print("Invalid choice, please try again.\n")
        time.sleep(1)