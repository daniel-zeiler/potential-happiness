"""
You want to schedule a certain number of trips with a collection of several cabs.

Given an integer n representing a desired number of trips, and an array cabTravelTime representing your cabs and how
long it takes each cab (at that index of the array) to make a trip, return the minimum time required to make n trips.

Assume that cabs can run simultaneously and there is no waiting period between trips. There may be multiple cabs with
the same time cost.*

Examples If n=3 and cabTravelTime=[1,2], then the answer is 2. This is because the first cab (index 0, cost 1) can
make 2 trips costing a total of 2 time units, and the second cab can make a single trip costing 2 at the same time.

n=10
cabTravelTime=[1,3,5,7,8]

* 7 trips with cab 0 (cost 1)
* 2 trips with cab 1 (cost 3)
* 1 trip with cab 2 (cost 5)
So, answer is 7 (there could be other combinations)

n=3
cabTravelTime=[3,4,8]

* 2 trips with cab 0 (cost 6)
* 1 trip with cab 1 (cost 4)
Time = 6
"""


def min_time_required(n, cab_travel_time):
    result = 1
    while n >= 0:
        for cab_time in cab_travel_time:
            if cab_time <= result and not result % cab_time:
                n -= 1
            if n == 0:
                return result
        result += 1
    return result


n = 10
cabTravelTime = [1, 3, 5, 7, 8]
print(min_time_required(n, cabTravelTime))

"""
There is a long road with markers on it after each unit of distance. There are some ubers standing on the road. 
You are given the starting and ending coordinate of each uber (both inclusive). Note: At any given marker there may 
be multiple ubers or there may be none at all. 

Your task is to find the number of markers on which at least one uber is present. An uber with coordinates (l, 
r) is considered to be present on a marker m if and only if l ≤ m ≤ r. 

Example

For coordinates=[[4, 7], [-1, 5], [3, 6]], the output should be easyCountUber(coordinates) = 9.
"""
