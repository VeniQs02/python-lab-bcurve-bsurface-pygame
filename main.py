import matplotlib.pyplot as plt
import numpy as np
import random

import pygame


# Jakub Kańgowski 85705: krzywe Beziera, dzbanek 3D, gra w pygame
#       Każda część zadania jest umieszczona w oddzielnej funkcji i wywołuje się je bez żadnych argumentów, jedynie
#       odkomentowując wywołanie funkcji.

# two_dimensional_initials() - krzywe Beziera, zaprogramowałem w tej funkcji moje inicjały z życiem krzywych, nie tylko
#                              w formie 4 punktowych krzywych, lecz krzywych o różnych ilościach punktów aby uzyskać
#                              ładniejsze przejścia i czytelniejszą czcionkę.
#
#
# three_dimensional_pot() - dzbanek 3D, nie byłem w stanie doprowadzić kodu do działania, program się kompiluje, lecz
#                           sam dzbanek się nie wyświetla.
#
#
# my_pygame() - gra typu icy tower w pygame, w prawdzie to bardziej demo, bo ma wiele niedopracowań i niedokładności, ale
#               została stworzona w bardzo krótkim czasie

def two_dimensional_initials():
    def bezier_curve(points, n_points=100):
        t = np.linspace(0, 1, n_points)
        n = len(points) - 1
        curve = np.zeros((n_points, 2))
        for i in range(n_points):
            for j in range(n + 1):
                curve[i] += points[j] * newton(n, j) * (1 - t[i]) ** (n - j) * t[i] ** j
        return curve

    def newton(n, k):
        return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

    l1 = np.array([[100, 50], [100, 100], [100, 100], [150, 100], [200, 150], [200, 200], [200, 400]])
    l2 = np.array([[100, 50], [200, 50], [250, 150], [250, 250], [250, 400]])
    l3 = np.array([[250, 400], [200, 400]])

    l4 = np.array([[300, 400], [300, 50]])
    l5 = np.array([[300, 400], [350, 400]])
    l6 = np.array([[350, 400], [350, 270]])
    l7 = np.array([[350, 270], [360, 330], [385, 380], [400, 400]])
    l8 = np.array([[400, 400], [450, 400]])
    l9 = np.array([[450, 400], [390, 295], [380, 225], [450, 50]])
    l10 = np.array([[450, 50], [400, 50]])
    l11 = np.array([[400, 50], [380, 100], [360, 160], [350, 220]])
    l12 = np.array([[350, 220], [350, 50]])
    l13 = np.array([[350, 50], [300, 50]])

    c1 = bezier_curve(l1)
    c2 = bezier_curve(l2)
    c3 = bezier_curve(l3)
    c4 = bezier_curve(l4)
    c5 = bezier_curve(l5)
    c6 = bezier_curve(l6)
    c7 = bezier_curve(l7)
    c8 = bezier_curve(l8)
    c9 = bezier_curve(l9)
    c10 = bezier_curve(l10)
    c11 = bezier_curve(l11)
    c12 = bezier_curve(l12)
    c13 = bezier_curve(l13)

    plt.plot(c1[:, 0], c1[:, 1], c2[:, 0], c2[:, 1], c3[:, 0], c3[:, 1], c4[:, 0], c4[:, 1], c5[:, 0], c5[:, 1],
             c6[:, 0], c6[:, 1], c7[:, 0], c7[:, 1], c8[:, 0], c8[:, 1], c9[:, 0], c9[:, 1], c10[:, 0], c10[:, 1],
             c11[:, 0], c11[:, 1], c12[:, 0], c12[:, 1], c13[:, 0], c13[:, 1])

    plt.xlim([0, 500])
    plt.ylim([0, 500])
    plt.show()


# two_dimensional_initials()


