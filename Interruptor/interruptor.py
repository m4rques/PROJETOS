# Importação das bibliotecas
from tkinter import *
from tkinter import ttk
import serial


# Cores
branco = '#FFFFFF'
preto = '#000000'
verde = '#008000'
vermelho = '#FF0000'

# Criação da janela principal
interruptor = Tk()
interruptor.title("Interruptor")
interruptor.geometry('350x200')
interruptor.configure(background=branco)
interruptor.resizable(width= FALSE, height= FALSE)
estilo = ttk.Style(interruptor)
estilo.theme_use('clam')

#lincando com o arduino

try:
    arduino = serial.Serial("COM4", 9600, timeout=1)
    print("Arduino conectado com sucesso!")
except:
    print("Não foi possível realizar a conexão.")
    pass

# Funcionalidades
def acender_lampada():
    arduino.write('Ligar Lampada' .encode())
    print("Arduino foi notificado para ligar a lampada.")


def apagar_lampada():
    arduino.write('Desligar Lampada' .encode())
    print("Arduino foi notificado para desligar a lampada.")


def ligar_ventilador():
    arduino.write('Ligar Ventilador' .encode())
    print("Arduino foi notificado para ligar o ventilador.")


def desligar_ventilador():
    arduino.write('Desligar Ventilador' .encode())
    print("Arduino foi notificado para deligar o ventilador.")


def trancar_fechadura():
    arduino.write('Trancar Fechadura' .encode())    
    print("Arduino foi notificado para trancar fechadura.")


def destrancar_fechadura():
    arduino.write('Destrancar Fechadura' .encode())
    print("Arduino foi notificado para destrancar fechadura.")

# Criação do cabeçalho
cabeçalho = Frame(interruptor, width= 350, height= 50, bg = preto, relief='flat')
cabeçalho.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
cabeçalho_nome = Label(cabeçalho, text='Interruptor', height=1, anchor=NE, font= ('Verdana 17 bold'), bg= preto, fg= branco)
cabeçalho_nome.place(x=90, y=5)

# Criação e configuração butões da lamanda
lampada = Label(text='LAMPADA', height=1, anchor= CENTER, font=('Ivy 10 bold'), bg=preto,fg= branco)
lampada.place(x=30, y=70)
lampada_ligar = Button(command=acender_lampada,text='LIGAR', height=1, bg= verde, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
lampada_ligar.place(x= 40, y= 100)
lampada_desligar = Button(command=apagar_lampada,text='DESLIGAR', height=1, bg= vermelho, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
lampada_desligar.place(x= 30, y= 130)

# Criação e configuração  butões do ventilador
ventilador = Label(text='VENTILADOR', height=1, anchor= CENTER, font=('Ivy 10 bold'), bg=preto,fg= branco)
ventilador.place(x=125, y=70)
ventilador_ligar = Button(command=ligar_ventilador,text='LIGAR', height=1, bg= verde, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
ventilador_ligar.place(x= 145, y= 100)
ventilador_desligar = Button(command=desligar_ventilador,text='DESLIGAR', height=1, bg= vermelho, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
ventilador_desligar.place(x= 135, y=130)

# Criação e configuração butões da fechadura
fechadura = Label(text='FECHADURA', height=1, anchor= CENTER, font=('Ivy 10 bold'), bg=preto,fg= branco)
fechadura.place(x=240, y=70)
fechadura_trancar = Button(command=trancar_fechadura,text='TRANCAR', height=1, bg= verde, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
fechadura_trancar.place(x= 250, y= 100)
fechadura_destrancar =  Button(command=destrancar_fechadura,text='DESLIGAR', height=1, bg= vermelho, fg = preto, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
fechadura_destrancar.place(x= 250, y= 130)

interruptor.mainloop()

#Codigo do arduino

#// C++ code
#//
#int lampada = 1;
#int ventilador = 2;
#int fechadura = 3;


#void setup()
#{
#  pinMode(lampada, OUTPUT);
#  pinMode(ventilador, OUTPUT);
#  pinMode(fechadura, OUTPUT);
#  Serial.begin(9600);
#}

#void loop()
#{
#  char c = Serial.read();
#  
#  if (c == 'Ligar Lampada'){
#  	digitalWrite (lampada, HIGH);
#  }else if ( c == 'Desligar Lampada'){
#  	digitalWrite (lampada, LOW);
#  } else if (c == 'Ligar Ventilador'){
#  	digitalWrite (ventilador,HIGH);
#  }	else if (c == 'Desligar Ventilador'){
#  	digitalWrite (ventilador, LOW);
#  }	else if (c == 'Trancar Fechadura'){
#  	digitalWrite (fechadura, HIGH);
#  }else if (c == 'Destrancar Fechadura'){
#  	digitalWrite (fechadura, LOW);
#  }
 # 
 # delay(10);
#}