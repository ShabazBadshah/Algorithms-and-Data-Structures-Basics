def print_fibbonaci(num_of_elements):
    fib = [1, 1] 

    if (num_of_elements <= 2):
        return 1

    for i in range(2, num_of_elements + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        print (fib[i])    


print_fibbonaci(5) #8
