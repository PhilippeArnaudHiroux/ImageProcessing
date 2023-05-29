import cv2                                              #Import cv2
from matplotlib import pyplot as plt                    #Import matplotlib

img = cv2.imread('foto_2.bmp')                          #Lees de foto in
cv2.imshow("window_name", img)                          #Toon de foto

color = ('b','g','r')                                   #Zet in color b(blauw), g(groen), r(rood)

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])  #Maak de historgram aan calcHist(afbeelding, channels, mask, histSize, ranges)
    plt.plot(histr,color = col)                         #Plot de histogram plot(x, y)
    plt.xlim([0,256])                                   #Plot waardes van de histogram xlim(begin punt, eind punt)
plt.show()                                              #Toon de plot

