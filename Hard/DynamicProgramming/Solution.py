from typing import List


def calculateMinimumHP(dungeon: List[List[int]]) -> int:
    answer = [[float('inf') for _ in range(len(dungeon[0]) + 1)] for _ in range(len(dungeon) + 1)]

    for x in range(len(dungeon) - 1, -1, -1):
        for y in range(len(dungeon[0]) - 1, -1, -1):

            current_health = dungeon[x][y]

            right = max(1, answer[x][y + 1] - current_health)
            below = max(1, answer[x + 1][y] - current_health)
            next_health = min(right, below)

            if next_health != float('inf'):
                # the result is the minimum of the necessary health of adjacent cells minus the current value,
                # max 1 because we need to survive.
                min_health = next_health
            elif current_health >= 0:
                # we reached a health position
                min_health = 1
            else:
                # base case at monster.  Everything is inf around it.
                min_health = 1 - current_health
            answer[x][y] = min_health

    return answer[0][0]
