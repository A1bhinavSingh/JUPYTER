import pyjokes
import time
from PIL import Image
from translate import Translator
from playsound import playsound
from gtts import gTTS
import webbrowser
import wikipedia
import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty('rate', 150) 
def browser(s):
    str0=s
    lit=[" ",",","."]
    li=str0.split("open")
    str1=li[1].strip()
    str1=str1
    for i in lit:
      str2=str1.split(i)
      str2[0]=str2[0]
    print("opening your website...")
    playsound("val34.mp3")
    website="https://www."+str2[0]+".com/"
    webbrowser.open(website)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

time.ctime()
str=time.ctime()
tme=(str[11:13])
hour=int(tme)
min=str[14:16]
min=int(min)
if hour<=12:
    print("Good Morning")
    playsound("morning.mp3")
    
elif( hour>=12 and min> 0 ) and( hour<=18 ):
    print("Good Afternoon")
    playsound("afternoon.mp3")
    
elif hour>18 and min>0:
    print("Good Evening")
    playsound("evening.mp3")

def jokes():
 print("Ok..but I\'m very bad at this.Here is your joke")
 playsound("jok1.mp3")
 playsound("hj.mp3")
 time.sleep(1)
 jok=pyjokes.get_joke()
 print(jok)
 speak(jok)
def wiki(a):
 #a=input("What you want to search?\n")
 try:
  a=a.lower()
  if "search" in a:
    a=a.replace("search","")
    print("You are searching")
    playsound("se.mp3")
    print(a)
    time.sleep(1)
    print("Searching wikipedia....\n")
    playsound("wi.mp3")
    print(wikipedia.summary(a, sentences=2))
    playsound("res.mp3")
    speak(wikipedia.summary(a,sentences=2))
  else:
     print("Please enter a valid command")
     playsound("pl.mp3")
 except:
     print("Cannot connect Wikipedia at the moment")
     playsound("er.mp3")
def image():
  img=Image.open("./download.png")
  print("Ok.But I can only show you the image of PIKACHU..and here is your image")
  playsound("pics1.mp3")
  time.sleep(1)
  return img.show()
  
def tym():
      s=time.time()
      local_tym=time.ctime(s)
      print('Here is your time')
      playsound("tim.mp3")
      print(local_tym)
      speak(local_tym)
def lang(): 
   dict={1:"en",2:"es",3:"pt",4:"zh",5:"ja"}
   time.sleep(0.8)
   print("I can translate your words into five different languges.please type OK to continue")
   playsound("tr.mp3")
   a1= input()
   s=a1.lower()
   if s.count("ok")>0 or s.count("show"):
    time.sleep(1)
    print("OK so..\n enter 1 for english\n 2 for spanish\n 3 for portuguese\n 4 for chinese \n 5 for japanese\n")
    playsound("op.mp3")
    a= int(input())
   x=dict[a]
   y=to_lang=x
   t= Translator(y)
   print("Enter text to translate")
   playsound("tran.mp3")
   b= input()
   print("Here is the translated version")
   playsound("yo.mp3")
   ta=t.translate(b)
   print(ta)
   speak(ta)
   

def love():
 l=[" d88b.d88b","88888888888 "," Y8888888Y","  Y88888Y","   Y888Y","    Y8Y","     Y"]
 for i in l:
     print("                 ",end="")
     print(i)
 time.sleep(1.1)
 print("I Love You too")
 a="i love you too"
 n=len(a)
 x=n/2
 
 for i in range(n):
  for j in range(n):
   if i==0 or i==n-1 or j==0 or j== n-1:
    print("*.*",end=" ")
   elif i==x and j==x:
    print()
    print(love())
    print("                 "+"I Love You ")
   else:
    print(" ",end=" ")
  print()
  break

