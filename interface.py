from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import cv2 as cv
import os
from Transformacoes_Img.apli_cores import cores
from Transformacoes_Img.apli_filtros import filtros
from Transformacoes_Img.apli_bordas import bordas
from Transformacoes_Img.apli_binarizacao import binarizacoes
from Transformacoes_Img.apli_morfologias import morfologias
from Reaplicar_Transformacoes_img.reap_filtros import reap_filtros
from Reaplicar_Transformacoes_img.reap_bordas import reap_bordas
from Reaplicar_Transformacoes_img.reap_binarizacao import reap_binarizacoes
from Reaplicar_Transformacoes_img.reap_morfologias import reap_morfologias

alteracoes = [] # continuar //nome do tipo da alteração, alteração feita, dado informados

janela_principal = Tk()
janela_principal.title('Editor de Imagens')
janela_principal.geometry('988x588')
janela_principal.resizable(False, False)

imagem_lixeira = Image.open("D:\\Processamento_de_imagem\\TrabalhoBimestral1\\Icones\\icone_lixeira.png")
imagem_limpeza = Image.open("D:\\Processamento_de_imagem\\TrabalhoBimestral1\\Icones\\icone_limpeza.png")
tamanho_icone_limpeza = (30, 30)
imagem_limpeza = imagem_limpeza.resize(tamanho_icone_limpeza)

icone_lixeira = ImageTk.PhotoImage(imagem_lixeira)
icone_limpeza = ImageTk.PhotoImage(imagem_limpeza)

cor_aplicada = False
imagem_or = None
index_selecionado = None

def carregar_img_original():
    caminho_imagem = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif")])

    if caminho_imagem:
        global img_original
        global imagem_or
        global largura_frame
        global altura_frame

        imagem = cv.imread(caminho_imagem)
        
        largura_frame = 470
        altura_frame = 280
    
        imagem_rgb = cv.cvtColor(imagem, cv.COLOR_BGR2RGB) 
        altura_imagem, largura_imagem, _ = imagem_rgb.shape
        
        # Redimensionar a imagem para se ajustar ao frame
        proporcao = min(largura_frame / largura_imagem, altura_frame / altura_imagem)
        nova_largura = int(largura_imagem * proporcao)
        nova_altura = int(altura_imagem * proporcao)
        imagem_redimensionada = cv.resize(imagem_rgb, (nova_largura, nova_altura))

        imagem_or = imagem_redimensionada
        img_original = imagem_redimensionada

        imagem_rgb = Image.fromarray(imagem_redimensionada)

        for widget in imagem_original.winfo_children():
            widget.destroy()

        imagem_ori_tk = ImageTk.PhotoImage(imagem_rgb)
        
        imagem_ori = Label(imagem_original, image=imagem_ori_tk)
        imagem_ori.imagem_tk = imagem_ori_tk  
        imagem_ori.pack()
    else:
        print("Erro ao carregar a imagem")

def salvar_imagem(imagem): 
    if imagem is not None:
        caminho_salvar = 'D:\\Processamento_de_imagem\\TrabalhoBimestral1\\Imagens_salvas'
    
        nome_arquivo = simpledialog.askstring("Salvar Imagem", "Digite o nome do arquivo:")
        imagem_pil = Image.fromarray(imagem)

        if nome_arquivo:
            imagem_pil.save(os.path.join(caminho_salvar, f"{nome_arquivo}.png"))
    else:
        messagebox.showerror("Erro","Selecione uma imagem para poder salvar.")
        return

    
def tela():
    global menu_edicoes_opcoes
    global menu_botoes
    global imagem_original
    global imagem_editada
    global menu_edicoes_feitas

    janela_principal.configure(background='#0D1117')

    imagem_original = Frame(janela_principal, width=476, height=286, bg='#151a21', highlightbackground='white', highlightthickness=2)
    imagem_original.pack(side=LEFT, padx=9, pady=10, anchor='n')
    imagem_original.pack_propagate(False) 

    imagem_editada = Frame(janela_principal, width=476, height=286, bg='#151a21', highlightbackground='white', highlightthickness=2)
    imagem_editada.pack(side=RIGHT, padx=9, pady=10, anchor='n')
    imagem_editada.pack_propagate(False) 

    menu_edicoes_opcoes = Frame(janela_principal, width=150, height=276, bg='#0D1117')
    menu_edicoes_opcoes.place(x=15, y=580-268-10)

    menu_edicoes_feitas = Frame(janela_principal, width=730, height=256, bg='#151a21', highlightbackground='blue', highlightthickness=2)
    menu_edicoes_feitas.place(x=185, y=580-260-10)
    menu_edicoes_feitas.pack_propagate(False) 

    menu_botoes = Frame(janela_principal, width=60, height=276, bg='#0D1117')
    menu_botoes.place(x=926, y=580-260-10)

