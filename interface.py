from customtkinter import *
from tkinter import ttk
from PIL import Image
from CTkMessagebox import CTkMessagebox
import time as tm
from datetime import datetime as dt, timedelta, time
from pygame import mixer

class MainInterface:
    def __init__(self, root, tela_width, tela_height, version):
        self.root = root
        self.tela_width = tela_width
        self.tela_height = tela_height
        #variaveis para controle de janelas toplevel
        self.yon = False
        self.tp_password = None
        #general estilização treeview 
        style = ttk.Style()
        style.map("Treeview", 
                background=[("selected", "orange")])
        style.configure("Treeview", font=("arial", 12))
        style.configure("Treeview.Heading", font=("Arial", 10, 'bold'))

        #relogio
        self.clock = CTkLabel(self.root, font=("Arial", 20))
        self.clock.place(relx=0.93, rely=0.95)
        self.clock.lift()
        self.update_clock()

        #outras definições
        mixer.init()
        self.formas_pgmt_ativas = ('DINHEIRO', 'DÉBITO', 'CRÉDITO', 'PIX', 'OUTRO')
        self.general_product_id = '20'
        self.customer_id = 0
        self.oncredit_ids = []
        self.version = version
        self.contato = '51 989705423'
        self.tv_colunas = ('ID', 'PROFISSIONAL', 'SERVIÇO', 'FORMA DE PGMT', 'VALOR', 'HORA')

        #fontes
        self.basic = CTkFont('arial', 15, 'bold')
        self.fonte_padrao_bold = CTkFont('arial', 18, 'bold')
        self.fonte_padrao = CTkFont('arial', 16)

        #self.profissionais
        self.profissionais = ('LUCIANO', 'KAUAN', 'DEIVISON', 'SAMUEL')



        #imgs
        self.somar_img = CTkImage(light_image=Image.open(r'images\botao_somar.png'), size=(30, 30 ))
        self.logo_img = CTkImage(light_image=Image.open(r'images\logo.png'), size=(80, 80))


        self.abrir_root()

    def update_clock(self):
        now = tm.strftime("%H:%M:%S")
        self.clock.configure(text=now)
        self.root.after(1000, self.update_clock)

    def abrir_root(self):
        pady = 10 

        #Header
        self.root_title = CTkLabel(self.root, text=f'  BARBEARIA ENTRE AMIGOS {self.version}  ',  image= self.logo_img, font=CTkFont('helvetica', 60, 'bold'), compound='left', 
        fg_color='black', text_color='white', width=self.tela_width, height=100, corner_radius=10)
        self.root_title.place(relx=0.5, rely=0, anchor='n')

        # FRAME 0 \\ REGISTRAR ENTRADA
        
        tb_0_fm_0_width= 650
        tb_0_fm_0 = CTkFrame(self.root, fg_color='white', width= tb_0_fm_0_width, height=507)
        tb_0_fm_0.place(relx=0.01, rely=0.2)

        #titlo
        tb_0_fm_0_wg_0 = CTkLabel(tb_0_fm_0, text='REGISTRAR SERVIÇO', width= tb_0_fm_0_width, height=30, font=self.fonte_padrao_bold)
        tb_0_fm_0_wg_0.place(relx=0,rely=0.05)

        #wgs profissional
        def Toggle():
            if last_selected_profissional_var != '':
                if profissional_var.get() == last_selected_profissional_var.get():
                    profissional_var.set('')
            last_selected_profissional_var.set(profissional_var.get())

        tb_0_fm_0_wg_1 = CTkLabel(tb_0_fm_0, text='Profissional:', font= self.fonte_padrao, text_color='black')
        tb_0_fm_0_wg_1.place(relx=0.05, rely=0.25)
        profissional_var = StringVar()
        last_selected_profissional_var = StringVar()
        tb_0_fm_0_wg_2 = CTkRadioButton(tb_0_fm_0, text=self.profissionais[0], variable=profissional_var, value=self.profissionais[0], command=lambda:Toggle(), text_color='black', font=self.fonte_padrao, border_width_checked=10)
        tb_0_fm_0_wg_2.place(relx=0.20, rely=0.25)
        tb_0_fm_0_wg_2_1 = CTkRadioButton(tb_0_fm_0, text=self.profissionais[1], variable=profissional_var, value=self.profissionais[1], command=lambda:Toggle(), text_color='black', font=self.fonte_padrao, border_width_checked=10)
        tb_0_fm_0_wg_2_1.place(relx=0.40, rely=0.25)
        tb_0_fm_0_wg_2_2 = CTkRadioButton(tb_0_fm_0, text=self.profissionais[2], variable=profissional_var, value=self.profissionais[2], command=lambda:Toggle(), text_color='black', font=self.fonte_padrao, border_width_checked=10)
        tb_0_fm_0_wg_2_2.place(relx=0.60, rely=0.25)
        tb_0_fm_0_wg_2_3 = CTkRadioButton(tb_0_fm_0, text=self.profissionais[3], variable=profissional_var, value=self.profissionais[3], command=lambda:Toggle(), text_color='black', font=self.fonte_padrao, border_width_checked=10)
        tb_0_fm_0_wg_2_3.place(relx=0.80, rely=0.25)
        sinalizer = CTkLabel(tb_0_fm_0, text='Selecionar um profissional', text_color='red', font=self.basic)

        tb_0_fm_0_wg_4_var = StringVar(value='')
        tb_0_fm_0_wg_3 = CTkLabel(tb_0_fm_0, text='Serviços:', font= self.fonte_padrao, text_color='black')
        tb_0_fm_0_wg_3.place(relx=0.05, rely=0.4)
        tb_0_fm_0_wg_4 = CTkEntry(tb_0_fm_0, textvariable=tb_0_fm_0_wg_4_var,font= self.fonte_padrao, width=400, height=30, fg_color='black', text_color='white')
        tb_0_fm_0_wg_4.place(relx=0.20, rely=0.4)
        tb_0_fm_0_wg_4.configure(state='disabled')
        tb_0_fm_0_wg_5 = CTkButton(tb_0_fm_0, width=10, height=10 , image=self.somar_img, text='', hover=True, fg_color='white', command=lambda:abrir_tl_0(), border_width=2, border_color='black', font= self.fonte_padrao)
        tb_0_fm_0_wg_5.place(relx=0.9, rely=0.4)

        #wgs form pgmt
        tb_0_fm_0_wg_6 = CTkLabel(tb_0_fm_0, text='Modo Pgmt.:', font= self.fonte_padrao, text_color='black')
        tb_0_fm_0_wg_6.place(relx=0.05, rely=0.55)
        tb_0_fm_0_wg_7 = CTkComboBox(tb_0_fm_0,font= self.fonte_padrao, values=self.formas_pgmt_ativas, fg_color='black', width=200, dropdown_hover_color='blue', text_color='white')  
        tb_0_fm_0_wg_7.place(relx=0.20, rely=0.55)
        tb_0_fm_0_wg_7.set('MODO DE PGMT. 1')
        sinalizer_0 = CTkLabel(tb_0_fm_0, text='Selecione uma forma de pagamento válida', text_color='red', font=self.basic, height=4)

        #wgs valor
        tb_0_fm_0_wg_10 = CTkLabel(tb_0_fm_0, text='R$:', font= self.fonte_padrao, text_color='black')
        tb_0_fm_0_wg_10.place(relx=0.05, rely=0.7)
        tb_0_fm_0_wg_9 = CTkEntry(tb_0_fm_0, font= self.fonte_padrao, width=100, height=30, fg_color='black', text_color='white')
        tb_0_fm_0_wg_9.place(relx=0.20, rely=0.7)
        sinalizer_2 = CTkLabel(tb_0_fm_0, text='Insira um valor válido', text_color='red', font=self.basic, height=4)
        
        #botao registrar
        tb_0_fm_0_wg_11 = CTkButton(tb_0_fm_0, state='normal',text='Registrar Entrada', font= self.fonte_padrao, command=lambda:registrarEntrada(), text_color='black')
        tb_0_fm_0_wg_11.place(relx=0.40, rely=0.9)


        # TREEVIEW

        tv = ttk.Treeview(self.root, columns=self.tv_colunas , show='headings', height=24, selectmode='browse')
        tv.place(relx= 0.5, rely=0.2)
        tv.column(self.tv_colunas[0], width=50, anchor=CENTER)
        tv.column(self.tv_colunas[1], width=120, anchor=CENTER)
        tv.column(self.tv_colunas[2], width=250, anchor=CENTER)
        tv.column(self.tv_colunas[3], width=80)
        tv.column(self.tv_colunas[4], width=80)
        tv.column(self.tv_colunas[5], width=80)
        tv.heading(self.tv_colunas[0], text='ID', anchor=CENTER)
        tv.heading(self.tv_colunas[1], text='PROFISSIONAL')
        tv.heading(self.tv_colunas[2], text='SERVIÇOS')
        tv.heading(self.tv_colunas[3], text='FORMA PGMT')
        tv.heading(self.tv_colunas[4], text='VALOR')
        tv.heading(self.tv_colunas[5], text='HORA')

        self.root.update()
        print()

        vs=CTkScrollbar(self.root, command=tv.yview)
        tv.configure(yscrollcommand=vs.set)
        x = round((tv.winfo_rootx() + tv.winfo_width())* 1)
        vs.place(x=x, rely=0.2)

        self.root.bind('<Right>', lambda event: move_to_next_prof())
        self.root.bind('<Left>', lambda event: move_to_previous_prof())
        self.root.bind('<Down>', lambda event: form_pgmt_up())
        self.root.bind('<Up>', lambda event: form_pgmt_down())
        self.root.bind('<+>', lambda event: tb_0_fm_0_wg_5.invoke())
        self.root.bind('<Return>', lambda event: tb_0_fm_0_wg_11.invoke())

        def move_to_next_prof(self):
            pass

        def move_to_previous_prof(self):
            pass

        def form_pgmt_up(self):
            pass

        def form_pgmt_down(self):
            pass

        def registrarEntrada(self):
            pass

        def abrir_tl_0(self):
            pass

        def abrir_tl_1(self):
            pass

        def abrir_tl_2(self):
            pass

        def add_forma_pgmt_2(self):
            pass
    