from pygame.locals import * 
import pygame

#game physics

def stick_ball_collision_update(stick1, stick2, ball):
	x1 = stick1.x
	y1 = stick1.y
	x2 = stick2.x
	y2 = stick2.y
	x3 = ball.x
	y3 = ball.y
	sizeStick = stick1.size

	top_y2 = y2 - (sizeStick - 1) * 20
	bot_y2 = y2 + (sizeStick - 1) * 20

	top_y1 = y1 - (sizeStick - 1) * 20
	bot_y1 = y1 + (sizeStick - 1) * 20	

	if x3 >= x2-20 and (y3 >= top_y2 and y3 <= bot_y2): 
		ball.xVelocity*=-1
	if x3 <= x1+15 and (y3 >= top_y1 and y3 <= bot_y1):
		ball.xVelocity*=-1

	return False

def wall_ball_collision_update(ball, windowWidth, windowHeight):	
		if ball.x > windowWidth or ball.x < 0: 
			ball.xVelocity*=-1
		if ball.y > windowHeight or ball.y < 0:
			ball.yVelocity*=-1

class Stick:
	def __init__(self, size, x, y):
		self.size = size
		self.x = x
		self.y = y

	def render(self, surface, stickImage):
		for i in range(self.size): 
			surface.blit(stickImage, (self.x, self.y - i*20))
			surface.blit(stickImage, (self.x, self.y + i*20))

	def moveUp(self):
		self.y-=1

	def moveDown(self):
		self.y+=1

class Ball:

	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.speed = speed
		self.xVelocity = self.speed
		self.yVelocity = self.speed

	def render(self, surface, image):
		surface.blit(image, (self.x, self.y)) 

	def update(self):
		self.x+=self.xVelocity
		self.y+=self.yVelocity



class App:
	windowWidth = 1000
	windowHeight = 600

	def __init__(self):
		self._background = None
		self._stick_image = None
		self._ball_image = None
		self._stick1 = Stick(5, 50, 250)
		self._stick2 = Stick(5, 950, 250)
		self._ball = Ball(500, 300, 0.5)

	def init(self):
		pygame.init()
		self._background = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
		pygame.display.set_caption('my snake game')
		self._stick_image = pygame.image.load('stick.jpg').convert()
		self._ball_image = pygame.image.load('ball.jpg').convert()

	def loop(self):
		self._ball.update()
		stick_ball_collision_update(self._stick1, self._stick2, self._ball)
		wall_ball_collision_update(self._ball, self.windowWidth, self.windowHeight)


	def render(self):
		self._background.fill((0,0,0))
		self._stick1.render(self._background, self._stick_image)
		self._stick2.render(self._background, self._stick_image)
		self._ball.render(self._background, self._ball_image)
		pygame.display.flip()

	def quit_game(self):
		pygame.quit()
		
	def execute(self):
		self.init()
		while (True): 
			pygame.event.pump()
			keys = pygame.key.get_pressed()

			if (keys[K_ESCAPE]):
				self.quit_game()

			if (keys[K_UP]):
				self._stick2.moveUp()

			if (keys[K_DOWN]):
				self._stick2.moveDown()

			if (keys[K_w]): 
				self._stick1.moveUp()

			if (keys[K_s]): 
				self._stick1.moveDown()

			self.loop()
			self.render()
		quit_game()

if __name__== "__main__":
	APP = App()
	APP.execute()