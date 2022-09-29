import pickle                      # This module is used for data manipulation in binary files
import os                          # This module is used for rename, copy and moving of files
import datetime                    # This module is used for producing dates in program
import random                      # This module is used for generating random elements in program
import time                        # This module is used for producing time in program
import keyboard                    # This module is used for making hotkeys in program
import subprocess                  # This module is used for opening pdf files


# This function is used for generating random Book IDs
def bookid():
    with open("assets\\files\\booklist.dat", "rb") as f:
        a = random.randint(1000000, 9999999)
        try:
            while True:
                l = pickle.load(f)
                if f"#{a}" == l[0]:  # This statement helps in producing unique Book IDs
                    a += 1
                else:
                    pass
        except EOFError:
            return f"#{a}"


# This function is used to add books in library
def addbook():
    with open("assets\\files\\booklist.dat", "ab") as f:
        bid = bookid()
        bname = input("Enter book name:")
        author = input("Enter author name:")
        wfee = int(input("Enter weekly fees:"))
        mfee = int(input("Enter monthly fees:"))
        file = input("Do you want to add pdf of the book[y/n]? ")
        if file == "y" or file == "Y":
            bookpath = input("Enter book source path: ")
            bookdir = f"assets\\books\\{bid}.pdf"
            os.system(f"copy {bookpath} {bookdir}")  # This statement copy the pdf file to the database
            l1 = [bid, bname.upper(), author.upper(), wfee, mfee, "Yes"]
            l2 = [bid, bname.upper(), author.upper(), wfee, mfee, "Admin", "Added(pdf)",
                  9632587415, datetime.date.today()]
        else:
            l1 = [bid, bname.upper(), author.upper(), wfee, mfee, "No"]
            l2 = [bid, bname.upper(), author.upper(), wfee, mfee, "Admin", "Added",
                  9632587415, datetime.date.today()]
        pickle.dump(l1, f)
        with open("assets\\files\\libbookdet.dat", "ab") as y:
            pickle.dump(l2, y)
        print(f"operation completed successfully. Book Id is {bid}.")


# This function is used to remove books from library
def removebook():
    with open("assets\\files\\booklist.dat", "rb") as f:
        bid = input("Enter Book Id: ")
        bookdir = f"assets\\books\\{bid}.pdf"
        lostdir = f"lost.dir"
        s = 0
        l = []
        l2 = []
        try:
            while True:
                p = pickle.load(f)
                if bid != p[0]:
                    l.append(p)
                else:
                    l2 = p
                    l2.append("Admin")
                    l2.append("Removed")
                    l2.append(9632587415)
                    l2.append(datetime.date.today())
                    s += 1
        except Exception:
            if s == 0:
                print("No book is found")
            elif s == 1:
                with open("assets\\files\\libbookdet.dat", "ab") as y:
                    pickle.dump(l2, y)
                print("One book is removed")
            else:
                with open("assets\\files\\libbookdet.dat", "ab") as y:
                    pickle.dump(l2, y)
                print("Multiple books are removed")
            try:
                os.system(f"move {bookdir} {lostdir}")  # This statement is used to move pdf of book to lostdir
            except Exception:
                pass
            with open("assets\\files\\temp.dat", "wb") as q:
                for i in l:
                    pickle.dump(i, q)
    os.remove("assets\\files\\booklist.dat")  # This statement is used to remove old book list
    os.rename("assets\\files\\temp.dat",
              "assets\\files\\booklist.dat")  # This statement is used to rename temp.dat to booklist.dat
    print("Operation completed successfully.")


# This function is used for donation of books by users
def donation():
    con = input("Do you want to continue[y/n]?")
    if con == "y" or con == "Y":
        with open("assets\\files\\booklist.dat", "ab") as f:
            print(f"\n+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+\n"
                  f"|W|E|L|C|O|M|E| |T|O| |D|O|N|A|T|I|O|N| |B|O|X|\n"
                  f"+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+\n")
            bid = bookid()
            bname = input("Enter book name:")
            author = input("Enter author name:")
            name1 = input("Enter your full name:")
            phone1 = int(input("Enter your phone no.:"))
            file = input("Do you want to add pdf of the book[y/n]? ")
            if file == "y" or file == "Y":
                bookpath = input("Enter book source path: ")
                bookdir = f"assets\\books\\{bid}.pdf"
                os.system(f"copy {bookpath} {bookdir}")
                l1 = [bid, bname.upper(), author.upper(), "Free", "Free", "Yes"]
                l2 = [bid, bname.upper(), author.upper(), "Free", "Free", name1, "Added(pdf)",
                      phone1, datetime.date.today()]
            else:
                l1 = [bid, bname.upper(), author.upper(), "Free", "Free", "No"]
                l2 = [bid, bname.upper(), author.upper(), "Free", "Free", name1, "Added",
                      phone1, datetime.date.today()]
            pickle.dump(l1, f)
            with open("assets\\files\\libbookdet.dat", "ab") as y:
                pickle.dump(l2, y)
            print(f"operation completed successfully. Book Id is {bid}.")
            print("Thanking you for your contribution.")
        pass
    else:
        pass


