def calculator(*numbers):
    add=0
    n=0
    for number in numbers:
        if number != 0:
            add += number
            n += 1
        else:
            break
    avg = add/n
    return (add, round(avg))
