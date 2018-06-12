def all_even():
    n = 2
    while True:
        yield n
        n += 2


if __name__ == '__main__':
    print all_even().next()
    print all_even().next()
    print all_even().next()
