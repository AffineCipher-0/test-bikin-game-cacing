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
red = (255, 0, 0)

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

        # Memeriksa batas layar
        if self.x[0] < 0:
            self.x[0] = width - self.speed
        elif self.x[0] >= width:
            self.x[0] = 0
        if self.y[0] < 0:
            self.y[0] = height - self.speed
        elif self.y[0] >= height:
            self.y[0] = 0

        # Memperbarui posisi cacing
        for i in range(len(self.x)-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # Menambah elemen baru jika cacing bertambah ukuran
        while len(self.x) < self.size:
            self.x.append(self.x[-1])
            self.y.append(self.y[-1])

    def draw(self):
        # Menggambar cacing
        for i in range(self.size):
            pygame.draw.rect(screen, white, (self.x[i], self.y[i], self.speed, self.speed))

    def check_collision(self, x, y):
        # Memeriksa tabrakan dengan makanan
        if self.x[0] == x and self.y[0] == y:
            self.size += self.grow
            return True
        return False

# Membuat objek cacing
worm = Worm()

# Membuat objek makanan
food_x = random.randint(0, width // worm.speed - 1) * worm.speed
food_y = random.randint(0, height // worm.speed - 1) * worm.speed

# Misi poin
target_points = 10
current_points = 0
font = pygame.font.Font(None, 36)

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

    # Menggambar makanan
    pygame.draw.rect(screen, red, (food_x, food_y, worm.speed, worm.speed))

    # Memeriksa tabrakan dengan makanan
    if worm.check_collision(food_x, food_y):
        # Menghasilkan makanan baru
        food_x = random.randint(0, width // worm.speed - 1) * worm.speed
        food_y = random.randint(0, height // worm.speed - 1) * worm.speed
        current_points += 1

    # Menggambar poin
    text = font.render("Points: " + str(current_points), True, white)
    screen.blit(text, (10, 10))

    # Memeriksa jika misi poin tercapai
    if current_points >= target_points:
        # Menampilkan pesan kemenangan
        win_text = font.render("You Win!", True, white)
        screen.blit(win_text, (width // 2 - 50, height // 2 - 50))
        running = False

    # Menampilkan semua perubahan ke layar
    pygame.display.flip()

# Menghentikan Pygame
pygame.quit()