def menu_tela():
    menu_principal = Menu(janela_principal)

    menu_arquivo = Menu(menu_principal, tearoff=0)
    menu_arquivo.add_command(label="Abrir", command=carregar_img_original)
    menu_arquivo.add_command(label="Salvar", command=lambda: salvar_imagem(imagem_or))
    menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)

    janela_principal.config(menu=menu_principal)

def mostrar_imagem_editada(imagem_convertida):
    global imagem_or
    imagem_or = imagem_convertida

    imagem_pil = Image.fromarray(imagem_convertida)
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    
    for widget in imagem_editada.winfo_children():
        widget.destroy()

    label_imagem = Label(imagem_editada, image=imagem_tk)
    label_imagem.imagem_tk = imagem_tk
    label_imagem.pack()

def adicionar_detalhes_alteracao(tipo_alteracao, op, nome_alteracao, dado1=None, dado2=None):
    alteracao = {
        "tipo": tipo_alteracao,
        "opcao": op,
        "nome": nome_alteracao,
        "dado1": dado1,
        "dado2": dado2
    }
    alteracoes.append(alteracao)
    mostrar_detalhes_alteracoes()
    
def mostrar_detalhes_alteracoes():
    global index
    for widget in menu_edicoes_feitas.winfo_children():
        widget.destroy()

    for i, alteracao in enumerate(alteracoes):
        if alteracao['dado1'] == None and alteracao['dado2'] == None:
            detalhes_label = Label(menu_edicoes_feitas, text=f"Alteração {i+1}: {alteracao['nome']}", bg='#151a21', fg='white', anchor='w')
        elif alteracao['dado2'] == None:
            detalhes_label = Label(menu_edicoes_feitas, text=f"Alteração {i+1}: {alteracao['nome']}, {alteracao['dado1']}", bg='#151a21', fg='white', anchor='w') 
        else:    
            detalhes_label = Label(menu_edicoes_feitas, text=f"Alteração {i+1}: {alteracao['nome']}, {alteracao['dado1']}, {alteracao['dado2']}", bg='#151a21', fg='white', anchor='w')
        detalhes_label.bind("<Button-1>", lambda event, index=i: selecionar_linha(event, index))
        detalhes_label.pack(fill='x', side='top')  
        
def selecionar_linha(event, index):
    global index_selecionado
    index_selecionado = index
    for widget in menu_edicoes_feitas.winfo_children():
        widget.configure(bg='#151a21')
    event.widget.configure(bg='#252b33')

def excluir_uma_alteracao():
    global index_selecionado
    if index_selecionado is None:
        messagebox.showerror("Erro", "Nenhuma alteração selecionada.")
        return

    alteracao = alteracoes[index_selecionado]  # Obter a alteração selecionada
    del alteracoes[index_selecionado]
    if alteracao['tipo'] == 'cores':
        global cor_aplicada
        cor_aplicada = False

    reaplicar_transformacoes(img_original)

    messagebox.showinfo("Aviso", "Alteração selecionada foi deletada")
    if not alteracoes:
        for widget in imagem_editada.winfo_children():
            widget.destroy()

    mostrar_detalhes_alteracoes()

def excluir_todas_alteracoes():
    global alteracoes
    global cor_aplicada
    global imagem_or
    if alteracoes != []:
        alteracoes = []

        for widget in imagem_editada.winfo_children():
            widget.destroy()

        cor_aplicada = False
        mostrar_detalhes_alteracoes()
        imagem_or = img_original
        messagebox.showinfo("Aviso", "As alterações foram deletadas")
    else:
        messagebox.showinfo("Aviso", "Não tem nenhuma alteração.")
        return

