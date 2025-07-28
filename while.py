count = 0

while count < 5:
    count += 1
    print(count)
..............................................................
Break Satatement
count = 0

while count < 5:
    count += 1

    if count == 3:
        break 
    print(count)
    Result = 1,2
.............................................................
Continue Statement
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue
    print(count)
Result = 1,2,4,5
.............................................................
Used the Logical Operatior
i = 0
j = 20
while i < 10 and j > 10:
    print(f"i:{i},j:{j}")
    i += 1
    j -= 1

Result i:0 to 9
       j:19 to 11
.............................................................

i = 0
j = 20
while i < 10 and j > 10:
    print(f"i:{i},j:{j}")
    i += 1
    j -= 1
.............................................................
Different of While and For

life = 10
while life > 0:
    print("Continure Play Game")
    life = life - 1
**************************************
    
friends = ["Alice","Bob","Charlie"]
for friend in friends:
    print("Hello,"+friend+"!")
.............................................................

