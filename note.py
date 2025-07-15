total = (1+2)
print (total)

total1 = 3-2
print (total1)

total2 = 5*3
print(total2)

total3 = 5**3
print(total3) #Square Root

total4 = 3/2
print(total4)

total5 = 3//2
print(total5)

total6 = 10%3
print(total6)#四則演算子

total7 = 10+20-10/5*100**0　優先順位

print(1/0) 0 Division Error
...........................................................
変数の使い方
price = 100
print(price)

price1 = price +10
print (price1)

price_b = 100
price_a = price_b
print(price_a)
.............................................................
文字列型
name = 'Wutt Yi Htun'
print(name)

text  = 'Hello "World"'
text1 = "Hello My World 'Wutt Yi'"
print(text + "\n" + text1)

text2 = ''
text2 += 'Hello'
text2 += 'World'
print(text2)　文字を結語できる

sample = 10
print (str(10))#数値を文字列に変換することもできます。

sample1 = 14.5
print(int(14.5))#Double型を整数方に変換することできます

sample2 = 1.6
sample3 = sample2
print(int(sample3))

name = 'taro'
print(name.title())
print(name.upper())#Methodを付けることでいろいろな形を変換できる
............................................................
name = 'taro'
print(name.title())

name1 = 'Wutt yi htun'
print(name1.upper())

name2 = 'Wutt Yi HHtun'
print(name2.replace('HHtun','Htun'))

#Indexing 
text = '今日はいい天気ですね'
print(text[0])
print(text[-2])

print(text[1:4])
print(text[2:5])#[step:end]
print(text[::2])#[step:end:step]
...................................................................
my_list = ['hello',10,True,False,None]
empty_list = []
str_list = list('hello')
print(str_list)

foods = ['Coffee','Tea','Pasta']
print(foods)
print(foods[0])
print(foods.append('Cake'))#追加する
print(foods.pop(0))#削除する


#リスト「」でカンマを区切で格納のデータを書く
#リスト中にもリストを入れる
foods = ['Coffee','Bread','Sandwich','Candy']
print (foods[0])
print (foods[::2])

#追加する(append)、削除(pop)、データを変える
foods.append('Butter')
print (foods)

foods.pop()
print(foods)

del foods[0]
print(foods)

#使用頻度が高い関数(len,max,min,sum,sorted)
.................................................

#ミュータブル（変更可能）
numbers = [1,2,3,4,5]
numbers[0] = 100 #0に100を入れ変わります
print(numbers)#文字列を許してない

numbers1 = [6,3,5,4,7,2,1,9]
numbers1.sort()
print(numbers1)#昇順に並べ替え
..................................................
Tupleはイミュータブルで変更できないです
リストと似っています、リスト「」を（）として変わるだけです
データの追加、削除が必要ない連続したデータです。
append,popなどができないです

my_tuple = ('hello',10,True,False,None)
print(my_tuple[0])

empty_tuple = ()
print(empty_tuple)

one_tuple2 = (10)
print(one_tuple2)

#括弧を付けなくてそのまま使える、自由です
#アンパック代入
tuple1 = 'Cake',10,True,False
print(tuple1)

a,b = 1,2
print(a,b)
............................................................
#辞書
report = {'match':80,'science':100}#'キーとなる名前':'値'
print(report)

print(report['match'])
print(report['science'])

#1はint型のオブジェクト
#Halloはstr型のオブジェクト
.............................................................
report = {'match':80,'science':100}
print(report)

print(report['match'])
print(report['science'])

report['Japanese'] = 70
print(report)＃追加する

del report['science']
print(report)＃削除する

report['English'] = 80
print(report)＃追加する
.............................................................
＃集合は辞書と似ってる。辞書をキーだけにしたもの
＃set関数の引数にリストやタプル、辞書などを渡すと集合方に変換されます

numbers = {1,2,3,4,5}
print(numbers)

empty_set = set()
print(empty_set)

numbers = {1,2,1,5,3,1,2,4,4}
print(numbers)＃実際にある番号だけを取りだす(重複をもとめない）

numbers.add(6)
print(numbers)＃追加する

numbers.remove(5)
print(numbers)＃削除する

.......................................................................
mutable = {'list','dict','set'}
imutable = {'str','numbeer','tuple'}
seq = {'list','tuple','str'}

print(mutable)
print(imutable)
print(seq)

print(mutable & seq)
print(mutable.intersection(seq))＃積集合ー共通点を取り出す

print(mutable | seq)
print(mutable.union(seq))＃和集合ー共通点を含め全部を取り出す

print(imutable - seq)
print(imutable.difference(seq))

print(mutable ^ seq)
print(mutable.symmetric_difference(seq))