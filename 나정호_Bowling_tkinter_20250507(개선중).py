import tkinter as tk
from tkinter import ttk
import random

class Bowling_game:
    def __init__(self):
        # 기본상수
        self.d_frame = 10 # 전체 프레임
        self.d_pin = 10 # 기본 핀의 수
        # 상태
        self.strike = 2 # 스트라이크 처리
        self.spare = 1 # 스페어 처리
        self.normal = 0
        # 연산값 초기화
        self.score = 0 # 해당 프레임의 점수
        self.total = 0 # 누적합
        # 전체 프레임 점수를 저장할 자료형
        self.player_name = input("플레이어의 이름을 입력하세요. :")
        self.player = [] #플레이어 점수 기록

# 지역변수와 전역변수 활용

    def playing_game(self):

        for frame in range(self.d_frame-1): # 1~9 프레임까지
            # 지역변수 초기화
            throw1 = 0
            throw2 = 0
            p_list = [0,0,0,0,0] #프레임별 점수를 기록할 자료형

            throw1 = random.randint(0,self.d_pin)
        
            if throw1 == self.d_pin: # 스트라이크
                p_list[0] = throw1
                p_list[3] = p_list[0]
                p_list[4] = self.strike
                # 보너스확인
                self.bonus_point(throw1)

            else: # 스트라이크 실패
                left_pin = self.d_pin - throw1

                throw2 = random.randint(0,left_pin)
                p_list[0] = throw1
                p_list[1] = throw2
                p_list[3] = p_list[0] + p_list[1]

                if left_pin == throw2:
                    p_list[4] = self.spare

                else: # 스페어 처리 실패
                    p_list[4] = self.normal
                # 보너스확인   
                self.bonus_point(throw1, throw2) 
                

            self.player.append(p_list)

        if len(self.player) == 9: #조건문을 없애고 그냥 나열하고 마지막에 리스트 할당 가능
            throw1 = random.randint(0,self.d_pin)
            throw2 = 0
            throw3 = 0
            p_list = [0,0,0,0,0]

            # 보너스 확인
            self.bonus_point(throw1)

            if throw1 == self.d_pin:
                throw2 = random.randint(0,self.d_pin)
                self.bonus_point(throw2)
                if throw2 == self.d_pin:
                    throw3 = random.randint(0,self.d_pin)
                    p_list[0] = throw1
                    p_list[1] = throw2
                    p_list[2] = throw3
                    p_list[3] = p_list[0] + p_list[1] + p_list[2]
                    p_list[4] = self.normal

                else: 
                    left_pin = self.d_pin - throw2
                    throw3 = random.randint(0,left_pin)
                    p_list[0] = throw1
                    p_list[1] = throw2
                    p_list[2] = throw3
                    p_list[3] = p_list[0] + p_list[1] + p_list[2]
                    p_list[4] = self.normal

            else:
                left_pin = self.d_pin - throw1
                throw2 = random.randint(0,left_pin)
                self.bonus_point(throw2)
                if throw2 == left_pin:
                    throw3 = random.randint(0,self.d_pin)
                    p_list[0] = throw1
                    p_list[1] = throw2
                    p_list[2] = throw3
                    p_list[3] = p_list[0] + p_list[1] + p_list[2]
                    p_list[4] = self.normal

                else:
                    p_list[0] = throw1
                    p_list[1] = throw2
                    p_list[3] = p_list[0] + p_list[1]
                    p_list[4] = self.normal
            self.player.append(p_list)                    


    def bonus_point(self,throw1,throw2 = 0): # throw1은 필수값, throw2는 조건부
        n = len(self.player)

        # 직전 프레임
        if n >= 1: #플레이어 리스트가 1보다 크다.
            prev = self.player[-1]
            if prev[4] == self.strike:
                prev[3] += throw1 + throw2
            elif prev[4] == self.spare:
                prev[3] += throw1

        # 두 프레임 전 (더블 스트라이크 보너스 처리)
        if n >= 2: # 플레이어 리스트가 2보다 클 때, 위에도 포함되게됨
            prev2 = self.player[-2]
            prev1 = self.player[-1]
            if prev2[4] == self.strike and prev1[4] == self.strike:
                prev2[3] += throw1


def display_scores(game: Bowling_game):
    game.playing_game()
    scores = game.player
    total = sum([frame[3] for frame in scores])  # 합계 계산

    root = tk.Tk()
    root.title("볼링 점수판")

    # 제목 행
    tk.Label(root, text="플레이어", borderwidth=1, relief="solid", width=10).grid(row=0, column=0)

    for i in range(10):
        tk.Label(root, text=f"{i+1}프레임", borderwidth=1, relief="solid", width=10).grid(row=0, column=i+1)

    tk.Label(root, text="총합", borderwidth=1, relief="solid", width=10).grid(row=0, column=11)

    # 이름 출력
    tk.Label(root, text=game.player_name, borderwidth=1, relief="solid", width=10).grid(row=1, column=0,rowspan=4,sticky="nsew")

    # 점수 출력: 1투, 2투, 합계만
    for i, frame in enumerate(scores):
        # 1투
        tk.Label(root, text=str(frame[0]), borderwidth=1, relief="solid", width=10).grid(row=1, column=i+1)
        # 2투
        tk.Label(root, text=str(frame[1]), borderwidth=1, relief="solid", width=10).grid(row=2, column=i+1)
        # 3투
        tk.Label(root, text=str(frame[2]), borderwidth=1, relief="solid", width=10).grid(row=3, column=i+1)
        # 합계
        tk.Label(root, text=str(frame[3]), borderwidth=1, relief="solid", width=10).grid(row=4, column=i+1)

    # 총합 출력
    tk.Label(root, text=str(total), borderwidth=1, relief="solid", width=10).grid(row=1, column=11, rowspan=4,sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    game = Bowling_game()