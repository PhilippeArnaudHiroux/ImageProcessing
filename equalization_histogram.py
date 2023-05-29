#Importeer libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

afbeelding = cv2.imread("foto_2.bmp")                             #Lees de afbeelding in
afbeelding_rgb = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2RGB)    #Converteer naar rood, groen en blauw

rood, groen, blauw = cv2.split(afbeelding_rgb) #Splits de afbeelding

egaliseer_rood = cv2.equalizeHist(rood)     #Egaliseer de kleur rood
egaliseer_groen = cv2.equalizeHist(groen)   #Egaliseer de kleur groen
egaliseer_blauw = cv2.equalizeHist(blauw)   #Egaliseer de kleur blauw

egaliseer = cv2.merge((egaliseer_rood, egaliseer_groen, egaliseer_blauw)) #Foto terug samenstellen

histogram_blauw_1 = cv2.calcHist([afbeelding_rgb],[0],None,[256],[0,256])   #Bereken de histogram van de blauwe kleur van de norale afbeelding
histogram_groen_1 = cv2.calcHist([afbeelding_rgb],[1],None,[256],[0,256])   #Bereken de histogram van de groen kleur van de norale afbeelding
histogram_rood_1 = cv2.calcHist([afbeelding_rgb],[2],None,[256],[0,256])    #Bereken de histogram van de rood kleur van de norale afbeelding

histogram_blauw_2 = cv2.calcHist([egaliseer],[0],None,[256],[0,256])    #Bereken de histogram van de blauwe kleur van de geëgalisseerde afbeelding
histogram_groen_2 = cv2.calcHist([egaliseer],[1],None,[256],[0,256])    #Bereken de histogram van de groen kleur van de geëgalisseerde afbeelding
histogram_rood_2 = cv2.calcHist([egaliseer],[2],None,[256],[0,256])     #Bereken de histogram van de rood kleur van de geëgalisseerde afbeelding

plt.subplot(221), plt.imshow(afbeelding_rgb)                                                            #Toon de normale afbeelding
plt.subplot(222), plt.plot(histogram_blauw_1), plt.plot(histogram_groen_1),plt.plot(histogram_rood_1)   #Plot de kleuren histogrammen samen van de normale afbeelding
plt.subplot(223), plt.imshow(egaliseer)                                                                 #Toon de geëgalisserde afbeelding
plt.subplot(224), plt.plot(histogram_blauw_2), plt.plot(histogram_groen_2),plt.plot(histogram_rood_2)   #Plot de kleuren histogram samen van de geëgalisserde afbeelding
plt.xlim([0,256])
plt.show()