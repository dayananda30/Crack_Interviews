def parent(number):
    def first_child():
        return "I am Number One"

    def second_child():
        return "I am Number Two"

    if number == 1:
        return first_child

    else:
        return second_child


first = parent(1)
print(first)
print(first())
second = parent(2)
print(second)
print(second())
