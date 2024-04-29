import cv2 as cv
from tkinter import simpledialog, messagebox
 
def filtros(opcao, imagem):

    if opcao == 1:
        while True:
            tamanho_kernel1 = simpledialog.askstring("Variável", "Digite o tamanho do kernel1: ")

            if tamanho_kernel1 == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                tamanho_kernel1 = int(tamanho_kernel1)
                if tamanho_kernel1 > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")
        
        while True:
            tamanho_kernel2 = simpledialog.askstring("Variável", "Digite o tamanho do kernel2: ")

            if tamanho_kernel2 == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                tamanho_kernel2 = int(tamanho_kernel2)
                if tamanho_kernel2 > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")

        imagem_convertida = cv.blur(imagem, (tamanho_kernel1, tamanho_kernel2))

        return imagem_convertida, tamanho_kernel1, tamanho_kernel2
    elif opcao == 2:
        while True:
            sigma_color = simpledialog.askstring("Variável", "Digite o valor do sigmaColor: ")

            if sigma_color == "":
                messagebox.showerror("Erro", "Digite um número.")
            else:
                sigma_color = int(sigma_color)
                if sigma_color > 0:
                    break
                else:
                    messagebox.showerror("Erro", "O número precisa ser maior que zero.")

        imagem_convertida = cv.bilateralFilter(imagem, d=9, sigmaColor=sigma_color, sigmaSpace=75)

        return imagem_convertida, sigma_color, None
    elif opcao == 3:
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
        
        imagem_convertida = cv.medianBlur(imagem, tamanho_kernel)
        
        return imagem_convertida, tamanho_kernel, None


