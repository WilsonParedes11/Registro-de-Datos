#Registro de datos en MYSQL con Python
#-----@Wilson11-----#


from tkinter import Entry, Label, Frame, Tk, Button, font, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END,PhotoImage,messagebox


from numpy import pad

from conexion import registro_datos
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
        self.telefono=StringVar()
        self.correo=StringVar()
        self.direccion=StringVar()
        self.buscar=StringVar()

        self.base_datos=registro_datos()
        self.wietgs()

    def wietgs(self):

        self.imagen_contacto=PhotoImage( file=r'./img/contacto.png')
        
        Label(self.frame1, text='Registro de Contactos',bg='#1d2127',fg='#98c379',font=('Overpass Mono',12,'bold')).grid(column=0,row=0)
        
        Label(self.frame2,image=self.imagen_contacto,bg='#1d2127',width='100',height='100',anchor='center').grid(column=0,row=1,padx=5)
        Label(self.frame2, text='Agregar Contacto',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(columnspan=2,column=1,row=1,pady=5)
        Label(self.frame2, text='Codigo',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=2,pady=15)
        Label(self.frame2, text='Nombre',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame2, text='Telefono',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=4,pady=15)
        Label(self.frame2, text='Correo',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=5,pady=15)
        Label(self.frame2, text='Direccion',fg='#61afef',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(column=0,row=6,pady=15)

        Entry(self.frame2,textvariable=self.codigo,font=('Overpass Mono',12)).grid(column=1,row=2,padx=5)
        Entry(self.frame2,textvariable=self.nombre,font=('Overpass Mono',12,)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.telefono,font=('Overpass Mono',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.correo,font=('Overpass Mono',12)).grid(column=1,row=5)
        Entry(self.frame2,textvariable=self.direccion,font=('Overpass Mono',12)).grid(column=1,row=6)

        Label(self.frame4, text='Control',fg='#98c379',bg='#1d2127',font=('Overpass Mono',12,'bold')).grid(columnspan=3,column=0,row=0,pady=2,padx=4)

        Button(self.frame4,text='Registrar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.agregar_datos).grid(column=0,row=1,pady=10,padx=4)
        Button(self.frame4,text='Actualiza',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.actualizar_tabla).grid(column=1,row=1,padx=4)
        Button(self.frame4,text='Eliminar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.eliminar_fila).grid(column=2,row=1,padx=4)
        Button(self.frame4,text='Buscar por Nombre',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.buscar_nombre).grid(columnspan=2,column=1,row=2,pady=2)
        
        Entry(self.frame4,textvariable=self.buscar,font=('Overpass Mono',12),width=10).grid(column=0,row=2,pady=10,padx=4)
        Button(self.frame4,text='Limpiar',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.limpiar_datos).grid(column=0,row=3)
        Button(self.frame4,text='Mostrar Datos',font=('Overpass Mono',12,'bold'),bg='#282c34',fg='#61afef',command=self.mostrar_datos).grid(columnspan=3,column=1,row=3,pady=2)

        self.tabla=ttk.Treeview(self.frame3,height=21)
        self.tabla.grid(column=0,row=0)

        ladox = Scrollbar(self.frame3,orient=HORIZONTAL,command=self.tabla.xview)
        ladox.grid(column=0,row=1,sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(column=1,row=0,sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set,yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Nombre','Telefono','Correo','Direccion')

        self.tabla.column('#0',minwidth=100,width=120,anchor='center')
        self.tabla.column('Nombre',minwidth=100,width=130,anchor='center')
        self.tabla.column('Telefono',minwidth=100,width=130,anchor='center')
        self.tabla.column('Correo',minwidth=100,width=130,anchor='center')
        self.tabla.column('Direccion',minwidth=100,width=130,anchor='center')

        self.tabla.heading('#0',text='Codigo',anchor='center')
        self.tabla.heading('Nombre',text='Nombre',anchor='center')
        self.tabla.heading('Telefono',text='Telefono',anchor='center')
        self.tabla.heading('Correo',text='Correo',anchor='center')
        self.tabla.heading('Direccion',text='Direccion',anchor='center')

        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure('.',font=('Overpass Mono',12,'bold'),foreground='#98c379')
        estilo.configure('Treeview',font=('Overpass Mono',12,'bold'),foreground='black',background='white')
        estilo.map('Treeview',background=[('selected','#61afef')],foreground=[('selected','black')])
        self.tabla.bind('<<TreeviewSelect>>',self.obtener_fila)

    def agregar_datos(self):

        self.tabla.get_children()
        codigo=self.codigo.get()
        nombre=self.nombre.get()
        telefono=self.telefono.get()
        correo=self.correo.get()
        direccion=self.direccion.get()

        datos=(nombre,telefono,correo,direccion)

        if codigo and nombre and telefono and correo and direccion !='':
            self.tabla.insert('',0,text=codigo,values=datos)
            self.base_datos.insertar_contacto(codigo,nombre,telefono,correo,direccion)

        messagebox.showinfo('!Atencion','Contacto Registrado Correctamente.')

    def actualizar_tabla(self):
        codigo=self.codigo.get()
        nombre=self.nombre.get()
        telefono=self.telefono.get()
        correo=self.correo.get()
        direccion=self.direccion.get()
        self.base_datos.actualizar()


    def limpiar_datos(self):

        self.tabla.delete(*self.tabla.get_children())

        self.codigo.set('')
        self.nombre.set('')
        self.telefono.set('')
        self.correo.set('')
        self.direccion.set('')
        self.buscar.set('')

    def buscar_nombre(self):

        nombre_contacto=self.buscar.get()
        nombre_contacto=str("'" + nombre_contacto + "'")
        nombre_buscado=self.base_datos.busca_contacto(nombre_contacto)
        self.tabla.delete(*self.tabla.get_children())
        i=-1
        for dato in nombre_buscado:
            i=i+1
            self.tabla.insert('',i, text=nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])
    
    def mostrar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        registro=self.base_datos.mostrar_contacto()
        i=-1
        for dato in registro:
            i=i+1
            self.tabla.insert('',i, text=registro[i][1:2], values=registro[i][2:6])

    def eliminar_fila(self):

        fila=self.tabla.selection()
        if len(fila) !=0:
            self.tabla.delete(fila)
            nombre=("'"+ str(self.nombre_borar) + "'")
            self.base_datos.elimina_contacto(nombre)

        messagebox.showinfo('!Atencion','Contacto Eliminado Correctamente.')
    
    def obtener_fila(self, event):

        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]

    

 
        
def main():
    ventana = Tk()
    ventana.wm_title('Registro de Datos')
    ventana.config(bg='#1d2127')
    ventana.geometry('980x575')
    ventana.resizable(0,0)
    ventana.tk.call('wm', 'iconphoto', ventana, PhotoImage(file='./img/registro.png'))
    app=Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()


