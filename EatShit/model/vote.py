

from utility.sql_helper import MySQLHelper
from utility import Time
import conf
class vote(object):
    def __init__(self):
        self.db=MySQLHelper('eatshit')
    
        
    def Add_Record(self,v,voter):  
        sql='insert into vote(id,date,voter) values(%s,%s,%s)'
        params=(v,Time.Get_Date(),voter)
        self.db.Modify_Table_One(sql, params)
        
    def Search_Record(self,voter):
        sql='select * from vote where date=%s and voter=%s'
        params=(Time.Get_Date(),voter)
        if self.db.Get_Data_One(sql, params):
            return True
        else:
            return False
    
    def Get_Vote_Count(self,shop_id):
        sql="select count(*) from vote where date=%s and id=%s"
        params=(Time.Get_Date(),shop_id)
        count=self.db.Get_Data_One(sql, params)['count(*)']
        return count
    
    def Get_Voter_list(self):
        sql="select voter from vote where date=%s"
        params=(Time.Get_Date(),)
        voter_dict_list=self.db.Get_Data_Dict(sql, params)
        voter_list=list()
        for item in voter_dict_list:
            voter_list.append(item['voter'])
        return voter_list
    
    def Regret_Vote(self):
        sql="delete from vote where voter=%s" 
        params=(conf.voter,)
        self.db.Modify_Table_One(sql, params)

#vote().Add_Record(1)  
#print vote().Get_Vote_Count(1)

