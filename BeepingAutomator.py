"""
Este é um exemplo de aplicativo tkinter com funcionalidade de automação usando PyAutoGUI.
Ele permite que o usuário insira informações sobre caixas e medidores e, em seguida, inicie a automação
para inserir os dados conforme necessário.

Instruções de uso:
- Caso não esteja logado clique em login que ele irá pedir seu user e senha do eletraea, certificar que esta correto!.
- Clique em login novamente para que ele faça o login automaticamente.
- Preencha os campos com as informações necessárias.
- Clique no botão 'START' para iniciar a automação.
- Finalizando clique em fechar palete para que ele coloque os dois ultimos codigos.
- Quando for iniciar um novo codigo clique em clear para limpar todos os valores digitados.

@author: Denilson
"""
import random
import pyautogui as pg
import tkinter as tk
from tkinter import messagebox
from time import sleep

# Lista onde guarda os códigos de fechamento
codigos = []
user_eletraea = {'user': '', 'senha': ''}

xy = "300x400"
azul_claro = "#5F9F9F"
cinza = "#2E353D"
cinza_claro1 = "#F0FfF9"
cinza_claro2 = "#666666"
tamanho_fonte = 9
fonte = ('Helvetica', tamanho_fonte, 'bold')
fonte_creditos = ('Courier', 9, 'bold')

root = tk.Tk()
root.title("Beeping Automator")
root.geometry(xy)
root.resizable(False, False)
root.iconbitmap("C:\\Users\\denilson.bessa.ELETRA\\PycharmProjects\\pythonProject\\automatic_logo_icon_145470.ico")


def iniciar_programa():
    """
    Função para iniciar o programa de automação.
    - Obtém informações inseridas pelo usuário.
    - Inicia a automação para inserir os dados conforme necessário.
    """
    texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop = guardar_texto()
    if not texto_caixas or not texto_primeira_caixa or not texto_medidores_caixa or not texto_primeiro_codigo or not texto_prefix_codigo:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
        return

    medidores_inteiro = int(texto_medidores_caixa)

    # Abrir o navegador Chrome
    pg.keyDown('alt')  # Chrome
    pg.press('tab')
    pg.keyUp('alt')
    sleep(1)

    # Mover o cursor para a entrada de dados
    pg.moveTo(261, 222)  # Move para a entrada de dados
    pg.click()
    pg.hotkey('ctrl', 'a')

    # Escrever o código do primeiro medidor
    sleep(1)
    if prefix_codigo_loop == False:
        pg.typewrite(str(texto_primeiro_codigo), interval=0)
        pg.press('enter')
    else:
        pg.typewrite(texto_prefix_codigo + str(texto_primeiro_codigo), interval=0)
        pg.press('enter')

    # Loop para inserir códigos de medidores para cada caixa
    print('<LOG')
    for c in range(int(texto_caixas) - 1):
        # Imprime a contagem para cada caixa
        print(f'    {contagem}')
        codigos.append(contagem)
        sleep(0.5)
        if prefix_codigo_loop:
            pg.typewrite(texto_prefix_codigo + str(contagem), interval=0)
        else:
            pg.typewrite(str(contagem), interval=0)
        pg.press('enter')

        # Adiciona a quantidade de medidores na caixa atual
        contagem += medidores_inteiro
    print('          LOG>')
    sleep(1)
    # Escrever um código especial no final
    pg.typewrite(str('00000000'), interval=0)
    pg.press('enter')
    sleep(1)
    messagebox.showinfo('Finish', 'Codigos digitados com sucesso!')


def fechar_palete():
    """
    Função para fechar a paleta.
    - Obtém informações inseridas pelo usuário.
    - Insere os dois últimos códigos.
    """
    texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop = guardar_texto()
    # Abrir o navegador Chrome
    if not codigos:
        messagebox.showwarning("ATENÇÃO!", "VOCÊ PRECISA INICIAR O PROGRAMA PRIMEIRO")
        return
    pg.keyDown('alt')  # Chrome
    pg.press('tab')
    pg.keyUp('alt')
    sleep(1)

    if not prefix_codigo_loop:
        for n in range(2):
            pg.typewrite(str(codigos[n]), interval=1)
            pg.press('enter')
            pg.press('tab')
    else:
        for n in range(2):
            pg.typewrite(texto_prefix_codigo + str(codigos[n]), interval=1)
            pg.press('enter')
            pg.press('tab')


