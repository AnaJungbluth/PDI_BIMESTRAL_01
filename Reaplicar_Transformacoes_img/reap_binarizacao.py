import cv2 as cv

def reap_binarizacoes(imagem, dado1):
    _, imagem_convertida = cv.threshold(imagem, dado1, 255, cv.THRESH_BINARY)
 
    return imagem_convertida
    