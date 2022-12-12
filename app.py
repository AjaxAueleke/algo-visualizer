import sys
import pygame
import random
import time

pygame.init()

size = width, height = 720,480

speed = [2, 2]

black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Algorithm Visualizer")
clock = pygame.time.Clock()
sorting = False
menu = True


def bubble_sort(arr, screen, padding, screen_width, x):
    sorting = True
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                try:
                    pygame.event.pump()
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    draw_array("Bubble Sort", arr, screen, padding, screen_width=screen_width, x=x,
                               special_colors={j: (0, 255, 0), j + 1: (0, 0, 255)})
                    pygame.display.update()
                    pygame.time.wait(5)
                except Exception as e:
                    print(e)
                    sys.exc_info()
                    pass
    sorting = False


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


def merge_sort(arr, screen, padding, screen_width, x):
    sorting = True

    # iterative merge sort
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width, x=x,
                       special_colors={i: (0, 255, 0), j + 1: (0, 0, 255)})
            pygame.display.update()
            pygame.time.wait(5)
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width, x=x,
                       special_colors={i: (0, 255, 0), j + 1: (0, 0, 255)})
            pygame.display.update()
            pygame.time.wait(5)
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width, x=x,
                       special_colors={i: (0, 255, 0), j + 1: (0, 0, 255)})
            pygame.display.update()
            pygame.time.wait(5)

    def mergeSort(arr, l, r):
        if l < r:
            m = (l + (r - 1)) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

    mergeSort(arr, 0, len(arr) - 1)
    sorting = False


def heap_sort(arr, screen, padding, screen_width, x):
    sorting = True

    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            draw_array("Heap Sort", arr, screen, padding, screen_width=screen_width, x=x,
                       special_colors={i: (0, 255, 0), largest: (0, 0, 255)})
            pygame.display.update()
            pygame.time.wait(5)
            # Heapify the root.
            heapify(arr, n, largest)

    # The main function to sort an array of given size
    def heapSort(arr):
        n = len(arr)
        # Build a maxheap.
        for i in range(n, -1, -1):
            heapify(arr, n, i)
        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            draw_array("Heap Sort", arr, screen, padding, screen_width=screen_width, x=x,
                       special_colors={i: (0, 255, 0), 0: (0, 0, 255)})
            pygame.display.update()
            pygame.time.wait(5)
            heapify(arr, i, 0)

    heapSort(arr)
    sorting = False


# random array with 1000 elements
n = 100
arr = [random.randint(0, 1000 - 2 * 5) for i in range(n)]

