import pygame, random, math

pygame.init()


class base:
    FONT = pygame.font.SysFont('Poppins-Regular', 30)
    BLACK = 6, 57, 112
    WHITE = 238, 238, 228
    SORTING_COLOUR = 135, 62, 35
    SIDE_PADDING = 120
    TOP_PADDING = 150

    def __init__(self, w, h, lst):
        self.startingX = None
        self.barHeight = None
        self.barWidth = None
        self.maxVal = None
        self.minVal = None
        self.arr = None

        self.width = w
        self.height = h
        self.window = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_arr(lst)

    def set_arr(self, lst):
        self.arr = lst
        self.minVal = min(lst)
        self.maxVal = max(lst)

        self.barWidth = round(self.width - self.SIDE_PADDING) / (2 * len(lst))
        self.barHeight = math.floor((self.height - self.TOP_PADDING) / (self.maxVal - self.minVal))
        self.startingX = self.SIDE_PADDING // 2


# display draw
def draw(draw_info_block):
    draw_info_block.window.fill(draw_info_block.BLACK)

    menu = draw_info_block.FONT.render("Reset (R) | Sort (Space) | Ascending (A) | Descending (D)", 1,
                                       draw_info_block.WHITE)
    algo = draw_info_block.FONT.render("Bubble (B) | Insertion (I) | Selection (S) | Merge (M) | Quick (Q)", 1,
                                       draw_info_block.WHITE)
    draw_info_block.window.blit(menu, (draw_info_block.width / 2 - menu.get_width() / 2, 25))
    draw_info_block.window.blit(algo, (draw_info_block.width / 2 - algo.get_width() / 2, 50))

    draw_bars(draw_info_block, -1, -1)
    pygame.display.update()


# draws bars
def draw_bars(draw_information, a, b, c=-1, clr=False):
    lst = draw_information.arr

    if clr:
        # create a bar for each "number" to be sorted
        rect = (draw_information.SIDE_PADDING // 2, draw_information.TOP_PADDING, draw_information.width -
                draw_information.SIDE_PADDING, draw_information.height)
        pygame.draw.rect(draw_information.window, draw_information.BLACK, rect)

    # convert each number in the array to a bar
    for i, val in enumerate(lst):
        x = draw_information.startingX + (2 * i) * draw_information.barWidth
        y = draw_information.height - (val - draw_information.minVal +
                                       1) * draw_information.barHeight
        colour = (217, 212, 195)
        # while the bar is being checked, change the colour (to show it is being iterated over)
        if i == a or i == b or i == c:
            colour = draw_information.SORTING_COLOUR

        # draw each bar
        pygame.draw.rect(draw_information.window, colour, (x, y, draw_information.barWidth, draw_information.height))

    if clr:
        pygame.display.update()


# generate the array of numbers to be sorted
def generate_array(n, minVal, maxVal):
    lst = []

    for i in range(n):
        lst.append(random.randint(minVal, maxVal))

    return lst


def bubble_sort(draw_info, ascending):
    lst = draw_info.arr  # initialize array
    clock = pygame.time.Clock()

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            clock.tick(150)
            if (ascending and lst[i] > lst[j]) or (not ascending and lst[i] < lst[j]):
                lst[i], lst[j] = lst[j], lst[i]  # swap adjacent elements
            draw_bars(draw_info, i, j, -1, True)


def insertion_sort(draw_info, ascending):
    arr = draw_info.arr  # initialize array
    clock = pygame.time.Clock()

    # iterate through the array
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            clock.tick(50)

            if (ascending and arr[j] < arr[j - 1]) or (not ascending and arr[j] > arr[j - 1]):
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            draw_bars(draw_info, j, j - 1, -1, True)


# selection sort algorithm
def selectionSort(draw_info, ascending):
    arr = draw_info.arr  # initalize array
    clock = pygame.time.Clock()

    index = 0  # initialize minimum value to location 0

    # traverse through array to find minimum value
    for i in range(len(arr)):
        index = i  # set index of siu
        for j in range(i, len(arr)):
            clock.tick(150)
            # if any element is smaller than the element at index, swap the values
            if (ascending and arr[j] < arr[index]) or (not ascending and arr[j] > arr[index]):
                index = j  # update the index of the minimum value
            draw_bars(draw_info, index, j, -1, True)
        arr[i], arr[index] = arr[index], arr[i]


# quick sort algorithm
def quickSort(draw_info, ascending):
    quickSortHelper(draw_info, ascending, 0, len(draw_info.arr))


