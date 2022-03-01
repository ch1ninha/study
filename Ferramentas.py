def gen_prime(n):
    """Sieve of Eratosthenes. geeksforgeeks.org"""
    # criamos uma lista com o tamanho de N posicoes e valor True em cada
    list_prime = [True for _ range(n+1)]
    # números primos são maiores que 1. 
    p = 2

    
    while (p * p <= n):
        #

def check_prime(n):
    """Checa se o número é primo"""
    check = True
    if n > 1:
        for num in range(2,n):
            if n % num == 0:
                check = False
                break
        return check
    else:
        return False
