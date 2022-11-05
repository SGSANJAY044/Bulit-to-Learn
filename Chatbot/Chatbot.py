from random import randint
from nltk.corpus import wordnet
def greet_random():
    greetings=["Hi","Hello","Vanakam","Hey","Yo","Dude!","Welcome","Tell me what do you want","Good Evening","Namastea","What’s up?","What’s new?","It’s nice to meet you","Good to see you ","Hiya!"]
    return greetings[randint(0,len(greetings)-1)]
print(greet_random())
while True:
    msg=input()
    msg_sp=msg.split()
    if msg in "quit exit bye tata varta_mama":
        break
    elif "add" in msg:
        result=0
        for i in range(1,len(msg_sp)):
            result+=float(msg_sp[i])
        print(result)
    elif "subtract" in msg:
        result=float(msg_sp[1])
        for i in range(2,len(msg_sp)):
            result-=float(msg_sp[i])
        print(result)
    elif "multiply" in msg:
        result=1
        for i in range(1,len(msg_sp)):
            result*=float(msg_sp[i])
        print(result)
    elif "divide" in msg:
        result=float(msg_sp[1])
        for i in range(2,len(msg_sp)):
            result/=float(msg_sp[i])
        print(result)
    elif "what" in msg:
        syns = wordnet.synsets(msg_sp[2])
        print(syns[0].lemmas()[0].name())
    elif "define" in msg:
        syns = wordnet.synsets(msg_sp[2])
        print(syns[0].definition())