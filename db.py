import yaml
import pymysql.cursors
import warnings
import pymysql
from pathlib import Path
import os

class DB:
    def __init__(self):
        config = {}
        cwd = Path(os.path.abspath(__file__)).parent
        with  (cwd / Path('config/config.yml')).open('r') as f:
            config = yaml.load(f)
        self.config = config['db']

        self.connection = pymysql.connect(host=config["db"]["host"],
                                          user=config["db"]["user"],
                                          password=config["db"]["password"],
                                          db=config["db"]["database"],
                                          charset=config["db"]["charset"],
                                          cursorclass=pymysql.cursors.DictCursor)

    def insertUserInfomation(self, info, table_name = 'users'):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with self.connection.cursor() as cursor:
                column = " (name, category, twitter, instagram, facebook, homepage, coinprism)"
                sql = 'INSERT IGNORE INTO '+ table_name + column +' VALUES (%s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql,info)
                self.connection.commit()

    def __del__(self):
        self.connection.close()