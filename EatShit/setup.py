
voter=raw_input('Please tell me your name:')
with open('.\conf.py','wb') as f:
    f.write("voter='%s'\n"%voter)
    f.write("db_ip='10.32.233.50'")
