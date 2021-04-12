import pygame 

pygame.init()

win = pygame.display.set_mode((500,300))
pygame.display.set_caption('pong')

WHITE = (255,255,255)
BLACK = (0,0,0)
PADDLE_SPEED = 10

class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,60])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.points = 0 

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill(WHITE)
		self.rect = self.image.get_rect()
		self.speed = 10
		self.dx = 1
		self.dy = 1 


paddle1 = Paddle()
paddle1.rect.x = 25
paddle1.rect.y = 150

paddle2 = Paddle()
paddle2.rect.x = 475
paddle2.rect.y = 150

ball = Ball()
ball.rect.x = 250
ball.rect.y = 150

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ball)

def redraw():
	win.fill(BLACK)
	font = pygame.font.SysFont('Comic Sans MS', 30)
	text = font.render('pong', False, WHITE)
	textRect = text.get_rect()
	textRect.center = (500//2, 25)
	win.blit(text, textRect) 

	p1_score = font.render(str(paddle1.points), False, WHITE)
	p1Rect = p1_score.get_rect()
	p1Rect.center = (50,50)
	win.blit(p1_score, p1Rect)

	p2_score = font.render(str(paddle2.points), False, WHITE)
	p2Rect = p2_score.get_rect()
	p2Rect.center = (450,250)
	win.blit(p2_score, p2Rect)

	all_sprites.draw(win)
	pygame.display.update()

run = True 
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	key = pygame.key.get_pressed()
	if key[pygame.K_w]:
		paddle1.rect.y += -PADDLE_SPEED
	if key[pygame.K_s]:
		paddle1.rect.y += PADDLE_SPEED
	if key[pygame.K_UP]:
		paddle2.rect.y += -PADDLE_SPEED
	if key[pygame.K_DOWN]:
		paddle2.rect.y += PADDLE_SPEED

	ball.rect.x += ball.speed * ball.dx
	ball.rect.y += ball.speed * ball.dy

	if ball.rect.y > 290:
		ball.dy = -1
	if ball.rect.x > 490:
		ball.rect.x, ball.rect.y = 250, 150
		ball.dx = -1
		paddle1.points += 1
	if ball.rect.y < 10:
		ball.dy = 1
	if ball.rect.x < 10:
		ball.rect.x, ball.rect.y = 250, 150
		ball.dx = 1 
		paddle2.points += 1 

	if paddle1.rect.colliderect(ball.rect):
		ball.dx = 1 
	if paddle2.rect.colliderect(ball.rect):
		ball.dx = -1

	redraw()

pygame.quit()




