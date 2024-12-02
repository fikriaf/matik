import pygame
import math
import random
import time
# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width = 1280
height = 720

# Warna RGB
white = (255, 255, 255)
black = (0, 0, 0)

# Titik pusat mata
left_eye_center = [width // 3, height // 2]
right_eye_center = [2 * width // 3, height // 2]

# Ukuran mata
eye_radius = 50
pupil_radius = 40

# Kecepatan pergerakan
speed = 0.05

# Jendela Pygame
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Eyes")

clock = pygame.time.Clock()

running = True
current_pos_left = left_eye_center.copy()  # Posisi saat ini mata kiri
current_pos_right = right_eye_center.copy()  # Posisi saat ini mata kanan
left_eye_look = left_eye_center.copy()  # Posisi titik pandang mata kiri
right_eye_look = right_eye_center.copy()  # Posisi titik pandang mata kanan

def draw_eyes():
    # Gambar mata putih
    pygame.draw.circle(screen, white, left_eye_center, eye_radius)
    pygame.draw.circle(screen, white, right_eye_center, eye_radius)

    # Gambar pupil hitam mata kiri
    pygame.draw.circle(screen, black, (int(current_pos_left[0]), int(current_pos_left[1])), pupil_radius)

    # Gambar pupil hitam mata kanan
    pygame.draw.circle(screen, black, (int(current_pos_right[0]), int(current_pos_right[1])), pupil_radius)

def move_pupil(eye_center, current_pos, eye_look):
    distance_threshold = 3.0
    if abs(eye_look[0] - current_pos[0]) < distance_threshold and abs(eye_look[1] - current_pos[1]) < distance_threshold:
        current_pos[0] = eye_look[0]
        current_pos[1] = eye_look[1]
    else:
        current_pos[0] += (eye_look[0] - current_pos[0]) * speed
        current_pos[1] += (eye_look[1] - current_pos[1]) * speed

def look_at_mouse():
    # Mendapatkan posisi kursor mouse
    mouse_pos = pygame.mouse.get_pos()

    # Menghitung sudut pandangan mata kiri berdasarkan posisi kursor mouse
    left_eye_angle = math.atan2(mouse_pos[1] - left_eye_center[1], mouse_pos[0] - left_eye_center[0])

    # Menghitung posisi titik pandang mata kiri berdasarkan sudut pandangan dan jarak relatif
    left_eye_look[0] = left_eye_center[0] + math.cos(left_eye_angle) * (eye_radius - pupil_radius)
    left_eye_look[1] = left_eye_center[1] + math.sin(left_eye_angle) * (eye_radius - pupil_radius)

    # Menghitung sudut pandangan mata kanan berdasarkan posisi kursor mouse
    right_eye_angle = math.atan2(mouse_pos[1] - right_eye_center[1], mouse_pos[0] - right_eye_center[0])

    # Menghitung posisi titik pandang mata kanan berdasarkan sudut pandangan dan jarak relatif
    right_eye_look[0] = right_eye_center[0] + math.cos(right_eye_angle) * (eye_radius - pupil_radius)
    right_eye_look[1] = right_eye_center[1] + math.sin(right_eye_angle) * (eye_radius - pupil_radius)

while running:
    h = random.randint(50, 90)
    # Mendapatkan posisi kursor acak jika tidak ada kursor mouse di sekitar jendela pygame
    mouse_pos = (random.randint(0, width), random.randint(0, height))
    while True:
        if h == 0:
            print("ganti gerakan")
            break
        h -= 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Memeriksa apakah ada kursor mouse di sekitar jendela pygame
        if pygame.mouse.get_focused():
            look_at_mouse()
        else:

            # Menghitung sudut pandangan mata kiri berdasarkan posisi kursor acak
            left_eye_angle = math.atan2(mouse_pos[1] - left_eye_center[1], mouse_pos[0] - left_eye_center[0])

            # Menghitung posisi titik pandang mata kiri berdasarkan sudut pandangan dan jarak relatif
            left_eye_look[0] = left_eye_center[0] + math.cos(left_eye_angle) * (eye_radius - pupil_radius)
            left_eye_look[1] = left_eye_center[1] + math.sin(left_eye_angle) * (eye_radius - pupil_radius)

            # Menghitung sudut pandangan mata kanan berdasarkan posisi kursor acak
            right_eye_angle = math.atan2(mouse_pos[1] - right_eye_center[1], mouse_pos[0] - right_eye_center[0])

            # Menghitung posisi titik pandang mata kanan berdasarkan sudut pandangan dan jarak relatif
            right_eye_look[0] = right_eye_center[0] + math.cos(right_eye_angle) * (eye_radius - pupil_radius)
            right_eye_look[1] = right_eye_center[1] + math.sin(right_eye_angle) * (eye_radius - pupil_radius)

        # Animasi pergerakan pupil mata kiri
        move_pupil(left_eye_center, current_pos_left, left_eye_look)

        # Animasi pergerakan pupil mata kanan
        move_pupil(right_eye_center, current_pos_right, right_eye_look)

        # Menggambar mata dan pupil
        screen.fill((0, 0, 0))
        draw_eyes()

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