# This function is for the admin of the library
# This function contains special access and features of library
def admin():
    print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+")
    print("|W|E|L|C|O|M|E| |T|O| |A|D|M|I|N| |M|O|D|E|")
    print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+")
    time.sleep(1)
    while True:
        print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        print(" |    * To view all books press       [Ctrl + 1]  |")
        print(" |    * To view borrowed books press  [Ctrl + 2]  |")
        print(" |    * To view borrowed books detail [Ctrl + 3]  |")
        print(" |    * To view library books detail  [Ctrl + 4]  |")
        print(" |    * To view suggested book press  [Ctrl + 5]  |")
        print(" |    * To view read book detail      [Ctrl + 6]  |")
        print(" |    * To add book                   [Ctrl + 7]  |")
        print(" |    * To remove book                [Ctrl + 8]  |")
        print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
        while True:
            if keyboard.is_pressed("Ctrl + 1"):
                book_list()
                time.sleep(1)
                while True:
                    if keyboard.is_pressed("Enter"):
                        break
                break

            if keyboard.is_pressed("Ctrl + 2"):
                a = readlendbook()
                if a == []:
                    print("No Book borrowed")
                for i in a:
                    print(i)
                time.sleep(1)
                break
            if keyboard.is_pressed("Ctrl + 3"):
                a = lendbookdet()
                for i in a:
                    print(i)
                time.sleep(1)
                break
            if keyboard.is_pressed("Ctrl + 4"):
                a = libbookdet()
                if a == []:
                    print("No Information Available")
                for i in a:
                    print(i)
                time.sleep(1)
                break
            if keyboard.is_pressed("Ctrl + 5"):
                a = suggestion()
                if a == []:
                    print("No Information Available")
                for i in a:
                    print(i)
                time.sleep(1)
                break
            if keyboard.is_pressed("Ctrl + 6"):
                a = readbookdet()
                if a == []:
                    print("No Information Available")
                for i in a:
                    print(i)
                time.sleep(1)
                break
            if keyboard.is_pressed("Ctrl + 7"):
                addbook()
                break
            if keyboard.is_pressed("Ctrl + 8"):
                removebook()
            if keyboard.is_pressed("Esc"):
                break
        if keyboard.is_pressed("Esc"):
            print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
            print("|W|E|L|C|O|M|E| |T|O| |X|Y|Z| |L|I|B|R|A|R|Y|")
            print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
            time.sleep(1)
            break


