from tkinter import *
import turtle as t
from tkinter import ttk
import random

#french - words
def freWindow():
    freWindow=Toplevel()
    freWindow.title("Words | French")
    freWindow.geometry("1080x800")
    freWindow.configure(bg="lightcoral")

    canvas=Canvas(freWindow,width=150,height=100,bg="lightyellow")
    text=canvas.create_text(80,50,text="I'M SORRY",fill="black",font=("Helvetica 10 bold"))
    label=Label(freWindow,text="Je suis desole",bg="black",fg="white",font=("MSSerif 13"))
    canvas.grid(row=1,column=1,pady=10,padx=60)
    label.grid(row=2,column=1,pady=10,padx=60)

    canvas1=Canvas(freWindow,width=150,height=100,bg="mistyrose")
    '''line1=canvas1.create_line(60,20,20,60,fill="black",width=5)'''
    text1=canvas1.create_text(80,50,text="MY NAME IS Amina",fill="black",font=("Helvetica 10 bold"))
    label1=Label(freWindow,text="Je m'apple Amina",bg="black",fg="white",font=("MSSerif 13"))
    canvas1.grid(row=4,column=1,pady=10,padx=60)
    label1.grid(row=5,column=1,pady=10,padx=60)

    canvas2=Canvas(freWindow,width=150,height=100,bg="hotpink")
    '''rec2=canvas2.create_rectangle(90,90,10,10,fill="pink")'''
    text2=canvas2.create_text(80,50,text="HOW ARE YOU?",fill="black",font=("Helvetica 10 bold"))
    label2=Label(freWindow,text="Comment allez-vous?",bg="black",fg="white",font=("MSSerif 13"))
    canvas2.grid(row=7,column=1,pady=10,padx=60)
    label2.grid(row=8,column=1,pady=10,padx=60)
   

    canvas3=Canvas(freWindow,width=150,height=100,bg="cyan")
    text3=canvas3.create_text(80,50,text="WOMEN",fill="black",font=("Helvetica 10 bold"))
    label3=Label(freWindow,text="Femme",bg="black",fg="white",font=("MSSerif 13"))
    canvas3.grid(row=1,column=2,pady=10,padx=60)
    label3.grid(row=2,column=2,pady=10,padx=60)
        
    canvas4=Canvas(freWindow,width=150,height=100,bg="seashell")
    text4=canvas4.create_text(80,50,text="SEE YOU LATER",fill="black",font=("Helvetica 10 bold"))
    label4=Label(freWindow,text="A tout a l'heure",bg="black",fg="white",font=("MSSerif 13"))
    canvas4.grid(row=4,column=2,pady=10,padx=60)
    label4.grid(row=5,column=2,pady=10,padx=60)

    canvas5=Canvas(freWindow,width=150,height=100,bg="tomato")
    text5=canvas5.create_text(80,50,text="HOW MUCH IS THIS?",fill="black",font=("Helvetica 10 bold"))
    label5=Label(freWindow,text="Combien ca coute",bg="black",fg="white",font=("MSSerif 13"))
    canvas5.grid(row=7,column=2,pady=10,padx=60)
    label5.grid(row=8,column=2,pady=10,padx=60)
    
    canvas6=Canvas(freWindow,width=150,height=100,bg="white")
    text6=canvas6.create_text(80,50,text="HELLO",fill="black",font=("Helvetica 10 bold"))
    label6=Label(freWindow,text="BONJOUR",bg="black",fg="white",font=("MSSerif 13"))
    canvas6.grid(row=1,column=3,pady=10,padx=60)
    label6.grid(row=2,column=3,pady=10,padx=60)
         
    canvas7=Canvas(freWindow,width=150,height=100,bg="lemon chiffon")
    text7=canvas7.create_text(80,50,text="THANK YOU",fill="black",font=("Helvetica 10 bold"))
    label7=Label(freWindow,text="Merci",bg="black",fg="white",font=("MSSerif 13"))
    canvas7.grid(row=4,column=3,pady=10,padx=60)
    label7.grid(row=5,column=3,pady=10,padx=60)

    canvas8=Canvas(freWindow,width=150,height=100,bg="aquamarine")
    text8=canvas8.create_text(80,50,text="GOOD BYE",fill="black",font=("Helvetica 10 bold"))
    label8=Label(freWindow,text="Au Revoir",bg="black",fg="white",font=("MSSerif 13"))
    canvas8.grid(row=7,column=3,pady=10,padx=60)
    label8.grid(row=8,column=3,pady=10,padx=60)
    
    canvas9=Canvas(freWindow,width=150,height=100,bg="aquamarine")
    text9=canvas9.create_text(80,50,text="EXCUSE ME",fill="black",font=("Helvetica 10 bold"))
    label9=Label(freWindow,text="Excusez-moi",bg="black",fg="white",font=("MSSerif 13"))
    canvas9.grid(row=1,column=4,pady=10,padx=60)
    label9.grid(row=2,column=4,pady=10,padx=60)
         
    canvas10=Canvas(freWindow,width=150,height=100,bg="mediumvioletred")
    text10=canvas10.create_text(80,50,text="BEAUTIFUL",fill="black",font=("Helvetica 10 bold"))
    label10=Label(freWindow,text="Belle",bg="black",fg="white",font=("MSSerif 13"))
    canvas10.grid(row=4,column=4,pady=10,padx=60)
    label10.grid(row=5,column=4,pady=10,padx=60)

    canvas11=Canvas(freWindow,width=150,height=100,bg="red")
    text11=canvas11.create_text(80,50,text="LOVE",fill="black",font=("Helvetica 10 bold"))
    label11=Label(freWindow,text="Amour",bg="black",fg="white",font=("MSSerif 13"))
    canvas11.grid(row=7,column=4,pady=10,padx=60)
    label11.grid(row=8,column=4,pady=10,padx=60)

    
    canvas12=Canvas(freWindow,width=150,height=100,bg="plum")
    text12=canvas12.create_text(80,50,text="GOOD NIGHT",fill="black",font=("Helvetica 10 bold"))
    label12=Label(freWindow,text="Bonne nuit",bg="black",fg="white",font=("MSSerif 13"))
    canvas12.grid(row=1,column=5,pady=10,padx=60)
    label12.grid(row=2,column=5,pady=10,padx=60)
    
     
    canvas13=Canvas(freWindow,width=150,height=100,bg="peachpuff")
    text13=canvas13.create_text(80,50,text="YOU'RE WELCOME",fill="black",font=("Helvetica 10 bold"))
    label13=Label(freWindow,text="Je vous en prie",bg="black",fg="white",font=("MSSerif 13"))
    canvas13.grid(row=4,column=5,pady=10,padx=60)
    label13.grid(row=5,column=5,pady=10,padx=60)

    canvas14=Canvas(freWindow,width=150,height=100,bg="lightsalmon")
    text14=canvas14.create_text(80,50,text="TIME",fill="black",font=("Helvetica 10 bold"))
    label14=Label(freWindow,text="Temps",bg="black",fg="white",font=("MSSerif 13"))
    canvas14.grid(row=7,column=5,pady=10,padx=60)
    label14.grid(row=8,column=5,pady=10,padx=60)

    next=Button(freWindow,text="NEXT",bg="white",fg="crimson",height=3,width=15,font=myfont,command=freWindow2)
    next.grid(row=10,column=3,pady=40)

