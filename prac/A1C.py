def fib_iterative(n):
    sc = 0
    series = [0,1]

    if n<=0:
        return "Please Enter valid input.", sc
    elif n==1:
        sc += 1
        return [0], sc
    elif n==2:
        sc += 1
        return [0, 1], sc
    
    first, sec = 0, 1
    for i in range(2, n):
        nth = first + sec
        series.append(nth)
        first = sec
        sec = nth
        sc += 3
    return series, sc

def fib_recursive(n, series=None, sc=0):
    if n<=0:
        return "Please Enter the valid input.", sc
    elif n==1:
        sc += 1
        return [0], sc
    elif n==2:
        sc += 1
        return [0, 1], sc
    
    if series == None:
        series = [0, 1]
    if len(series) == n:
        return series, sc
    
    series.append(series[-1] + series[-2])
    sc += 2
    return fib_recursive(n, series, sc)
    
def main():
    while(True):
        print("1. Fibonacci series using iterative approach.")
        print("2. Fibonacci series using recursive approach.")
        print("3. Exit")
        ch = int(input("Choose an option : "))
        if ch==1:
            in1 = int(input("Enter the number of elements : "))
            series, sc = fib_iterative(in1)
            print(f"Fibonacci series : {series}")
            print(f"Step Count : {sc}")

        elif ch==2:
            in2 = int(input("Enter the number of elements : "))
            series, sc = fib_recursive(in2)
            print(f"Fibonacci series : {series}")
            print(f"Step Count : {sc}")
        else:
            break

        

if __name__=="__main__":
    main()