# This function is used to borrow books from library
def lendbook(book__name, name1, username="", phone1=""):
    reff = referenceno()
    a = book__name.upper()
    book1 = []
    name1 = name1.upper()
    username = username
    phone1 = str(phone1)
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            print(
                f"______________________________________________"
                f"___________________________________"
                f"________________________________________________"
                f"________________")
            print(
                f"S.no.    Book I.D.            Author                       "
                f"Availability                          Book Name"
                f"                                       ")
            print(
                f"__________________________________________"
                f"_______________________________________"
                f"____________________________________________"
                f"____________________")
            b = a.split(" ")
            w = 1
            n = 1
            while True:
                l = pickle.load(f)
                r0 = str(l[0]).split(" ")
                r1 = str(l[1]).split(" ")
                r2 = str(l[2]).split(" ")
                r3 = str(l[3]).split(" ")
                r4 = str(l[4]).split(" ")
                w1 = 0
                w2 = 0
                w3 = 0
                w4 = 0
                for i in r0:
                    for k in b:
                        if k == i:
                            if l in readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    "
                                    f"{' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                                break
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    "
                                    f"{' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                                book1 = l

                for i in r1:
                    for k in b:
                        if k in i and w1 == 0 and len(k) != 0:
                            if l in readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    "
                                    f"{' ' * (30 - len('Not available'))}{l[1]}0")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    "
                                    f"{' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r2:
                    for k in b:
                        if k in i and w2 == 0 and len(k) != 0:
                            if l in readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    "
                                    f"{' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    "
                                    f"{' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r3:
                    for k in b:
                        if k == i and w3 == 0:
                            if l in readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    "
                                    f"{' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    "
                                    f"{' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

                for i in r4:
                    for k in b:
                        if k == i and w4 == 0:
                            if l in readlendbook():
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Not available    "
                                    f"{' ' * (30 - len('Not available'))}{l[1]}")
                                w += 1
                                n += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1
                            else:
                                print(
                                    f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                    f"     {l[2]}{' ' * (30 - len(l[2]))}    Available    "
                                    f"{' ' * (30 - len('Available'))}{l[1]}")
                                w += 1
                                w1 += 1
                                w2 += 1
                                w3 += 1
                                w4 += 1

        except EOFError:
            if w == 2:
                if w == n:
                    print(
                        f"____________________________________________"
                        f"_____________________________________"
                        f"____________________________________________"
                        f"____________________")
                    print(
                        f"                                                   "
                        f"The book is not available in the library")
                    print(
                        f"______________________________________________"
                        f"___________________________________"
                        f"_____________________________________________"
                        f"___________________\n")

                else:
                    if book__name[0] == "#":
                        print(
                            f"___________________________________________"
                            f"______________________________________"
                            f"__________________________________________"
                            f"______________________")
                        if phone1 == "":
                            phone1 = input(
                                f"\nEnter your 10 digit mobile no.:  ")

                        try:
                            phon = int(phone1)
                            if len(phone1) == 10:
                                print(f"\nYour Name = {name1}\n"
                                      f"Your username = {username}\n"
                                      f"Phone no. = {phon}\n"
                                      f"Book Name = {book1[1]}\n"
                                      f"Price = ₹{book1[3]}/week or ₹{book1[4]}/month\n"
                                      f"\nIf you want to continue press [Ctrl + 1] "
                                      f"otherwise press[Ctrl + 2].")
                                while True:
                                    if keyboard.is_pressed('Ctrl + 1'):
                                        time.sleep(0.2)
                                        print(
                                            f"\nFor weekly subscription press [Ctrl + 3] "
                                            f"for monthly subscription press [Ctrl + 4]:")
                                        while True:
                                            if keyboard.is_pressed('Ctrl + 3'):
                                                with open("assets\\files\\lendbook.dat", "ab") as m:
                                                    pickle.dump(book1, m)
                                                with open("assets\\files\\lendbookdet.dat", "ab") as m:
                                                    book1.append(name1)
                                                    book1.append(username)
                                                    book1.append(phon)
                                                    book1.append(datetime.date.today())
                                                    book1.append(datetime.date.today() + datetime.timedelta(days=7))
                                                    book1.append("Borrowed")
                                                    book1.append(reff)
                                                    pickle.dump(book1, m)
                                                print(
                                                    f"\nPlease renew the book before "
                                                    f"{datetime.date.today() + datetime.timedelta(days=7)}. "
                                                    f"Your reference number is {reff}.")
                                                break
                                            elif keyboard.is_pressed('Ctrl + 4'):
                                                with open("assets\\files\\lendbook.dat", "ab") as m:
                                                    pickle.dump(book1, m)
                                                with open("assets\\files\\lendbookdet.dat", "ab") as m:
                                                    book1.append(name1)
                                                    book1.append(username)
                                                    book1.append(phon)
                                                    book1.append(datetime.date.today())
                                                    book1.append(datetime.date.today() + datetime.timedelta(days=30))
                                                    book1.append("Borrowed")
                                                    book1.append(reff)
                                                    pickle.dump(book1, m)
                                                print(
                                                    f"\nPlease renew the book before "
                                                    f"{datetime.date.today() + datetime.timedelta(days=30)}. "
                                                    f"Your reference number is {reff}.")
                                                break
                                            elif keyboard.is_pressed('q'):
                                                print(f"\nOperation canceled")
                                                break
                                    if keyboard.is_pressed('Ctrl + 2'):
                                        print(f"\nOperation canceled")
                                        break
                                    if keyboard.is_pressed("Ctrl + 3") or keyboard.is_pressed("Ctrl + 4"):
                                        break
                                    if keyboard.is_pressed("q"):
                                        print(f"\nOperation canceled")
                                        break
                            else:
                                print(f"\nInvalid Input")
                        except Exception:
                            print(f"\nInvalid Input")

                    else:
                        print(
                            f"____________________________________________"
                            f"_____________________________________"
                            f"____________________________________________"
                            f"____________________")
                        print(
                            f"                                                   "
                            f"{w - 1} book found in the library")
                        print(
                            f"_____________________________________________"
                            f"____________________________________"
                            f"______________________________________________"
                            f"__________________")
                        book__name = input(
                            f"\nEnter Book I.D.(Book I.D. should start with # symbol):  ")
                        print()
                        lendbook(book__name, name1, username, phone1)

            elif w == 1:
                print(
                    f"                                                   "
                    f"Sorry no book found in the library")
                print(
                    f"___________________________________________________"
                    f"______________________________"
                    f"__________________________________________________"
                    f"______________")
            else:
                if w == n:
                    print(
                        f"___________________________________________"
                        f"______________________________________"
                        f"___________________________________________"
                        f"_____________________")
                    print(
                        f"                                                   "
                        f"No books available in the library")
                    print(
                        f"_______________________________________________"
                        f"__________________________________"
                        f"______________________________________________"
                        f"__________________\n")

                else:
                    print(
                        f"______________________________________________"
                        f"___________________________________"
                        f"____________________________________________"
                        f"____________________")
                    print(
                        f"                                                   "
                        f"{w - 1} books available in the library")
                    print(
                        f"__________________________________________"
                        f"_______________________________________"
                        f"__________________________________________"
                        f"______________________\n")

                    if book__name[0] == "#":
                        pass
                    else:
                        book__name = input(
                            f"Enter Book I.D.(Book I.D. should start with # symbol):  ")
                        print()
                        lendbook(book__name, name1, username, phone1)


