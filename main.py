#Registro de datos en MYSQL con Python
#-----@Wilson11-----#

from cProfile import label
from tkinter import Entry, Label, Frame, Tk, Button, font, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END,PhotoImage

from numpy import pad
class Registro(Frame):

    def __init__(self,master,*args, **Kwargs):
        super().__init__(master,*args, **Kwargs)

        self.frame1=Frame(master)
        self.frame1.grid(columnspan=2,column=0,row=0)

        self.frame2=Frame(master,bg='#1d2127')
        self.frame2.grid(column=0,row=1)

        self.frame3=Frame(master)
        self.frame3.grid(rowspan=2,column=1,row=1)

        self.frame4=Frame(master,bg='black')
        self.frame4.grid(column=0,row=2)
        self.frame4.config(bg='#1d2127')

        self.codigo=StringVar()
        self.nombre=StringVar()
        self.modelo=StringVar()
        self.precio=StringVar()
        self.cantidad=StringVar()
        self.buscar=StringVar()

        self.wietgs()

    def wietgs(self):
        
        Label(self.frame1, text='Resgistro de Datos',bg='#1d2127',fg='#98c379',font=('Overpass Mono',12,'bold')).grid(column=0,row=0)

        Label(self.frame2, text='Agregar Datos',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(columnspan=2,column=0,row=0,pady=5)
        Label(self.frame2, text='Codigo',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=1,pady=15)
        Label(self.frame2, text='Nombre',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=2,pady=15)
        Label(self.frame2, text='Modelo',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame2, text='Precio',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=4,pady=15)
        Label(self.frame2, text='Cantidad',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=5,pady=15)

        Entry(self.frame2,textvariable=self.codigo,font=('Overpass Mono',12)).grid(column=1,row=1,padx=5)
        Entry(self.frame2,textvariable=self.nombre,font=('Overpass Mono',12,)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.modelo,font=('Overpass Mono',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.precio,font=('Overpass Mono',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.cantidad,font=('Overpass Mono',12)).grid(column=1,row=5)

        Label(self.frame4, text='Control',fg='#98c379',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(columnspan=3,column=0,row=0,pady=2,padx=4)

        Button(self.frame4,text='Registrar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='white').grid(column=0,row=1,pady=10,padx=4)
        Button(self.frame4,text='Limpiar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='white').grid(column=1,row=1,padx=4)
        Button(self.frame4,text='Eliminar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='white').grid(column=2,row=1,padx=4)
        Button(self.frame4,text='Buscar por ID',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='white').grid(columnspan=2,column=1,row=2,pady=2)
        
        Entry(self.frame4,textvariable=self.buscar,font=('Overpass Mono',12),width=10).grid(column=0,row=2,pady=10,padx=4)

        Button(self.frame4,text='Mostrar Datos',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='white').grid(columnspan=3,column=0,row=3,pady=2)

        self.tabla=ttk.Treeview(self.frame3,height=21)
        self.tabla.grid(column=0,row=0)

        ladox = Scrollbar(self.frame3,orient=HORIZONTAL,command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(column=1,row=0,sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Nombre','Modelo','Precio','Cantidad')

        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Nombre',minwidth=100,width=130,anchor='center')
        self.tabla.column('Modelo',minwidth=100,width=130,anchor='center')
        self.tabla.column('Precio',minwidth=100,width=130,anchor='center')
        self.tabla.column('Cantidad',minwidth=100,width=130,anchor='center')

        self.tabla.heading('#0',text='Codigo',anchor='center')
        self.tabla.heading('Nombre',text='Nombre',anchor='center')
        self.tabla.heading('Modelo',text='Modelo',anchor='center')
        self.tabla.heading('Precio',text='Precio',anchor='center')
        self.tabla.heading('Cantidad',text='Cantidad',anchor='center')

        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure('.',font=('Overpass Mono',12,'bold'),fg='black')
        estilo.configure('Treeview',font=('Overpass Mono',12,'bold'),fg='black',bg='white')
        estilo.map('Treeview',bg=[('selected','green2')],fg=[('selected','black')])
        self.tabla.bind('<<TreeviewSelect>>')




        








def main():
    ventana = Tk()
    ventana.wm_title('Registro de Datos')
    ventana.config(bg='#1d2127')
    ventana.geometry('900x500')
    ventana.resizable(0,0)
    ventana.tk.call('wm', 'iconphoto', ventana, PhotoImage(file='./img/registro.png'))
    app=Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()


