from numpy import random
import numpy as np
import math

N = 10000 #number of people
P = 0.1 #probability
N_H = 100 #number of hotels
N_D = 100 #number of days
SIMULATIONS_COUNT = 1 #number of simulations

#permutation function
def permutation(value):
    return math.factorial(value) / (math.factorial(2) * (math.factorial(value - 2)))

#function to create pair 'pair - day'
def calcPairTwoPeople_Day(arr):
    res = 0
    for i in range(len(arr)):
        if(i != 0):
            res += arr[i]*permutation(i+1)
    return res

def addToSuspected(a,b,suspectedPeople):
    suspectedPeople.add(a)
    suspectedPeople.add(b)

#function to join pairs
def createAllPairs(pairs: dict, hotelGuests, person, suspectedPeople):
    for i in hotelGuests:
        if((person, i) in pairs):
            pairs[(person, i)] += 1
            if(pairs[(person, i)] == 2):
                addToSuspected(i,person,suspectedPeople)
        elif((i, person) in pairs):
            pairs[(i, person)] += 1
            if (pairs[(i,person)] == 2):
                addToSuspected(person, i, suspectedPeople)
        else:
            pairs.update({(person, i): 1})

#function that creates pair's
def createPairs():
    pairs = dict()
    suspectedPeople = set()
    for j in range(N_D):
        hotelsDict = dict()
        for k in range(N):
            if random.rand() < P:
                hotel = random.randint(1, N_H)
                if (hotel in hotelsDict.keys()):
                    createAllPairs(pairs, hotelsDict[hotel], k, suspectedPeople)
                    hotelsDict[hotel].append(k)
                else:
                    hotelsDict.update({hotel: [k]})

    maxNoOfMeetings = max(list(pairs.values()))
    bins = np.arange(1, maxNoOfMeetings + 2, 1)
    histogram, binEdges = np.histogram(list(pairs.values()), bins = bins)
    return sum(histogram[1:]), histogram.tolist(), len(suspectedPeople), calcPairTwoPeople_Day(histogram), maxNoOfMeetings

def getHistogramAVG(localMax, histogram):
    avgList = list()
    for i in range(localMax):
        temp = list()
        for j in range(len(histogram)):
            if(len(histogram[j]) < localMax):
                histogram[j].append(0)
            temp.append(histogram[j][i])
        avgList.append(np.average(temp))
    return avgList

def normalize(localMax, histogram, numberOfSuspectedPeople, PairTwoPeople_Day, pairs):
    normalizedHistogram = getHistogramAVG(localMax, histogram)
    return np.average(PairTwoPeople_Day),np.average(pairs),normalizedHistogram,np.average(numberOfSuspectedPeople)

def main():
    pairs = list()
    PairTwoPeople_Day = list()
    histogram = list()
    numberOfSuspectedPeople = list()
    localMax = 0

    for i in range(SIMULATIONS_COUNT):
        print(" ------- SYMULACJA " + str(i+1) + "/" + str(SIMULATIONS_COUNT) + " -------")
        tempPairs = createPairs()
        pairs.append(tempPairs[0])
        histogram.append(tempPairs[1])
        numberOfSuspectedPeople.append(tempPairs[2])
        PairTwoPeople_Day.append(tempPairs[3])
        if(localMax < tempPairs[4]):
            localMax = tempPairs[4]
        normalizedRes = normalize(localMax,histogram,numberOfSuspectedPeople,PairTwoPeople_Day,pairs)
        print("Liczba podejrzanych par 'osób i dni': " + str(normalizedRes[0]) + "\n" +
              "Liczba podejrzanych par: " + str(normalizedRes[1]) + "\n" +
              "Histogram: " + str(normalizedRes[2]) + "\n" +
              "Liczba podejrzanych osób: " + str(normalizedRes[3]))

if __name__ == "__main__":
    main()