# This function is used to return borrowed books to library
def returnlend(self, name1, phone1):
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        k = open("assets\\files\\lendbook.dat", "rb")
        s = 0
        c = 0
        name1 = name1.upper()
        retbook = []
        book1 = []
        try:
            while True:
                l = pickle.load(f)
                if self == l[12]:
                    s += 1
                    try:
                        while True:
                            x = pickle.load(k)
                            if l[0] == x[0]:
                                c += 1
                                print(
                                    f"_________________________________________"
                                    f"________________________________________"
                                    f"_________________________________________"
                                    f"_______________________")
                                print(
                                    f"Book I.D.            Author                         "
                                    f"Book Name                                       ")
                                print(
                                    f"_______________________________________"
                                    f"__________________________________________"
                                    f"_________________________________________"
                                    f"_______________________")
                                print(f"{x[0]}{' ' * (10 - len(x[0]))}           "
                                      f"{x[2]}{' ' * (30 - len(l[2]))}{x[1]}")

                                print(
                                    f"______________________________________"
                                    f"___________________________________________"
                                    f"____________________________________"
                                    f"____________________________")

                                print("Do you want to continue[y/n]?")
                                a = input()
                                if a == "y" or a == "Y":
                                    if l[0] == x[0]:
                                        retbook.append(x[0])
                                        retbook.append(x[1])
                                        retbook.append(x[2])
                                        retbook.append(x[3])
                                        retbook.append(x[4])
                                        retbook.append(x[5])
                                        retbook.append(name1)
                                        retbook.append(l[7])
                                        retbook.append(phone1)
                                        retbook.append(l[9])
                                        retbook.append(datetime.date.today())
                                        retbook.append('Return')
                                        retbook.append(l[12])
                                        with open("assets\\files\\lendbookdet.dat", "ab") as r:
                                            pickle.dump(retbook, r)
                                        s += 1
                                        if l[9] < datetime.date.today():
                                            print("You are late.")
                                        print("Operation Completed.\nThank you for visiting our library.")
                            else:
                                book1.append(x)
                    except EOFError:
                        pass

        except EOFError:
            if c == 0:
                print("Book is already returned")
            if s == 0:
                print("No book is assigned with is reference number")
            with open("assets\\files\\temp.dat", "wb") as k:
                for i in book1:
                    pickle.dump(i, k)
            os.remove("assets\\files\\lendbook.dat")
            os.rename("assets\\files\\temp.dat", "assets\\files\\lendbook.dat")


