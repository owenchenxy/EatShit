
from utility.sql_helper import MySQLHelper

class shop(object):
    def __init__(self):
        self.db=MySQLHelper('eatshit')
   
    def Add_Shops(self,shops):
        sql='insert into shop(name) values(%s)'
        params=shops
        self.db.Modify_Table_Many(sql, params)
  
    def Delete_Shops(self,shops):
        sql='delete from shop where name=%s'
        params=shops
        self.db.Modify_Table_Many(sql, params)
    
    def Get_Shops(self):
        sql='select * from shop'
        params=()
        shop_dict=self.db.Get_Data_Dict(sql, params)
        return shop_dict
'''
shop_lists=['Le Shu','He Fu Lao Mian','Wai Po Jia','Nan Jing Da Pai Dang','Hai Nan Ji','Yu Sheng Yuan','Su Xiao Liu','Ma Ma De Wei Dao',]
shop().Add_Shops(shop_lists)
'''