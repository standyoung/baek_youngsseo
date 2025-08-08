curr = list(map(int, list(input().split(":"))))
goal = list(map(int, list(input().split(":"))))
anws = [0, 0, 0]

curr_sum = curr[0] * 3600 + curr[1] * 60 + curr[2]
goal_sum = goal[0] * 3600 + goal[1] * 60 + goal[2]

if goal_sum <= curr_sum:
    goal_sum += 24 * 3600 # 24시간

diff = goal_sum - curr_sum
anws = [diff // 3600, (diff % 3600) // 60, diff % 60]

print(f"{anws[0]:02d}:{anws[1]:02d}:{anws[2]:02d}")