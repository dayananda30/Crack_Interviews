def contains(hayStack,needle):
    '''

    :param hayStack: List of items
    :param needle: Item needs to be check against hayStack
    :return: break if it exists else raise ValueError
    '''

    for item in hayStack:
        if item == needle:
            print("Exists")
            break

    else:
        #raise ValueError("{} is not exists in haystack {}".format(needle,hayStack))
        print("{} is not exists in haystack {}".format(needle,hayStack))



if __name__ == '__main__':
    contains(['India,SriLanks','Pakistan','Nepal'],'China')
