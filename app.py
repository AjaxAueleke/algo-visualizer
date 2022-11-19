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

def merge_sort(arr, screen, padding, screen_width, x):
    sorting = True
    # iterative merge sort
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r- m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0 , n1):
            L[i] = arr[l + i]
        for j in range(0 , n2):
            R[j] = arr[m + 1 + j]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), j+1: (0,0,255)})
            pygame.display.update()
            pygame.time.wait(5)
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), j+1: (0,0,255)})
            pygame.display.update()
            pygame.time.wait(5)
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            draw_array("Merge Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), j+1: (0,0,255)})
            pygame.display.update()
            pygame.time.wait(5)
    def mergeSort(arr,l,r):
        if l < r:
            m = (l+(r-1))//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
    mergeSort(arr, 0, len(arr)-1)
    sorting = False

def heap_sort(arr, screen, padding, screen_width, x):
    sorting = True
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
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
            arr[i],arr[largest] = arr[largest],arr[i]  # swap
            draw_array("Heap Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), largest: (0,0,255)})
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
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]   # swap
            draw_array("Heap Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), 0: (0,0,255)})
            pygame.display.update()
            pygame.time.wait(5)
            heapify(arr, i, 0)
    heapSort(arr)
    sorting = False

# random array with 1000 elements
n = 100
arr = [random.randint(0,480 - 2*5) for i in range(n)]


print(arr)
def draw_array(sorting,arr, screen, padding, screen_width, x, special_colors={}):
    # put a heading

    pygame.event.pump()
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



def quick_sort(sorting, arr, screen, padding, screen_width,x, special_colors={}):
    sorting = True
    #create an empty stack
    size = len(arr)
    stack = [0] * (size)
    #initialize top of stack
    top = -1
    #push initial values of l and h to stack
    top = top + 1
    stack[top] = 0
    top = top + 1
    stack[top] = size - 1
    #keep popping from stack while is not empty
    while top >= 0:
        #pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        #set pivot element at its correct position in sorted array
        p = partition( arr, l, h)
        #if there are elements on left side of pivot, then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
        #if there are elements on right side of pivot, then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

        def partition(arr, l, h):
            i = ( l - 1 )
            x = arr[h]
            for j in range(l , h):
                if   arr[j] <= x:
                    # increment index of smaller element
                    i = i+1
                    arr[i],arr[j] = arr[j],arr[i]
                    draw_array("Quick Sort", arr, screen, padding, screen_width=screen_width,x=x, special_colors={i: (0,255,0), j: (0,0,255)})
                    pygame.display.update()
                    pygame.time.wait(5)
            arr[i+1],arr[h] = arr[h],arr[i+1]
            return ( i+1 )



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
            if event.key == pygame.K_3 and not sorting:
                pygame.event.pump()
                sorting_name = "Merge Sort"
                screen.fill(black)
                merge_sort(arr, screen, padding=padding, screen_width=screen_width,x=padding)
            if event.key == pygame.K_4 and not sorting:
                pygame.event.pump()
                sorting_name = "Heap Sort"
                screen.fill(black)
                heap_sort(arr, screen, padding=padding, screen_width=screen_width,x=padding)
            if event.key == pygame.K_5 and not sorting:
                pygame.event.pump()
                sorting_name = "Quick Sort"
                screen.fill(black)
                quick_sort(arr, screen, padding=padding, screen_width=screen_width,x=padding)
            
    clock.tick(3)

    screen.fill(black)
    padding = screen.get_width() // n * 0.05
    screen_width = (screen.get_width() - 2*padding)/n
    screen_height = screen.get_height()
    time.sleep(0.1)
    # getting all the events
    


    x = padding
