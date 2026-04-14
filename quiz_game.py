# quiz_game.py

class QuizGame:
    def run(self):
        while True:
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = input("선택: ")

            if choice == "1":
                print("퀴즈 풀기 (아직 미구현)")
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