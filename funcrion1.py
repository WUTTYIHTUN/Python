s = [1,2,3,4,5]
t = 0

for i in s:
    t = i + s
t
.................................................
a = [10,20,30,40,50,60]
b = [20,40,50,60,80,70]
c = [50,90,70,80,50,70]

def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

d = sum(a)
e = sum(b)
f = sum(c)

print(d,e,f)

Result ＝210，....
................................................
a = [10,20,30,40,50,60]
b = [20,40,50,60,80,70]
c = [50,90,70,80,50,70]

num_list = [a,b,c]
ap_list = []

for i in num_list:
    ap_list.append(sum(i))

print(ap_list)

Result ＝　[210,,]
...................................................
