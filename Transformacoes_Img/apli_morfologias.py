import cv2 as cv
import numpy as np
from tkinter import simpledialog, messagebox

def morfologias(opcao, imagem):
    while True:
            tamanho_kernel = simpledialog.askstring("Variável", "Digite o tamanho do kernel: ")

            if tamanho_kernel == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                tamanho_kernel = int(tamanho_kernel)
                if tamanho_kernel > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")

    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)

    if opcao == 1:
        imagem_convertida = cv.erode(imagem, kernel, iterations=1)

        return imagem_convertida, tamanho_kernel
    
    elif opcao == 2:
        imagem_convertida = cv.dilate(imagem, kernel, iterations=1)

        return imagem_convertida, tamanho_kernel
    