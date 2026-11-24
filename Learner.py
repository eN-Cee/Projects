def fizz_buzz(n):
    result = []

    for n in range(1, n +1):
        if n%5 ==0 and n%3 ==0:
            result.append("FizzBuzz")
        elif n%5 == 0:
            result.append("Buzz")
        elif n%3 ==0:
            result.append("Fizz")
        else:
            result.append(n)
            print(result)
    return result

fizz_buzz(4)