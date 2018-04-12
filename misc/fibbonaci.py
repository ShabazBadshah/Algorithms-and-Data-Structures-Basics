def print_fibbonaci(num_of_elements):
    
    fib = [1] 

    if (num_of_elements <= 2):
        return 1

    for i in range(1, num_of_elements):
        fib.append(fib[i - 1] + fib[i - 2])
        
    return fib[num_of_elements - 1]

print(print_fibbonaci(5))
print(print_fibbonaci(10))
print(print_fibbonaci(1000))
print(print_fibbonaci(10000))
