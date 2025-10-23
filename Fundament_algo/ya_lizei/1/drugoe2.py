n, m = map(int, input().split())
s = input().strip()

parts = [input().strip() for _ in range(m)]

len_part = n // m

part_to_idx = {part: i + 1 for i, part in enumerate(parts)}

result = []
for i in range(0, n, len_part):
    segment = s[i:i + len_part]
    result.append(part_to_idx[segment])

print(' '.join(map(str, result)))
