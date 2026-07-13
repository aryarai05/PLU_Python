'''
7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.

'''
score = list(map(int, input("Enter scores: ").split()))

n = len(score)

for i in range(n):
    for j in range(n - i - 1):
        if score[j] < score[j + 1]:
            score[j], score[j + 1] = score[j + 1], score[j]

print("Leaderboard:", score)