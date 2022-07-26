from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Password guesser")

password_entry = Entry(root)
password_entry.place(relx=0.5,rely=0.3,anchor=CENTER)

label_password_guess = Label(root)
label_password_guess.place(relx=0.5,rely=0.4,anchor=CENTER)

label_random_pass = Label(root)
label_random_pass.place(relx=0.5,rely=0.6,anchor=CENTER)


three_d_array = [[['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],["King","Queen"],["!","@","#","$","%","^","&","*"]]]

def password_genrator():
    
    password_guess = password_entry.get()
    label_password_guess["text"]="Guessed Password: " + password_guess 
    
    random_1 = random.randint(0,25)
    random_2 = random.randint(0,1)
    random_3 = random.randint(0,7)
    
    print(str(random_1) + " " + str(random_2) + " " + str(random_3))
    
    letter_1 = three_d_array[0][0][random_1]
    letter_2 = three_d_array[0][1][random_2]
    letter_3 = three_d_array[0][2][random_3]
    
    password = str(letter_1) +""+ str(letter_2)+"" +str(letter_3)
    label_random_pass["text"]="Genrated Password: " + password





button1 = Button(root,text="New Password",command=password_genrator)
button1.place(relx=0.5,rely=0.5,anchor=CENTER)





root.mainloop()