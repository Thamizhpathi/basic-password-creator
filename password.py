import random

#variables
numbers=[]
alphabet=[]
small_letter=[]
symbol=["@","$","&",'#','%','?','.','/','|','*']
password=""

#get th password length
len_of_passwd=input("Enter the length of passwd you want:")

#check if len_of_passwd is greater than 12
while not len_of_passwd.isdigit()or int(len_of_passwd)<12:
      print("Enter the correct format it must be number and number should be greater than 11")
      len_of_passwd=input("Enter the length of passwd you want:")

#get the username
user_name= input("Enter your full name:")

#check the username is alphabets
while not user_name.isalpha()  :
      print("Enter only tha alphabets keys")
      user_name= input("Enter your name:")

#append the 0 to 9 numeric value in number list
for number in range(0,10):
    numbers.append(number)

#append the alphaets in alphabet list
for alpha in range(65,91):
    alphabet.append(chr(alpha))
#append tha small letter in small letter list
for alpha in  range(97,123):
    small_letter.append(chr(alpha))
 #combining all list    
combined_list=numbers+alphabet+symbol+small_letter

def add_username_to_password():    
    for i in user_name:
        global password
        password+=i
        if int(len(password))==4:
            break
def add_random_symbol_to_password(add_username_fun=add_username_to_password()):
    global password
    symbol_choice=random.choice(symbol)
    password+=symbol_choice

def add_password_length(add_number_fun=add_random_symbol_to_password()):
    global password
    password+=len_of_passwd
   
def  construct_password(add_all_fun=add_password_length()):
     global password
     count=int(len_of_passwd)-int(len(password))
     for i in range(count):
        random_pick=random.choice(combined_list)
        password+=str(random_pick)            
     print("your random password is:{}".format(password))

def start(add=construct_password()):
    add
    
#starting the our tool
start()