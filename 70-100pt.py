# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.destroy(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
missile = drawpad.create_rectangle(395,582,405,598)
missile1 = drawpad.create_rectangle(395,582,405,598)
missile2 = drawpad.create_rectangle(395,582,405,598)
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemy = drawpad.create_rectangle(50,50,100,60, fill="red")
missileFired = 0

muevate = 0
direction = 5

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
        self.rockets = 3
        
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
        x1,y1,x2,y2 = drawpad.coords(enemy)
        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(enemy, direction, 0)
        if missileFired == True:
            drawpad.move(missile,0,-10)
        if missileFired1 == True:
            drawpad.move(missile1,0,-10)
        if missileFired2 == True:
            drawpad.move(missile2,0,-10)
        drawpad.after(5,self.animate)
    def key(self,event):
        global player
        global missileFired
        global missileFired1
        global missileFired2
        px1,py1,px2,py2 = drawpad.coords(player)
        if event.char == "w":
            if py1 > 0:
                drawpad.move(player,0,-4) 
                drawpad.move(missile, 0, -4)
                drawpad.move(missile1, 0, -4) 
                drawpad.move(missile2, 0, -4)           
        if event.char == "a":
            if px1 > 0:
                drawpad.move(player,-4,0)
                drawpad.move(missile,-4,0)
                drawpad.move(missile1, -4, 0) 
                drawpad.move(missile2, -4, 0) 
        if event.char == "s":
            if py2 < 600:
                drawpad.move(player,0,4)
                drawpad.move(missile,0,4)
                drawpad.move(missile1, 0, 4)  
                drawpad.move(missile2, 0, 4) 
        if event.char == "d":
            if px2 < 800:
                drawpad.move(player,4,0) 
                drawpad.move(missile,4,0)  
                drawpad.move(missile1, 4, 0)
                drawpad.move(missile2, 4, 0) 
        if event.char == "1":
            print "working"  
            missileFired = True       
        mx1,my1,mx2,my2 = drawpad.coords(missile)
        if my1 < 0 :
         missileFired = False     
     
        if event.char == "2":
            print "working"  
            missileFired1 = True       
        mx3,my3,mx4,my4 = drawpad.coords(missile1)
        if my1 < 0 :
         missileFired1 = False 
         
        if event.char == "3":
            print "working"  
            missileFired2 = True       
        mx5,my5,mx6,my6 = drawpad.coords(missile2)
        if my1 < 0 :
         missileFired2 = False       
                                                                         
                                                                                                                                             
    def collisionDetect(self,rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
        


app = myApp(root)
root.mainloop()