# This function is used to renew borrowed books from library
def lendrenew(self):
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        k = open("assets\\files\\lendbook.dat", "rb")
        s = 0
        c = 0
        retbook = []
        try:
            while True:
                l = pickle.load(f)
                if self == l[12]:
                    s += 1
                    try:
                        while True:
                            x = pickle.load(k)
                            if l[0] == x[0]:
                                c += 1
                                print(
                                    f"_________________________________________"
                                    f"________________________________________"
                                    f"_________________________________________"
                                    f"_______________________")
                                print(
                                    f"Book I.D.            Author                         "
                                    f"Book Name                                       ")
                                print(
                                    f"_______________________________________________"
                                    f"__________________________________"
                                    f"____________________________________"
                                    f"____________________________")
                                print(f"{x[0]}{' ' * (10 - len(x[0]))}           "
                                      f"{x[2]}{' ' * (30 - len(l[2]))}{x[1]}")

                                print(
                                    f"________________________________________"
                                    f"_________________________________________"
                                    f"__________________________________________"
                                    f"______________________")

                                print("Do you want to continue[y/n]?")
                                a = input()
                                if a == "y" or a == "Y":
                                    retbook.append(x[0])
                                    retbook.append(x[1])
                                    retbook.append(x[2])
                                    retbook.append(x[3])
                                    retbook.append(x[4])
                                    retbook.append(l[5])
                                    retbook.append(l[6])
                                    retbook.append(l[7])
                                    retbook.append(l[8])
                                    retbook.append(l[9])
                                    retbook.append(datetime.date.today() + datetime.timedelta(days=7))
                                    retbook.append('Renew')
                                    retbook.append(l[12])
                                    with open("assets\\files\\lendbookdet.dat", "ab") as r:
                                        pickle.dump(retbook, r)
                                    if l[9] < datetime.date.today():
                                        print("You are late.")
                                    print("Operation Completed")
                                    print(
                                        f"Please renew the book before "
                                        f"{datetime.date.today() + datetime.timedelta(days=7)}. "
                                        f"Your reference number is {l[12]}.")
                                else:
                                    break
                    except EOFError:
                        pass

                    if c == 0:
                        print("Book is already returned")
        except EOFError:
            if s == 0:
                print("No book is assigned with is reference number")