# function to find the partition position
def quickSortHelper(draw_info, ascending, start, end):
    arr = draw_info.arr  # initialize array

    if end <= start:
        return

    pos = end - 1  # pointer for the greater element
    clock = pygame.time.Clock()

    # traverse through all elements and compare each element with pivot
    for i in range(end - 1, start, -1):
        clock.tick(150)

        # if element smaller than the pivot is found, swap it with the greater element pointed
        if (ascending and arr[i] > arr[start]) or (not ascending and arr[i] < arr[start]):
            arr[pos], arr[i] = arr[i], arr[pos]
            pos -= 1
        draw_bars(draw_info, start, i, pos, True)
        arr[pos], arr[start] = arr[start], arr[pos]

    quickSortHelper(draw_info, ascending, start, pos)  # recursive call to the left of pivot
    quickSortHelper(draw_info, ascending, pos + 1, end)  # recursive call to the right of pivot


# merge sort algorithm (merging the two halves)
def merge(draw_info, arr, l, r, ascending):
    i = j = 0
    clock = pygame.time.Clock()

    for pos in range(len(l) + len(r)):
        clock.tick(100)
        temp = arr  # copy data to temp array
        p1 = p2 = -1
        list1 = True

        # find smaller element
        if i == len(l) or (j < len(r) and ((ascending and r[j] < l[i]) or (not ascending and r[j] > l[i]))):
            arr[pos] = l[j]
            j += 1
            list1 = False
        else:
            arr[pos] = l[i]
            i += 1

        for k in range(len(arr)):
            if arr[k] != temp[k]:
                if p1 == -1:
                    p1 = k
                else:
                    p2 = k

        draw_bars(draw_info, p1, p2, -1, True)

        if list1:
            i += 1
        else:
            j += 1

    return arr


# merge sort algorithm (merging the two halves)
# overloaded with extra parameter
def merge(draw_info, arr, l, r, ascending, start):
    i = j = 0
    clock = pygame.time.Clock()
    for pos in range(len(l) + len(r)):
        clock.tick(150)
        # find smaller element
        if i == len(l) or (j < len(r) and ((ascending and r[j] < l[i]) or (not ascending and r[j] > l[i]))):
            arr[pos] = r[j]
            j += 1
            draw_bars(draw_info, pos + start, len(l) + start + j, -1, True)
        else:
            arr[pos] = l[i]
            draw_bars(draw_info, pos + start, start + i, -1, True)
            i += 1

    return arr


def mergeSort(draw_info, ascending):
    mergeSortHelper(draw_info, draw_info.arr, ascending, 0)


# function that splits the array into 2 halves and then remerges them
def mergeSortHelper(draw_info, arr, ascending, start):
    if len(arr) == 1:
        return

    # finds the mid index of the array
    mid = len(arr) // 2

    # divides array into 2 halves
    l = arr[:mid]
    r = arr[mid:]

    mergeSortHelper(draw_info, l, ascending, start)  # sort first half
    mergeSortHelper(draw_info, r, ascending, start + len(arr) // 2)  # sort second half
    arr = merge(draw_info, arr, l, r, ascending, start)  # merge the two halves


# -------------main-------------
run = True
n = 40
minVal, maxVal = 0, 100

sorting = False
ascending = True
clock = pygame.time.Clock()

arr = generate_array(n, minVal, maxVal) 
draw_info = base(1000, 800, arr) 
algorithm = bubble_sort

while run:
    clock.tick(300)
    draw(draw_info)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run = False
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_r:  
            arr = generate_array(n, minVal, maxVal)
            draw_info.set_arr(arr)
            sorting = False
        elif event.key == pygame.K_SPACE and sorting == False: 
            sorting = True
            algorithm(draw_info, ascending)


        # ascending or descending
        elif event.key == pygame.K_a and not sorting:
            ascending = True
        elif event.key == pygame.K_d and not sorting:
            ascending = False

        # picking sorting algo
        elif event.key == pygame.K_b and not sorting:
            algorithm = bubble_sort
        elif event.key == pygame.K_i and not sorting:
            algorithm = insertion_sort
        elif event.key == pygame.K_s and not sorting:
            algorithm = selectionSort
        elif event.key == pygame.K_q and not sorting:
            algorithm = quickSort
        elif event.key == pygame.K_m and not sorting:
            algorithm = mergeSort

pygame.quit()
