'''
Rank Participants
A sports academy has recorded the timings (in seconds) of participants in
a race.
Write a program to arrange the timings from the fastest to the slowest so
that the winners can be announced.
'''
time = list(map(int, input("Enter timings: ").split()))

n = len(time)

for i in range(n):
    for j in range(n - i - 1):
        if time[j] > time[j + 1]:
            time[j], time[j + 1] = time[j + 1], time[j]

print("Fastest to Slowest:", time)