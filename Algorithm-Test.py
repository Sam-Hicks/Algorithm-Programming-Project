import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

"""Insertion Sort Algorithm"""
def INSERTION_SORT(A,n):
    for j in range(1,n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

"""Heapsort Algorithm"""
def MAX_HEAPIFY(A,i,n):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MAX_HEAPIFY(A,largest,n)

def BUILD_MAX_HEAP(A,n):
    for i in range(n//2-1,-1,-1):
        MAX_HEAPIFY(A,i,n)  

def HEAPSORT(A,n):
    BUILD_MAX_HEAP(A,n)

    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        MAX_HEAPIFY(A,0,i)

"""Randomized Select Algorithm"""
def RANDOMIZED_SELECT(A,p,r,i):
    if p == r:
        return A[p]
    
    q = RANDOMIZED_PARTITION(A,p,r) #q is index of pivot
    k = q-p+1

    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A,p,q-1,i)
    else:
        return RANDOMIZED_SELECT(A,q+1,r,i-k)
    
def PARTITION(A,p,r):
    x = A[r] #Pivot
    i = p-1
    
    for j in range(p,r):
        if A[j] <= x:
            
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def RANDOMIZED_PARTITION(A,p,r):
    i = random.randrange(p,r)
    A[r], A[i-1] = A[i-1], A[r]
    return PARTITION(A,p,r)


"""Start of Algorithm Testing"""
def ALG1(A,n,i): #Insertion sort algorithm
    INSERTION_SORT(A,n)
    return A[i-1]

def ALG2(A,n,i): #Heapsort algorithm
    HEAPSORT(A,n)
    return A[i-1]

def ALG3(A,n,i): #Randomized select algorithm
    RANDOMIZED_SELECT(A,0,n-1,i)
    return A[i-1]


"""Main Function"""
def main(): 
    A = [[],[],[],[],[]] #Declare an empty array with 5 indices for testing
    B = [] #Temp array for testing parts of array A
    x_vals = [1000,2000,3000,4000,5000,6000,7000,8000,9000,
    10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000] #Declare an array for the x values for graphing the run times
    m = 5 #Declare a value for how many runs are required for each input size

    #Fill the indices of array A with random numbers
    for j in range(0,5):
        for k in range(20000):
            rand_num = random.randint(0,32767)
            A[j].append(rand_num)


    #Measurements for ALG1
    print("ALG1 TESTING\n")
    n = 1000 #Initial input size
    ALG1_y = [] #Declare an empty array for ALG1's y values for graphing the run time
    start1 = timer() #Start a timer for calculating the run time of the whole algorithm testing

    for n in range(n,20001,1000): #Loop through 20,000 random numbers, starting with 1,000 and increamenting by 1,000 every call
        i=0
        i = (2*n)//3 #ith order statistic to find
        avg=0
        print("\nn:",n)

        for j in range(0,m): #Loop through m times, changing the array in which is tested each time
            print("run:",j+1)
            t1 = t2 = 0 #Timer variables

            s = slice(0,n) #Get a slice of n numbers
            B = A[j][s] #Slice array A[j] with slice s and append it to array B

            t1 = timer() #Start a timer for calculating the run time
            print("i:",ALG1(B,n,i)) #Run ALG1 and print the ith order statistic for the current run
            t2 = timer() #Stop the timer for calculating the run time
            
            tavg = t2-t1 #Subtract the timer start and end times to get the run time
            print("t1: {:.2f} | t2: {:.2f} | avg: {:.2f}\n".format(t1,t2,tavg))

        # avg = "{:.6f}".format(tavg/m)
        avg = tavg/m #Calculate the total average of the current input value n
        ALG1_y.append(avg) #Append the average value to the y value array

    end1 = timer() #Stop the timer for calculating the run time of the whole algorithm testing
    print("ALG1 finished in {} seconds".format(end1))

    print("\n=======================================================\n")

    # #Measurements for ALG2
    print("ALG2 TESTING")
    n = 1000 #Initial input size
    ALG2_y = [] #Declare an empty array for ALG2's y values for graphing the run time
    start2 = timer() #Start a timer for calculating the run time of the whole algorithm testing

    for n in range(n,20001,1000): #Loop through 20,000 random numbers, starting with 1,000 and increamenting by 1,000 every call
        i=0
        i = (2*n)//3 #ith order statistic to find
        avg=0
        print("\nn:",n)

        for j in range(0,m): #Loop through m times, changing the array in which is tested each time
            print("run:",j+1)
            t1 = t2 = 0 #Timer variables

            s = slice(0,n) #Get a slice of n numbers
            B = A[j][s] #Slice array A[j] with slice s and append it to array B

            t1 = timer() #Start a timer for calculating the run time
            print("i:",ALG2(B,n,i)) #Run ALG2 and print the ith order statistic for the current run
            t2 = timer() #Stop the timer for calculating the run time
            
            tavg = t2-t1 #Subtract the timer start and end times to get the run time
            print("t1: {:.2f} | t2: {:.2f} | avg: {:.2f}\n".format(t1,t2,tavg))

        # avg = "{:.6f}".format(tavg/m)
        avg = tavg/m #Calculate the total average of the current input value n
        ALG2_y.append(avg) #Append the average value to the y value array

    end2 = timer() #Stop the timer for calculating the run time of the whole algorithm testing
    print("\nALG2 finished in {} seconds".format(end2-end1))

    print("\n=======================================================\n")

    # Measurements for ALG3
    print("ALG3 TESTING")
    n = 1000 #Initial input size
    ALG3_y = [] #Declare an empty array for ALG3's y values for graphing the run time
    start3 = timer() #Start a timer for calculating the run time of the whole algorithm testing

    for n in range(n,20001,1000): #Loop through 20,000 random numbers, starting with 1,000 and increamenting by 1,000 every call
        i=0
        i = (2*n)//3 #ith order statistic to find
        avg=0
        print("\nn:",n)

        for j in range(0,m): #Loop through m times, changing the array in which is tested each time
            print("run:",j+1)
            t1 = t2 = 0 #Timer variables

            s = slice(0,n) #Get a slice of n numbers
            B = A[j][s] #Slice array A[j] with slice s and append it to array B

            t1 = timer() #Start a timer for calculating the run time
            print("i:",ALG3(B,n,i)) #Run ALG3 and print the ith order statistic for the current run
            t2 = timer() #Stop the timer for calculating the run time
            
            tavg = t2-t1 #Subtract the timer start and end times to get the run time
            print("t1: {} | t2: {} | avg: {}\n".format(t1,t2,tavg))

        # avg = "{:.6f}".format(tavg/m)
        avg = tavg/m #Calculate the total average of the current input value n
        ALG3_y.append(avg) #Append the average value to the y value array

    end3 = timer() #Stop the timer for calculating the run time of the whole algorithm testing
    print("ALG3 finished in {} seconds".format(end3-end2))

    print("\n=======================================================")
    print("ALG1 finished in: {} seconds \nALG2 finished in: {} seconds \nALG3 finished in: {} seconds".format(end1,end2-end1,end3-end2))


    """Plot the algorithm's RT's"""
    plt.plot(x_vals,ALG1_y,"ro",label="ALG1",ls='-',ms=5)
    plt.plot(x_vals,ALG2_y,"bo",label="ALG2",ls='-',ms=5)
    plt.plot(x_vals,ALG3_y,"go",label="ALG3",ls='-',ms=5)
    plt.legend(loc="upper left")
    plt.xlabel("n")
    plt.ylabel("RT(Milliseconds)")
    plt.xlim([0,21000])
    plt.xticks([0,2000,4000,6000,8000,10000,12000,14000,16000,18000,20000])
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
