import cv2 as cv
from tkinter import simpledialog, messagebox


def bordas(opcao, imagem):

    if opcao == 1:
        imagem_convertida = cv.Laplacian(imagem, cv.CV_64F)
        imagem_convertida = cv.convertScaleAbs(imagem_convertida)

        return imagem_convertida, None, None
    elif opcao == 2:

        while True:
            limiar_inferior = simpledialog.askstring("Variável", "Digite o valor do limiar inferior: ")

            if limiar_inferior == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                limiar_inferior = int(limiar_inferior)
                if limiar_inferior > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")
        
        while True:
            limiar_superior = simpledialog.askstring("Variável", "Digite o valor do limiar superior: ")

            if limiar_superior == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                limiar_superior = int(limiar_superior)
                if limiar_superior > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")

        imagem_convertida = cv.Canny(imagem, limiar_inferior, limiar_superior)
        imagem_convertida = cv.cvtColor(imagem_convertida, cv.COLOR_GRAY2RGB)

        return imagem_convertida, limiar_inferior, limiar_superior
    elif opcao == 3:
    
        imagem_tons_de_cinza = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY)
        
        # Calcula a magnitude do gradiente usando o operador Sobel
        sobel_x = cv.Sobel(imagem_tons_de_cinza, cv.CV_64F, 1, 0, ksize=9)
        sobel_y = cv.Sobel(imagem_tons_de_cinza, cv.CV_64F, 0, 1, ksize=9)
        magnitude_gradiente = cv.magnitude(sobel_x, sobel_y)
        
        # Normaliza os valores da imagem para o intervalo [0, 255]
        magnitude_gradiente = cv.normalize(magnitude_gradiente, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

        imagem_convertida = cv.cvtColor(magnitude_gradiente, cv.COLOR_GRAY2RGB)

        return imagem_convertida, None, None