def talk():
 import random
 li=["Do you have any pets?",
"What's your favorite food?",
"How old are you?",
"What are your hobbies?",
"Would you like to be famous?",
"What is your goal in life?",
"What was the last book you read?",
"Do you like to cook?",
"What is your favorite way to waste time?"
]
 li2=["nice ","I like that too..","You are pretty young and cute","That is really good hobby","Awesome","Hope you achieve it my friend","It is very good book","Hope you will invite me some day "," Haha..That is so cool"]
 li3=["qu1.mp3","qu2.mp3","qu3.mp3","qu4.mp3","qu5.mp3","qu6.mp3","qu7.mp3","qu8.mp3","qu9.mp3"]
 li4=["an1.mp3","an2.mp3","an3.mp3","an4.mp3","an5.mp3","an6.mp3","an7.mp3","an8.mp3","an9.mp3"]
 l=len(li)
 b=l
 li1=[]
 print("Ok then tell me..")
 playsound("ok1.mp3")
 time.sleep(1.1)
 for i in range(b):
  time.sleep(0.25)
  c=random.randint(0,8)
  li1.append(c)
  if li1.count(c)>1:
      continue
  else:
   print(li[c])
   playsound(li3[c])
   s=input("")
   s1=s.lower()
   if "no" in s1 or "nothing" in s1 or"none" in s1:
       time.sleep(1)
       print("Ok..let\'s continue")
       playsound("ok1.mp3")
   elif "bye" in s1:
        time.sleep(1)
        print("It was nice talking to you..")
        playsound("nicetalk.mp3")
        break
   else:
     time.sleep(1.1)
     print(li2[c])
     playsound(li4[c])
 else:
     print("I am out of questions my friend..!! Bye Pal... Have a good day.. :-)")
     playsound("nicetalk2.mp3")
 return ":-)"

print(" I\'m  Aadya ")
playsound("ad.mp3")
print("What is your name..?",end=" ")
time.sleep(0.2)
playsound("getname.mp3")
que=input()
print("Glad to meet you",end=" ")
qu=que.title()

li=list(qu.split(" "))
while(True):
 if "Is" in li:
  c=li.index("Is")
  name=li[c+1]
  print(name)
  time.sleep(0.2)
  playsound("greet.mp3")
  speak(name)
  break
 elif "Am" in li and "Called" in li:
     c=li.index("Called")
     name=li[c+1]
     print(name)
     time.sleep(0.2)
     playsound("greet.mp3")
     speak(name)
     break
 elif "Call" in li and "Me"  in li:
  c=li.index("Me")
  name=li[c+1]
  print(name)
  time.sleep(0.2)
  playsound("greet.mp3")
  speak(name)
  break
 elif  "Am" in li:
  c=li.index("Am")
  name=li[c+1]
  print(name)
  time.sleep(0.2)
  playsound("greet.mp3")
  speak(name)
  break
 elif "It'S" in li:
  c=li.index("It'S")
  name=li[c+1]
  print(name)
  time.sleep(0.2)
  playsound("greet.mp3")
  speak(name)
  break
 elif "I\'M" in li:
  c=li.index("I\'M")
  name=li[c+1]
  print(name)
  time.sleep(0.2)
  playsound("greet.mp3")
  speak(name)
  break
 else:
    name=li[0]
    print(name)
    time.sleep(0.2)
    playsound("greet.mp3")
    speak(name)
    break

