from urllib.parse import parse_qs

values = parse_qs('a=123&b=6666&c=8888&a=654')
print(values.get("a"))

f = values.get("f", [""])[0] or "999"
f2 = int(f)
if isinstance(f2, str):
    print("yeah")
else:
    print("oh no")    

