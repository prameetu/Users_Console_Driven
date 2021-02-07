from DB_connector_func import DB

def menu_program():
    db = DB()
    while True:
        print('**************USERS--DIRECTORY************')
        print()
        print('1 FOR INSERTING NEW USER')
        print('2 FOR DELETING A USER')
        print('3 FOR UPDATING A USER')
        print('4 TO SEE ALL USERS ')
        print('5 TO EXIT PROGRAM')
        print()

        try:
            n = int(input())
            print()
            if n==1:
                uid = int(input('Enter user id: '))
                uname = input('Enter username: ')
                phone = input('Enter phone number: ')

                db.insert_data(uid,uname,phone)

            elif n==2:
                uid = int(input('Enter user id: '))
                db.delete_user(uid)

            elif n == 3:
                uid = int(input('Enter user id: '))
                uname = input('Enter new username: ')
                phone = input('Enter new phone number: ')

                db.update_user(uid,uname,phone)

            elif n == 4:
                db.fetch_all()
                print()

            elif n == 5:
                break
            else:
                print('Invalid Response ! Try Again  ')

        except Exception as e:
            print(e)
            print('An error occured ! TRY AGAIN !')
            print()


if __name__ == "__main__":
    menu_program()