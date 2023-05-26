import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran window game
width = 800
height = 600

# Warna
black = (0, 0, 0)
white = (255, 255, 255)

# Membuat window game
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Cacing")

class Worm:
    def __init__(self):
        self.size = 1
        self.grow = 1
        self.x = [width // 2]
        self.y = [height // 2]
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.speed = 10

    def move(self):
        if self.direction == 'up':
            self.y[0] -= self.speed
        elif self.direction == 'down':
            self.y[0] += self.speed
        elif self.direction == 'left':
            self.x[0] -= self.speed
        elif self.direction == 'right':
            self.x[0] += self.speed

        # Memperbarui posisi cacing
        for i in range(len(self.x)-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def draw(self):
        # Menggambar cacing
        for i in range(self.size):
            pygame.draw.rect(screen, white, (self.x[i], self.y[i], self.speed, self.speed))

# Membuat objek cacing
worm = Worm()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Mengatur kecepatan frame
    clock.tick(10)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and worm.direction != 'down':
                worm.direction = 'up'
            elif event.key == pygame.K_DOWN and worm.direction != 'up':
                worm.direction = 'down'
            elif event.key == pygame.K_LEFT and worm.direction != 'right':
                worm.direction = 'left'
            elif event.key == pygame.K_RIGHT and worm.direction != 'left':
                worm.direction = 'right'

    # Menggambar background
    screen.fill(black)

    # Menggerakkan dan menggambar cacing
    worm.move()
    worm.draw()

    # Menampilkan semua perubahan ke layar
    pygame.display.flip()

# Menghentikan Pygame
pygame.quit()
