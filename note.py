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
print(total6)#�l�����Z�q

total7 = 10+20-10/5*100**0�@�D�揇��

print(1/0) 0 Division Error
...........................................................
�ϐ��̎g����
price = 100
print(price)

price1 = price +10
print (price1)

price_b = 100
price_a = price_b
print(price_a)
.............................................................
������^
name = 'Wutt Yi Htun'
print(name)

text  = 'Hello "World"'
text1 = "Hello My World 'Wutt Yi'"
print(text + "\n" + text1)

text2 = ''
text2 += 'Hello'
text2 += 'World'
print(text2)�@����������ł���

sample = 10
print (str(10))#���l�𕶎���ɕϊ����邱�Ƃ��ł��܂��B

sample1 = 14.5
print(int(14.5))#Double�^�𐮐����ɕϊ����邱�Ƃł��܂�

sample2 = 1.6
sample3 = sample2
print(int(sample3))

name = 'taro'
print(name.title())
print(name.upper())#Method��t���邱�Ƃł��낢��Ȍ`��ϊ��ł���
............................................................
name = 'taro'
print(name.title())

name1 = 'Wutt yi htun'
print(name1.upper())

name2 = 'Wutt Yi HHtun'
print(name2.replace('HHtun','Htun'))

#Indexing 
text = '�����͂����V�C�ł���'
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
print(foods.append('Cake'))#�ǉ�����
print(foods.pop(0))#�폜����


#���X�g�u�v�ŃJ���}����؂Ŋi�[�̃f�[�^������
#���X�g���ɂ����X�g������
foods = ['Coffee','Bread','Sandwich','Candy']
print (foods[0])
print (foods[::2])

#�ǉ�����(append)�A�폜(pop)�A�f�[�^��ς���
foods.append('Butter')
print (foods)

foods.pop()
print(foods)

del foods[0]
print(foods)

#�g�p�p�x�������֐�(len,max,min,sum,sorted)
.................................................

#�~���[�^�u���i�ύX�\�j
numbers = [1,2,3,4,5]
numbers[0] = 100 #0��100�����ς��܂�
print(numbers)#������������ĂȂ�

numbers1 = [6,3,5,4,7,2,1,9]
numbers1.sort()
print(numbers1)#�����ɕ��בւ�
..................................................
Tuple�̓C�~���[�^�u���ŕύX�ł��Ȃ��ł�
���X�g�Ǝ����Ă��܂��A���X�g�u�v���i�j�Ƃ��ĕς�邾���ł�
�f�[�^�̒ǉ��A�폜���K�v�Ȃ��A�������f�[�^�ł��B
append,pop�Ȃǂ��ł��Ȃ��ł�

my_tuple = ('hello',10,True,False,None)
print(my_tuple[0])

empty_tuple = ()
print(empty_tuple)

one_tuple2 = (10)
print(one_tuple2)

#���ʂ�t���Ȃ��Ă��̂܂܎g����A���R�ł�
#�A���p�b�N���
tuple1 = 'Cake',10,True,False
print(tuple1)

a,b = 1,2
print(a,b)
............................................................
#����
report = {'match':80,'science':100}#'�L�[�ƂȂ閼�O':'�l'
print(report)

print(report['match'])
print(report['science'])

#1��int�^�̃I�u�W�F�N�g
#Hallo��str�^�̃I�u�W�F�N�g
.............................................................
report = {'match':80,'science':100}
print(report)

print(report['match'])
print(report['science'])

report['Japanese'] = 70
print(report)���ǉ�����

del report['science']
print(report)���폜����

report['English'] = 80
print(report)���ǉ�����
.............................................................
���W���͎����Ǝ����Ă�B�������L�[�����ɂ�������
��set�֐��̈����Ƀ��X�g��^�v���A�����Ȃǂ�n���ƏW�����ɕϊ�����܂�

numbers = {1,2,3,4,5}
print(numbers)

empty_set = set()
print(empty_set)

numbers = {1,2,1,5,3,1,2,4,4}
print(numbers)�����ۂɂ���ԍ���������肾��(�d�������Ƃ߂Ȃ��j

numbers.add(6)
print(numbers)���ǉ�����

numbers.remove(5)
print(numbers)���폜����

.......................................................................
mutable = {'list','dict','set'}
imutable = {'str','numbeer','tuple'}
seq = {'list','tuple','str'}

print(mutable)
print(imutable)
print(seq)

print(mutable & seq)
print(mutable.intersection(seq))���ϏW���[���ʓ_�����o��

print(mutable | seq)
print(mutable.union(seq))���a�W���[���ʓ_���܂ߑS�������o��

print(imutable - seq)
print(imutable.difference(seq))

print(mutable ^ seq)
print(mutable.symmetric_difference(seq))