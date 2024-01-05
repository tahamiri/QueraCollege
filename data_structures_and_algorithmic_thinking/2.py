# جستجو در دنباله 2


sequence_length, question_count = map(int, input().split())
values = list(map(int, input().split()))

m = max(values)
result = []

cnt = [values.count(i) for i in range(0, m+1)]
x = 0
ps = []
for i in cnt:
    x = x + i
    ps.append(x)
    
for i in range(0, question_count):
    question = int(input())
    if question > m:
        result.append(sequence_length)
        
    else:
        result.append(ps[question-1])

print(*result, sep="\n")