def menu_botos_frame():
    botao_lixeira = Button(menu_botoes, image=icone_lixeira, command= excluir_uma_alteracao)
    botao_lixeira.pack(padx=5)

    botao_limpeza = Button(menu_botoes, image=icone_limpeza, command=excluir_todas_alteracoes)
    botao_limpeza.pack(padx=5, pady=14)

def menu_opcoes_cores():
    global selecionar_cores
    
    def selecionar_cores(opcao, imagem):
        global cor_aplicada

        if imagem_or is not None:
            if cor_aplicada == False:
                imagem_editada = cores(opcao, imagem)
                cor_aplicada = True
                adicionar_detalhes_alteracao('cores', opcao,"Cor: RGB -> GRAY" if opcao == 1 else "Cor: RGB -> HSV" if opcao == 2 else "Cor: RGB -> HLS")
                mostrar_imagem_editada(imagem_editada)
            else:    
                messagebox.showerror("Erro", "Uma cor já foi aplicada. Limpe a edição antes de aplicar outra cor.")
                return
        else:
            messagebox.showerror("Erro","Selecione uma imagem para aplicar alguma alteração.")
            return

    menu_cores = Menubutton(menu_edicoes_opcoes, text="Cores", indicatoron=True, borderwidth=1, relief="raised",width=20, height=2)
    menu_cores.menu = Menu(menu_cores, tearoff=0)
    menu_cores["menu"] = menu_cores.menu
    menu_cores.menu.add_command(label="       RGB -> GRAY       ", command=lambda:selecionar_cores(1, imagem_or))
    menu_cores.menu.add_command(label="       RGB -> HSV        ", command=lambda:selecionar_cores(2, imagem_or))
    menu_cores.menu.add_command(label="       RGB -> HLS        ", command=lambda:selecionar_cores(3, imagem_or))
    menu_cores.pack(pady=7)

def menu_opcoes_filtro():
    global selecionar_filtros

    def selecionar_filtros(opcao, imagem):
        if imagem_or is not None:
            imagem_editada, dado1, dado2 = filtros(opcao, imagem)
            adicionar_detalhes_alteracao('filtros', opcao, "Filtro: Blur" if opcao == 1 else "Filtros: Bilateral" if opcao == 2 else "Filtro: Mediana", dado1, dado2)
            mostrar_imagem_editada(imagem_editada)
        else:
            messagebox.showerror("Erro","Selecione uma imagem para aplicar alguma alteração.")
            return

    menu_filtro = Menubutton(menu_edicoes_opcoes, text="Filtro", indicatoron=True, borderwidth=1, relief="raised",width=20, height=2)
    menu_filtro.menu = Menu(menu_filtro, tearoff=0)
    menu_filtro["menu"] = menu_filtro.menu
    menu_filtro.menu.add_command(label="            Blur             ", command=lambda:selecionar_filtros(1, imagem_or))
    menu_filtro.menu.add_command(label="            Bilateral        ", command=lambda:selecionar_filtros(2, imagem_or))
    menu_filtro.menu.add_command(label="            Mediana          ", command=lambda:selecionar_filtros(3, imagem_or))
    menu_filtro.pack(pady=7)

def menu_opcoes_borda():
    global selecionar_bordas

    def selecionar_bordas(opcao, imagem):
        global cor_aplicada

        if imagem_or is not None:
            imagem_editada, dado1, dado2 = bordas(opcao, imagem)
            cor_aplicada = True
            adicionar_detalhes_alteracao('bordas', opcao, 'Borda: laplace' if opcao == 1 else 'Borda: canny' if opcao == 2 else 'Borda: solve', dado1, dado2)
            mostrar_imagem_editada(imagem_editada)
        else:
            messagebox.showerror("Erro","Selecione uma imagem para aplicar alguma alteração.")
            return

    menu_borda = Menubutton(menu_edicoes_opcoes, text="Borda", indicatoron=True, borderwidth=1, relief="raised",width=20, height=2)
    menu_borda.menu = Menu(menu_borda, tearoff=0)
    menu_borda["menu"] = menu_borda.menu
    menu_borda.menu.add_command(label="           Laplace             ", command=lambda:selecionar_bordas(1, imagem_or))
    menu_borda.menu.add_command(label="           Canny               ", command=lambda:selecionar_bordas(2, imagem_or))
    menu_borda.menu.add_command(label="           Solve               ", command=lambda:selecionar_bordas(3, imagem_or))
    menu_borda.pack(pady=7) 