def guardar_texto():
    """
    Função para obter os valores inseridos pelo usuário.
    """
    texto_caixas = caixas_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE CAIXAS"
    texto_medidores_caixa = medidores_caixas_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE MEDIDORES POR CAIXA"
    texto_primeira_caixa = primeira_caixa_entry.get()  # Obtém o texto inserido no campo "QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA"
    texto_primeiro_codigo = primeiro_codigo_entry.get()  # Obtém o texto inserido no campo "CODIGO DO PRIMEIRO MEDIDOR"
    texto_prefix_codigo = prefix_codigo_entry.get()  # Obtém o texto inserido no campo "PREFIXO (0 SE NÃO HOUVER)"

    prefix_codigo_loop = True  # Define a variável prefix_codigo_loop como True por padrão
    if texto_prefix_codigo == '0':  # Verifica se o texto do campo "PREFIXO (0 SE NÃO HOUVER)" é '0'
        prefix_codigo_loop = False  # Se for, define prefix_codigo_loop como False

    # Verificar se o campo "CODIGO DO PRIMEIRO MEDIDOR" está vazio
    # Evita erro para que possa ser exibida a mensagem de popup NÃO APAGAAAAAAAAAAA
    if texto_primeiro_codigo == '':
        return None, None, None, None, None, None, None
        pass

    contagem = int(texto_primeiro_codigo) + int(
        texto_primeira_caixa)  # Calcula a contagem somando o valor inserido no campo "CODIGO DO PRIMEIRO MEDIDOR" com o valor inserido no campo "QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA"

    return texto_caixas, texto_primeira_caixa, texto_medidores_caixa, texto_primeiro_codigo, contagem, texto_prefix_codigo, prefix_codigo_loop  # Retorna todos os textos e variáveis calculadas


def abrir_janela_login():
    """
    Função para abrir a janela de login.
    - Solicita usuário e senha.
    """
    if not user_eletraea['user'] and not user_eletraea['senha']:
        janela_login = tk.Toplevel(root)
        janela_login.config(bg=cinza)
        janela_login.title('Login')
        janela_login.geometry("200x150")
        janela_login.resizable(False, False)
        janela_login.iconbitmap("C:\\Users\\denilson.bessa.ELETRA\\PycharmProjects\\pythonProject\\automatic_logo_icon_145470.ico")


        # Widgets de login
        tk.Label(janela_login, text='User:', font=('Press Start 2P', 9, 'bold'), bg=cinza, fg='white').pack()
        usuario_entry = tk.Entry(janela_login, font=('Press Start 2P', 9))
        usuario_entry.pack()

        tk.Label(janela_login, text='Password:', font=('Press Start 2P', 9, 'bold'), bg=cinza, fg='white').pack()
        senha_entry = tk.Entry(janela_login, show='*', font=('Press Start 2P', 9))
        senha_entry.pack()

        def fazer_login():
            # Obtém os valores dos campos de entrada
            usuario = usuario_entry.get()
            senha = senha_entry.get()

            if usuario == '' or senha == '':
                # Mostra um aviso se os campos estiverem vazios
                messagebox.showwarning('Erro', 'Usuario ou senha invalidos, tente novamente!')
            else:
                # Armazena usuário e senha nas variáveis
                user_eletraea['user'] = usuario
                user_eletraea['senha'] = senha

                if user_eletraea['user'] or user_eletraea['senha']:

                    # Fecha a janela depois de fazer login
                    janela_login.destroy()
                return user_eletraea
        login = tk.Button(janela_login, text='LOGIN', font=('Press Start 2P', 10, 'bold'), bg=cinza_claro2,
                          command=fazer_login)
        login.pack(pady=5)


