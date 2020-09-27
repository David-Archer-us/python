"""
This is one of Round F in Google Kickstart 2020

You are in charge of deploying robots to harvest Kickium from a nearby asteroid. 
Robots are not designed to work as a team, 
so only one robot can harvest at any point of time. 
A single robot can be deployed for up to K units of time in a row before it returns for calibration, 
regardless of how much time it spends on harvesting during that period. 
Harvesting can only be done during specific time intervals. 
These time intervals do not overlap. Given K and the time intervals in which harvesting is allowed, 
what is the minimum number of robot deployments required to harvest at all possible times?
"""

import heapq
cases = int(input())
for j in range(cases):
    botsdura = input().split()
    bots = int(botsdura[0])
    duration = int(botsdura[1])
    intervals = []
    for i in range(bots):
        heapq.heappush(intervals, [int(x) for x in input().split()])
    
    result = 1
    interval = heapq.heappop(intervals)
    botst = interval[0]
    botdue = botst + duration
    havst = interval[0]
    havdue = interval[1]
    while havdue > botdue:
        result += 1
        botdue += duration
    while intervals:
        interval = heapq.heappop(intervals)
        havst = interval[0]
        havdue = interval[1]
        if havdue > botdue:
            result += 1
            if havst > botdue:
                botdue = havst + duration
            else:
                botdue += duration
        while havdue > botdue:
            result += 1
            botdue += duration
    print("Case #" + str(j+1) + ": " + str(result))
