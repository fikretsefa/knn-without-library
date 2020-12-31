
#region Import
#eğitim ve test csv verilerini dizilere aktarmak için kullanılır.
import csv
#karekök almak için kullanılır.
import numpy as np
#test verisinden random veri çekmek için kullanılır.
import random
#dosyanın var olup olmadığını kontrol etmek için kullanılır.
import os.path
#endregion

#region Variable
#Eğitim verisi
Train_X =[]
#Eğitim label
Train_Y =[]
#Eğitim verisi
Test_X = []
#Test label
Test_Y = []
#Test verilerinden seçilen rastgele veri parçası
Random_Test_Point_X = []
#Test verilerinden seçilen rastgele veri parçası label
Random_Test_Point_Y = []
#endregion

#region Import
def import_train(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile) 
        for i,row in enumerate(reader): 
            if i is not 0:
                line = []
                line.append(float(row[0]))
                line.append(float(row[1]))
                line.append(float(row[2]))
                line.append(float(row[3]))
                line.append(float(row[4]))
                line.append(float(row[5]))
                Train_X.append(line)
                Train_Y.append(row[6])


def import_test(path):
    with open(path) as csvfile:
        reader = csv.reader(csvfile) 
        for i,row in enumerate(reader): 
            if i is not 0:
                line = []
                line.append(float(row[0]))
                line.append(float(row[1]))
                line.append(float(row[2]))
                line.append(float(row[3]))
                line.append(float(row[4]))
                line.append(float(row[5]))
                Test_X.append(line)
                Test_Y.append(row[6])
              

def show_import_data():

    print("---------------Train X----------------")
    for i,row in enumerate(Train_X): 
        print(i,".Data = ", row) 
    
    print("---------------Train Y----------------")
    for i,row in enumerate(Train_Y): 
        print(i,".Data = ", row) 

    print("---------------Test X----------------")
    for i,row in enumerate(Test_X): 
        print(i,".Data = ", row) 
    
    print("---------------Test Y----------------")
    for i,row in enumerate(Test_Y): 
        print(i,".Data = ", row) 

    print("#####################################")

#endregion

#region RandomTest
def random_test_point():
    Test_X_length = len(Test_X)-1;
    Random_Point_Index = random.randint(0,Test_X_length)
    Random_Test_Point_X.append(Test_X[Random_Point_Index])
    Random_Test_Point_Y.append(Test_Y[Random_Point_Index])
    print("Random Data : ", Random_Test_Point_X[0])
    print("Random Data Label : ", Random_Test_Point_Y[0])
#endregion

#region KNN
def most_found(array):
    list_of_words = []
    #array uzunluğu kadar döngü oluşturulur
    for i in range(len(array)):
        #eğer dizinin içerisinde değilse diziye eklenir.
        if array[i] not in list_of_words:
            list_of_words.append(array[i])
    
    most_counted = ''
    n_of_most_counted = None
    #dizinin uzunlugu kadar döngü oluşturulur
    #array dizisi içerisindeki farklı elemanların sayıları kontrol edilir.
    for i in range(len(list_of_words)):
        counted = array.count(list_of_words[i])
        if n_of_most_counted == None:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted < counted:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted == counted:
            most_counted = None
            
    return most_counted

def find_neighbors(point, data, labels, k):
    #test sayısı
    n_of_dimensions = len(point)
    #komşu dizisi
    neighbors = []
    #komşu dizisi etiketleri
    neighbor_labels = []    
    #0'dan başlayarak k kadar arama yapılır
    for i in range(0, k):        
        #En yakın komşu ID
        nearest_neighbor_id = None
        #en kısa uzaklık
        smallest_distance = None        
        print("------------------ k index : %d ------------------" %(i+1))
        #0'dan başlayarak data uzunluğu kadar arama yapılır
        for i in range(0, len(data)):
            #öklid uzaklığı tanımlanır
            eucledian_dist = 0
            #0'dan başlayarak test sayısı uzunluğu kadar arama yapılır
            for d in range(0, n_of_dimensions):
                #point ile data noktaları birbirinden çıkarılır multlak değeri alınır
                dist = abs(point[d] - data[i][d])
                #öklid uzaklığına eklendi
                eucledian_dist += dist
                #to:do delete                
                # print(point[d] , "-" , data[i][d] , "= " , dist)
            #öklid uzaklığı karekökü alınır.
            eucledian_dist = np.sqrt(eucledian_dist)

            #to:do delete
            print(i,".eucledian_dist =" , eucledian_dist)
            
            #en kısa uzaklık diğer uzaklığıa bakarak en kısa uzaklık belirlenir ve ID atanır
            if smallest_distance == None:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i
            elif smallest_distance > eucledian_dist:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i
        
        #to:do delete
        print("Info, Find in k:",nearest_neighbor_id,".",labels[nearest_neighbor_id])
        
        #komşu dizisine eğitim datası eklenir.
        neighbors.append(data[nearest_neighbor_id])
        #komşu etiket dizisine eğitim datası etiketi eklenir.
        neighbor_labels.append(labels[nearest_neighbor_id])        
        #aranan dizi eğitim dizisinden kaldırıldı
        data.remove(data[nearest_neighbor_id])
        #aranan dizi etiketi eğitim dizisinden kaldırıldı
        labels.remove(labels[nearest_neighbor_id])

    return neighbor_labels

def k_nearest_neighbor(point, data, labels, k):
    while True:
        neighbor_labels = find_neighbors(point, data, labels, k)
        #to:do delete
        print("==================================================")
        print("Info, All neighbor prediction", neighbor_labels)
        label = most_found(neighbor_labels)        
        if label != None:
            break
        k += 1
        if k >= len(data):
            break
    return label
#endregion

#region IsTrueResult
def isTrueResult(result):
    if Random_Test_Point_Y[0] == result:
        print("Info, Prediction is true : " , result)
    else:
        print("Warning, Prediction is false. ", "Testing Label :" , Random_Test_Point_Y[0], "Prediction:" , result)
#endregion

#region Main
train_path = input("Set Train Path: ")
if os.path.exists(train_path):
    print("Info, successfully added train: ",train_path)
else:
    print("Warning, No such file or directory. Setting defaut path: train.csv ")
    train_path = "train.csv"

test_path = input("Set Test Path: ")
if os.path.exists(test_path):
   print("Info, successfully added test : ",test_path)
else:
    print("Warning, No such file or directory. Setting defaut path: test.csv ")
    test_path = "train.csv"

try:
    k = int(input("K: "))
    if k <= 0:
        print("Warning, k must be min 1. Setting defaut k variable: 1 ")
        k=1
except:
    print("Warning, Setting defaut k variable: 1 ")
    k=1

import_train(train_path)
import_test(test_path)

#if you want print data remove comment line
#show_import_data()

random_test_point()
result  = k_nearest_neighbor(Random_Test_Point_X[0], Train_X, Train_Y, k)
isTrueResult(result)
#endregion


