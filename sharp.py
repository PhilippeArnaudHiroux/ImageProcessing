#Importeer libraries
import cv2
from matplotlib import pyplot as plt

afbeelding = cv2.imread('foto_2.bmp')                         #Lees de afbeelding in
afbeelding_rgb = cv2.cvtColor(afbeelding, cv2.COLOR_BGR2RGB)  #Vorm de afbeelding van BGR naar RGB

blured_afbeelding = cv2.GaussianBlur(afbeelding_rgb, (9,9), 0)    #Blure de afbeelding
mask_afbeelding = cv2.subtract(afbeelding_rgb, blured_afbeelding) #Maak een mask van de afbeelding
sharp_afbeelding = cv2.add(mask_afbeelding, afbeelding_rgb)       #Voeg de mask en de orginele afbeelding samen

plt.subplot(221), plt.imshow(afbeelding_rgb)     #Voeg image toe aan plot
plt.subplot(222), plt.imshow(blured_afbeelding)  #Voeg bluredImage toe aan plot
plt.subplot(223), plt.imshow(mask_afbeelding)    #Voeg maskImage toe aan plot
plt.subplot(224), plt.imshow(sharp_afbeelding)   #Voeg sharpImage toe aan plot
plt.show()                                       #Show plot