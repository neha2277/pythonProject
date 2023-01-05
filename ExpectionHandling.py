#pass and assert
#in python we user except instead of catch block
#finally will run everytime irrespective of try except blocks

ItemsinCart = 0
if ItemsinCart !=2 :
    pass

assert(ItemsinCart == 0)

try:
    with open('chvhdcv.txt','r')as reader:
        reader.readline()

except:
    print('Oopss!!! I missed this block')

try:
    with open('test.txt','r')as reader:
        reader.readline()

except Exception as e:
    print(e)
finally:
    print("this code is executed")