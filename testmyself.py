str1="Watching my grandparents and my parents pay all these bills, really excites me for the future. -___- "

def cut_sentence(str1):
    count=len(str1.split())
    block=""
    listn=[]
    for c in range(0,count):
        save=str1.split(' ',1)[0]
        str1= str1.split(' ',1)[1]
        block=block+' '+save

        print([block]+[str1])




cut_sentence(str1)