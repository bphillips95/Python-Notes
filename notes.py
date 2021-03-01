msg = "Hello World"
# print(msg)
# In python variables can be declared without a declaration
# print(type(msg))
# You can convert data types by writing in the data type 
num = 28764
# print(msg + str(num))

def aFunc():
    msg = "This is a function"
    print(msg)

# aFunc()
# unlike JS u can declare a variable inside a function
def compare():
    x,y = 1000,1000
    if (x > y):
        st = "X is greater than Y"
    elif(x == y):
        st = "X is the same as Y"
    else:
        st = "X is less than Y"
    print(st)
    # dont repeat variable name by else statement
    st = "X is greater than Y" if (x>y) else "X isnt greater than y"
    print(st)
# compare()
food = ["pizza","pasta","soup","chips","hot dogs"]
# def loopFunc():
#     for f in food:
#         if (f == "chips"): break
#         print(f)


# loopFunc()
# function to find if arr includes chips return index
def findChips():
    for i,f in enumerate(food):
        if(f == "chips"):
            print(f + " are located at index " + str(i))

findChips()
# break and continue in loops

instead of console logging use print to debug