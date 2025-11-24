def check(num):
    if num<1:
        print("If part executed")
        print("CODE ENDED")
    else:
        print("else part executed")
        check(num-1) #recursion

check(5)