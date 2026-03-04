names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

num_days = len(steps[0])

daily_totals = []
for day in range(num_days):
    total = 0
    for person in steps:
        total += person[day]
    daily_totals.append(total)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(num_days):
    print(f"{days[i]}: {daily_totals[i]} total steps")

max_total = max(daily_totals)
most_active_index = daily_totals.index(max_total)
print(f"Most active day overall: {days[most_active_index]} with {max_total} steps")
