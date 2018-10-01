"""
It uses Map and Reduce algorithm to allocate the wotk between the cpu cores and aggragate the results at the end give back the result
"""


from multiprocessing import Pool



def f(n):
    return n*n



if __name__ == '__main__':
    p = Pool(processes=5)
    result = p.map(f,[1,2,3,4,5])

    for n in result:
        print(n)
