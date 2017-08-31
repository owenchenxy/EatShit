import time


def Get_Year():
    return str(time.localtime(time.time())[0])

def Get_Month():
    return str(time.localtime(time.time())[1])

def Get_Day():
    return str(time.localtime(time.time())[2]) 

def Get_Hour():
    return str(time.localtime(time.time())[3])

def Get_Date():
    return Get_Year()+'-'+Get_Month()+'-'+Get_Day()