def menu_opcoes_binarizacao():
    global selecionar_binarizacoes

    def selecionar_binarizacoes(imagem):
        global cor_aplicada

        if imagem_or is not None:
            imagem_editada, limiar = binarizacoes(imagem)
            cor_aplicada = True
            adicionar_detalhes_alteracao('binarizacao', 'Binarização: threshold', limiar)
            mostrar_imagem_editada(imagem_editada)
        else:
            messagebox.showerror("Erro","Selecione uma imagem para aplicar alguma alteração.")
            return

    menu_binarizacao = Menubutton(menu_edicoes_opcoes, text="Binarização", indicatoron=True, borderwidth=1, relief="raised",width=20, height=2)
    menu_binarizacao.menu = Menu(menu_binarizacao, tearoff=0)
    menu_binarizacao["menu"] = menu_binarizacao.menu
    menu_binarizacao.menu.add_command(label="        Threshold            ", command=lambda:selecionar_binarizacoes(imagem_or))
    menu_binarizacao.pack(pady=7)

def menu_opcoes_morfologia():
    global selecionar_morfologias

    def selecionar_morfologias(opcao, imagem):
        if imagem_or is not None:
            imagem_editada, tamanho_kernel = morfologias(opcao, imagem)
            adicionar_detalhes_alteracao('morfologia', opcao, 'Morfologia: erosão' if opcao == 1 else 'Morfologia: dilatação', tamanho_kernel)
            mostrar_imagem_editada(imagem_editada)
        else:
            messagebox.showerror("Erro","Selecione uma imagem para aplicar alguma alteração.")
            return
    
    menu_morfologia = Menubutton(menu_edicoes_opcoes, text="Morfologia", indicatoron=True, borderwidth=1, relief="raised",width=20, height=2)
    menu_morfologia.menu = Menu(menu_morfologia, tearoff=0)
    menu_morfologia["menu"] = menu_morfologia.menu
    menu_morfologia.menu.add_command(label="          Erosão              ", command=lambda:selecionar_morfologias(1, imagem_or))
    menu_morfologia.menu.add_command(label="          Dilatação           ", command=lambda:selecionar_morfologias(2, imagem_or))
    menu_morfologia.pack(pady=7)

def limpar_edicoes():
    global cor_aplicada
    cor_aplicada = False
    for widget in imagem_editada.winfo_children():
        widget.destroy()

def reaplicar_transformacoes(imagem):
    imagem_editada = imagem.copy()
    for alteracao in alteracoes:
        tipo = alteracao['tipo']
        if tipo == 'cores':
            imagem_editada = cores(alteracao['opcao'], imagem_editada)
        elif tipo == 'filtros':
            imagem_editada = reap_filtros(alteracao['opcao'], imagem_editada, alteracao['dado1'], alteracao['dado2'])
        elif tipo == 'bordas':
            if alteracao['opcao'] == 1 or alteracao['opcao'] == 3:
                imagem_editada = bordas(alteracao['opcao'], imagem_editada)
            else:
                imagem_editada = reap_bordas(imagem_editada, alteracao['dado1'], alteracao['dado2'])
        elif tipo == 'binarizacao':
            imagem_editada = reap_binarizacoes(imagem_editada, alteracao['dado1'])
        elif tipo == 'morfologia':
            imagem_editada = reap_morfologias(alteracao['opcao'], imagem_editada, alteracao['dado1'])
    
    mostrar_imagem_editada(imagem_editada)


def chama_menus():
    menu_tela()
    menu_opcoes_cores() 
    menu_opcoes_filtro() 
    menu_opcoes_borda()
    menu_opcoes_binarizacao()
    menu_opcoes_morfologia()
    menu_botos_frame()
    
tela()
chama_menus()

janela_principal.mainloop()
