arr = [2, 3, 6, 6, 5]

max_scors = max(arr)
print(max_scors)
print("$" * 20)
while max_scors in arr:
    arr.remove(max_scors)

print(arr)
x = max(arr)
print(x)

# Another Solution
# arr = list(set(arr))

# arr.sort(reverse=True)

# print(arr)
# print(arr[1])
n = int(input())
records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append((name, score))


lowest_score = sorted(set(score for name, score in records))

# lowest_score.sort(reverse=False)
print(lowest_score[1])

lowest_name = [name for name, score in records if score == lowest_score]

lowest_name.sort()
# lowest_name.append(lowest_score)

if _ in lowest_name:
    print(_)
