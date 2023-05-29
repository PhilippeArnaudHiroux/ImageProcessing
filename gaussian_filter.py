import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Frequency Domain filters")
    #read image
    img = cv2.imread('foto_2.bmp',cv2.IMREAD_GRAYSCALE) # <<< insert image path here
    #convert to float32 for DTF function
    img_f = np.float32(img)

    #discrete fourier transform
    dft = cv2.dft(img_f, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    #do some calculations on shape
    rows, cols = img.shape
    #print("#rows= " + str(rows))
    #print("#columns= " + str(cols))
    center_row, center_col = int(rows / 2), int(cols / 2)  # center
    #print("#center rows= " + str(center_row))
    #print("#center columns= " + str(center_col))

    # create a mask first, center square is 0, remaining all ones
    mask = np.ones((rows, cols, 2), np.uint8)
    mask_width = 50
    mask[center_row - mask_width:center_row + mask_width, center_col - mask_width:center_col + mask_width] = 0

    #Apply Mask
    fshift = dft_shift * mask
    masked_magnitude_spectrum = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

    #inverse transform
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    #Plot the images
    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.subplot(223), plt.imshow(masked_magnitude_spectrum, cmap='gray')
    plt.title('DFT masked'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img_back, cmap='gray')
    plt.title('Result'), plt.xticks([]), plt.yticks([])

    plt.show()

    # Destroys all the windows created
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


