# Displaybook() : To display the available books
# Lendbook(): To lend a book to a user
# Addbook(): To add a book in the library
# Returnbook(): To return the book in the library.



# a=1
import datetime
from getpass import getpass
import random
import time
import os
import pyfiglet
import keyboard
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#final with style
class Abhash_lib:
    # def __init__(self, bookname):
    #     self.bookname = bookname



    #final with style
    def book_list():
        with open("Booklist.txt", "r") as f:
            z = len(f.readlines())
        with open("Booklist.txt", "r") as f:
            print(f"{Back.LIGHTRED_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}S.no.   Book I.D.                   Book Name                              ")
            print(
                f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")
            for i in range(z):
                e = f.readline()
                print(f"{Fore.LIGHTYELLOW_EX}{i + 1}. {Fore.LIGHTMAGENTA_EX}{e[0:13]}{Fore.LIGHTCYAN_EX}{e[13::]}", end='')
        print(
            f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")
        print(f"{Fore.LIGHTCYAN_EX}                 Total {Fore.LIGHTMAGENTA_EX}{z} {Fore.LIGHTCYAN_EX}Books present in the library")
        print(
            f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")

    #final with style
    def add_book(self):
        b = str("")
        a = str(datetime.datetime.today())
        s = a.split(" ")[1]
        q = s.split(".")[0]
        x = q.split(":")
        print(f"{Fore.LIGHTBLUE_EX}Enter writer's name:")
        writer = input()
        if writer=="q" or writer=="Q":
            print(f"{Fore.RED}Quiting...")
        else:
            print(f"{Fore.LIGHTBLUE_EX}Enter your full name:")
            user = input()
            if user == "q" or user == "Q":
                print(f"{Fore.RED}Quiting...")
            else:
                for i in x:
                    b = str(b + i)
                z = random.randint(0, 9)
                with open("Booklist.txt", "a") as f:
                    f.write(f"     #{z}{b}        {self.upper()} by {writer.upper()}\n")
                print(f"\n{Fore.LIGHTCYAN_EX}Your book is added to the library with {Fore.LIGHTMAGENTA_EX}#{z}{b}{Fore.LIGHTCYAN_EX} Book I.D.")
                with open("libbookdet.txt", "a") as f:
                    f.write(f"Book given by {user.upper()} on {time.asctime(time.localtime(time.time()))}\nBook I.D. = #{z}{b}     "
                            f"Book Name = {self.upper()} by {writer.upper()}\n")

#final with style
class lend_return_renew:
    #final with style
    def lend_book(self):
        with open("Booklist.txt", "r") as f:
            z = f.readlines()
        with open("lendbook.txt", "r") as x:
            q = x.readlines()
            s = 0
            r = 0
            e = ''
            print(f"{Back.LIGHTRED_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}S.no       Availability         Book I.D.                   Book Name                               ")
            print(
                f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
            for i in z:
                if self in i:
                    if i not in q:
                        print(f"{Fore.LIGHTYELLOW_EX}{s+r+1}.         {Fore.LIGHTBLUE_EX}It is available {Fore.LIGHTMAGENTA_EX}{i[0:13]}{Fore.LIGHTCYAN_EX}{i[13::]}", end='')
                        e = e + i
                        s += 1
                    elif i in q:
                        print(f"{Fore.LIGHTYELLOW_EX}{s+r+1}.         {Fore.LIGHTRED_EX}Not   available {Fore.LIGHTMAGENTA_EX}{i[0:13]}{Fore.LIGHTCYAN_EX}{i[13::]}", end='')
                        r += 1
            if (s+r)==0:
                print(f"{Fore.RED}                                      No record found")
                print(
                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
            elif s==0:
                print(
                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                print(f"{Fore.CYAN}                               Sorry no book is Available")
                print(
                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
            else:
                r = e.split("\n")
                if s==1:
                    print(
                        f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                    print(f"                                  {Fore.LIGHTGREEN_EX}{s} Book is Available")
                else:
                    print(
                        f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                    print(f"                                  {Fore.LIGHTGREEN_EX}{s} Books are Available")
                print(
                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________\n")


                if self[0]=="#" and len(self)==8:
                    o = self
                    for i in r:
                        if o in i:
                            print(f"{Fore.LIGHTBLUE_EX}Enter your full name:")
                            name = input()
                            if name == "q" or name == "Q":
                                print(f"{Fore.RED}Quiting...")
                            else:
                                print(f"{Fore.LIGHTBLUE_EX}Enter your 6 digits postal pin code:")
                                postal_code = input()
                                if postal_code == "q" or postal_code == "Q" or len(postal_code)!=6:
                                    print(f"{Fore.RED}Quiting...")
                                else:
                                    print(f"{Fore.LIGHTBLUE_EX}Enter name of your city:")
                                    city = input()
                                    if city == "q" or city == "Q":
                                        print(f"{Fore.RED}Quiting...")
                                    else:
                                        print(f"{Fore.LIGHTBLUE_EX}Enter your 10 digits mobile no.:")
                                        mobile = input()
                                        if mobile == "q" or mobile == "Q" or len(mobile)!=10:
                                            print(f"{Fore.RED}Quiting...")
                                        else:
                                            print(f"{Fore.LIGHTRED_EX}Do you want to continue y/n?")
                                            con = input()
                                            if con=="y" or con=="Y":
                                                with open("lendbook.txt", "a") as f:
                                                    f.write(f"{i}\n")
                                                with open("lendbookdet.txt", "a") as x:
                                                    x.write(f"{i[5:13]}       {datetime.datetime.today()}"
                                                            f"          {datetime.datetime.today() + datetime.timedelta(days=8)}"
                                                            f"          Borrowed\n"
                                                            f"Username - {name.upper()}\nBook Name - {i[21::]}\n"
                                                            f"Postal code = {postal_code}         Mobile No. = {mobile}         "
                                                            f"City = {city.upper()}\n")
                                                print(
                                                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                                                print(f"{Fore.LIGHTGREEN_EX}Book has been lend to you for {Fore.LIGHTMAGENTA_EX}7 days{Fore.LIGHTGREEN_EX}. Please return/renew the "
                                                      f"book before {Fore.LIGHTMAGENTA_EX}{datetime.date.today() + datetime.timedelta(days=8)}{Fore.LIGHTGREEN_EX}.")
                                                print(
                                                    f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                                            elif con=="n" or con=="N":
                                                print(f"{Fore.RED}Operation canceled...")

                else:
                    s = 0
                    while s<2:
                        print(f"\n{Fore.LIGHTBLUE_EX}Please enter Book I.D. to lend book({Fore.LIGHTRED_EX}Start with # sign{Fore.LIGHTBLUE_EX}):")
                        o = input()
                        m = 0
                        if o == "q" or o == "Q":
                            print(f"{Fore.RED}Quiting...")
                            break

                        if o[0]=="#" and len(o)==8:
                            for i in r:
                                if o in i:
                                    print(f"{Fore.LIGHTBLUE_EX}Enter your full name:")
                                    name = input()
                                    if name == "q" or name == "Q":
                                        print(f"{Fore.RED}Quiting...")
                                    else:
                                        print(f"{Fore.LIGHTBLUE_EX}Enter your 6 digits postal pin code:")
                                        postal_code = input()
                                        if postal_code == "q" or postal_code == "Q" or len(postal_code)!=6:
                                            print(f"{Fore.RED}Quiting...")
                                        else:
                                            print(f"{Fore.LIGHTBLUE_EX}Enter name of your city:")
                                            city = input()
                                            if city == "q" or city == "Q":
                                                print(f"{Fore.RED}Quiting...")
                                            else:
                                                print(f"{Fore.LIGHTBLUE_EX}Enter your 10 digits mobile no.:")
                                                mobile = input()
                                                if mobile == "q" or mobile == "Q" or len(mobile)!=10:
                                                    print(f"{Fore.RED}Quiting...")
                                                else:
                                                    print(f"{Fore.LIGHTRED_EX}Do you want to continue y/n?")
                                                    con = input()
                                                    if con == "y" or con == "Y":
                                                        with open("lendbook.txt","a") as f:
                                                            f.write(f"{i}\n")
                                                        with open("lendbookdet.txt", "a") as x:
                                                            x.write(f"{i[5:13]}       {datetime.datetime.today()}"
                                                                    f"          {datetime.datetime.today() + datetime.timedelta(days=8)}"
                                                                    f"          Borrowed\n"
                                                                    f"Username - {name.upper()}\nBook Name - {i[21::]}\n"
                                                                    f"Postal code = {postal_code}         Mobile No. = {mobile}         "
                                                                    f"City = {city.upper()}\n")
                                                        print(
                                                            f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                                                        print(f"{Fore.LIGHTGREEN_EX}Book has been lend to you for {Fore.LIGHTMAGENTA_EX}7 days{Fore.LIGHTGREEN_EX}. Please return/renew the "
                                                              f"book before {Fore.LIGHTMAGENTA_EX}{datetime.date.today() + datetime.timedelta(days=8)}{Fore.LIGHTGREEN_EX}.")
                                                        print(
                                                            f"{Fore.LIGHTRED_EX}{Style.DIM}____________________________________________________________________________________________________")
                                                    elif con == "n" or con == "N":
                                                        print(f"{Fore.RED}Operation canceled...")

                                elif m==(len(r)-1):
                                    print(f"{Fore.CYAN}The Book I.D. is not available with the book name")

                                else:
                                    m += 1
                            break

                        elif o[0]!="#" and len(o)!=8:
                            if s<1:
                                print(f"{Fore.RED}Try again")
                            s+=1


                        else:
                            print(f"{Fore.RED}Wrong input")
                    if s==2:
                        print(f"{Fore.RED}Sorry you have entered wrong Book I.D. 2 times, try again")

    #final with style
    def return_renew_book(self):
        with open("lendbook.txt", "r") as f:
            r = f.readlines()
        with open("Booklist.txt", "r") as t:
            z = t.readlines()
        q = open('lendbookdet.txt', "a")
        s = 0
        w = 0
        print(f"{Fore.LIGHTBLUE_EX}If you want to return the book enter [{Fore.LIGHTRED_EX}1{Fore.LIGHTBLUE_EX}] and if you want to renew enter [{Fore.LIGHTRED_EX}2{Fore.LIGHTBLUE_EX}]:")
        inp = input()
        if inp == "q" or inp == "Q":
            print(f"{Fore.RED}Quiting...")
        else:
            if inp == "1":
                x = open("temp.txt", "w")
                print(f"{Fore.LIGHTBLUE_EX}Enter your name:")
                name = input()
                if name == "q" or name == "Q":
                    print(f"{Fore.RED}Quiting...")
                else:
                    for i in r:
                        if self not in i:
                            x.write(i)
                            s+=1
                        if s == (len(r)):
                            for p in z:
                                if self in p:
                                    print(f"{Fore.CYAN}The book is not borrowed yet, please borrow the book first")
                                elif w==(len(z)-1):
                                    print(f"{Fore.RED}You have entered wrong Book I.D., try again")
                                else:
                                    w+=1
                        if self in i:
                            q.write(f"{i[5:13]}       {datetime.datetime.today()}"
                                    f"          {datetime.datetime.today() + datetime.timedelta(days=8)}"
                                    f"          Return\n"
                                    f"Username - {name.upper()}\nBook Name - {i[21::]}\n")
                            print(
                                f"\n{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________________")
                            print(f"{Fore.LIGHTGREEN_EX}Thank you for borrowing book from our library. We hope you liked our services.")
                            print(
                                f"{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________________")
                    x.close()
                    q.close()
                    os.remove("lendbook.txt")
                    os.rename("temp.txt", "lendbook.txt")

            elif inp == "2":
                print(f"{Fore.LIGHTBLUE_EX}Enter your name:")
                name = input()
                if name == "q" or name == "Q":
                    print(f"{Fore.RED}Quiting...")
                else:
                    for i in r:
                        if self in i:
                            print(f"{Fore.LIGHTBLUE_EX}Enter your 6 digits postal pin code:")
                            postal_code = input()
                            if postal_code == "q" or postal_code == "Q" or len(postal_code)!=6:
                                print(f"{Fore.RED}Quiting...")
                            else:
                                print(f"{Fore.LIGHTBLUE_EX}Enter name of your city:")
                                city = input()
                                if city == "q" or city == "Q":
                                    print(f"{Fore.RED}Quiting...")
                                else:
                                    print(f"{Fore.LIGHTBLUE_EX}Enter your 10 digits mobile no.:")
                                    mobile = input()
                                    if mobile == "q" or mobile == "Q" or len(mobile)!=10:
                                        print(f"{Fore.RED}Quiting...")
                                    else:
                                        q.write(f"{i[5:13]}       {datetime.datetime.today()}"
                                                f"          {datetime.datetime.today() + datetime.timedelta(days=8)}"
                                                f"          Renewed\n"
                                                f"Username - {name.upper()}\nBook Name - {i[21::]}"
                                                f"Postal code = {postal_code}         Mobile No. = {mobile}         "
                                                f"City = {city.upper()}\n")
                                        print(
                                            f"\n{Fore.LIGHTRED_EX}{Style.DIM}______________________________________________________________________________________")
                                        print(
                                            f"{Fore.LIGHTGREEN_EX}Book has been lend to you for {Fore.LIGHTMAGENTA_EX}7 days{Fore.LIGHTGREEN_EX}. Please return/renew the "
                                            f"book before {Fore.LIGHTMAGENTA_EX}{datetime.date.today() + datetime.timedelta(days=8)}{Fore.LIGHTGREEN_EX}.")
                                        print(
                                            f"{Fore.LIGHTRED_EX}{Style.DIM}______________________________________________________________________________________")
                                        q.close()
                                        break
                        elif s==(len(r)-1):
                            for p in z:
                                if self in p:
                                    print(f"{Fore.CYAN}The book is not borrowed yet, please the book first")
                                elif w==(len(z)-1):
                                    print(f"{Fore.RED}You have entered wrong Book I.D., try again")
                                else:
                                    w+=1
                        else:
                            s = s+1

#final with style
class book_search:

    def book_search(self):
        a = str(self).upper()
        with open("Booklist.txt", "r") as f:
            x = f.readlines()
            s = len(x)
            w = 0
            l = 1
            print(
                f"{Back.LIGHTRED_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}S.no.   Book I.D.                   "
                f"Book Name                              ")
            print(
                f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")
            for i in x:

                if a in i:
                    c = list(i)
                    print(f"{Fore.LIGHTYELLOW_EX}{l}.", end='')
                    for u in c[0:13]:
                        if u in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{u}", end='')
                    for u in c[13::]:
                        if u in a:
                            print(f"{Fore.LIGHTBLUE_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTCYAN_EX}{u}", end='')


                elif a[0:3] in i:
                    c = list(i)
                    print(f"{Fore.LIGHTYELLOW_EX}{l}.", end='')
                    for u in c[0:13]:
                        if u in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{u}", end='')
                    for u in c[13::]:
                        if u in a:
                            print(f"{Fore.LIGHTBLUE_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTCYAN_EX}{u}", end='')


                elif a[0:2] in i:
                    c = list(i)
                    print(f"{Fore.LIGHTYELLOW_EX}{l}.", end='')
                    for u in c[0:13]:
                        if u in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{u}", end='')
                    for u in c[13::]:
                        if u in a:
                            print(f"{Fore.LIGHTBLUE_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTCYAN_EX}{u}", end='')


                elif a[0:4] in i:
                    c = list(i)
                    print(f"{Fore.LIGHTYELLOW_EX}{l}.", end='')
                    for u in c[0:13]:
                        if u in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTMAGENTA_EX}{u}", end='')
                    for u in c[13::]:
                        if u in a:
                            print(f"{Fore.LIGHTBLUE_EX}{Back.LIGHTBLACK_EX}{Style.BRIGHT}{u}", end='')
                        if u not in a:
                            print(f"{Fore.LIGHTCYAN_EX}{u}", end='')


                elif w == (s - 1):
                    print(f"                          {Fore.LIGHTCYAN_EX}No book found")
                else:
                    w += 1
                l += 1
            print(
                f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")
            if w != (s - 1):
                print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}*Note{Fore.BLUE} -{Fore.CYAN} "
                      f"S.no. is given according to book position in library")
            print(
                f"{Fore.LIGHTRED_EX}{Style.DIM}___________________________________________________________________________")

#final
class administrator(Abhash_lib,lend_return_renew,book_search):

    # final with style
    def read_lend():
        with open("lendbook.txt", "r") as f:
            z = len(f.readlines())
        with open("lendbook.txt", "r") as f:
            print(f"{Back.LIGHTRED_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}S.no.   Book I.D.                    Book Name                        ")
            print(f"{Fore.LIGHTRED_EX}{Style.DIM}______________________________________________________________________")
            if z==0:
                print(f"{Fore.CYAN}                  No books borrowed yet\n")
            for i in range(z):
                r1 = f.readline()
                print(f"{Fore.LIGHTYELLOW_EX}{i + 1}. {Fore.LIGHTMAGENTA_EX}{r1[0:13]}{Fore.LIGHTCYAN_EX}{r1[13::]}", end='')
                print(f"{Fore.LIGHTRED_EX}{Style.DIM}______________________________________________________________________")

    # final with style
    def lend_bookdet():
        with open("lendbookdet.txt","r") as f:
            z = f.readlines()
            q = int(len(z)/4)
            w = 1
        with open("lendbookdet.txt", "r") as f:
            print(f"{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________"
                  "_________________________________")
            for i in range(0, q):
                print(
                    f"{Back.LIGHTRED_EX}{Fore.LIGHTWHITE_EX}{Style.BRIGHT}S.no.     Book I.D.             From Date                             "
                    f"To Date                    Status   ")
                print(
                    f"{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________"
                    "___________________________________")
                r1 = f.readline()
                r2 = f.readline()
                r3 = f.readline()
                r4 = f.readline()
                print(f"{Fore.LIGHTYELLOW_EX}{w}.        {Fore.LIGHTMAGENTA_EX}{r1[0:8]}{Fore.LIGHTCYAN_EX}{r1[8:87]}{Fore.LIGHTMAGENTA_EX}{r1[87::]}", end='')
                print(f"          {Fore.LIGHTCYAN_EX}{r2[0:10]}{Fore.LIGHTMAGENTA_EX}{r2[10::]}", end='')
                print(f"          {Fore.LIGHTCYAN_EX}{r3[0:11]}{Fore.LIGHTMAGENTA_EX}{r3[11::]}", end='')
                print(f"          {Fore.LIGHTCYAN_EX}{r4[0:14]}{Fore.LIGHTMAGENTA_EX}{r4[14:21]}{Fore.LIGHTCYAN_EX}{r4[21:42]}{Fore.LIGHTMAGENTA_EX}{r4[42:53]}{Fore.LIGHTCYAN_EX}{r4[53:68]}{Fore.LIGHTMAGENTA_EX}{r4[68::]}",end='')
                print(f"{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________"
                      "___________________________________")
                w+=1

    #final with style
    def lib_bookdet():
        with open("libbookdet.txt", 'r') as f:
            z = f.readlines()
            q = int(len(z) / 2)
            w = 1
        with open("libbookdet.txt", 'r') as f:
            for i in range(0, q):
                r1 = f.readline()
                r2 = f.readline()
                print(f"{Fore.LIGHTRED_EX}{Style.DIM}_______________________________________________________________________"
                      "___________________________________")
                print(f"{Fore.LIGHTYELLOW_EX}{w}.        {Fore.LIGHTCYAN_EX}{r1}", end='')
                print(f"          {Fore.LIGHTCYAN_EX}{r2[0:11]}{Fore.LIGHTMAGENTA_EX}{r2[11:20]}{Fore.LIGHTCYAN_EX}{r2[20:36]}{Fore.LIGHTMAGENTA_EX}{r2[36::]}", end='')
                w+=1
            print(f"{Fore.LIGHTRED_EX}_______________________________________________________________________"
                  "___________________________________")

    #final with style
    def remove_book(self):
        q = open("temp.txt","a")
        f = open("Booklist.txt", "r")
        r = f.readlines()
        with open("libbookdet.txt","a") as x:
            w=0
            print(f"{Fore.LIGHTBLUE_EX}Enter password to continue:")
            _pass = input()
            if _pass=="14062004":
                for i in r:
                    if self not in i:
                        q.write(i)
                    if self in i:
                        w+=1
                if w==0:
                    print(f"{Fore.RED}Book not found")
                if w>0:
                    print(F"{Fore.LIGHTGREEN_EX}Operation successful")
                    x.write(f"Book removed on {time.asctime(time.localtime(time.time()))}\nBook I.D. = {self}     "
                            f"Book Name = {i[21::]}")
                q.close()
                f.close()
                os.remove("Booklist.txt")
                os.rename("temp.txt", "Booklist.txt")


            else:
                print(f"{Fore.RED}Incorrect password")


print(f"{Style.DIM}{Fore.LIGHTBLACK_EX}\nProject Library[Version 0.01.160421]")
print(f"{Style.DIM}{Fore.LIGHTBLACK_EX}©2021 Abhash Chakraborty. Some right reserved\n\n")
time.sleep(1)

P = pyfiglet.figlet_format("WELCOME TO XYZ LIBRARY", font="digital")
print(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}{P}")


while True:
    time.sleep(1)
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

    print(f"{Fore.LIGHTYELLOW_EX}"
          f"           *To list book press [{Fore.LIGHTRED_EX}1{Fore.LIGHTYELLOW_EX}]\n"
          f"           *To add book press [{Fore.LIGHTRED_EX}2{Fore.LIGHTYELLOW_EX}]\n"
          f"           *To borrow book press [{Fore.LIGHTRED_EX}3{Fore.LIGHTYELLOW_EX}]\n"
          f"           *To return/renew book press [{Fore.LIGHTRED_EX}4{Fore.LIGHTYELLOW_EX}]\n"
          f"           *To search book press [{Fore.LIGHTRED_EX}5{Fore.LIGHTYELLOW_EX}]\n"
          f"           You can enter [{Fore.LIGHTRED_EX}q{Fore.LIGHTYELLOW_EX}] to cancel any operation\n"
          f"           Press [{Fore.LIGHTRED_EX}Esc{Fore.LIGHTYELLOW_EX}] to exit library")
    print(
        f"{Fore.LIGHTRED_EX}{Style.BRIGHT}+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    s = 0
    while s<1:
        if keyboard.is_pressed("1"):
            print()
            Abhash_lib.book_list()
            s+=1
        elif keyboard.is_pressed("2"):
            print(f"\n{Fore.LIGHTBLUE_EX}Enter full Book Name:")
            n = input()
            Abhash_lib.add_book(n)
            s += 1
        elif keyboard.is_pressed("3"):
            print(f"\n{Fore.LIGHTBLUE_EX}Enter Book Name or Book I.D.({Fore.LIGHTRED_EX}Book I.D. should start with # symbol{Fore.LIGHTBLUE_EX}):")
            n = input()
            lend_return_renew.lend_book(n.upper())
            s += 1
        elif keyboard.is_pressed("4"):
            print(f"\n{Fore.LIGHTBLUE_EX}Please enter Book I.D.({Fore.LIGHTRED_EX}Book I.D. should start with # symbol{Fore.LIGHTBLUE_EX}):")
            n = input()
            lend_return_renew.return_renew_book(n)
            s += 1
        elif keyboard.is_pressed("5"):
            print(f"\n{Fore.LIGHTBLUE_EX}Enter keywords to search book:")
            n = input()
            book_search.book_search(n)
            s += 1
        elif keyboard.is_pressed("Shift + Ctrl + Alt + 1"):
            print(f"\n{Fore.YELLOW}Username:", end='')
            m = input()
            n = getpass()
            if n=="123456" and m=="XYZ":
                k=0
                while k<1:
                    t = 0
                    P = pyfiglet.figlet_format("\nADMINISTRATOR MODE", font="digital")
                    print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}{P}")
                    time.sleep(1)
                    print(
                        f"{Fore.LIGHTRED_EX}{Style.BRIGHT}\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print(f"{Fore.LIGHTYELLOW_EX}"
                          f"           *To list book press [{Fore.LIGHTRED_EX}1{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To add book press [{Fore.LIGHTRED_EX}2{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To borrow book press [{Fore.LIGHTRED_EX}3{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To return/renew book press [{Fore.LIGHTRED_EX}4{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To search book press [{Fore.LIGHTRED_EX}5{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To read lend book press [{Fore.LIGHTRED_EX}6{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To read lend book details press [{Fore.LIGHTRED_EX}7{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To read library book details press [{Fore.LIGHTRED_EX}8{Fore.LIGHTYELLOW_EX}]\n"
                          f"           *To remove book press [{Fore.LIGHTRED_EX}9{Fore.LIGHTYELLOW_EX}]\n"
                          f"           You can enter [{Fore.LIGHTRED_EX}q{Fore.LIGHTYELLOW_EX}] to cancel any operation\n"
                          f"           Press [{Fore.LIGHTRED_EX}Esc{Fore.LIGHTYELLOW_EX}] to exit library")
                    print(
                        f"{Fore.LIGHTRED_EX}{Style.BRIGHT}+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
                    while t<1:
                        if keyboard.is_pressed("1"):
                            print()
                            administrator.book_list()
                            t+=1

                        elif keyboard.is_pressed("2"):
                            print(f"\n{Fore.LIGHTBLUE_EX}Enter full Book Name:")
                            n = input()
                            administrator.add_book(n)
                            t += 1

                        elif keyboard.is_pressed("3"):
                            print(f"\n{Fore.LIGHTBLUE_EX}Enter Book Name or Book I.D.({Fore.LIGHTRED_EX}Book I.D. should start with # symbol{Fore.LIGHTBLUE_EX}):")
                            n = input()
                            administrator.lend_book(n.upper())
                            t += 1

                        elif keyboard.is_pressed("4"):
                            print(f"\n{Fore.LIGHTBLUE_EX}Please enter Book I.D.({Fore.LIGHTRED_EX}Book I.D. should start with # symbol{Fore.LIGHTBLUE_EX}):")
                            n = input()
                            administrator.return_renew_book(n)
                            t += 1

                        elif keyboard.is_pressed("5"):
                            print(f"\n{Fore.LIGHTBLUE_EX}Enter keywords to search book:")
                            n = input()
                            administrator.book_search(n)
                            t += 1

                        elif keyboard.is_pressed("6"):
                            print()
                            administrator.read_lend()
                            t+=1

                        elif keyboard.is_pressed("7"):
                            print()
                            administrator.lend_bookdet()
                            t+=1

                        elif keyboard.is_pressed("8"):
                            print()
                            administrator.lib_bookdet()
                            t += 1

                        elif keyboard.is_pressed("9"):
                            print(f"\n{Fore.LIGHTBLUE_EX}Enter Book I.D. to remove book:")
                            n = input()
                            administrator.remove_book(n)
                            t += 1

                        elif keyboard.is_pressed("Esc"):
                            os.system("cls")
                            k+=1
                            break


            else:
                print(f"{Fore.RED}Wrong password")
                break
        elif keyboard.is_pressed("Esc"):
            time.sleep(2)
            break
    if keyboard.is_pressed("Esc"):
        break
