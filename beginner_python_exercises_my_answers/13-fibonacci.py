"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of
the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

user_imp = int(input('Informe quantos elementos quer em sua sequencia Fibonacci: '))
fib_list = []

def gerar_fibonacci(numero):
    if user_imp == 0:
        return fib_list
    elif user_imp == 1:
        fib_list.append(1)
        return fib_list
    else:
        fib_list.append(1)
        while len(fib_list) < numero:
            if len(fib_list) <= 1:
                fib_list.append(fib_list[-1])
            else:
                c = fib_list[-1] + fib_list[-2]
                fib_list.append(c)
    return fib_list

print(gerar_fibonacci(user_imp))

