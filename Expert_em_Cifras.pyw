# _*_ coding:utf-8 _*_
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import os
import pyautogui
from time import sleep
from trans_A import *
from trans_Am import *
from trans_Astm import *
from trans_Ast import *
from trans_B import *
from trans_Bm import *
from trans_C import *
from trans_Cm import *
from trans_Cst import *
from trans_Cstm import *
from trans_D import *
from trans_Dm import *
from trans_Dst import *
from trans_Dstm import *
from trans_E import *
from trans_Em import *
from trans_F import *
from trans_Fm import *
from trans_Fst import *
from trans_Fstm import *
from trans_G import *
from trans_Gm import *
from trans_Gst import *
from trans_Gstm import *
from enviar_file import *
from pdf import *
from time import sleep
from escala import *
from PIL import Image
from tkinter.filedialog import askopenfilename



def main():
        try:
                janela.destroy()
        except:pass
        def translate():
                if str(n_cifra.get()) != '':
                    try:

                        root.update()
                        bt['text'] = 'Aguarde a conclusão...'
                        bt['bg'] = 'gray'
                        root.update()
                        if original.get().upper() == 'A':
                            root.update()
                            Trans_A(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Am':
                            root.update()
                            Trans_Am(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'A#':
                            root.update()
                            Trans_Ast(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'A#m':
                            root.update()
                            Trans_Astm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'B':
                            root.update()
                            Trans_B(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Bm':
                            root.update()
                            Trans_Bm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'C':
                            root.update()
                            Trans_C(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()                    
                        if original.get() == 'Cm':
                            root.update()
                            Trans_Cm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'C#':
                            root.update()
                            Trans_Cst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'C#m':
                            root.update()
                            Trans_Cstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'D':
                            root.update()
                            Trans_D(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Dm':
                            root.update()
                            Trans_Dm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'D#':
                            root.update()
                            Trans_Dst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'D#m':
                            root.update()
                            Trans_Dstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'E':
                            root.update()
                            Trans_E(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Em':
                            root.update()
                            Trans_Em(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'F':
                            root.update()
                            Trans_F(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Fm':
                            root.update()
                            Trans_Fm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'F#':
                            root.update()
                            Trans_Fst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'F#m':
                            root.update()
                            Trans_Fstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'G':
                            root.update()
                            Trans_G(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get() == 'Gm':
                            root.update()
                            Trans_Gm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                        if original.get().upper() == 'G#':
                            root.update()
                            Trans_Gst(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END),'')
                            root.update()
                        if original.get() == 'G#m':
                            root.update()
                            Trans_Gstm(n_cifra.get(), original.get(), mudado.get(), text_area.get(1.0, END), '')
                            root.update()
                      
                        text_area.delete(1.0, END)
                        with open(fr'Minhas_cifras/{n_cifra.get()}.txt', 'r', encoding='utf-8') as texto:
                            text_area.insert(1.0, str(texto.read()))
                            #enviar_email_2(f'Sua nova cifra "{n_cifra.get()}"', f'{text_area.get(1.0, END)}', 'moises.miss@gmail.com')
                            root.update()
                            create_pdf(fr'Minhas_cifras/{n_cifra.get()}', f'Minhas_cifras/{n_cifra.get()}')
                        
                        bt['bg'] = 'lime'
                        bt['text'] = 'Start'
                        root.update()
                        messagebox.showinfo(title='info', message='Sucesso, a troca de escala foi concluída')
                    except Exception as error:
                        messagebox.showerror(title='ERRO!', message=f'Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!\n{error}')
                        bt['bg'] = 'lime'
                        bt['text'] = 'Start'
                    root.update()
                else:
                    messagebox.showerror(title='ERRO!', message='Ouve um erro!\n Por favor cheque se digitou todas as informações necessária!')
                    bt['bg'] = 'lime'
                    bt['text'] = 'Start'
                root.update()


        root = Tk()
        pasta2 = PhotoImage(file='pasta1.png')
        logo = PhotoImage(file='logo.png')
        titulo = Label(root, image=logo, bg='#DDA0DD', height=150)
        titulo.pack()

        cif = Label(root,text='''Para começa faça uma copia de sua cifra, depois click dentro da caixa de texto abaixo e
click em colar e sua cifra será carregada; Ou click em escolher cifra e selecione o arquivo de texto com sua cifra.
        Observação o tom original e o novo tom só funciona se for: A, B, C, D, E, F, G, A#, C#, D#, F#, G#, Am, Bm, Cm, Dm, Em, Fm, Gm, A#m, C#m, D#m, F#m, G#m.    ''', bg='#DDA0DD')
        cif.pack()

        nome = Label(root,text='Para ver suas cifras click na pasta ao lado ou digite um nome na caixinha de texto "Título para nova cifra" e click em open', bg='#DDA0DD')
        nome.pack()
            
        f = Frame(root, bg='#DDA0DD', bd=7, relief=GROOVE)
        Label(f, text='Tom original ', bg='#DDA0DD').grid(row=0, column=0)
        original = Entry(f, bd=4, width=5)
        original.grid(row=0, column=1)

        Label(f, text='Novo Tom', bg='#DDA0DD').grid(row=0, column=2)
        mudado = Entry(f, bd=4, width=5)
        mudado.grid(row=0, column=3)

        Label(f, text='Título para nova cifra', bg='#DDA0DD').grid(row=0, column=4)
        n_cifra = Entry(f, bd=4, width=50)
        n_cifra.grid(row=0, column=5)


        def open_pasta():
            os.startfile(os.getcwd() + fr'/minhas_cifras')


        Label(root,text='\nMinhas Cifras', bg='#DDA0DD').pack(side=TOP, anchor=W)
        pasta_l = Button(root,image=pasta2, bg='#DDA0DD', bd=4, relief=GROOVE, command=open_pasta)
        pasta_l.pack(side=TOP, anchor=W)

        def enviar():
                Email()
                


        Button(root, text='Click aqui e envie cifras', bd=4, command=enviar, bg='lime', relief=GROOVE).pack(anchor=W)

        f.pack()
        def open_file():

                filename = askopenfilename()
                try:
                        with open(f'{filename}', 'r', encoding='utf-8') as f:
                                text_area.insert(1.0, str(f.read()))
                        messagebox.showinfo(title='Info', message='Sua cifra foi carregada com sucesso!')
                except Exception as error:
                        messagebox.showerror(title='Erro', message=f'Ouve um erro favor escolher um arquivo .txt!\n{error}')


        text_area = scrolledtext.ScrolledText(root,
                                                wrap = WORD, 
                                                width = 60, 
                                                height = 6, 
                                                font = ("Times New Roman",
                                                        12))
        text_area.pack()
        text_area.focus()

        file = Button(root, text='Escolher cifra', bd=4, command=open_file, bg='Yellow')
        file.pack(fill=X)

        def colar():
            pyautogui.hotkey('ctrl', 'v')


        bt_colar = Button(root, text='colar', bd=4, command=colar, bg='#9370DB', width=15)
        bt_colar.pack()

        bt = Button(root, text='start', bd=4, command=translate, bg='lime', relief=GROOVE)
        bt.pack(fill=X)


        def abrir():
            if str(n_cifra.get()) != '':
                try:
                    os.startfile(os.getcwd() + fr'/minhas_cifras/{n_cifra.get()}.txt')
                except:
                    pass


        open_arq = Button(f, text='Open', bd=4, command=abrir, bg='#9370DB', relief=GROOVE)
        open_arq.grid(row=0, column=6)


        def sair():
            root.destroy()


        bt_sair = Button(root, text='Exit', bd=4, command=sair, width=15)
        bt_sair.pack()
        root.title('Expert em Cifras')
        root.config(bg='#DDA0DD')
        root.geometry('+50+5')

        if __name__ == '__main__':
            root.mainloop()


import ver_escalas
janela = Tk()

logo2 = PhotoImage(file='ico.png')
janela.iconphoto(False,logo2)

titulo = Label(janela, image=logo2, bg='#DDA0DD', height=150)
titulo.pack()

inf = Label(janela,text='''O Expert em Cifras faz a troca de escalas musicais
e tudo de forma automática.
Agora em questão de segundos você pode mudar o tom de sua cifra, e também,
se não sabe subir ou baixar de tom, o app faz isso por você;
Da também acesso a todas as escalas musicais maiores e menores.
Ah! se parecer que o app travou é porque sua cifra tem muitas linhas mais mesmo assim ele vai executar o trabalho aguarde.
'''
, bg='#DDA0DD')
inf.pack()

Label(janela, text='''
Atenção o aplicativo pega as notas das cifras que estão em linhas individuais;
sendo assim, se na linha estiver qualquer palavra; por exemplo: [Solo] C9 D9,
está linha será pulada, e também se houver uma mudança de tom no meio da cifra, não passe ela pelo aplicativo,
pois ele não indentifica mudanças de tons.
''', bg='#DDA0DD', fg='red').pack()

def v():
        ver()


Button(janela, text='ver todas as escalas', bd=4, command=v, bg='#9370DB', relief=GROOVE, width=20).pack(anchor=W)

def AmentarBaixar():
        aumentar_baixar()


Button(janela, text='Aumentar ou baixar tons', bd=4, command=AmentarBaixar, bg='#9370DB', relief=GROOVE, width=20).pack(anchor=W)


def e_d():
        messagebox.showinfo(message=ver_escalas.ver_escalas(t.get()))

                                          
f = Frame(janela, bd=2, bg='#9370DB')
Label(f, text='Ver a escala de um tom; digite a frente qual quer ver exemplo: "A, B, C,Am, Bm, Cm"',bg='#DDA0DD').grid(row=0, column=0)
t = Entry(f, width=5, bd=4)
t.grid(row=0, column=1)
t.focus()
Button(f, text='Open', command=e_d, bg='#9370DB', bd=4).grid(row=0, column=2)
f.pack(anchor=W)

def entrar():
        main()


entrar = Button(janela, text='Trocar tom de cifras', bd=4, command=entrar, bg='lime', relief=GROOVE)
entrar.pack(fill=X)

def sai():
        janela.destroy()


sair = Button(janela, text='Exit', bd=4, command=sai, width=15)
sair.pack()

janela.title('Expert em Cifras')
janela.config(bg='#DDA0DD')
if __name__ == '__main__':
        janela.mainloop()

