import pygame

class Ball:
    def __init__(self,size,color,gravity,new_x=None,old_x=None,new_y=None,old_y=None,old_v_y=400,new_v_y=None,old_time = 0,old_v_x = 400,new_v_x=0):
        self.size = size
        self.color = color
        self.acceleration_y = gravity
        self.new_x = new_x
        self.old_x = old_x
        self.new_y = new_y
        self.old_y = old_y
        self.old_v_y = old_v_y
        self.old_v_x = old_v_x
        self.new_v_y = new_v_y
        self.new_v_x = new_v_x
        self.old_time_y = old_time
        self.old_time_x = old_time


    def draw(self,gameDisplay):
        pygame.draw.circle(gameDisplay,self.color,(self.new_x,self.new_y),self.size)
    
    def set_position(self,screensize):
        self.old_x = screensize // 2
        self.old_y = screensize // 2
        self.new_x = screensize // 2
        self.new_y = screensize // 2

    def move(self,time): # time is in milliseconds
        time = time / 1000
        time_change_y = time - self.old_time_y
        self.new_y = int(self.old_y + (self.old_v_y)*time_change_y + (1/2)*self.acceleration_y*(time_change_y**2))
        self.new_v_y = int(self.old_v_y + self.acceleration_y*time_change_y)

        if self.new_y >= 1975 or self.new_y <= 25 :
            self.old_y = self.new_y
            self.old_v_y = int(-1.01 * self.new_v_y)
            self.old_time_y = time

        time_change_x = time - self.old_time_x
        self.new_x = int(self.old_x + (self.old_v_x)*time_change_x)
        self.new_v_x = int(self.old_v_x)

        if self.new_x >= 1975 or self.new_x <= 25 :
            self.old_x = self.new_x
            self.old_v_x = int(-1.05 * self.new_v_x)
            self.old_time_x = time

    def user_input(self,key):
        if (key == pygame.K_UP):
            print('t')
            self.old_v_y -= 50
        elif (key== pygame.K_DOWN):
            self.old_v_y += 50
        elif (key == pygame.K_LEFT):
            self.old_v_x -= 50
        elif (key == pygame.K_RIGHT):
            self.old_v_x += 50


