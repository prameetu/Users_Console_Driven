import mysql.connector as msc

class DB:

    def __init__(self):
        self.con = msc.connect(host='localhost',
                               user='root',
                               password='11061106',
                               database = 'my_db')
        query = 'CREATE TABLE IF NOT EXISTS USER (user_id INT PRIMARY KEY,username varchar(20),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print('Created')

    def insert_data(self,userid, username, phone):
        query = f"""INSERT INTO user(user_id,username,phone)
                    VALUES ({userid},'{username}','{phone}')"""
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('User values saved to db')

    #fetch_all
    def fetch_all(self):
        query = f''' SELECT * FROM user'''
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f'USER_ID:{row[0]}   NAME:{row[1]}    PHONE : {row[2]}')

    def delete_user(self,user_id):
        query = f'''DELETE FROM user
                    WHERE user_id = {user_id}'''
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Deleted')

    def update_user(self,user_id,username,phone):
        query = f''' UPDATE user
                      SET
                        username = '{username}',
                        phone = '{phone}' 
                      WHERE user_id = {user_id}'''
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Record updated')
