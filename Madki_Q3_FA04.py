names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_steps = []
for person_steps in steps:
    total = sum(person_steps)
    total_steps.append(total)

max_steps = max(total_steps)
min_steps = min(total_steps)
top_index = total_steps.index(max_steps)

print(f"Total steps per person: {dict(zip(names, total_steps))}")
print(f"Top performer: {names[top_index]} with {max_steps} steps")
print(f"Difference between highest and lowest: {max_steps - min_steps} steps")