def three_dimensional_pot():
    def read_file(file_path):
        with open(file_path, 'r') as f:
            data = f.read()
        print(data)
        return data

    def parse_data(data):
        lines = data.split('\n')
        vertices = []
        faces = []
        for line in lines:
            if line.startswith('v'):
                vertex = line.split()[1:]
                vertices.append([float(v) for v in vertex])
            elif line.startswith('f'):
                face = line.split()[1:]
                faces.append([int(f.split('/')[0]) - 1 for f in face])
        print(vertices)  # add this line
        print(faces)  # add this line
        return vertices, faces

    def scale_model(vertices, scale_factor):
        for i, vertex in enumerate(vertices):
            vertices[i] = [vertex[0] * scale_factor, vertex[1] * scale_factor, vertex[2] * scale_factor]
        return vertices

    def draw_teapot(vertices, faces):
        pygame.init()
        size = (500, 400)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Utah Teapot')
        clock = pygame.time.Clock()
        # vertices = [[v[0] * 200, v[1] * 200, v[2] * 500] for v in vertices]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            screen.fill((255, 255, 255))
            for face in faces:
                pygame.draw.polygon(screen, (255, 0, 0), [vertices[i][:2] for i in face], 1)
            pygame.display.flip()
            clock.tick(60)

    if __name__ == '__main__':
        data = read_file('teapot_points.txt')
        vertices, faces = parse_data(data)
        vertices = scale_model(vertices, 5)
        draw_teapot(vertices, faces)


# three_dimensional_pot()


def my_pygame():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    player_image = pygame.image.load('player.png').convert_alpha()
    background_image = pygame.image.load('background.png').convert()
    background_rect = background_image.get_rect()
    background_y = 0
    # dzwieki działały ale były za głośne i nie zawsze działały jak powinny
    #jump_sound = pygame.mixer.Sound('jump.mp3')
    #land_sound = pygame.mixer.Sound('land.wav')
    #game_over_sound = pygame.mixer.Sound('game_over.wav')
    brick_image = pygame.image.load('brick.png').convert_alpha()
    player_rect = player_image.get_rect()
    player_rect.midbottom = (screen_width // 2, screen_height - 10)

    player_speed = 10
    player_jump = 26
    player_gravity = 1
    player_y_velocity = 0
    player_can_jump = True
    clock = pygame.time.Clock()

    platforms = []
    platform_width = 80
    platform_height = 80
    platform_y_spacing = 100
    platform_x_spacing = 200
    for i in range(10):
        while True:
            platform_x = random.randint(0, screen_width - platform_width)
            platform_y = screen_height - platform_y_spacing * i
            platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
            overlap = False
            for other_rect in platforms:
                if platform_rect.colliderect(other_rect):
                    overlap = True
                    break
            if not overlap:
                break
        platforms.append(platform_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= player_speed
        elif keys[pygame.K_RIGHT]:
            player_rect.x += player_speed
        if keys[pygame.K_SPACE] and player_can_jump:
            player_y_velocity = -player_jump
            player_can_jump = False

        player_y_velocity += player_gravity
        player_rect.y += player_y_velocity

        if player_rect.bottom >= screen_height - 10:
            player_rect.bottom = screen_height - 10
            player_can_jump = True
            player_y_velocity = 0

        for platform_rect in platforms:
            if player_rect.colliderect(platform_rect):
                player_rect.bottom = platform_rect.top
                player_can_jump = True
                player_y_velocity = 0

        # Move the screen with the player
        if player_rect.top < screen_height // 3:
            player_rect.top = screen_height // 3
            for platform_rect in platforms:
                platform_rect.top += abs(player_y_velocity)
                if platform_rect.top > screen_height:
                    platform_rect.top = 0
                    platform_rect.left = random.randint(0, screen_width - platform_width)

        screen.fill((0, 0, 0))
        screen.blit(player_image, player_rect)

        screen.blit(background_image, (0, background_y - screen_height))
        screen.blit(background_image, (0, background_y))
        for platform_rect in platforms:
            screen.blit(brick_image, platform_rect)
        screen.blit(player_image, player_rect)

        pygame.display.update()
        clock.tick(60)
    pygame.quit()


# my_pygame()
