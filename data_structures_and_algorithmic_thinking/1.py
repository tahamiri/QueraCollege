# جست‌وجو در دنباله ۱

input_str1 = input()

a,b = input_str1.split()

sequence_length,question_count = int(a), int(b)

input_str2 = input()


v = input_str2.split()

values = [int(i) for i in v]

output_list = []

for i in range(0, question_count):
    list = []
    x = int(input())
    for j in range(0, sequence_length):
        if values[j] < x:
            list.append(values[j])
    output_list.append(len(list))

for i in output_list:
    print(i)

