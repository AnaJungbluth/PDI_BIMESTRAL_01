import cv2 as cv
 
def reap_filtros(opcao, imagem, dado1, dado2 = None):

    if opcao == 1:
        imagem_convertida = cv.blur(imagem, (dado1, dado2))

        return imagem_convertida
    elif opcao == 2:
        imagem_convertida = cv.bilateralFilter(imagem, d=9, sigmaColor=dado1, sigmaSpace=75)

        return imagem_convertida
    elif opcao == 3:
        imagem_convertida = cv.medianBlur(imagem, dado1)
        
        return imagem_convertida


