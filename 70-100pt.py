# 70pt done
# 80pt done
# 90pt done
# done
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# done
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590, fill = "black")
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
rocket1Fired = False
direction = 5
a = 3

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        
        # Enter my text
        self.prompt = "Rockets left :"
        
        self.label1 = Label(root, text=self.prompt, width=len(self.prompt), bg='green')
        self.label1.pack()

        self.rockets = a
        
        self.rocketsTxt = Label(root, text=str(self.rockets), width=len(str(self.rockets)), bg='green')
        self.rocketsTxt.pack()
        
        # Adding the drawpad, adding the key listener, starting animation
        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
    
    def animate(self):
        global drawpad
        global enemy
        global direction
        global rocket
        global rocket1Fired
        x1,y1,x2,y2 = drawpad.coords(enemy)
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)       
        
        if x2 > 800:
            direction = - 5
            
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        
        if rocket1Fired == True:
            drawpad.move(rocket1, 0,-4)
            didWeHit = self.collisionDetect()
        if ry2 < 0:
            rocket1Fired = False
            drawpad.move(rocket1, px1-rx1 + 3, py1-ry1 + 3)
        drawpad.after(5,self.animate)

    def key(self,event):
        global player
        global rocket1Fired
        global rocket1
        px1,py1,px2,py2 = drawpad.coords(player)
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1) 
        if event.char == "w":
            if py1 > 0:
                drawpad.move(player,0,-4) 
                if rocket1Fired == False:
                    drawpad.move(rocket1,0,-4)
        if event.char == "a":
            if px1 > 0:
                drawpad.move(player,-4,0)
                if rocket1Fired == False:
                    drawpad.move(rocket1,-4,0)
        if event.char == "s":
            if py2 < 600:
                drawpad.move(player,0,4)
                if rocket1Fired == False:
                    drawpad.move(rocket1,0,4)
        if event.char == "d":
            if px2 < 800:
                drawpad.move(player,4,0)
                if rocket1Fired == False:  
                    drawpad.move(rocket1,4,0) 
        if event.char == " ":
            rocket1Fired = True
            self.rockets = self.rockets - 1
            self.rocketsTxt.configure(text=str(self.rockets))
            

    
    def collisionDetect(self):
        global enemy
        global rocket1
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket1)
        ex1,ey1,ex2,ey2 = drawpad.coords(enemy)
        if (rx1 > ex1 and rx2 < ex2) and (ry1 > ey1 and ry2 < ey2 ):
            print "hello"
            drawpad.delete(enemy)
            drawpad.delete(rocket1)
            
app = myApp(root)
root.mainloop()