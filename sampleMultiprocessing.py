from multiprocessing import Process, Value, Array
import time
import random
##execute a python script to perform multiprocessing and access (share) the variables in real-time
def f(a,n):
    global ak, nk
    num.value = 3.1415927
    k=0
    while True:
        k=k+1
        for i in range(len(a)):
            a[i] = -random.random()*a[i]
        a[0]=k*1.0
        ak=a
        nk=n
        time.sleep(1)


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('d', range(10))

    p = Process(target=f, args=(arr,num))
    p.start()
    #p.join()

    print num.value
    print arr[:]