print(arr)


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
            x-2*padding, (480 - 2 * padding) - arr[i], screen_width - padding, arr[i]))

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
                pygame.time.wait(5)
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    sorting = True
    # create an empty stack
    size = len(arr)
    stack = [0] * (size)
    # initialize top of stack
    top = -1
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = 0
    top = top + 1
    stack[top] = size - 1
    # keep popping from stack while is not empty
    while top >= 0:
        # pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        # set pivot element at its correct position in sorted array
        p = partition(arr, l, h)
        draw_array("Quick Sort", arr, screen, padding,
                   screen_width=screen_width, x=x, )
        # if there are elements on left side of pivot, then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        # if there are elements on right side of pivot, then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def counting_sort(arr, screen, padding, screen_width, x):
    print("Counting Sort is running...")
    sorting = True
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(max(arr) + 1)]
    ans = [0 for _ in arr]
    for i in arr:
        count[i] += 1
        draw_array("Count Array", count, screen, padding, screen_width=screen_width, x=x,
                   special_colors={i: (0, 255, 0), })
        pygame.display.update()
        pygame.time.wait(5)

    screen.fill((0, 0, 0))
    # Change count[i] so that count[i] now contains actual position of this character in output array
    for i in range(1, len(count) - 1):
        count[i] += count[i - 1]
        draw_array("Counting Sort", count, screen, padding, screen_width=screen_width, x=x,
                   special_colors={i: (0, 255, 0), i - 1: (0, 0, 255)})
        pygame.display.update()
        pygame.time.wait(5)
    screen.fill((0, 0, 0))
    for i in range(len(arr) - 1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        draw_array("Counting Sort", output, screen, padding,
                   screen_width=screen_width, x=x, special_colors={i: (0, 255, 0)})
        pygame.display.update()
        pygame.time.wait(5)


    screen.fill((0, 0, 0))
    for i in range(len(arr)):
        ans[i] = output[i]
        draw_array("Counting Sort", ans, screen, padding, screen_width=screen_width, x=x,
                   special_colors={i: (0, 255, 0)})
        pygame.display.update()
    screen.fill((0, 0, 0))
    arr = ans
    sorting = False


def radix_sort(arr, screen, padding, screen_width, x):
    sorting = True
    iter = max(arr)
    maxIter = len(str(iter))

    exp = 1
    for i in range(maxIter + 1):
        counting_sort(arr, screen, padding, screen_width, x)
        draw_array("Radix Sort", arr, screen, padding,
                   screen_width=screen_width, x=x)
        pygame.display.update()
        pygame.time.wait(5)
        screen.fill((0, 0, 0))
        exp *= 10
    sorting = False


sorting = False
menu = True

def read_array(n):
    arr = []
    with open("array.txt", "r") as f:
        for line in f:
            arr.append(int(line))

    return arr[0:n] if n < len(arr) else arr

def draw_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Helvetica', 30)
    text = font.render("Sorting Algorithms", 1, (255, 255, 255))
    # show key bindings for sorting algorithms , bubble, insertion, merge, heap, quicksort,
    font = pygame.font.SysFont('Helvetica', 20)
    text1 = font.render("Press 1 for Bubble Sort", 1, (255, 255, 255))
    text2 = font.render("Press 2 for Insertion Sort", 1, (255, 255, 255))
    text3 = font.render("Press 3 for Merge Sort", 1, (255, 255, 255))
    text4 = font.render("Press 4 for Heap Sort", 1, (255, 255, 255))
    text5 = font.render("Press 5 for Quick Sort", 1, (255, 255, 255))
    text6 = font.render("Press 6 for Counting Sort", 1, (255, 255, 255))
    text7 = font.render("Press 7 for Radix Sort", 1, (255, 255, 255))

    screen.blit(text, (100, 0))
    screen.blit(text1, (100, 50))
    screen.blit(text2, (100, 100))
    screen.blit(text3, (100, 150))
    screen.blit(text4, (100, 200))
    screen.blit(text5, (100, 250))
    screen.blit(text6, (100, 300))
    screen.blit(text7, (100, 350))
    pygame.display.update()
    pygame.time.wait(10)


while True:
    sorting_name = "No sorting algorithm selected"
    padding = screen.get_width() // n * 0.05

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not sorting:
                sorting = False
                draw_menu()
            if event.key == pygame.K_1 and not sorting:
                pygame.event.pump()
                sorting_name = "Bubble Sort"
                arr = read_array(n)
                screen.fill(black)
                bubble_sort(arr, screen, padding=padding,
                            screen_width=screen_width, x=padding)
            if event.key == pygame.K_2 and not sorting:
                pygame.event.pump()
                sorting_name = "Insertion Sort"
                
                screen.fill(black)
                arr = read_array(n)
                insertion_sort(arr, screen, padding=padding,
                               screen_width=screen_width, x=padding)
            if event.key == pygame.K_3 and not sorting:
                pygame.event.pump()
                sorting_name = "Merge Sort"
                screen.fill(black)
                arr = read_array(n)
                merge_sort(arr, screen, padding=padding,
                           screen_width=screen_width, x=padding)
            if event.key == pygame.K_4 and not sorting:
                pygame.event.pump()
                sorting_name = "Heap Sort"
                screen.fill(black)
                arr = read_array(n)
                heap_sort(arr, screen, padding=padding,
                          screen_width=screen_width, x=padding)
            if event.key == pygame.K_5 and not sorting:
                pygame.event.pump()
                sorting_name = "Quick Sort"
                screen.fill(black)
                arr = read_array(n)
                quick_sort(arr, screen, padding=padding,
                           screen_width=screen_width, x=padding)
            if event.key == pygame.K_6 and not sorting:
                print("Counting Sort")
                pygame.event.pump()
                sorting_name = "Counting Sort"
                screen.fill(black)
                arr = read_array(n)
                counting_sort(arr, screen, padding=padding,
                              screen_width=screen_width, x=padding)
            if event.key == pygame.K_7 and not sorting:
                print("Radix Sort")
                pygame.event.pump()
                sorting_name = "Radix Sort"
                screen.fill(black)
                arr = read_array(n)
                radix_sort(arr, screen, padding=padding,
                           screen_width=screen_width, x=padding)

    clock.tick(3)
    if not sorting:
        draw_menu()
    screen.fill(black)
    screen_width = (screen.get_width() - 2 * padding) / n
    screen_height = screen.get_height()
    time.sleep(0.1)
    # getting all the events

    x = padding
