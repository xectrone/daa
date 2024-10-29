# DAA A1 Write a program to calculate Fibonacci numbers and find its step count.

def fib_iterative(n):
    step_count = 0 
    series = [0, 1]
    if n <= 0:
        return "Please enter a positive integer.", step_count
    elif n == 1:
        step_count += 1  
        return [0], step_count
    elif n == 2:
        step_count += 1 
        return [0, 1], step_count

    first, sec = 0, 1
    for i in range(2, n):
        nth = first + sec
        series.append(nth)
        first = sec
        sec = nth
        step_count += 3
    return series, step_count

def fib_recursive_series(n, series=None, step_count=0):
    if n <= 0:
        return "Please enter a positive integer.", step_count
    elif n == 1:
        step_count += 1 
        return [0], step_count
    elif n == 2:
        step_count += 1  
        return [0, 1], step_count

    if series is None:
        series = [0, 1]
    
    if len(series) == n:
        return series, step_count
    
    series.append(series[-1] + series[-2])
    step_count += 2 
    return fib_recursive_series(n, series, step_count)


def main():
    while True:
        print("\n Menu:")
        print("1. Fibonacci Series using Iterative approach")
        print("2. Fibonacci Series using Recursive approach")
        print("3. Exit")
        
        choice = int(input("Choose an option : "))
        
        if choice == 1 or choice == 2:
            n = int(input("Enter the number of terms (n): "))
            
            if choice == 1:
                series, steps = fib_iterative(n)
                print(f"Fibonacci Series:", series)
                print(f"Step Count: {steps}")
                
            elif choice == 2:
                series, steps = fib_recursive_series(n)
                print(f"Fibonacci Series:", series)
                print(f"Step Count: {steps}")
                
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()