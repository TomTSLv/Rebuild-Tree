import pygame
import time
import sys
import random
import math
from rebuildTree import rebuildTree

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 1000
HEIGHT = 700
XBUFFER = 100
YBUFFER = 100
STEP = 1

size = (WIDTH+XBUFFER,HEIGHT+YBUFFER)
screen = None
font = None
clock = None

def randColor():
    while True:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        if red > 200 or green > 200 or blue > 200:
            break
    return (red, green, blue)

def randomList(n):
    l = [i for i in range(0,n)]
    random.shuffle(l)
    return l

def RebuildTreeInsert(n):
    tree=rebuildTree()
    for i in range(1,n+1):
        tree.insert(i)
	
def main():
    pygame.init()
    global screen, font, clock
    screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    font = pygame.font.SysFont("Tahoma", 25, True, False)
    pygame.display.set_caption("Runtime of Rebuild Tree")
    clock = pygame.time.Clock()

    functionList = [RebuildTreeInsert]

    sim(functionList)

def time_function(f, *args):
    start = time.clock()
    f(*args)
    return time.clock() - start

def print_text(text,location,color=BLACK):
    t=font.render(text,True,color)
    screen.blit(t,location)

def sim(functionList):
    done = False
    pause = False
    N = 0
    runtimes = [[] for i in range(len(functionList))]
    colors = [randColor() for i in range(len(functionList))]
    
    while not done:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
        if not pause:
            N += STEP

            for i in range(len(functionList)):
                runtimes[i].append(time_function(functionList[i],N))
	    # Max time over union of the functions' runtimes
	    # Used to determine the scale of the y-axis 
	    # (see arguments for line pygame.draw.line())
            MaxTime=max([max(i) for i in runtimes])
	    # Total number of runs
	    # Used to determine the scale of x-axis
	    # (see arguments for line pygame.draw.line())
        num_of_runtimes = len(runtimes[0])
        for i in range(len(functionList)):
            for j in range(1,len(runtimes[i])):
                x_start = WIDTH * (j - 1) / num_of_runtimes
                y_start = HEIGHT - HEIGHT *\
                    (runtimes[i][j - 1] / MaxTime)

                x_end = WIDTH * j / num_of_runtimes
                y_end = HEIGHT - HEIGHT * runtimes[i][j] / MaxTime

                start = (x_start, y_start)
                end = (x_end, y_end)
                pygame.draw.line(screen, colors[i], start, end)
        print_text(str(MaxTime),(WIDTH,0))
        print_text(str(N),(WIDTH,HEIGHT))

        for f in range(len(functionList)):
            print_text(functionList[f].__name__,(100,HEIGHT-20*f), colors[f])
            print_text(str(runtimes[f][-1]).format("f"),(400,HEIGHT-20*f),\
                       colors[f])

        pygame.display.flip()
        clock.tick(60)

main()
