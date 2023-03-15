import random
import datetime
import time

#Rastgele oluşturulmuş 10000 sayılık dizi
dizi = list()
for i in range(10000):
    dizi.append(random.randint(1,100000))

#BinarySearch algoritması için dizi sıralanır.
def partition(arr,low,high):
    i = ( low-1 )        
    pivot = arr[high]     
 
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
def quickSort(arr,low,high):
    if low < high:      
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high) 
quickSort(dizi,0,9999)

#Çalışması için dizinin sıralanmasını isteyen BinarySearch algoritması.
def binarySearch(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:#Zaman karmaşıklığı O(logN)
        mid=(high+low)//2
        if arr[mid]<x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

#En kötü çalışma zamanı O(logN)
#Ortalama çalışma zamanı O(logN)
#En iyi çalışma zamanı O(logN)

a = datetime.datetime.now()
binarySearch(dizi,dizi[9999])#Dizi sıralanmış olduğu için en büyük sayı en sondadır.
b = datetime.datetime.now()
print("BinarySearch algoritmasının çalışma süresi : {} ms".format((b-a).microseconds))

#Tekrardan rastgele dizi oluşturuluyor.
dizi = list()
for i in range(10000):
    dizi.append(random.randint(1,100000))

#Brute Force Yaklaşımına sahip Algoritma
def maximumNumber(array,size):
    maxnumber=array[0]
    for i in range(1,size-1):#N zaman karmaşıklığı
        if(array[i]>maxnumber):
            maxnumber=array[i]
    return maxnumber

#En kötü çalışma zamanı O(N)
#Ortalama çalışma zamanı O(N)
#En iyi çalışma zamanı O(N)

#Sonuç olarak BinarySearch O(logN), LinearSearch ise O(N) zaman karmaşıklığına sahiptir.

a = datetime.datetime.now()
maximumNumber(dizi,10000)
b = datetime.datetime.now()
print("BruteForce yaklaşımlı algoritmanın çalışma süresi : {} ms".format((b-a).microseconds))