# This function shows all the books available in the library
def book_list():
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            print(
                f"____________________________________________"
                f"_____________________________________"
                f"____________________________________________"
                f"____________________")
            print(
                f"S.no.    Book I.D.            Author                       "
                f"Rental Price                PDF          Book Name "
                f"                                      ")
            print(
                f"_____________________________________________"
                f"____________________________________"
                f"_____________________________________________"
                f"___________________")
            i = 1
            while True:
                l = pickle.load(f)
                print(
                    f"{i}.{' ' * (6 - len(str(i)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                    f"     {l[2][:30]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                    f"{' ' * (28 - len(f'₹{l[3]}/week or ₹{l[4]}/month'))}{l[5]}{' ' * (10 - len(l[5]))}{l[1]}")
                i += 1
        except EOFError:
            print(
                f"______________________________________________"
                f"___________________________________"
                f"______________________________________________"
                f"__________________")
            print(
                f"                                                   "
                f"Total {i - 1} books present in the library")
            print(
                f"_____________________________________________"
                f"____________________________________"
                f"_____________________________________________"
                f"___________________")
            print("Press [enter] to continue.")


# This function is used to search book from the library
def searchbook():
    book = input("Enter Book Name, Book Price, Author Name or Book Id to search: ")
    a = book.upper()
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            print(
                f"______________________________________________"
                f"___________________________________"
                f"______________________________________________"
                f"__________________")
            print(
                f"S.no.    Book I.D.            Author                       "
                f"Rental Price                          Book Name "
                f"                                      ")
            print(
                f"______________________________________________"
                f"___________________________________"
                f"______________________________________________"
                f"__________________")
            b = a.split(" ")
            w = 1
            while True:
                l = pickle.load(f)
                r0 = str(l[0]).split(" ")
                r1 = str(l[1]).split(" ")
                r2 = str(l[2]).split(" ")
                r3 = str(l[3]).split(" ")
                r4 = str(l[4]).split(" ")
                w1 = 0
                w2 = 0
                w3 = 0
                w4 = 0
                for i in r0:
                    for k in b:
                        if k == i:
                            print(
                                f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                f"     {l[2]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                                f"{' ' * (6 - len(l[4]))}{l[1]}")
                            w += 1
                            w1 += 1
                            w2 += 1
                            w3 += 1
                            w4 += 1

                for i in r1:
                    for k in b:
                        if k in i and w1 == 0 and len(k) != 0:
                            print(
                                f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                f"     {l[2]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                                f"{' ' * (6 - len(l[4]))}{l[1]}")
                            w += 1
                            w1 += 1
                            w2 += 1
                            w3 += 1
                            w4 += 1
                for i in r2:
                    for k in b:
                        if k in i and w2 == 0 and len(k) != 0:
                            print(
                                f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                f"     {l[2]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                                f"{' ' * (6 - len(l[4]))}{l[1]}{()}")
                            w += 1
                            w1 += 1
                            w2 += 1
                            w3 += 1
                            w4 += 1

                for i in r3:
                    for k in b:
                        if k == i and w3 == 0:
                            print(
                                f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                f"     {l[2]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                                f"{' ' * (6 - len(l[4]))}{l[1]}{()}")
                            w += 1
                            w1 += 1
                            w2 += 1
                            w3 += 1
                            w4 += 1
                for i in r4:
                    for k in b:
                        if k == i and w4 == 0:
                            print(
                                f"{w}.{' ' * (6 - len(str(w)))}  {l[0]}{' ' * (10 - len(l[0]))}"
                                f"     {l[2]}{' ' * (30 - len(l[2]))} ₹{l[3]}/week or ₹{l[4]}/month    "
                                f"{' ' * (6 - len(l[4]))}{l[1]}{()}")
                            w += 1
                            w1 += 1
                            w2 += 1
                            w3 += 1
                            w4 += 1
        except EOFError:
            if w == 2:
                print(
                    f"_________________________________________"
                    f"________________________________________"
                    f"_________________________________________"
                    f"_______________________")
                print(
                    f"                                                   "
                    f"{w - 1} book found in the library")
                print(
                    f"___________________________________________"
                    f"______________________________________"
                    f"____________________________________________"
                    f"____________________")

            elif w == 1:
                print(
                    f"                                                  "
                    f"Sorry book found in the library")
                print(
                    f"___________________________________________"
                    f"______________________________________"
                    f"___________________________________________"
                    f"_____________________")

            else:
                print(
                    f"_________________________________________"
                    f"________________________________________"
                    f"_________________________________________"
                    f"_______________________")
                print(
                    f"                                                   "
                    f"{w - 1} books found in the library")
                print(
                    f"_________________________________________"
                    f"________________________________________"
                    f"________________________________________"
                    f"________________________")
            print("Press [enter] to continue.")


# This function is for users to give book suggestions
def suggestion_box():
    bname = input(f"Enter name of the book:")
    author = input(f"Enter name of the Author:")
    name1 = input(f"Enter your name:")
    phone1 = int(input(f"Enter your phone no.:"))
    print(f"The name of the book: {bname}\n"
          f"The name of the Author: {author}\n"
          f"Your name: {name1}\n"
          f"Your phone no.: {phone1}\n")
    con = input(F"Do you want to continue[y/n]:")
    if con == "y" or con == "Y":
        with open("assets/files/Suggestion.dat", "ab") as f:
            l = [bname, author, name1, phone1]
            pickle.dump(l, f)

        print(f"Thank you for your Suggestion. You will be notified when the book is added to the library.")


# This function is used to start suggestion_box
def start():
    s = 0
    print("\nPress [Ctrl + 1] to continue or [Ctrl + q] to quit")
    while s < 1:
        if keyboard.is_pressed("Ctrl + 1"):
            print(f"\n+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+\n"
                  f"|W|E|L|C|O|M|E| |T|O| |S|U|G|G|E|S|T|I|O|N| |B|O|X|\n"
                  f"+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+ +-+-+-+")
            suggestion_box()
            s += 1
            break
        if keyboard.is_pressed("q"):
            print("Quiting...")
            break


# This function is used for generating reference numbers
def referenceno():
    with open("assets\\files\\lendbookdet.dat", "rb") as f:
        a = random.randint(10000000000, 99999999999)
        try:
            while True:
                l = pickle.load(f)
                if a == l[11]:
                    a += 1
                else:
                    pass
        except EOFError:
            return a


# This function will be accessed only by the admin to see all borrowed books
def readlendbook():
    w = []
    with open("assets\\files\\lendbook.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


# This function will be accessed only by the admin to read all suggestions
def suggestion():
    w = []
    with open("assets\\files\\Suggestion.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


# This function will be accessed only by the admin to see all borrowed books details
def lendbookdet():
    w = []
    with open("assets\\files\\lendbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


# This function will be accessed only by the admin to see all books details
def libbookdet():
    w = []
    with open("assets\\files\\libbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


# This function will be accessed only by the admin to see all readable books details
def readbookdet():
    w = []
    with open("assets\\files\\readbookdet.dat", "rb") as k:
        try:
            l = []
            while True:
                z = pickle.load(k)
                l.append(z)
                w = l
        except EOFError:
            pass
    return w


# This function will allow the user to read books without borrowing it
def readbook():
    name1 = input("Enter your name:")
    phone1 = int(input("Enter your number:"))
    date = str(datetime.datetime.now())
    book_id = input("Enter Book Id: ")
    s = 0
    with open("assets\\files\\booklist.dat", "rb") as f:
        try:
            while True:
                k = pickle.load(f)
                if k[0] == book_id and k[5] == "Yes":
                    subprocess.Popen([f"assets\\books\\{book_id}.pdf"], shell=True)  # This statement opens the pdf
                    l = [k[0], k[1], k[2], name1, phone1, date[0:10], date[11:19]]
                    with open("assets\\files\\readbookdet.dat", "ab") as t:
                        pickle.dump(l, t)
                    s += 1
        except EOFError:
            if s == 0:
                print("No book found")


print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
print("|W|E|L|C|O|M|E| |T|O| |X|Y|Z| |L|I|B|R|A|R|Y|")
print("+-+-+-+-+-+-+-+ +-+-+ +-+-+-+ +-+-+-+-+-+-+-+")
time.sleep(1)
while True:
    print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("|    * To view all books press    [Ctrl + 1]  |")
    print("|    * To borrow book press       [Ctrl + 2]  |")
    print("|    * To return/renew book press [Ctrl + 3]  |")
    print("|    * To search book press       [Ctrl + 4]  |")
    print("|    * To donate/add book press   [Ctrl + 5]  |")
    print("|    * To suggest book press      [Ctrl + 6]  |")
    print("|    * To read book press         [Ctrl + 7]  |")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    while True:
        if keyboard.is_pressed("Ctrl + 1"):
            book_list()
            time.sleep(1)
            while True:
                if keyboard.is_pressed("Enter"):
                    break
            break
        if keyboard.is_pressed("Ctrl + 2"):
            time.sleep(0.2)
            book_name = input("Enter Book Name or Book Id: ")
            time.sleep(0.2)
            name = input("Enter Your full name: ")
            lendbook(book_name, name)
            time.sleep(4)
            break
        if keyboard.is_pressed("Ctrl + 3"):
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("|    * To return book press       [Ctrl + 1]  |")
            print("|    * To renew book press        [Ctrl + 2]  |")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            while True:
                if keyboard.is_pressed("Ctrl + 1"):
                    ref = int(input("Enter Reference number: "))
                    name = input("Enter your full name: ")
                    phone = input("Enter your phone no.: ")
                    returnlend(ref, name, phone)
                    break
                if keyboard.is_pressed("Ctrl + 2"):
                    ref = int(input("Enter Reference number: "))
                    lendrenew(ref)
                    break
            time.sleep(4)
            break
        if keyboard.is_pressed("Ctrl + 4"):
            time.sleep(0.5)
            searchbook()
            time.sleep(2)
            while True:
                if keyboard.is_pressed("Enter"):
                    break
            break
        if keyboard.is_pressed("Ctrl + 5"):
            donation()
            time.sleep(3)
            break
        if keyboard.is_pressed("Ctrl + 6"):
            start()
            time.sleep(3)
            break
        if keyboard.is_pressed("Ctrl + 7"):
            readbook()
            break
        if keyboard.is_pressed("Ctrl + Shift + Alt + F1"):
            user = input("Enter user name:")
            password = input("Enter password:")
            if user == "xyz" and password == "1234":
                admin()
        if keyboard.is_pressed("Esc"):
            time.sleep(1)
            if keyboard.is_pressed("Esc"):
                break
    if keyboard.is_pressed("Esc"):
        time.sleep(2)
        if keyboard.is_pressed("Esc"):
            password = input("Enter password:")
            if password == "STOP":
                break
