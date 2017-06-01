import numpy as np
from threading import Thread
from sympy import *
import tkinter as tk
from sympy import plot

class SloppyCalc():
    
    def __init__(self, master):
        self.master = master
        self.master.minsize(width=350, height=500)
        self.master.maxsize(width=350, height=500)
        self.master.title('Sloppy Calculator')
        
        
        self.y1 = tk.Entry()
        self.y1.grid(row = 0, columnspan = 2, ipadx = 60, padx = 20)
        self.b = 4
        self.a = -4
        
        self.y2 = tk.Entry()
        self.y2.grid(row = 1, columnspan = 2, ipadx = 60, padx = 20)
        
        self.output_label = tk.Label(self.master, text="Output:")
        self.output_label.grid(row=2, column=0, sticky='w', padx = 20)
        
        self.output = tk.Label(self.master, text="")
        self.output.grid(row=3, column=0, sticky='w', padx = 20, pady = 20)
        self.output.config(font=("Arial", 20))
        
        self.submit = tk.Button(self.master, text=" = ", command=self.submit_calculate)
        self.submit.grid(row=4, column=0, sticky='w', padx = 20)
        
        self.submit = tk.Button(self.master, text="Limit", command=self.submit_limit)
        self.submit.grid(row=4, column=1, sticky='w', padx = 20)
        
        self.submit = tk.Button(self.master, text="Anti-Derivative", command=self.submit_antiderivative)
        self.submit.grid(row=5, column=0, sticky='w', padx = 20)
        
        self.submit = tk.Button(self.master, text="Derivative", command=self.submit_derivative)
        self.submit.grid(row=5, column=1, sticky='w', padx = 20)
        
        self.area_volume_label = tk.Label(self.master, text="Area and Volume:")
        self.area_volume_label.grid(row=6, column=0, sticky='w', padx = 20)
        
        self.a = tk.Entry(text="a")
        self.a.grid(row = 7, columnspan = 1, padx = 20)
        
        self.b = tk.Entry(text="b")
        self.b.grid(row = 8, columnspan = 1, padx = 20)
        
        self.submit = tk.Button(self.master, text="Area", command=self.submit_area)
        self.submit.grid(row=9, column=0, sticky='w', padx = 20)
        
        # from threading import Thread
        self.submit = tk.Button(self.master, text="Launch Graph", command=self.start_graph)
        self.submit.grid(row=10, column = 0, columnspan = 1, sticky='w', padx = 20)
        
        
        self.master.mainloop()
    
    
    def submit_limit(self):
        # submit something
        y1 = self.y1.get()
        to = self.y2.get()
        print('Calculating the limit of', y1)
        self.output.config(text=self.find_limit(to, y1))
    
    
    def submit_derivative(self):
        # submit something
        print('Calculating the derivative of', self.get_input())
        self.output.config(text=self.get_derivative(self.y1.get()))
    
    
    def submit_antiderivative(self):
        # submit something
        print('Calculating the anti-derivative of', self.get_input())
        self.output.config(text=self.get_antiderivative(self.y1.get()))
    
    
    def submit_area(self):
        # submit something
        print('Calculating the area of', self.y1.get(), 'and', self.y2.get())
        y1 = self.y1.get()
        y2 = self.y2.get()
        a = float(self.a.get())
        b = float(self.b.get())
        area = self.find_area(a, b, y1, y2)
        
        self.output.config(text=area)
    
    
    def submit_calculate(self):
        # submit something
        print('Calculating', self.get_input())
        x, y = symbols('x, y')
        print(self.y1.get())
        fx = sympify(self.y1.get())
        at = float(self.y2.get())
        print(fx, x)
        answer = fx.subs(x, at)
        self.output.config(text=str(answer))
    
    
    def show_graph(self):
        import matplotlib.pyplot
        print('Something Happened.')
        # submit something
        x = symbols('x')
        f1 = sympify(self.y1.get())
        f2 = sympify(self.y2.get())
        symplot = plot(f1, f2, (x, -5, 10))
        symplot.show(block=False)
        
        return 'Stopped'
        
        
    def start_graph(self):
        self.show_graph()
    
    
    def get_input(self):
        return self.y1.get()
        
    
    def find_area(self, a, b, top, bottom):
        top = sympify(top)
        bottom = sympify(bottom)
        x, y = symbols('x, y')
        increments = (b - a) / 1000
        area = 0
    
        incrementNumbers = np.arange(a, b, increments)
        for i in incrementNumbers:
            height1 = top.evalf(subs={x: i}) - bottom.evalf(subs={x: i})
            height2 = top.evalf(subs={x: i + increments}) - bottom.evalf(subs={x: i + increments})
            width = increments
        
            # Trapezoidal Sum
            # a = w * ((h1 + h2) / 2)
            area += width * ((height1 + height2) / 2.0)
        
        return area
    

    def find_limit(self, to, function):
        x, y = symbols('x, y')
        of = sympify(function)
        lim = limit(of, x, to)
            
        return lim
    

    def get_derivative(self, function):
        x, y = symbols('x, y')
        fx = sympify(function)
        derivative = diff(fx, x)
    
        return derivative
    

    def get_antiderivative(self, function):
        fx = sympify(function)
        x, y = symbols('x, y')
        antiderivative = integrate(fx, x)
        
        return antiderivative
    

    def eval_defintegral(self, a, b, function):
        fx = sympify(function)
        x, y = symbols('x, y')
    
        defintegral = integrate(fx, (x, a, b))
    
        return defintegral
        

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    
    calc = SloppyCalc(root)
    calc.get_input()
    root.mainloop()
    
    

if __name__ == '__main__':
    main()
