from pickle import REDUCE
from pickletools import read_unicodestring1
import pygame
from pygame import K_RIGHT, QUIT,KEYDOWN, K_LEFT, Rect, K_DOWN

# 창크기
w = 800 #가로크기
h = 800 #세로크기
# s: 창에 관한 모든 정보
s = pygame.display.set_mode(   (w,h)     )
# 시간과 관련된 모든 정보
cloc = pygame.time.Clock()
# 사각형의 최초위치
x1 = 100
y1 = 100

x2 = 400
y2 = 100


x3 = 50
y3 = 200
w3 = 300
h3 = 50

x4 = 50
y4 = 500
w4 = 100
h4 = 200

# 색상 튜플 (R, G, B)
BLACK = ( 0, 0 , 0)
GREEN = (0 , 255, 0 )
BLUE = (0 , 0, 255)
RED = (255,0,0)
# 테두리 굶기 (0이면 안쪽 색칠)
Th = 0
# 파이게임 루프
running =True

mx = 0
my = 0
while running:
    
    # 모든 이벤트를 검사
    for event in pygame.event.get():
        # 만약 가져온 이벤트가
        # 종료버튼을 누른 것이라면
        if event.type == QUIT:
            running = False
            break
        # 마우스 버튼을 클릭했다면
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
        # 키보드를 눌렀다면
        # if event.type == KEYDOWN:
        #     # 오른쪽 방향키가 눌렸다면
        #     if event.key == K_RIGHT:
        #         x += 5
        #         # x = x % 3


    # 키보드 눌려진 상태인지 검사
    myKeys = pygame.key.get_pressed()
    if myKeys[K_RIGHT]:
        x1 += 1
        x2 -= 1
    elif myKeys[K_DOWN]:
        y3 += 1


    


    # 두 사각형의 충돌 감지
    # rect 형식의 사각형 모양 (시작 x위치, 시작 y위치, 가로길이, 세로길이)
    Rect1 = Rect(x1, y1, 200,80)
    Rect2 = Rect(x2, y2, 200,80)
    if pygame.Rect.colliderect(Rect1, Rect2):
        print("두 사각형이 충돌하였습니다!")
        COLOR1 = COLOR2 = RED
    else:
        COLOR1 = GREEN
        COLOR2 = BLUE

    Rect3 = Rect(x3, y3, w3, h3)
    Rect4 = Rect(x4, y4, w4, h4)
    if pygame.Rect.colliderect(Rect3, Rect4):
        print("두 타원이 충돌하였습니다!")
        COLOR3 = COLOR4 = RED
    else:
        COLOR3 = GREEN
        COLOR4 = BLUE
    
    
    # 클릭한 위치가 사각형 1 버튼 위인지 검사한다
    if mx >= Rect1.topleft[0] and mx <= Rect1.topright[0]:
        if my >= Rect1.topleft[1] and my <= Rect1.bottomright[1]:
            COLOR1 = (255,0,255)
            print("버튼을 눌렀습니다")



    # 화면의 색을 흰색으로
    s.fill( (255,255,255)   )
    # 사각형 1 그리기
    pygame.draw.rect(s, COLOR1, Rect1, Th)
    # 사각형 2 그리기
    pygame.draw.rect(s, COLOR2, Rect2, Th)
    # 원 1 그리기
    pygame.draw.ellipse(s, COLOR3, Rect3, Th)
     # 원 1을 둘러싸는 사각형 그리기
    pygame.draw.rect(s, (0,0,0),Rect3 , 1)
    pygame.draw.ellipse(s, COLOR4, Rect4, Th)
    pygame.draw.rect(s, (0,0,0),Rect4 , 1)
    # 화면을 주기적으로 다시 그려줌(1/60초,마다)
    pygame.display.update()
    cloc.tick(60)