def logar():
    """
    Função para fazer login no sistema.
    """
    abrir_janela_login()

    if user_eletraea['user'] and user_eletraea['senha']:
        pg.press('win')
        sleep(0.3)
        pg.write('chrome')
        pg.press('enter')
        sleep(1)
        pg.write('http://sistemas/InspectionMeter/TelephoneList.aspx')
        pg.press('enter')
        pg.sleep(1)
        pg.click(605, 325)
        sleep(6)
        pg.click(677, 297)
        pg.hotkey('ctrl', 'a')
        pg.write(user_eletraea['user'])
        pg.hotkey('tab')
        sleep(0.5)
        pg.write(user_eletraea['senha'])
        pg.press('enter')
        sleep(1)
        pg.click(37, 601)
        sleep(0.1)
        pg.click(57, 632)
        sleep(0.1)
        pg.click(32, 692)


def clear():
    """
    Função para limpar os campos de entrada.
    """
    caixas_entry.delete(0, tk.END)
    medidores_caixas_entry.delete(0, tk.END)
    primeira_caixa_entry.delete(0, tk.END)
    primeiro_codigo_entry.delete(0, tk.END)
    prefix_codigo_entry.delete(0, tk.END)


# Carregar a imagem de plano de fundo
imagem_fundo = tk.PhotoImage(file='C:\\Users\\denilson.bessa.ELETRA\\PycharmProjects\\pythonProject\\wp_bdi_096.png')
fundo_label = tk.Label(root, image=imagem_fundo)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Outros widgets
caixas = tk.Label(root, text='QUANTIDADE DE CAIXAS', font=fonte, background=cinza,
                  fg='white')  # Pede a quantidade de caixas
caixas.pack(padx=10)
caixas_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
caixas_entry.pack(pady=5)

medidores_caixas = tk.Label(root, text='QUANTIDADE DE MEDIDORES POR CAIXA', font=fonte, background=cinza,
                            fg='white')  # Pede a quantidade de medidores
medidores_caixas.pack(pady=5)
medidores_caixas_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
medidores_caixas_entry.pack(pady=5)

primeira_caixa = tk.Label(root, text='QUANTIDADE DE MEDIDORES NA PRIMEIRA CAIXA', font=fonte, background=cinza,
                          fg='white')  # Pede a quantidade de medidores na primeira caixa
primeira_caixa.pack(pady=5)
primeira_caixa_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
primeira_caixa_entry.pack(pady=5)

primeiro_codigo = tk.Label(root, text='CODIGO DO PRIMEIRO MEDIDOR', font=fonte, background=cinza,
                           fg='white')  # Pede o codigo do primeiro medidor
primeiro_codigo.pack(pady=5)
primeiro_codigo_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
primeiro_codigo_entry.pack(pady=5)

prefix_codigo = tk.Label(root, text='PREFIXO (0 SE NÃO HOUVER)', font=fonte, background=cinza,
                         fg='white')  # Pede o prefixo, se não houver digita 0(Todo resto considera prefixo)
prefix_codigo.pack(pady=5)
prefix_codigo_entry = tk.Entry(root, width=15, font=fonte_creditos, justify='center', bg=cinza_claro1)
prefix_codigo_entry.pack(pady=5)

botao_iniciar = tk.Button(root, text='START', font=('Press Start 2P', 12, 'bold'),
                          command=iniciar_programa)  # Botao start Chama a função iniciar programa e a magica acontece
botao_iniciar.config(bg=cinza_claro2)
botao_iniciar.pack(pady=10)

botao_fechar = tk.Button(root, text='FECHAR PALETE', font=('Press Start 2P', 9, 'bold'), command=fechar_palete)
botao_fechar.config(bg=cinza_claro2)
botao_fechar.place(x=100, y=347)

botao_login = tk.Button(root, text='LOGIN', font=('Press Start 2P', 9, 'bold'),
                        command=logar)  # Botão para logar no sistemas
botao_login.config(bg=cinza_claro2)
botao_login.place(x=250, y=375)

botao_clear = tk.Button(root, text='CLEAR', font=('Press Start 2P', 9, 'bold'), command=clear)  # Botao para limpar as entrys
botao_clear.config(bg=cinza_claro2)
botao_clear.place(x=5, y=375)
dev = tk.Label(root, font=fonte_creditos, text='@Author: Denilson', background=cinza, fg='white')  # Author Credits
dev.place(x=85, y=380)

root.mainloop()
