# checking the strength of the passw+ord based on some conditions

import string
import tkinter as tk

def strength_checker(pwd):

    #Criteria
    length = len(pwd)
    exist_upper = len([ch for ch in pwd if ch.isupper() == True])
    exist_lower = len([ch for ch in pwd if ch.islower() == True])
    exist_digit = len([ch for ch in pwd if ch.isdigit() == True])
    exist_spl = len([ch for ch in pwd if ch in string.punctuation])

    #Score Calculation

    score = 0

    if length>=12: score +=1
    if exist_upper>0: score +=1
    if exist_lower>0: score +=1
    if exist_digit>0: score +=1
    if exist_spl>0: score +=1

    score = (score/5) * 100
    return score

def common_list(pwd) -> str:
    with open("common_pwd.txt",'r') as fp:

        while(1):
            s = fp.readline().rstrip()

            if s=="":
                return "Good!, Your Password is not found in common password database"

            if(s==pwd):
                return "It is found in common password database"


root = tk.Tk()
root.title("Password Strength Checker")
password_label = tk.Label(root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

strength_label = tk.Label(root, text="", fg="black")
strength_label.pack()

cracked = tk.Label(root)
cracked.pack()

def score_category():

    password = password_entry.get()
    if password=="":
        raise Exception

    score = strength_checker(password)
    if(score == 20.0):
        strength_label.config(text ='Very Bad Password!, Please change it ASAP',)
    elif(score == 40.0):
        strength_label.config(text ="Bad Password!, Please change it")
    elif(score == 60.0):
        strength_label.config(text ="Moderate Password!, Make it more Complex")
    elif(score == 80.0):
        strength_label.config(text ="Good Password!, Need to improve")
    elif(score == 100.0):
        strength_label.config(text ="Strong Password!, Well Done")

    s = common_list(password)
    cracked.config(text = s)


check_button = tk.Button(root,text="Check Strength", command= score_category,bg="orange",fg='red')
check_button.pack()
root.mainloop()







