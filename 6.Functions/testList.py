
def fun_0(n):
    n[0] +=1
    print("Function 0 Frame")
    print(f"inside fun0\t-> {n}")
    print("-"*40)
    return fun_1(n)

def fun_1(x):
    x[0] += 1
    print("Function 1 Frame")
    print(f"inside fun1\t-> {x}")
    print("-"*40)
    return x

print("Global Frame")
test_list = [1]
print(f"start_num\t-> {test_list}")
print("-"*40)

final_list = fun_0(test_list)

print("After finish all functions and check the Global Frame")

print(f"Final_list:-> {final_list}")
print(f"test_list:-> {test_list}")