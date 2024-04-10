import sqlite3
import random

data = sqlite3.connect("data.db")
sql = data.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS DATA(
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            login VARCHAR(50),
                                            password INTEGER,
                                            balance INTEGER)""")
while True:
    query1 = int(input("(1)Sign In (2)Sign Up: "))
    if query1 == 1:
        sign = input("enter your login: ")
        login_pass = int(input("enter you password: "))
        cash = int(input("How much cash money? "))
        sql.execute(f"INSERT INTO data(login,password, balance) VALUES('{sign}', '{login_pass}', '{cash}')")
        data.commit()
        print("Success your login")
    elif query1 == 2:
        enter_login = int(input("enter your password"))
        try:
            sql.execute(f"SELECT password FROM data WHERE password = {enter_login}")
            if enter_login in sql.fetchone():
                while True:
                    query = int(input("(1)Play Game (2)Delete Your Profile (3)Check Balance, (4) Exit: "))
                    if query == 1:
                        sql.execute(f"SELECT balance FROM data WHERE password = {enter_login} ")
                        if sql.fetchone()[0] > 0:
                            money_put = int(input("how much money do you put in: "))
                            sql.execute(f"SELECT balance FROM data WHERE password = {enter_login} ")
                            if sql.fetchone()[0] > money_put:
                                guess = int(input("guess the number 1, 6"))
                                random_num = random.randint(1, 6)
                                if guess > random_num or guess < random_num:
                                    sql.execute(f"UPDATE data SET balance = balance- {money_put} WHERE password = {enter_login} ")
                                    data.commit()
                                    sql.execute(f"SELECT balance FROM data WHERE password = {enter_login}")
                                    print(f"You lost {money_put}  of money")
                                    print(f" There is ${sql.fetchone()[0]} in the balance: ")
                                else:
                                    sql.execute(f"UPDATE data SET balance = balance+{money_put*2} WHERE password = {enter_login} ")
                                    data.commit()
                                    sql.execute(f"SELECT balance FROM data WHERE password = {enter_login}")
                                    print(f"The money you put in doubled")
                                    print(f" There is ${sql.fetchone()[0]} in the balance: ")
                            else:
                                print("There is not enough balance in your account")
                    elif query == 2:
                        sql.execute("DELETE FROM data WHERE id=2")
                        data.commit()
                        print("Success your profile delete")
                    elif query == 3:
                        sql.execute(f"SELECT balance FROM data WHERE password = {enter_login} ")
                        print(f"You have ${sql.fetchone()[0]} in your balance ")
                    elif query == 4:
                        print("Hope to see you again")
                        break
        except TypeError:
            print("Password Incorrect")