#drawing all shapes in canvas
class Shapes:
    def __init__(self,canvas):
        self.canvas=canvas
        
    def circle(self):
        draw=t.RawTurtle(self.canvas)
        draw.begin_fill()
        draw.color("crimson")
        draw.circle(20)
        draw.end_fill()

    def square(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(-50,-30)
        draw.pendown()
        draw.begin_fill()
        draw.color("purple")
        draw.forward(100)
        draw.left(90)
        draw.forward(100)
        draw.left(90)
        draw.forward(100)
        draw.left(90)
        draw.forward(100)
        draw.left(90)
        draw.end_fill()

    def triangle(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(-50,-30)
        draw.pendown()
        draw.begin_fill()
        draw.color("navy")
        draw.forward(100)
        draw.left(120)
        draw.forward(100)
        draw.left(120)
        draw.forward(100)
        draw.end_fill()

    def star(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(-50,0)
        draw.pendown()
        draw.begin_fill()
        draw.color("teal")
        for i in range(5):
            draw.forward(100)
            draw.right(144)
        draw.end_fill()

    def moon(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(0,-100)
        draw.pendown()
        draw.begin_fill()
        draw.color("yellow")
        draw.circle(70)
        draw.end_fill()

        draw.penup()
        draw.goto(-50,-100)
        draw.pendown()
        draw.begin_fill()
        draw.color("white")
        draw.circle(70)
        draw.end_fill()

    def line(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(-50,-30)
        draw.pendown()
        draw.forward(100)
        
    def diamond(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(0,-50)
        draw.pendown()
        draw.begin_fill()
        draw.color("black")
        draw.circle(70,steps=4)
        draw.end_fill()

    def hexagon(self):
        draw=t.RawTurtle(self.canvas)
        draw.penup()
        draw.goto(0,-50)
        draw.pendown()
        draw.begin_fill()
        draw.color("darkred")
        draw.circle(70,steps=6)
        draw.end_fill()

#french - shapes
def freWindow2():
    freWindow2=Toplevel()
    freWindow2.title("Shapes | French")
    freWindow2.geometry("1080x700")

    lbl0 = Label(freWindow2,text="SHAPES AND COLORS",bg="yellow",font=("Arial 12"))
    lbl0.grid(row=0,column=2,pady=10,padx=30)
    
    #circle
    canva=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    label=Label(freWindow2,text="Cercle | Rouge",bg="black",fg="white",font=("MSSerif 13"))
    label.grid(row=2,column=1,pady=10,padx=30)
    canva.grid(row=1,column=1,pady=10,padx=30)
    freWin=Shapes(canva)
    freWin.circle()
    
    #square
    canva1=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    #draw=t.RawTurtle(canva1)
    canva1.grid(row=4,column=1,pady=10,padx=30)
    label1=Label(freWindow2,text="Carre | Violette",bg="black",fg="white",font=("MSSerif 13"))
    label1.grid(row=5,column=1,pady=10,padx=30)
    freWin=Shapes(canva1)
    freWin.square()
    
    #triangle
    canva2=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva2.grid(row=1,column=2,pady=10,padx=30)
    label2=Label(freWindow2,text="Triangle | Bleu",bg="black",fg="white",font=("MSSerif 13"))
    label2.grid(row=2,column=2,pady=10,padx=30)
    freWin=Shapes(canva2)
    freWin.triangle()
    
    #star
    canva3=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva3.grid(row=4,column=2,pady=10,padx=30)
    label3=Label(freWindow2,text="Debut | Vert",bg="black",fg="white",font=("MSSerif 13"))
    label3.grid(row=5,column=2,pady=10,padx=30)
    freWin=Shapes(canva3)
    freWin.star()
    
    #moon
    canva4=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva4.grid(row=1,column=3,pady=10,padx=30)
    label4=Label(freWindow2,text="Lune | Jaune",bg="black",fg="white",font=("MSSerif 13"))
    label4.grid(row=2,column=3,pady=10,padx=30)
    freWin=Shapes(canva4)
    freWin.moon()

    #line
    canva6=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva6.grid(row=4,column=3,pady=10,padx=30)
    label6=Label(freWindow2,text="Ligne ",bg="black",fg="white",font=("MSSerif 13"))
    label6.grid(row=5,column=3,pady=10,padx=30)
    freWin=Shapes(canva6)
    freWin.line()

    #diamond
    canva7=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva7.grid(row=1,column=4,pady=10,padx=30)
    label7=Label(freWindow2,text="Diamant | Brun",bg="black",fg="white",font=("MSSerif 13"))
    label7.grid(row=2,column=4,pady=10,padx=30)
    freWin=Shapes(canva7)
    freWin.diamond()
    
    #hexagon
    canva8=Canvas(freWindow2,width=200,height=200,bg="lightyellow")
    canva8.grid(row=4,column=4,pady=10,padx=30)
    label8=Label(freWindow2,text="Hexagone | Noir",bg="black",fg="white",font=("MSSerif 13"))
    label8.grid(row=5,column=4,pady=10,padx=30)
    freWin=Shapes(canva8)
    freWin.hexagon()

    list1=[canva,canva1,canva2,canva3,canva4,canva6,canva7,canva8]
    start=Button(freWindow2,text="START",bg="white",fg="navy",height=3,width=15,font=myfont,command=fc.flashcard0)
    start.grid(row=10,column=3)

global ans,ques, q_list

ques=[
    ("circle","Cercle"),("square","Carre"),("triangle","Triangle"),
    ("red","Rouge"),("blue","Bleu"),("yellow","Jaune"),("white","Blanc"),
    ("green","Vert"),("i'm sorry","Je suis desole"),("how are you?","Comment allez-vous"),
    ("thank you","Merci"),("excuse me","Excusez-moi"),("youre welcome","Je vous en price"),
    ("beautiful","belle"),("how much is this?","Combien ca coute")
    ]
random.shuffle(ques)

#temporary list for questions
q_list=[] + ques

#print("ques:",ques)
#print("qlist",q_list)
score=0
#list for storing answers from checkbutton
ans=['']
count=0

class Flash:

    def flashcard0(self):
        self.flashcard0 = Toplevel(window)
        self.flashcard0.title("Start")
        self.flashcard0.geometry("300x300")
        self.flashcard0.config(bg="blue")
        self.options = ['5','10','15']
        Label(self.flashcard0,text="Select number of questions:",font=("Arial 15"),fg="white",bg="blue").grid(row=0,column=1,padx=20,pady=20)
        
        self.clicked = StringVar()
        #dropdown list
        self.clicked.set(self.options[0])
        self.opt = OptionMenu(self.flashcard0,self.clicked, *self.options)
        self.choice=self.clicked.get()
        #print("self.choice",self.choice)
        
        self.sel = Button(self.flashcard0,text="Select",command=self.flashcard,fg="white",bg="black",font=("Ariel 15"))
        self.opt.grid(row=1,column=1,padx=10,pady=10)
        self.sel.grid(row=2,column=1,padx=10,pady=10)
        self.flashcard0.mainloop()

    def onCheck(self,chk,var0):
        if var0 > 0:
            ans[0] = chk["text"]
        else:
            ans[0]=''
        #print(var0,"\nans:",ans[0],"\nchk:",chk["text"])
        
    def checkAns(self):
        self.answerb.config(state=DISABLED)
        global score
        #print("\nans:",ans[0],"\ques:",q_list[rands][1],rands)
        if ans[0] == q_list[rands][1]:
            ans_lb.config(text="Correct Answer!!!")
            score+=1
            #print("score:",score)
        else:
            ans_lb.config(text="Incorrect Answer!!")
        q_list.remove(q_list[rands])
            
    def start(self):
        self.answerb = Button(self.flashcard, text="SUBMIT",command=self.checkAns,bg="yellow",font=("Arial 12"))
        self.answerb.grid(row=5,column=1,padx=30,pady=30)

        self.next = Button(self.flashcard, text="NEXT >",command=self.nextQues,bg="lightyellow",font=("Arial 12"))
        self.next.grid(row=5,column=2,padx=30,pady=30)

        self.startb.destroy()
        self.nextQues()
        
        
    def nextQues(self):
        global rands,count, chk1, chk2, chk3

        if count < int(self.choice):
            
            if count > 0:
                #checkbutton deleted for every questions
                chk1.destroy()
                chk2.destroy()
                chk3.destroy()
                
            #enable answer button
            self.answerb.config(state=ACTIVE)
            
            #print("count",count)
            self.frame = Frame(self.flashcard,bg="lightblue",width=500)
            self.frame.grid(row=1,column=1)

            #random number       
            rands = random.randint(0,(len(q_list)-1))
            #print("rands:",rands,"len[qlist]:",len(q_list))

            self.canvas0 = Canvas(self.frame,width=300,height=200)

            self.wordlb = Label(self.frame, text=q_list[rands][0].upper(),bg="white",font=("Aria 15"))
            self.canvas0.grid(row=2,column=1,padx=30,pady=40)
            
            if q_list[rands][0] in ["circle","square","triangle"]:
                #if shapes generated opens turtle
                self.turt = t.RawTurtle(self.canvas0,shape=q_list[rands][0])
                self.turt.turtlesize(6)
            elif q_list[rands][0] in ["red","blue","yellow","white","green"]:
                #if color generated changes color of canvas
                self.canvas0.config(bg=q_list[rands][0])
            else:
                #print("q_list[rands][1]):",q_list[rands][1])
                #else write text in canvas
                self.canvas0.config(width=400)
                self.canvas0.create_text(120,50,text=q_list[rands][0].upper(),font=("Georgia 20"))
                
            
            self.wordlb.grid(row=3,column=1,padx=30,pady=20)
            #new list for generating answer to radiobutton
            choice_list = [] + ques
            #removing generated item from temporary list to avoid duplicates
            choice_list.remove(q_list[rands])
            #assign to another list for displaying randomly in radiobutton
            self.answer_rand =[q_list[rands][1]]
            #generate other two choices for radiobutton
            for i in range(2):
                r1=random.randint(0,len(choice_list)-1)
                self.answer_rand.append(choice_list[r1][1])
                #removing generated choice to avoid duplicates
                choice_list.remove(choice_list[r1])
            
            #shuffle answer list to display to radiobutton
            random.shuffle(self.answer_rand)

            #var1 assigned same for all radiobutton so that only 1 button can be selected at a time
            
            self.var1 = IntVar()
            chk1 = Radiobutton(self.frame, text=self.answer_rand[0],variable=self.var1,value=1,font=("Arial 12"),command=lambda: self.onCheck(chk1,self.var1.get()))
            chk1.grid(row=4,column=0,padx=30,pady=20)

            chk2 = Radiobutton(self.frame, text=self.answer_rand[1],variable=self.var1,value=2, font=("Arial 12"),command=lambda: self.onCheck(chk2,self.var1.get()))
            chk2.grid(row=4,column=1,padx=30,pady=10)

            chk3 = Radiobutton(self.frame, text=self.answer_rand[2],variable=self.var1,value=3, font=("Arial 12"),command=lambda: self.onCheck(chk3,self.var1.get()))
            chk3.grid(row=4,column=2,padx=30,pady=10)
            #button label and variable is passed in function call
            #lambda func is used to pass the button itself as argument to other function

            count+=1
            
        elif count == int(self.choice):
            #when count reached total no. of questions score window in opened
            self.scoreWindow()

    def flashcard(self):
        self.flashcard = Toplevel(window)
        self.flashcard.title("Flashcards | French")
        self.flashcard.geometry("1000x700")
        self.flashcard.config(bg="lightblue")

        #no. questions selected from dropdown list
        self.choice=self.clicked.get()
        #print("self.choice:",self.choice)
        
        count = 0
        #print(count)
        self.lb0 = Label(self.flashcard, text="Select Correct French words for the Flashcards!!",bg="white",font=("Arial 12"))
        self.lb0.grid(row=0,column=1,padx=30,pady=20)        

        self.startb =Button(self.flashcard, text="START",command=self.start,bg="yellow",font=("Arial 15"))
        self.startb.grid(row=5,column=1,padx=30,pady=30)

        #displays correct/incorrect answer
        global ans_lb
        ans_lb = Label(self.flashcard)
        ans_lb.grid(row=6,column=1,padx=30,pady=30)
        
        self.flashcard.mainloop()

    def scoreWindow(self):
        self.scoreWindow = Toplevel(self.flashcard)
        self.scoreWindow.title("Score Flashcards | French")
        self.scoreWindow.geometry("700x500")
        self.scoreWindow.config(bg="lightyellow")

        self.msg = Label(self.scoreWindow,fg="red",bg="lightyellow",font=("Arial 30"))
        
        self.m = Label(self.scoreWindow,text="YOU HAVE SCORED:",fg="black",bg="white",font=("Arial 20"))
        self.score_lb = Label(self.scoreWindow,text=str(score)+" / "+self.choice,bg="black",fg="white",font=("Arial", 30,"bold"))

        #message for score
        if score == int(self.choice):
            self.msg.config(text="PERFECT SCORE!! YOU ARE A MASTER!")
        elif score > (int(self.choice)//2):
            self.msg.config(text="WELL DONE!! YOU ARE GOOD!")
        elif score == 0:
            self.msg.config(text="TOO BAD!! BETTER LUCK NEXT TIME!")
        elif score < (int(self.choice)//2):
            self.msg.config(text="GOOD!! CAN DO BETTER!")
        
        self.msg.grid(row=1,column=2,padx=30,pady=30)
        self.m.grid(row=2,column=2,padx=30,pady=30)
        self.score_lb.grid(row=3,column=2,padx=30,pady=30)
        
        self.scoreWindow.mainloop()

def pyWindow():
    pyWindow=Toplevel()
    pyWindow.title("Python")
    pyWindow.geometry("500x700")
    pyWindow.configure(bg="paleturquoise")

    label = Label(pyWindow, text="Welcome to Python!", bg="gold", fg="blue", font="Arial 26")
    label.pack(padx=30,pady=20)

    label = Label(pyWindow, text="What will be the output for the following code?",bg="paleturquoise" ,
                  fg="navy", font="Arial 15")
    label.pack(padx=30,pady=20)


    quest = [("d={0,1,2}\n for x in d: \n print(x)","0 1 2"),
             ("x,y=12,14 \n if(x+y==26): \n print('true') \n else: \n print('false')","true"),
             ("text='Hello'; \n print(text)","Hello"),
             ("for i in range(4): \n print(i)","0 1 2 3"),
             ("result=10+1-1 \n print(result)","10"),
             ("i='3' \n print(int(i)+2)","5"),
             ("l=[1,2] \n l.append([3,4]) \n print(l)","[1,2,[3,4]]"),
             ("x={1,2,3,4} \n y={3,4} \n print(x.difference(y))","{1,2}"),
             ("a=5 \n print('The value of a is', a)","The value of a is 5"),
             ("l=[9,5,3] \n l.sort() \n print(l)","[3,5,9]")]

    #shuffling questions
    random.shuffle(quest)
    #print(quest)
    global count,score1
    #count is for index
    count = 0
    score1 = 0

    def nextb():
        answer_label.config(text=" ")
        #deleting text for next input
        entry.delete(0,END)
        
        #random_ques = random.randint(0,len(quest)-1)

        if count>len(quest)-1:
            scorelb = Label(pyWindow,text="SCORE: "+str(score1)+"/10",font=("Arial 20"),bg="blue",fg="white")
            scorelb.pack(pady=30)
        else:
            #assign questions through count
            questions.config(text=quest[count][0])

    def answer():
        global count,score1
        #declaring global again because python creates new local var for every function
        
        if entry.get()==quest[count][1]:
            answer_label.config(text="Your answer is Correct!",font=("Helvetic",14))
            score1+=1
        else:
            answer_label.config(text="Your answer is Wrong!",font=("Helvetic",14))

        #incrementing count to go for next question
        count+=1


    questions=Label(pyWindow,text=" ",font=("Helvetic",25),bg="white")
    questions.pack(pady=20)

    answer_label=Label(pyWindow,text=" ",bg="paleturquoise")
    answer_label.pack(pady=20)

    entry=Entry(pyWindow,font=("Helvetica",18))
    entry.pack(pady=10)

    #buttons
    button_frame=Frame(pyWindow,bg="paleturquoise")
    button_frame.pack(pady=20)

    answerbtn=Button(button_frame,text="Answer",command=answer,bg="darkblue", fg="white",font=("Helvetica",13))
    answerbtn.grid(row=0,column=0,padx=20)

    nextbtn=Button(button_frame,text="Next",command=nextb,bg="darkblue", fg="white",font=("Helvetica",13))
    nextbtn.grid(row=0,column=1,padx=20)

    quitb=Button(pyWindow,command=window.destroy,text="QUIT",bg="darkblue", fg="white",font=("Helvetica",13))
    quitb.pack(pady=20)

    nextb()

def myfont():
    myfont=font.Font(size=5,family="Arial")

window=Tk()
window.title("Edu.co")
window.geometry("500x700")
window.configure(bg="darkslateblue")
#object for Flash class
fc=Flash()

head=Label(window,text="Choose Your Interest",fg="white",bg="darkslateblue",font=("Arial Bold",30))
head.pack(padx=20,pady=40)
french=Button(window,text="French",bg="white",fg="crimson",height=4,width=20,font=("Arial",15),command=freWindow)
python=Button(window,text="Python",bg="white",fg="darkblue",height=4,width=20,font=("Arial",15),command=pyWindow)
french.pack(pady=100)
python.pack()
window.mainloop()
