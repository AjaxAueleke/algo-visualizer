import sys,pygame,random,time
pygame.init()


size = width, height = 720, 520

speed = [2,2]

black = 0,0,0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Algorithm Visualizer")
clock=pygame.time.Clock()
sorting = False
menu = True
def bubble_sort(arr, screen, padding, screen_width,x):
    sorting = True
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                try:
                    pygame.event.pump()
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    draw_array("Bubble Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={j: (0,255,0), j+1: (0,0,255)})
                    pygame.display.update()
                    pygame.time.wait(5)
                except Exception as e:
                    print(e)
                    sys.exc_info()
                    pass
    sorting = False

def insertion_sort(arr, screen, padding, screen_width,x):
    sorting = True
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            try:
                pygame.event.pump()
                arr[j+1] = arr[j]
                j -= 1
                draw_array("Insertion Sort",arr, screen, padding, screen_width=screen_width,x=x, special_colors={j: (0,255,0), j+1: (0,0,255)})
                pygame.display.update()
                pygame.time.wait(5)
            except Exception as e:
                print(e)
                sys.exc_info()
                pass
        arr[j+1] = key
    sorting = False

# random array with 1000 elements
n = 100
arr = [random.randint(0,480 - 2*5) for i in range(n)]


print(arr)
def draw_array(sorting,arr, screen, padding, screen_width, x, special_colors={}):
    # put a heading
    font = pygame.font.SysFont('Helvetica', 30)
    text = font.render(sorting, 1, (255,255,255))
    # draw the array values
    screen.fill((0,0,0))
    screen.blit(text, (x+(len(arr)//2*x), 0))
    color = (255,0,0)
    for i in range(len(arr)):
        if i in special_colors:
            color = special_colors[i]
        pygame.draw.rect(screen, color, pygame.Rect(x, (520-2*padding)-arr[i], screen_width - padding, arr[i]))
        x = x+screen_width

sorting = False
menu = True
while True:
    sorting_name = "No sorting algorithm selected"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and not sorting:
                pygame.event.pump()
                sorting_name = "Bubble Sort"
                screen.fill(black)
                bubble_sort(arr, screen, padding=padding, screen_width=screen_width,x=padding)
            if event.key == pygame.K_2 and not sorting:
                pygame.event.pump()
                sorting_name = "Insertion Sort"
                screen.fill(black)
                insertion_sort(arr, screen, padding=padding, screen_width=screen_width,x=padding)
            
            
    clock.tick(3)

    screen.fill(black)
    padding = screen.get_width() // n * 0.05
    screen_width = (screen.get_width() - 2*padding)/n
    screen_height = screen.get_height()
    time.sleep(0.1)
    # getting all the events
    


    x = padding
