import sys
import pygame
import random
import time

pygame.init()

size = width, height = 820, 620

speed = [2, 2]

black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Algorithm Visualizer")
clock = pygame.time.Clock()
sorting = False
menu = True


def insertion_sort(arr, screen, padding, screen_width, x):
    sorting = True
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            try:
                arr[j + 1] = arr[j]
                j -= 1
                draw_array("Insertion Sort", arr, screen, padding, screen_width=screen_width, x=x,
                           special_colors={j: (0, 255, 0), j + 1: (0, 0, 255)})
                pygame.display.update()
                pygame.time.wait(5)
            except Exception as e:
                print(e)
                sys.exc_info()
                pass
        arr[j + 1] = key
    sorting = False


# random array with 1000 elements
n = 100
arr = [random.randint(0, 480 - 2 * 5) for i in range(n)]


def draw_array(sorting, arr, screen, padding, screen_width, x, special_colors={}):
    # put a heading

    pygame.event.pump()
    font = pygame.font.SysFont('Helvetica', 30)
    text = font.render(sorting, 1, (255, 255, 255))
    # draw the array values
    screen.fill((0, 0, 0))
    screen.blit(text, (x + (len(arr) // 2 * x), 0))
    color = (255, 0, 0)
    for i in range(len(arr)):
        if i in special_colors:
            color = special_colors[i]
        pygame.draw.rect(screen, color, pygame.Rect(
            x, (520 - 2 * padding) - arr[i], screen_width - padding, arr[i]))
        x = x + screen_width
    pygame.display.update()


def quick_sort(arr, screen, padding, screen_width, x, special_colors={}):
    def partition(arr, l, h):
        i = (l - 1)
        x = arr[h]
        for j in range(l, h):
            if arr[j] <= x:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                draw_array("Quick Sort", arr, screen, padding, screen_width=screen_width, x=x,
                           special_colors={i: (0, 255, 0), j: (0, 0, 255)})
                pygame.display.update()
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    def _quick_sort(arr, l, h):
        if l < h and (h - l) > 5:
            p = partition(arr, l, h)
            if p - 1 > l:
                _quick_sort(arr, l, p - 1)
                draw_array("Quick Sort", arr, screen, padding, screen_width=screen_width,
                           x=x, special_colors={p: (0, 255, 0), l: (0, 0, 255)})
            if p + 1 < h:
                _quick_sort(arr, p + 1, h)
                draw_array("Quick Sort", arr, screen, padding, screen_width=screen_width,
                           x=x, special_colors={p: (0, 255, 0), h: (0, 0, 255)})

    _quick_sort(arr, 0, len(arr) - 1)
    insertion_sort(arr, screen, padding, screen_width, x)


clock = pygame.time.Clock()

while True:
    sorting_name = "No sorting algorithm selected"
    padding = screen.get_width() // n * 0.05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                print("QUICKSORT")
                quick_sort(arr, screen, padding, screen_width, x)

    clock.tick(3)
    screen.fill(black)
    screen_width = (screen.get_width() - 2 * padding) / n
    screen_height = screen.get_height()
    time.sleep(0.1)
    # getting all the events


    x = padding
