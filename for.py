for文
for 変数名　in データの集まり:
処理
.................................................
for文の基本

score = {'match':100,'science':90}
for key,value in score.items():
    print(key)
.................................................
profiles =[
    ('sato',170,74),
    ('tanaka',180,70),
    ('yoshida',165,55),
]
    
for name,height,weight in profiles:
    print(name,height,weight)
  ...............................................
break & else 

numbers = [4,1,5,7,11,3,4,5]
for num in numbers:
    if num >= 10:
        print('10以上の整数がありました')
        break
else:
    print('ありませんでした')
  ................................................
numbers = [1,2,3,4,5]
numbers.reverse()
for num in numbers:
    print(num)
.................................................
names = ['Rudy','Lisa','Rose','Jisa']
for name in names:
    print(name+ '  Black Pink')
.................................................
for i in range(3):
    print('kikagaku')
.................................................
for i in range(5):
    double.append(i*2)#append = 追加したいとき使う
print(double)

double = [i*2 for i in range(5)]
print(double)
.................................................

