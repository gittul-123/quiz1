# quiz_game.py

class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz("겉은 빨갛고 아삭하며, '하루에 하나면 의사가 필요 없다는 과일은?", ["사과", "토마토", "자두", "체리"], 1),
            Quiz("여름철 대표 과일로, 검은 줄무늬가 있는 커다란 과일은?", ["딸기", "수박", "참외", "복숭아"], 2),
            Quiz("길쭉한 모양에 껍질을 까서 먹는 노란색 과일은?", ["바나나", "키위", "오렌지", "블루베리"], 1),
            Quiz("(넌센스퀴즈) 세상에서 가장 뜨거운 과일은?", ["백도복숭아", "황도복숭아", "납작복숭아", "천도복숭아"], 4),
            Quiz("껍질에 털이 있고 분홍빛이 도는 달콤한 과일은?", ["복숭아", "키위", "두리안", "람부탄"], 1),
        ]
        self.best_score = 0

        self.load()
    
    def run(self):
        while True:
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = input("선택: ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                print("퀴즈 추가 (아직 미구현)")
            elif choice == "3":
                print("목록 (아직 미구현)")
            elif choice == "4":
                print("점수 (아직 미구현)")
            elif choice == "5":
                print("종료합니다.")
                break
            else:
                print("잘못된 입력!")
    
    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            quiz.display()
            answer = int(input("정답: "))

            if quiz.check_answer(answer):
                print("정답!")
                score += 1
            else:
                print("오답!")

        print(f"점수: {score}/{len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("최고 점수 갱신!")

    
