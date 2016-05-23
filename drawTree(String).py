from rebuildTree import rebuildTree
import pygame
from pygame.locals import *

def drawRebuildTree(screen,node,x,y):
    inc=70
    if node!=None:
        if node._left is not None:
            leftChildPos=drawRebuildTree(screen,node._left,x,y+inc)
            x=x+inc*TreeSize(node._left)
            pygame.draw.line(screen,(0,0,0),leftChildPos,(x,y))
        string1='element: '+ str(node._element)
        text1=font.render(string1,True,(0,0,0))
        string2='Current: '+ str(node._currentSize)
        text2=font.render(string2,True,(0,0,0))
        string3='Last Rebuild: '+ str(node._rebuildSize)
        text3=font.render(string3,True,(0,0,0))
        screen.blit(text1,(x,y))
        screen.blit(text2,(x,y+20))
        screen.blit(text3,(x,y+40))
        retval=(x,y)
        x=x+inc
        if node._right is not None:
            rightChildPos=drawRebuildTree(screen,node._right,x,y+inc)
            pygame.draw.line(screen,(0,0,0),rightChildPos,retval)
        return retval

def TreeSize(node):
    if node._left is None and node._right is None:
        return 1

    elif node._left is None and node._right is not None:
        return 1+TreeSize(node._right)

    elif node._left is not None and node._right is None:
        return 1+TreeSize(node._left)

    elif node._left is not None and node._right is not None:
        return 1+TreeSize(node._left)+TreeSize(node._left)

def drawInsert(char):
    s = 'Input a string to insert: '+char
    text = font.render(s, True, (0,0,0))
    screen.blit(text,(10,10))

def main(): 
    pygame.init()
    global width,height,dim
    (width,height) = (1024,768)
    dim = (width,height)
    global screen
    screen = pygame.display.set_mode(dim, 0, 32)
    screen.fill((255,255,255))
    pygame.display.set_caption('Rebuild Tree')
    global font
    font = pygame.font.SysFont('times new roman', 15)

    rbTree=rebuildTree()
    Insert = False
    char = ''
    
    screen.fill((255,255,255))
    running=True
    while running:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_RETURN:
                    rbTree.insert(char)
                    char=''
                elif event.key==K_BACKSPACE:
                    char=char[:-1]
                else:
                    char+=chr(event.key)
        drawInsert(char)
        drawRebuildTree(screen,rbTree._root,100,50)
        pygame.display.update()
    
main()
