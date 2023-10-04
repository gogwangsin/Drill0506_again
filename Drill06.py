from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1000, 800


def load_resources():
    global TUK_ground, character
    global arrow

    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():  # 변수 초기화 initalization
    global running, cx, cy, frame
    global t
    global action
    global mx, my

    mx, my = 0, 0
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3  # 애니메이션 정지한 상태 default

    # set_new_target_arrow()


# def set_new_target_arrow():
#     global sx, sy, hx, hy, t
#     global action
#     global frame
#     sx, sy = cx, cy  # p1 : 시작점 - 시작 위치 == 처음 캐릭터 위치
#     # hx, hy = 50, 50 # 테스트 용도
#     hx, hy = random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)  # p2 : 끝점.
#     t = 0.0
#     action = 1 if sx < hx else 0  # 목적지 x보다 작은 x라면 액션 [1]로 바꾸기
#     frame = 0

def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(mx, my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)  # action에 따른 모션 변화 0,1,2,3
    update_canvas()


def update_world():
    global frame
    global cx, cy
    global t

    frame = (frame + 1) % 8

    # if t <= 1.0:
    #     cx = (1 - t) * sx + t * hx  # 시작점과 끝점을 기억해야함.
    #     cy = (1 - t) * sy + t * hy  # cx는 시작 x와 끝 x를 1-t:t의 비율로 섞은 위치
    #     t += 0.001  # t가 0일 때 처음 위치, t가 1일 때 목적 위치
    # else:  # 목적지에 도달했을 때
    #     cx, cy = hx, hy  # 강제로 캐릭터 위치를 목적지 위치와 정확히 일치시킴. 오차 해결
    #     set_new_target_arrow()


open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()  # 월드의 현재 내용을 그린다.
    handle_events()  # 사용자 입력을 받아들인다.
    update_world()  # 월드 안의 객체들의 상호작용을 계산하고 그 결과를 update한다.

close_canvas()
