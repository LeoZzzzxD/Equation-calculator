from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook 
import main_alg as m
import binary as b
import matplotlib.pyplot as plt
import show_graphic as show
from thread import *
import asyncio
import numpy as np

FUNCTION_LENGTH = 50

class App(Tk):

        __flag__ = True
        __flag1__ = False
         
        def __init__(self):
            super().__init__()
            self.geometry("320x360+450+180")
            self.resizable(width=False, height=False)
            self.title("Equation calculator")
            self.iconbitmap('calc_ico.ico')
            self.func()

        def func(self):
            self.notes = Notebook(self)
            self.notes.pack(pady=10, expand=True)
            self.frame1 = Frame(self.notes, width=400, height=380)
            self.frame2 = Frame(self.notes, width=400, height=380)
            self.frame3 = Frame(self.notes, width=400, height=380)
            self.notes.add(self.frame1, text="get solution")
            self.notes.add(self.frame2, text="show function")
            self.notes.add(self.frame3, text="how to use")
            self.aioloop = starting_process()
            self.release_info()          
            self.show_graphs()
            self.doc()
            self.notes.bind('<ButtonRelease-1>', self.hadler) 
            self.mainloop()       
       
        def release_info(self):
            
            self.text = StringVar()
            self.text_ = DoubleVar()
            self.text__ = IntVar()
            self.field_ = Entry(self.frame1, textvariable=self.text, width=20)
            self.field__ = Entry(self.frame1, textvariable=self.text_, width=20)
            self.show_ = Label(self.frame1, text="input some function:")
            self.show__ = Label(self.frame1, text="accuracy:")
            self.press = Button(self.frame1, text="get result", command=lambda: asyncio.run_coroutine_threadsafe(self.do_this(), self.aioloop), width=11)
            self.field_yo = Entry(self.frame1, textvariable=self.text__, width=20)
            self.power = Label(self.frame1, text="©Powered by LeoZzzz")
            self.show_yo = Label(self.frame1, text="init value:")
            self.show_inf_ = Label(self.frame1, text="working variable must be x")
            self.show_yo.place(x=10,y=20)
            self.field_yo.place(x=130, y=20)
            self.field_.place(x=130, y=80)
            self.show_.place(x=10, y=80)
            self.show__.place(x=10, y=50)
            self.field__.place(x=130, y=50)
            self.show_inf_.place(x=10, y=110)
            self.power.place(x=94, y=280)
            self.press.place(x=113, y=150)
        
        async def do_this(self):
          
          try:  
              if len(self.text.get()) <= FUNCTION_LENGTH:    
                  b.bin_first_in(self.text__.get(), self.text_.get(), self.text.get()) 
                  data = b.bin_first_out() 
                  self.x, self.prepared_func = m.alg(data[0], data[1], data[2])
                  if self.x == "error_":
                      messagebox.showerror("Alert", "Проверьте правильность введенных данных!")
                      #self.field__.delete("0", END)
                      #self.field_.delete("0", END)
                      #self.field_yo.delete("0", END)
                      self.__flag1__ = False
                      
                  elif self.x == "error":
                      messagebox.showerror("Alert", "Уравнение не сходится!")
                      #self.field__.delete("0", END)
                      #self.field_.delete("0", END)
                      #self.field_yo.delete("0", END)
                      self.__flag1__ = False
                            
                  else:
                      messagebox.showinfo("Message", f"Congratulations! You have the result: x={'{:.4f}'.format(self.x)}, more data in func_data.txt")
                      self.text_of_func = self.text.get()
                      self.field__.delete("0", END)
                      self.field_.delete("0", END)
                      self.field_yo.delete("0", END)
                      self.__flag1__ = True
              else:
                  messagebox.showerror("Alert", "Слишком длинное выражение!")
                  #self.field__.delete("0", END)
                  #self.field_.delete("0", END)
                  #self.field_yo.delete("0", END)
                  self.__flag1__ = False
          
          except TypeError:
                messagebox.showerror("Alert", "Попробуйте изменить входные данные...")
                #self.field__.delete("0", END)
                #self.field_.delete("0", END)
                #self.field_yo.delete("0", END)
                self.__flag1__ = False
                
          except Exception:
              messagebox.showerror("Alert", "Что то пошло не так...") 
              #self.field__.delete("0", END)
              #self.field_.delete("0", END)
              #self.field_yo.delete("0", END)
              self.__flag1__ = False
          
        def show_graphs(self):
                
                self.tumb = IntVar()
                self.tumb1 = IntVar()
                self.color = 'g'
                self.tumb.set(1)
                self.tumb1.set(1)
                self.value_list_x = list()
                self.value_list_y = list()
                self.way_to = StringVar()
                self.step = DoubleVar()
                self.but = Button(self.frame2, text="accept", command=self.draw_it)
                self.t = Label(self.frame2, text="add interval to format #:#")
                self.e = Entry(self.frame2, textvariable=self.way_to,width=12)
                self.t_ = Label(self.frame2, text="current func:")
                self.lab = Label(self.frame2, text="label:")
                self.p = Label(self.frame2, text="step:")
                self.e_ = Entry(self.frame2, textvariable=self.step, width=12)
                self.color_sw1 = Radiobutton(self.frame2, text="green", value=1, variable=self.tumb, command=self.checking_c)
                self.color_sw2 = Radiobutton(self.frame2, text="red", value=2, variable=self.tumb, command=self.checking_c)
                self.color_sw3 = Radiobutton(self.frame2, text="yellow", value=3, variable=self.tumb, command=self.checking_c)
                self.label1 =  Radiobutton(self.frame2, text="yes", value=1, variable=self.tumb1, command=self.checking_l)
                self.label2 =  Radiobutton(self.frame2, text="no", value=2, variable=self.tumb1, command=self.checking_l)
                self.t.place(x=10, y=20)
                self.t_.place(x=10, y=80)
                self.e.place(x=150, y=20)
                self.but.place(x=10, y=180)
                self.p.place(x=10, y=50)
                self.e_.place(x=45, y=50)
                self.color_sw1.place(x=10, y=110)
                self.color_sw2.place(x=10, y=130)
                self.color_sw3.place(x=10, y=150)
                self.lab.place(x=125, y=50)
                self.label1.place(x=160, y=50)
                self.label2.place(x=205, y=50)   
                   
                  
        def checking_c(self):
            value = self.tumb.get()
            if value == 1:
                self.color = 'g'
            elif value == 2:
                self.color = 'r'
            elif value == 3:
                self.color = 'y'
        
        def checking_l(self):
            value = self.tumb1.get()
            if value == 1:
                self.__flag__ = True
            elif value == 2:
                self.__flag__ = False
                
        def hadler(self, event):
        
            try:
                if event and self.__flag1__:
                    self.t_1 = Label(self.frame2, text=self.text_of_func)
                    self.t_1.place(x=85, y=80)
                
                plt.close(self.obj)
                #self.graph.get_tk_widget().destroy()
                self.e.delete("0", END)
                self.e_.delete("0", END)
                
            except:
                plugy = "plug"

        def draw_it(self):
            if self.__flag1__ and self.way_to.get() and self.step.get():
                try:
                    np.seterr(all='raise') 
                    self.value_list_x = list()
                    self.value_list_y = list()
                    value =  int(self.way_to.get().split(':')[1])
                    start_value = int(self.way_to.get().split(':')[0])
                    b.bin_second_in(start_value, value, self.step.get(), self.__flag__, self.color)
                    data_ = b.bin_second_out()
                    while  data_[0] <= data_[1]:
                       self.value_list_x.append(data_[0])
                       self.value_list_y.append(self.prepared_func(data_[0]))
                       data_[0] = data_[0] + data_[2]
               
                    try:
                        if self.obj: #and self.graph:
                            plt.close(self.obj)
                            #self.graph.get_tk_widget().destroy()
                    except:
                        pass
                    
                    self.obj = show.fig(self.value_list_x, self.value_list_y, data_[4], data_[3], self.x, self.prepared_func)
                    self.obj.show()
                    #self.graph = FigureCanvasTkAgg(self.obj, self.frame2)
                    #self.graph.get_tk_widget().place(x=75,y=110,width=260,height=200)
                    #self.graph.draw()
                    
                except FloatingPointError:
                    messagebox.showerror("Alert", "Недопустимый интервал для данной функции") 
                    self.e.delete("0", END)
                    self.e_.delete("0", END)
                    
                except Exception:
                    messagebox.showerror("Alert", "Некорректные данные в форме")
                    self.e.delete("0", END)
                    self.e_.delete("0", END)
        
        def doc(self):
            self.header = Label(self.frame3, text="допустимые математические функции:")   
            self.f = Label(self.frame3, text="cos(x) - функция косинуса")  
            self.f1 = Label(self.frame3, text="sin(x) - функция синуса")  
            self.f2 = Label(self.frame3, text="pow(x, 2) - возведение в степень \nили привычным умножением", justify=LEFT)  
            self.f3 = Label(self.frame3, text="tan(x) - функция тангенса")  
            self.f4 = Label(self.frame3, text="arcsin(x) - функция арксинуса")  
            self.f5 = Label(self.frame3, text="arccos(x) - функция арккосинуса") 
            self.f6 = Label(self.frame3, text="arctan(x) - функция арктангенса")   
            self.f7 = Label(self.frame3, text="log(x) - натуральный логарифм")  
            self.f8 = Label(self.frame3, text="log10(x) - десятичный логарифм") 
            self.f9 = Label(self.frame3, text="log(4) / log(x) - логарифм с переменным основанием \n(на основе свойства log)", justify=LEFT) 
            self.f10 = Label(self.frame3, text="sqrt(x) - квадратный корень") 
            
            self.header.place(x=10, y=20)
            self.f.place(x=10, y=40)
            self.f1.place(x=10, y=60)
            self.f2.place(x=10, y=80)
            self.f3.place(x=10, y=115)
            self.f4.place(x=10, y=135)
            self.f5.place(x=10, y=155)
            self.f6.place(x=10, y=175)
            self.f7.place(x=10, y=195)
            self.f8.place(x=10, y=215)
            self.f9.place(x=10, y=235)
            self.f10.place(x=10, y=270)
         
                    
if __name__ == "__main__":        
   App() 

   
   

