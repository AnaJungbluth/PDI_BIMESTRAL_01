import cv2 as cv
from tkinter import simpledialog, messagebox

def binarizacoes(imagem):
    imagem = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY)

    while True:
        limiar = simpledialog.askstring("Variável", "Digite o valor do Limiar: ")

        if limiar == "":
            messagebox.showerror("Erro", "Digite um número.")
        else:
            limiar = int(limiar)
            if limiar > 0:
                break
            else:
                messagebox.showerror("Erro", "O número precisa ser maior que zero.")

    _, imagem_convertida = cv.threshold(imagem, limiar, 255, cv.THRESH_BINARY)
 
    return imagem_convertida, limiar
