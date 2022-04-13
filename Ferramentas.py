# def gen_prime(n):
#     """Sieve of Eratosthenes. geeksforgeeks.org"""
#     # criamos uma lista com o tamanho de N posicoes e valor True em cada
#     list_prime = [True for _ range(n+1)]
#     # números primos são maiores que 1. 
#     p = 2

    
#     while (p * p <= n):
#         #

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

    
def gen_sieve_of_era():
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            if i == 2:
                yield i
            continue
        elif i % 3 == 0:
            if i == 3:
                yield i
            continue
        elif i % 5 == 0:
            if i == 5:
                yield i
            continue
        elif i % 7 == 0:
            if i == 7:
                yield i
            continue
        elif i % 11 == 0:
            if i == 11:
                yield i
            continue
        yield i
