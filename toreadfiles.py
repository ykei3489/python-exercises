phoneBook=[]

#if __name__=='__main__':
class personNum():
    def __init__(self,person):
        self.pnumber=pB.get(person)
        if self.pnumber!=None:
            print(person+'='+pB.get(person))
        else:
            print('Not found')
            #print(person+'='+pB.get(person))
with open('day8input.txt','r') as f:
        n=int(f.readline())
        print(n)
        #n=int(input())
    
        for i in range(n):
            arr=list(f.readline().split())
            phoneBook.append(arr)
        pB=dict(phoneBook)
        #print(pB)
        
        person=f.readline()
        
        ListofPerson=[]
        while person!='':
            ListofPerson.append(person.strip())
            person=f.readline()
        #print(ListofPerson)
        for i in ListofPerson:
            personNum(i)
        

#print(pB)


#print(phoneBook)
#print(pB)
#print(pB.keys())
##print(pB.values())

