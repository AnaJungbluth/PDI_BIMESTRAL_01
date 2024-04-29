import cv2 as cv

def reap_bordas(imagem, dado1, dado2):

    imagem_convertida = cv.Canny(imagem, dado1, dado2)
    imagem_convertida = cv.cvtColor(imagem_convertida, cv.COLOR_GRAY2RGB)

    return imagem_convertida  
    