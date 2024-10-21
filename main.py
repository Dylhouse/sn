
#Hooray!

#Pygame Setup
import pygame
pygame.init()
#Import other important libraries
import librosa
import numpy as np

w = pygame.display.set_mode((1920,1080),pygame.SCALED|pygame.FULLSCREEN)
pygame.display.set_caption("pyPhysics")

#Add icon to display
#pygame.display.set_icon(pygame.image.load("assets/Images/dead python logo.png"))

#Images
#Main_Menu_Logo=pygame.image.load("assets/Images/1st pyware logo.png")
c = pygame.time.Clock()
AIR_DENSITY = 1.225 #Air density, in kg/m^3
GRAVITY = 9.8
UP_DIR = np.pi / 2

class PhysObj():

    #Figure out type annotations and change mass to KG, force to Netwons, and x/y, velocity and acceleration all to meters

    def __init__(
            self, x, y, mass: int, drag_coeffecient: float,
            cross_sectional_area, image=None):
        
        self.acceleration = [0,0]
        self.velocity = [0,0]
        self.mass=mass
        self.x=x
        self.y=y
        self.width=50
        self.height=50
        self.gravitational_force=GRAVITY*mass
        self.drag_force_total_coeffecient = 0.5 * AIR_DENSITY * drag_coeffecient * cross_sectional_area
        if not image:
            self.rect=pygame.Rect(self.x,self.y,50,50)
        self.drag_coeffecient=drag_coeffecient
        self.cross_sectional_area=cross_sectional_area
    
    def apply_force(self, force: float, direction: "radians") -> None:
        #F/M = A
        #X = cos(radians)
        #Y = sin(radians)
        self.velocity[0] -= ((force/self.mass)*np.cos(direction))
        self.velocity[1] += ((force/self.mass)*np.sin(direction))
    
    def update(self) -> None:

        #Possibly make the 2 exponent allow imaginary numbers to remove
        #the velocity directional check?
        drag_force_x = (self.drag_force_total_coeffecient * (self.velocity[0] ** 2)) #Get drag force
        drag_force_y = (self.drag_force_total_coeffecient * (self.velocity[1] ** 2)) #Get drag force

        net_force = self.gravitational_force - drag_force_y #Get net force
        if self.velocity[0] > 0:
            self.acceleration[0] = -(drag_force_x/self.mass)
        else:
            self.acceleration[0] = (drag_force_x/self.mass)
        self.acceleration[1] = -(net_force/self.mass) #Calculate force effect on acceleration
        
        self.velocity[0] += (self.acceleration[0]*c.get_time())/1000
        self.velocity[1] += (self.acceleration[1]*c.get_time())/1000

        self.x += (((self.velocity)[0] * c.get_time())/1000)*100

        #-= because up is down in python
        self.y -= (((self.velocity)[1] * c.get_time())/1000)*100

        if self.y >= 1020:
            self.y=1020
            self.velocity[1] = -self.velocity[1] * 0.7

        elif self.y <= 50:
            self.y=50
            self.velocity[1] = -self.velocity[1] * 0.7
        
        if self.x >= 1870:
            self.x=1870
            self.velocity[0] = -self.velocity[0] * 0.7

        elif self.x <= 50:
            self.x=50
            self.velocity[0] = -self.velocity[0] * 0.7
        pygame.draw.rect(w,(0,200,0),pygame.Rect(self.x,self.y,50,50))

run = True
starttime=pygame.time.get_ticks()
_testobj = PhysObj(540,600,600,0.47,0.04523893421)
test = 0

while run:
    
    #Def mousepos here once so we don't have to get it multiple time each frame
    mousepos= pygame.mouse.get_pos()
    w.fill((255,0,0))
    
    #w.blit(Main_Menu_Background,(background_offset_x,background_offset_y))
    _testobj.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Get the angle between the mousepos and the object
            angle = np.atan2(mousepos[1] - _testobj.y, mousepos[0] - _testobj.x)
            print(angle)
            #Apply force of 10000 Newtons from angle
            _testobj.apply_force(10000,angle)
    pygame.display.flip()
    c.tick(120)