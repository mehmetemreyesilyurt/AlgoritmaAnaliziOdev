import random
import datetime
import time

#Rastgele oluşturulmuş 10000 sayılık dizi
dizi = list()
for i in range(10000):
    dizi.append(random.randint(1,100000))

#Quick Sort Parçalama Fonksiyonu
def partition(arr,low,high):
    i = ( low-1 )        
    pivot = arr[high]     
 
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

#Quick Sort Algoritması
def quickSort(arr,low,high):#Recursive olarak çalışır. Dizi önce parçalanır, sonra parçalar da kendi içlerinde parçalanır.
    if low < high:      
        pi = partition(arr,low,high) #Parçalama Fonksiyonu
        quickSort(arr, low, pi-1) #Pivotun aşağısındaki sayılar
        quickSort(arr, pi+1, high) #Pivotun yukarısındaki sayılar

#En kötü çalışma zamanı O(N2)
#Ortalama çalışma zamanı O(NlogN)
#En iyi çalışma zamanı O(NlogN)

a = datetime.datetime.now()
quickSort(dizi,0,9999)
b = datetime.datetime.now()
print("QuickSort algoritmasının çalışma süresi : {} ms".format((b-a).microseconds))

dizi = list()
for i in range(10000):
    dizi.append(random.randint(1,100000))

#Brute Force Yaklaşımına sahip Selection Sort Algoritması
def selectionSort(array, size):
   
    for step in range(size): #n lik zaman karmaşıklığı
        min_idx = step
        for i in range(step + 1, size): #n lik zaman karmaşıklığı
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step]) 
        #Sonuç olarak en kötü zaman karmaşıklığı O(N2) ye eşittir.

#En kötü çalışma zamanı O(N2)
#Ortalama çalışma zamanı O(N2)
#En iyi çalışma zamanı O(N2)

#Sonuç olarak QuickSort algoritması düşük olasılıkla O(N2) karmaşıklığına sahip olabilse de büyük dizileri sıralamada SelectionSort algoritmasına göre çok daha hızlı çalışmaktadır.

a = datetime.datetime.now()
selectionSort(dizi,10000)
b = datetime.datetime.now()
print("SelectionSort algoritmasının çalışma süresi : {} ms".format((b-a).microseconds))