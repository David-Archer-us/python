"""
This is one of Round F in 2020 Google Kickstart

There are N people numbered from 1 to N, 
standing in a queue to withdraw money from an ATM. 
The queue is formed in ascending order of their number. 
The person numbered i wants to withdraw amount Ai. 
The maximum amount a person can withdraw at a time is X. 
If they need more money than X, 
they need to go stand at the end of the queue and wait for their turn in line. 
A person leaves the queue once they have withdrawn the required amount.

You need to find the order in which all the people leave the queue.
"""

cases = int(input())
for i in range(1, cases+1):
    nx = input().split()
    num = int(nx[0])
    limit = int(nx[1])
    requres = list(map(int, input().split()))
    result = "Case #" + str(i) + ": "
    times = []
    for j in range(num):
        time = requres[j]//limit
        if requres[j]%limit != 0: time += 1
        times.append(time)
    sortedtimes = sorted(times)
    for i in range(num):
        for j in range(num):
            if times[j] == sortedtimes[i]:
                if i != num-1:
                    sortedtimes = sortedtimes[:i] + [str(j+1)] + sortedtimes[i+1:]
                else: sortedtimes = sortedtimes[:i] + [str(j+1)]
                times[j]=0
                break
    result += " ".join(sortedtimes)
    print(result)
