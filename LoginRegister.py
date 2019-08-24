# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:56:07 2019

@author: Ajayi Raymond T
"""

from tkinter import *
import os

def RegisterUser ():
    username_info = username.get()
    password_info = password.get()
    
    file = open(username_info,'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()
    
    username_entry.delete(0,'end')
    password_entry.delete(0,'end')
    
    Label(screen1,text = 'Registration Sucess',fg = 'green',font = ('calibri',11)).pack()
    
def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('Register')
    screen1.geometry('300x250')
    screen1.wm_iconbitmap('aduser.ico')
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1,text = 'Please Enter Details Below').pack()
    Label(screen1,text = '',fg = 'green',font = ('calibri',11)).pack()
    Label(screen1,text = 'Username  * ' ,fg = 'green',font = ('calibri',11)).pack()
    
   
    
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1,text = 'Password  * ' ,fg = 'green',font = ('calibri',11)).pack()
    password_entry = Entry(screen1, textvariable = password, show = '*')
    password_entry.pack()
    Label(screen1, text = '').pack()
    Button(screen1,text = 'Register',height = '2', width = '30', bg='#FFFACD', command = RegisterUser).pack()
def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def LoginSucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title('Sucessful Login')
    screen3.geometry('300x250')
    screen3.wm_iconbitmap('aduser.ico')
    Label(screen3,text = 'Sucess').pack()
    Button(screen3,text = 'LOGIN SUCESS',command = delete2,bg = 'green').pack()
def PasswordNotVerified():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title('Unsucessful Login')
    screen4.geometry('300x250')
    screen4.wm_iconbitmap('aduser.ico')
    Label(screen4,text = 'Unverified Password').pack()
    Button(screen4,text = 'LOGIN FAILED',command = delete3,bg = 'red').pack() 
def UserNotFound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title('Unsucessful Login')
    screen5.geometry('300x250')
    screen5.wm_iconbitmap('aduser.ico')
    Label(screen5,text = 'User Not Found').pack()
    Button(screen5,text = 'LOGIN FAILED',command = delete4,bg = 'red').pack()
    

def LoginVerify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,'end')
    password_entry1.delete(0,'end')
    
    file_list = os.listdir()
    if username1 in  file_list:
        file1 = open(username1, 'r')
        verify = file1.read().splitlines()
        if password1 in verify:
            LoginSucess()
        else:
            PasswordNotVerified()
    else:
        UserNotFound()
    
def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title('Login')
    screen2.geometry('300x250')
    screen2.wm_iconbitmap('aduser.ico')
    Label(screen2,text = 'Please Enter Details Below to Login').pack()
    Label(screen2, text = 'Password').pack()
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1

    Label(screen2,text = 'Username  * ').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = 'Password *').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = '*')
    password_entry1.pack()
    Label(screen2, text = '').pack()
    Button(screen2,text = 'Login',height = '1', fg='#F08080', bg='#FFFACD', width = '30', command = LoginVerify).pack()

def MainScreen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('SignUp')
    screen.wm_iconbitmap('aduser.ico')
    Label(text = 'Management Register Login System',bg = 'orange',width= '300',height= '2',font = ('calibri',13)).pack()
    Button(text = 'Login',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = Login).pack()
    Label( text = '').pack()
    Button(text = 'Register',height = '2', fg='#F08080', bg='#FFFACD', width = '30', command = Register).pack()
     
    screen.mainloop()

MainScreen()
    
    
    
    