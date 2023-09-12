from userManagement.config.DataBaseConfig import DataBaseConfig
import pymysql.cursors

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        connection = DataBaseConfig.getConnection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        sql = f"""
insert into user_tb
values(0, %s, %s, %s, %s)
"""
        insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
        connection.commit()
        return insertCount
