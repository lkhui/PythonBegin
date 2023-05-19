with open('string_1.txt', "r") as f:
    print(f.read())


ss = ["Helloworld", "Testing me again", "ohno"]

for s, n in zip(ss, [len(s) for s in ss]):
    print(f'{s} - length {n}')

arr = [(s, len(s)) for s in ss]

for i in arr :
    print(f'{i[0]} -- {i[1]}')
