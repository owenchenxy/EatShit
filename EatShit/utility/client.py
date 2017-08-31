from model.vote import vote
import Time
from conf import voter
from model.shop import shop

def Print_Voters():
    print 'participants:',
    for i in vote().Get_Voter_list():
        print i+',',

def Print_Vote_Progress(end=False):
    shop_list=shop().Get_Shops()
    print '%s%s%s'%('ID'.ljust(3),'Resturant'.center(40),'Count'.ljust(3))
    vote_result=0
    vote_shop=[]
    for shops in shop_list:
        shop_id=shops['id']
        shop_name=shops['name']
        vote_result_tmp=vote().Get_Vote_Count(int(shop_id))
        if vote_result_tmp>vote_result:
            vote_result=vote_result_tmp
            vote_shop=[shop_name]
        elif vote_result_tmp==vote_result:
            vote_shop.append(shop_name)
        else:
            pass
        print '%s%s%s'%(str(shop_id).ljust(8),shop_name.ljust(30),str(vote_result_tmp).center(3))
    Print_Voters()
    if end:                            
        print 'Voting Result:'
        if vote_result==0:
            print "###No one has yet voted###"
        else:
            for i in vote_shop:
                print i
        Print_Voters()
        #print str(shop_id)+"\t"+shop_name+"\t"+str(vote_result) 
        
def Print_Shop_List():
    shop_list=shop().Get_Shops()
    #print shop_list
    for item in shop_list:
        ID=item['id']
        NAME=item['name']
        print str(ID)+'\t'+NAME
        #print str(ID)+'\t'+str(NAME)
def Show_Current_Progress():
    print "Show current voting progress?(y/n)"
    a=raw_input()
    if a=='n' or a=='N':
        pass
    else:
        Print_Vote_Progress()
    print "\nResult will be realsed after 11:00AM. Please come then."   
         
def client():
    while True:
        if int(Time.Get_Hour())>=11:
            Print_Vote_Progress(True)
        else:
            if vote().Search_Record(voter):
                print "You have already voted for today. Please come tommorrow"
                a=raw_input("would you re-vote?(y/n)")
                if a=='y' or a=='Y':
                    vote().Regret_Vote()
                    continue
                else:
                    pass
                Show_Current_Progress()
                
            else: 
                Print_Shop_List()
                choice=raw_input('What is your choice?')
                vote().Add_Record(choice,voter)  
                Show_Current_Progress()
        break        
                
        

