from tkinter import *
from math import *
from time import *
root=Tk()
root.title("Зачетная работа")
root.geometry("1280x1024")
canv=Canvas(width=1280,height=1024,bg="white")
canv.pack()
canv.create_text(640,300,text="Проектная работа по информатике 8Г",font="Verdana 20")
canv.create_text(640,360,text="Удар мяча по воротам на холме ",font="Verdana 20")
canv.create_text(640,400,text="вариант 10",font="Verdana 15")
canv.create_text(640,450,text="2021 год",font="Verdana 15")

canv.create_text(900,800,text="Для перехода нажмите ENTER",font="Verdana 15")
g=10
s="_"
j=36
k=45
x3=80
y3=30
m=5
p=g*(x3*x3)
n=2*((x3*tan(k*pi/180))-(y3+m))
d=sqrt(p/n)
f=cos(k*pi/180)
V0=d/f
def f1(e):
 canv.delete("all")
 canv.create_rectangle(200,200,1080,300)
 canv.create_rectangle(200,350,1080,450)
 canv.create_rectangle(200,500,1080,600)
 canv.create_rectangle(200,650,1080,750)
 canv.create_rectangle(200,800,1080,900)
 canv.create_text(600,100,text="МЕНЮ",font="Verdana 30")
 canv.create_text(600,240,text="Условие",font="Verdana 20")
 canv.create_text(600,380,text="Решение",font="Verdana 20")
 canv.create_text(600,540,text="Краткое Условие",font="Verdana 20")
 canv.create_text(600,690,text="Демонстрация",font="Verdana 20")
 canv.create_text(600,820,text="Помощь",font="Verdana 20")
 canv.create_text(260,20,text="Для того,чтобы перейти вo вкладку в меню",font="Verdana 15")
 canv.create_text(490,40,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")
 

 root.unbind("<Return>")
def f2(e):
    
    canv.delete("all")
    
    canv.create_rectangle(200,200,1080,300)
    canv.create_rectangle(200,350,1080,450)
    canv.create_rectangle(200,500,1080,600)
    canv.create_rectangle(200,650,1080,750)
    canv.create_rectangle(200,800,1080,900)
    canv.create_text(600,100,text="МЕНЮ",font="Verdana 30")
    canv.create_text(600,240,text="Условие",font="Verdana 20")
    canv.create_text(600,380,text="Решение",font="Verdana 20")
    canv.create_text(600,540,text="Краткое Условие",font="Verdana 20")
    canv.create_text(600,690,text="Демонстрация",font="Verdana 20")
    canv.create_text(600,820,text="Помощь",font="Verdana 20")
    canv.create_text(260,20,text="Для того,чтобы перейти вo вкладку в меню",font="Verdana 15")
    canv.create_text(490,40,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")
        
    
    canv.update()
    root.unbind("<KeyRelease>")
    root.unbind("<Return>")
    root.unbind("<Escape>")
    root.bind("<Button-1>",f)

def f(e):
   
    if 200<e.x<1080 and 350<e.y<450: #решение
        canv.delete("all")
        canv.create_rectangle(0,0,150,250)


        
        canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
        canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
        canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
        canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
        canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
        canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
        canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
        canv.create_line(0,200,150,200)
        canv.create_line(200,498,1280,498)
        canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
        canv.create_oval(55,95,58,97)
        
        b=canv.create_oval(200+5*1-10-5,-1*1*5-10+500+5,200+5*1+10-5,-1*1*5+10+500+5)
        canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
        canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
        canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
        canv.create_line(200+(x3+10)*5,500-y3*5,200+(x3+10)*5+50,500-y3*5)
        canv.create_line(200+(x3+10)*5+50,500-y3*5,200+(x3+10)*5+50,500,arrow=FIRST)
        canv.create_line(200+(x3+10)*5+50,500-y3*5,200+(x3+10)*5+50,500,arrow=LAST)
        canv.create_text(200+(x3+10)*5+60,420,text="h",anchor="w",font="Arial 15")
        canv.create_line(200+(x3-20)*5,500,200+(x3-20)*5,550)

        canv.create_line(200+x3*5,500,200+x3*5,500-y3*5,fill="white")
        canv.create_line(200+x3*5,500,200+x3*5,550)
        canv.create_line(200+x3*5,550,200+(x3-20)*5,550,arrow=LAST)
        canv.create_line(200+x3*5,550,200+(x3-20)*5,550,arrow=FIRST)
        canv.create_text(540,565,text="d",anchor="w",font="Arial 15")
        canv.create_line(200,498,200,550)
        canv.create_line(200,550,200+(x3-20)*5,550,arrow=FIRST)
        canv.create_line(200,550,200+(x3-20)*5,550,arrow=LAST)
        canv.create_text(350,565,text="S",anchor="w",font="Arial 15")
        canv.create_line(200,500,250,450,arrow=LAST)
        canv.create_text(220,460,text="ϑ",anchor="w",font="Arial 15")
        canv.create_line(220,440,240,440,arrow=LAST)
        canv.create_line(225,475,240,500)
        canv.create_text(240,480,text="α",anchor="w",font="Arial 15")

        canv.create_text(800,550,text="1)Уравненение для оси ox:",anchor="w",font="Arial 17")
        canv.create_text(800,650,text="2)Уравненение для оси oy:",anchor="w",font="Arial 17")
        canv.create_text(800,830,text="3)Выводим t:",anchor="w",font="Arial 17")
        canv.create_text(230,625,text="4)Подставляем t и выносим V:",anchor="w",font="Arial 17")
        canv.create_text(230,750,text="5)Выражаем ϑ, подставляем значения:",anchor="w",font="Arial 17")


        canv.create_text(810,600,text="ϑsinαt - 5t = h",anchor="w",font="Arial 15")
        canv.create_text(810,700,text="ϑcosαt = S + d = A",anchor="w",font="Arial 15")
        
        canv.create_text(893,590,text="2",anchor="w",font="Arial 10")
        canv.create_text(810,750,text="ϑ=ϑcosα",anchor="w",font="Arial 15")
        canv.create_text(810,800,text="ϑ=ϑsinα",anchor="w",font="Arial 15")
        canv.create_text(819,758,text="x",anchor="w",font="Arial 7")
        canv.create_text(819,808,text="y",anchor="w",font="Arial 7")
        
        canv.create_text(810,880,text="t=",anchor="w",font="Arial 15")
        canv.create_line(840,880,870,880)
        canv.create_text(850,870,text="A",anchor="w",font="Arial 15")
        canv.create_text(850,890,text="ϑ",anchor="w",font="Arial 15")
        canv.create_text(859,898,text="x",anchor="w",font="Arial 7")
        

        canv.create_text(250,700,text="ϑ=",anchor="w",font="Arial 15")
        canv.create_line(300,700,420,700)
        canv.create_line(420,670,420,690)
        canv.create_line(290,695,297,720)
        canv.create_line(309,670,297,720)
        canv.create_line(309,670,420,670)
        canv.create_text(350,690,text="ℊA",anchor="w",font="Arial 15")
        canv.create_text(325,715,text="2 (tgαA-h)",anchor="w",font="Arial 15")
        
        canv.create_text(259,708,text="x",anchor="w",font="Arial 7")
        canv.create_text(337,712,text=".",anchor="w",font="Arial 15")
        canv.create_text(250,780,text="ϑ ≈ 36(м/с)",anchor="w",font="Arial 15")
        canv.create_text(380,830,text="Ответ:ϑ =36(м/с)",anchor="w",font="Arial 15")
        
        
        
        
        
        
        root.unbind("<Button-1>")
        root.bind("<Escape>",f2)
        
    if 200<e.x<1080 and 200<e.y<300: #условие
        canv.delete("all")
        canv.create_text(80,100,text="Какую начальную скорость, направленную под углом 45  к горизонту",anchor="w",font="Arial 20")
        canv.create_text(70,150,text="надо сообщить мячу, чтобы он попал в ворота, которые стоят на",anchor="w",font="Arial 20")
        canv.create_text(70,200,text="холме в 20 метрах от его края. Расстояние по горизонтальной",anchor="w",font="Arial 20")
        canv.create_text(70,250,text="плоскости от мяча до холма равно 60 метрам. Высота холма равна 30",anchor="w",font="Arial 20")
        canv.create_text(70,300,text="метрам.",anchor="w",font="Arial 20")
        canv.create_text(100,900,text="Для возвращения нажмите ESCAPE",anchor="w",font="Arial 15")
        canv.create_oval(796,90,800,94)
        root.unbind("<Button-1>")
        root.bind("<Escape>",f2)
    if 200<e.x<1080 and 500<e.y<600: #краткое условие


        canv.delete("all")
        canv.create_rectangle(0,0,150,250)
        #canv.create_rectangle(850,30,970,70)
        #canv.create_text(860,50,text="Перезапуск",anchor="w",font="Arial 15")
    
        canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
        canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
        canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
        canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
        canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
        canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
        canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
        canv.create_line(0,200,150,200)
        canv.create_line(200,498,1280,498)
        canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
        canv.create_oval(55,95,58,97)
        
        b=canv.create_oval(200+5*1-10-5,-1*1*5-10+500+5,200+5*1+10-5,-1*1*5+10+500+5)
        canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
        canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
        canv.create_text(0,600,text=s,anchor="w",font="Arial 15")
        canv.create_text(130,600,text="=ϑ.Для начала нажмите ENTER (Вбивать начальную скорость левее)",anchor="w",font="Arial 15")
        canv.create_text(130,640,text="Для перезапуска нажать BACKSPACE",anchor="w",font="Arial 15")
        
        canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
        root.bind("<Escape>",f2)
        
        def cruto(e):
            #if 850<e.x<970 and 30<e.y<70:
                canv.delete("all")
                root.unbind("<BackSpace>")
                canv.create_rectangle(0,0,150,250)
                #canv.create_rectangle(850,30,970,70)
                #canv.create_text(860,50,text="Перезапуск",anchor="w",font="Arial 15")
                canv.create_text(130,600,text="=ϑ.Для начала нажмите ENTER (Вбивать начальную скорость левее)",anchor="w",font="Arial 15")
    
                canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
                canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
                canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
                canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
                canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
                canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
                canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
                canv.create_line(0,200,150,200)
                canv.create_line(200,498,1280,498)
                canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
                canv.create_oval(55,95,58,97)
                canv.create_text(130,640,text="Для перезапуска нажать BACKSPACE",anchor="w",font="Arial 15")
                
                b=canv.create_oval(200+5*1-10-5,-1*1*5-10+500+5,200+5*1+10-5,-1*1*5+10+500+5)
                canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
                canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
                canv.create_text(0,600,text=s,anchor="w",font="Arial 15")
                canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
                def vvod(e):
                  canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
                  canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
                  global s,s1
                  if len(s)<6:   
                    if e.char.isdigit()or (e.char=="-" and len(s)==0 or e.char=="." and s.count(".")==0):
                       s=s[:-1]+e.char+"_"
                       canv.create_rectangle(0,800,100,500,fill="white",outline="white")
                       s1=canv.create_text(0,600,text=s,anchor="w",font="Arial 15")
                       root.bind("<Return>",zapusk)
                def BS(e):
                 global s
                 s=s[:-2]+"_"
                 canv.create_rectangle(0,800,70,500,fill="white",outline="white")
                 canv.create_text(0,600,text=s,anchor="w",font="Arial 15")
                def zapusk(e):
                   root.unbind("<KeyRelease>")
                   root.unbind("<Return>")
                   root.unbind("<Button-1>")
                   root.unbind("<Escape>")
                   canv.delete(b)
    
                   v=float(s[0:-1])
                   canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
                   canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
                   for tt in range(0,500):
                    t=tt/25
                    x=v*t*cos(k*pi/180)
                    y=v*t*sin(k*pi/180)-0.5*g*t**2
                    d=canv.create_oval(200+5*x-10,-1*y*5-10+500,200+5*x+10,-1*y*5+10+500)
                    canv.create_oval(200+5*x-2,-1*5*y-2+500,200+5*x+2,-1*5*y+2+500)
                    x1=10
                    y1=499
                    canv.update()
                    sleep(0.1)
                    canv.delete(d)

                    if 200+x3*5<200+5*x<200+x3*5+5 and 500-(m*5*2)-y3*5-10<-1*y*5+500<500-y3*5+10:
                      l=canv.create_text(300,700,text="попал",font="Verdana 30",fill="black")
                      #root.bind("<Button-1>",cruto)
                      root.bind("<BackSpace>",cruto)
                      #root.unbind("<BackSpace>")
                      root.bind("<Escape>",f2)
                      break
                    
                    if 200+(x3-20)*5<200+5*x<200+(x3+10)*5 and 500-y3*5<-1*y*5+500<500:
                        l=canv.create_text(300,700,text="не попал",font="Verdana 30",fill="black")
               
                        #root.bind("<Button-1>",cruto)
                        root.bind("<Escape>",f2)
                        root.bind("<BackSpace>",cruto)
                        #root.unbind("<BackSpace>")
                        break
                    if -1*y*5-10+500>500 or 200+5*x-10>1280:
                      canv.create_text(300,700,text="не попал",font="Verdana 30",fill="black")
                      #root.bind("<Button-1>",cruto)
                      root.bind("<Escape>",f2)
                      root.bind("<BackSpace>",cruto)
                      #root.unbind("<BackSpace>")
                      break
                root.bind("<KeyRelease>",vvod)
                root.bind("<Return>",zapusk)
                root.bind("<Button-1>",cruto)
                root.bind("<BackSpace>", BS)
                
                
                
        def vvod(e):
          canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
          canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
          global s,s1
          if len(s)<6:   
            if e.char.isdigit()or (e.char=="-" and len(s)==0 or e.char=="." and s.count(".")==0):
               s=s[:-1]+e.char+"_"
               canv.create_rectangle(0,800,100,500,fill="white",outline="white")
               s1=canv.create_text(0,600,text=s,anchor="w",font="Arial 15")
               root.bind("<Return>",zapusk)
        def BS(e):
           global s
           s=s[:-2]+"_"
           canv.create_rectangle(0,800,70,500,fill="white",outline="white")
           canv.create_text(0,600,text
                            =s,anchor="w",font="Arial 15")
        def zapusk(e):
          root.unbind("<KeyRelease>")
          root.unbind("<Return>")
          root.unbind("<Escape>")
          root.unbind("<Button-1>")
          canv.delete(b)
    
          v=float(s[0:-1])
          canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
          canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
          for tt in range(0,500):
            t=tt/25
            x=v*t*cos(k*pi/180)
            y=v*t*sin(k*pi/180)-0.5*g*t**2
            d=canv.create_oval(200+5*x-10,-1*y*5-10+500,200+5*x+10,-1*y*5+10+500)
            canv.create_oval(200+5*x-2,-1*5*y-2+500,200+5*x+2,-1*5*y+2+500)
            x1=10
            y1=499
            canv.update()
            sleep(0.1)
            canv.delete(d)

            if 200+x3*5<200+5*x<200+x3*5+5 and 500-(m*5*2)-y3*5-10<-1*y*5+500<500-y3*5+10:
              l=canv.create_text(300,700,text="попал",font="Verdana 30",fill="black")
              root.bind("<BackSpace>",cruto) 
              #root.bind("<Button-1>",cruto)
              root.bind("<Escape>",f2)
              #root.unbind("<BackSpace>")
              break
            if -1*y*5-10+500>500 or 200+5*x-10>1280:
              canv.create_text(300,700,text="не попал",font="Verdana 30",fill="black")
              #root.bind("<Button-1>",cruto)
              root.bind("<BackSpace>",cruto)
              root.bind("<Escape>",f2)
              #root.unbind("<BackSpace>")
              break
            if 200+(x3-20)*5<200+5*x<200+(x3+10)*5 and 500-y3*5<-1*y*5+500<500:
              l=canv.create_text(300,700,text="не попал",font="Verdana 30",fill="black")
              root.bind("<BackSpace>",cruto)
              #root.bind("<Button-1>",cruto)
              root.bind("<Escape>",f2)
              #root.unbind("<BackSpace>")
              break
        root.bind("<KeyRelease>",vvod)
        root.bind("<BackSpace>", BS)
        
        root.unbind("<Button-1>")
        root.unbind("<Return>")
        root.bind("<Button-1>",cruto)

        
        
        
       
        

    if 200<e.x<1080 and 650<e.y<750: #демонстрация
       
        
        canv.delete("all")
        canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
        b=canv.create_oval(200+5*1-10-5,-1*1*5-10+500+5,200+5*1+10-5,-1*1*5+10+500+5)
        
        canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
        canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
        canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
        canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
        canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
        canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
        canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
        canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
        canv.create_line(0,200,150,200)
        canv.create_line(200,498,1280,498)
        canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
        canv.create_oval(55,95,58,97)
        
        canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
        canv.create_text(10,930,text="Для начала нажмите ENTER",anchor="w",font="Arial 15")
    
    
        
        canv.create_rectangle(0,0,150,250)
        
       
        def cruto2(e):
         if 850<e.x<970 and 30<e.y<70:
          canv.delete("all")
          
          canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
          canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
          canv.create_line(0,498,1000,502)
          canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
          canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
          canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
          canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
          canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
          canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
          canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
          canv.create_line(0,200,150,200)
          canv.create_line(200,498,1280,498)
          canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
          canv.create_oval(55,95,58,97)
          
          canv.create_rectangle(0,0,150,250)
          
          canv.create_text(10,900,text="Для возвращения нажмите ESCAPE",anchor="w",font="Arial 15")
          canv.create_text(10,930,text="Для начала нажмите ENTER",anchor="w",font="Arial 15")
          root.bind("Return",dod)
          
          for tt in range(0,1000):
             root.unbind("<Button-1>")
             root.unbind("<Escape>")
             t=tt/25
             x=V0*t*cos(k*pi/180)
             y=V0*t*sin(k*pi/180)-0.5*g*t**2
             d=canv.create_oval(200+5*x-10,-1*y*5-10+500,200+5*x+10,-1*y*5+10+500)
             canv.create_oval(200+5*x-2,-1*5*y-2+500,200+5*x+2,-1*5*y+2+500)
             x1=10
             y1=499
             canv.update()
             sleep(0.1)
             canv.delete(d)

             if x3*5<5*x<x3*5+5 and 500-(m*5*2)-y3*5<-1*y*5+500<500-y3*5:
              l=canv.create_text(300,700,text="попал",font="Verdana 30",fill="black")
              root.unbind("<Button-1>")
              root.bind("<Escape>",f2)
              root.bind("<Button-1>",cruto2)

              break
        def dod(e):
          canv.delete("all")
           
          canv.create_rectangle(200+(x3-20)*5,500,200+(x3+10)*5,500-y3*5,fill="black")
          b=canv.create_oval(200+5*1-10-5,-1*1*5-10+500+5,200+5*1+10-5,-1*1*5+10+500+5)
        
          canv.create_rectangle(200+x3*5,500-y3*5,200+x3*5+5,500-(m*5*2)-y3*5)
          canv.create_text(20,25,text="Дано:",anchor="w",font="Arial 20")
          canv.create_text(25,55,text="h=30(м)",anchor="w",font="Arial 10")
          canv.create_text(25,70,text="S=60(м)",anchor="w",font="Arial 10")
          canv.create_text(25,85,text="d=20(м)",anchor="w",font="Arial 10")
          canv.create_text(25,100,text="α=45",anchor="w",font="Arial 10")
          canv.create_text(77,111,text="2",anchor="w",font="Arial 7")
          canv.create_text(25,115,text="ℊ=10(м/с )",anchor="w",font="Arial 10")
          canv.create_line(0,200,150,200)
          canv.create_line(200,498,1280,498)
          canv.create_text(25,230,text="ϑ =?(м)",anchor="w",font="Arial 10")
          canv.create_oval(55,95,58,97)
          
          canv.create_text(10,900,text="Для возвращения в меню нажмите ESCAPE",anchor="w",font="Arial 15")
          canv.create_text(10,930,text="Для начала нажмите ENTER",anchor="w",font="Arial 15")
    
    
          
          canv.create_rectangle(0,0,150,250)
          
          canv.delete(b)
          for tt in range(0,1000):
            root.unbind("<Escape>")
            root.unbind("<Button-1>")
            root.unbind("<Return>")
            t=tt/25
            x=V0*t*cos(k*pi/180)
            y=V0*t*sin(k*pi/180)-0.5*g*t**2
            d=canv.create_oval(200+5*x-10,-1*y*5-10+500,200+5*x+10,-1*y*5+10+500)
            canv.create_oval(200+5*x-2,-1*5*y-2+500,200+5*x+2,-1*5*y+2+500)
            x1=10
            y1=499
            canv.update()
            sleep(0.1)
            canv.delete(d)

            if x3*5<5*x<x3*5+5 and 500-(m*5*2)-y3*5<-1*y*5+500<500-y3*5:
              l=canv.create_text(300,700,text="попал",font="Verdana 30",fill="black")
              root.unbind("<Button-1>")
              root.bind("<Escape>",f2)
              root.bind("<Button-1>",cruto2)
              root.bind("<Return>",dod)
              break
        root.bind("<Return>",dod)
        root.bind("<Escape>",f2)
        
        
            
    
    if 200<e.x<1080 and 800<e.y<900: #помощь
        canv.delete("all")
        canv.create_text(580,400,text="1)Для перехода из вкладок в меню надо нажать ESCAPE",font="Verdana 15")
        canv.create_text(614,440,text="2)Для перехода с титульного листа в меню надо нажать ENTER",font="Verdana 15")
        canv.create_text(506,480,text="3)Для старта функция надо нажать ENTER",font="Verdana 15")
        canv.create_text(518,520,text="4)Для того,чтобы перейти вo вкладку в меню",font="Verdana 15")
        canv.create_text(720,560,text="надо навести курсор на прямоугольник с нужным названием и нажать левой кнопкой мыши",font="Verdana 15")

        root.unbind("<Button-1>")
        root.bind("<Escape>",f2)
    

root.bind("<Return>",f1)
root.bind("<Button-1>",f)

root.mainloop()
    
    
    
    
    
    