i=1
while True:
 if i==1:
  print("What can I do for you..?",end=" ")
  time.sleep(0.2)
  playsound("do.mp3")
  a= input()
  s=a.lower()
 elif i==2:
     time.sleep(1)
     print("What else can I do for you..?")
     playsound("doing.mp3")
     a= input()
     s=a.lower()
 else:
     print("Ok...")
     playsound("ok.mp3")
 if s.count("pic")>0 or s.count("pics")>0:
        print(image())
        i=2
        continue
 elif s.count("open")>0:
   browser(s) 
   i=2
   continue
 elif s.count("sing")>0:
     playsound("gulabi.mp3")
     i=2
     continue
 elif s.count("joke")>0 or s.count("jokes")>0:
         jokes()
         time.sleep(1.4)
         print("I know that was really bad joke so let\'s move on")
         playsound("bad.mp3")
         i=2
         continue
 elif s.count("time")>0:
         tym()
         i=2
         continue
 elif s.count("speak")>0 or s.count("translate")>0:
         lang()
         i=2
         continue
 elif s.count("love")>0:
         print(love())
         playsound("love.mp3")
         i=2
         continue
 elif s.count("talk")>0:
      print(talk())
      i=2
      continue
 elif s.count("search")>0:
     wiki(s)
     continue
 elif s.count("bye")>0 or s.count("nothing") or "exit" in s:
          if  hour<=12 or ( hour>=12 and min> 0 ) and( hour<=18 ):
           print("Ok..bye then..Have a good day..!!")
           playsound("bye1.mp3")
           break
          else:
              print("Ok..Bye\nGood Night")
              playsound("ni8.mp3")
 elif s.count("love")>0:
         playsound("love.mp3")
         print(love())
         continue
 if s.count("do")>0 or s.count("list")>0:
     print(" I can sing \n I can show you pics\n I can tell you jokes\n I can show you time\n Can speak 5 different languages\n If you want we can talk\n I can even open sites \n And can search wikipedia for you")
     time.sleep(0.2)
     speak(" I can sing I can show you pics I can tell you jokes I can show you time Can speak 5 different languages If you want we can talk I can even open sites And can search wikipedia for you")
     a= input()
     s=a.lower()
     if s.count("pic")>0 or s.count("pics")>0:
        image()
        i=2
        continue
     elif s.count("open")>0:
          browser(s)
          i=2
          continue
     elif s.count("sing")>0:
           playsound("gulabi.mp3")
           i=2
           continue
     elif s.count("joke")>0 or s.count("jokes")>0:
         jokes()
         time.sleep(1.4)
         print("I know that was really bad joke so let\'s move on")
         playsound("bad.mp3")
         i=2
         continue
     elif s.count("time")>0:
         tym()
         i=2
         continue
     elif s.count("speak")>0 or "translate" in s:
         lang()
         i=2
         continue
     elif s.count("love")>0:
         print(love())
         playsound("love.mp3")
         i=2
         continue
     elif s.count("talk")>0:
      print(talk())
      i=2
      continue
     elif s.count("search")>0:
      wiki(s)
      continue
     elif s.count("bye")>0 or s.count("nothing") or "exit" in s:
      if  hour<=12 or ( hour>=12 and min> 0 ) and( hour<=18 ):
           print("Ok..bye then..Have a good day..!!")
           playsound("bye1.mp3")
           break
      else:
              print("Ok..Bye\nGood Night")
              playsound("ni8.mp3")
              break
     else:
      print("UNIDENTIFIED COMMAND.\nPlease enter a valid command or type \"exit\"")
      playsound("ex.mp3")
      a=input()
      s=a.lower()
      if "exit" in s:
       if  hour<=12 or ( hour>=12 and min> 0 ) and( hour<=18 ):
           print("Ok..bye then..Have a good day..!!")
           playsound("bye1.mp3")
           break
       else:
              print("Ok..Bye\nGood Night")
              playsound("ni8.mp3")
              break
 else:
     print("UNIDENTIFIED COMMAND.\nPlease enter a valid command or type \"exit\"")
     playsound("ex.mp3")
     a=input()
     s=a.lower()
     if "exit" in s:
      if  hour<=12 or ( hour>=12 and min> 0 ) and( hour<=18 ):
           print("Ok..bye then..Have a good day..!!")
           playsound("bye1.mp3")
           break
      else:
              print("Ok..Bye\nGood Night")
              playsound("ni8.mp3")
              break
     else:
         i=0
         continue

