import cv2 as cv

def cores(opcao, imagem):
    if opcao == 1:
        imagem_convertida = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY)
        
        return imagem_convertida
    elif opcao == 2:
        imagem_convertida = cv.cvtColor(imagem, cv.COLOR_RGB2HSV)

        return imagem_convertida
    elif opcao == 3:
        imagem_convertida = cv.cvtColor(imagem, cv.COLOR_RGB2HLS)

        return imagem_convertida
