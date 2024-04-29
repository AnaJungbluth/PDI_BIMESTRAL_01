import cv2 as cv
import numpy as np

def reap_morfologias(opcao, imagem, dado1):
    kernel = np.ones((dado1, dado1), np.uint8)

    if opcao == 1:
        imagem_convertida = cv.erode(imagem, kernel, iterations=1)

        return imagem_convertida
    
    elif opcao == 2:
        imagem_convertida = cv.dilate(imagem, kernel, iterations=1)

        return imagem_convertida
    