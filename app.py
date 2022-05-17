import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from click import command
import pandas as pd
from tkinter import ttk
from PIL import Image, ImageTk
from plotdata import plot_chart
from stats import stats_columns
from model import model_result
from tkinter.messagebox import showwarning


class StartPage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        main_title = tk.Label(
            self, text="BREAST CANCER WISCONSIN", bg="sky blue", font=(50))
        menu = tk.Label(self, text="MENU", font=(20))
        btn1 = tk.Button(self, text="Statistic", font=(50),
                         command=lambda: appController.showPage(StatsPage))
        btn2 = tk.Button(self, text="Visualize", font=(50),
                         command=lambda: appController.showPage(VisualizePage))
        btn3 = tk.Button(self, text="Diagnosis", font=(50),
                         command=lambda: appController.showPage(ModelPage))

        main_title.place(x=400, y=120)

        menu.place(x=510, y=200)
        btn1.place(x=500, y=260)
        btn2.place(x=497, y=320)
        btn3.place(x=496, y=380)


class VisualizePage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        visual_title = tk.Label(
            self, text="Choose attribute(s):", font=(25), bg="sky blue")
        visual_title.place(x=20, y=20)

        var1 = IntVar(self)
        var2 = IntVar(self)
        var3 = IntVar(self)
        var4 = IntVar(self)
        var5 = IntVar(self)
        var6 = IntVar(self)
        var7 = IntVar(self)
        var8 = IntVar(self)
        var9 = IntVar(self)
        var10 = IntVar(self)
        var11 = IntVar(self)
        var12 = IntVar(self)
        var13 = IntVar(self)
        var14 = IntVar(self)
        var15 = IntVar(self)
        var16 = IntVar(self)
        var17 = IntVar(self)
        var18 = IntVar(self)
        var19 = IntVar(self)
        var20 = IntVar(self)
        var21 = IntVar(self)
        var22 = IntVar(self)
        var23 = IntVar(self)
        var24 = IntVar(self)
        var25 = IntVar(self)
        var26 = IntVar(self)
        var27 = IntVar(self)
        var28 = IntVar(self)
        var29 = IntVar(self)
        var30 = IntVar(self)

        c1 = Checkbutton(
            self, text="radius_mean", variable=var1)
        c2 = Checkbutton(
            self, text="texture_mean", variable=var2)
        c3 = Checkbutton(
            self, text="perimeter_mean", variable=var3)
        c4 = Checkbutton(
            self, text="area_mean", variable=var4)
        c5 = Checkbutton(
            self, text="smoothness_mean", variable=var5)
        c6 = Checkbutton(
            self, text="compactness_mean", variable=var6)
        c7 = Checkbutton(
            self, text="concavity_mean", variable=var7)
        c8 = Checkbutton(
            self, text="concave points_mean", variable=var8)
        c9 = Checkbutton(
            self, text="symmetry_mean", variable=var9)
        c10 = Checkbutton(
            self, text="fractal_dimension_mean", variable=var10)
        c11 = Checkbutton(
            self, text="radius_se", variable=var11)
        c12 = Checkbutton(
            self, text="texture_se", variable=var12)
        c13 = Checkbutton(
            self, text="perimeter_se", variable=var13)
        c14 = Checkbutton(
            self, text="area_se", variable=var14)
        c15 = Checkbutton(
            self, text="smoothness_se", variable=var15)
        c16 = Checkbutton(
            self, text="compactness_se", variable=var16)
        c17 = Checkbutton(
            self, text="concavity_se", variable=var17)
        c18 = Checkbutton(
            self, text="concave points_se", variable=var18)
        c19 = Checkbutton(
            self, text="symmetry_se", variable=var19)
        c20 = Checkbutton(
            self, text="fractal_dimension_se", variable=var20)
        c21 = Checkbutton(
            self, text="radius_worst", variable=var21)
        c22 = Checkbutton(
            self, text="texture_worst", variable=var22)
        c23 = Checkbutton(
            self, text="perimeter_worst", variable=var23)
        c24 = Checkbutton(
            self, text="area_worst", variable=var24)
        c25 = Checkbutton(
            self, text="smoothness_worst", variable=var25)
        c26 = Checkbutton(
            self, text="compactness_worst", variable=var26)
        c27 = Checkbutton(
            self, text="concavity_worst", variable=var27)
        c28 = Checkbutton(
            self, text="concave points_worst", variable=var28)
        c29 = Checkbutton(
            self, text="symmetry_worst", variable=var29)
        c30 = Checkbutton(
            self, text="fractal_dimension_worst", variable=var30)

        c1.place(x=20, y=50)
        c2.place(x=20, y=75)
        c3.place(x=20, y=100)
        c4.place(x=20, y=125)
        c5.place(x=20, y=150)
        c6.place(x=20, y=175)
        c7.place(x=20, y=200)
        c8.place(x=220, y=50)
        c9.place(x=220, y=75)
        c10.place(x=220, y=100)
        c11.place(x=220, y=125)
        c12.place(x=220, y=150)
        c13.place(x=220, y=175)
        c14.place(x=220, y=200)
        c15.place(x=420, y=50)
        c16.place(x=420, y=75)
        c17.place(x=420, y=100)
        c18.place(x=420, y=125)
        c19.place(x=420, y=150)
        c20.place(x=420, y=175)
        c21.place(x=420, y=200)
        c22.place(x=620, y=50)
        c23.place(x=620, y=75)
        c24.place(x=620, y=100)
        c25.place(x=620, y=125)
        c26.place(x=620, y=150)
        c27.place(x=620, y=175)
        c28.place(x=620, y=200)
        c29.place(x=820, y=50)
        c30.place(x=820, y=75)

        def show_graph():
            arr = []
            if var1.get() == 1:
                arr.append("radius_mean")
            if var2.get() == 1:
                arr.append("texture_mean")
            if var3.get() == 1:
                arr.append("perimeter_mean")
            if var4.get() == 1:
                arr.append("area_mean")
            if var5.get() == 1:
                arr.append("smoothness_mean")
            if var6.get() == 1:
                arr.append("compactness_mean")
            if var7.get() == 1:
                arr.append("concavity_mean")
            if var8.get() == 1:
                arr.append("concave points_mean")
            if var9.get() == 1:
                arr.append("symmetry_mean")
            if var10.get() == 1:
                arr.append("fractal_dimension_mean")
            if var11.get() == 1:
                arr.append("radius_se")
            if var12.get() == 1:
                arr.append("texture_se")
            if var13.get() == 1:
                arr.append("perimeter_se")
            if var14.get() == 1:
                arr.append("area_se")
            if var15.get() == 1:
                arr.append("smoothness_se")
            if var16.get() == 1:
                arr.append("compactness_se")
            if var17.get() == 1:
                arr.append("concavity_se")
            if var18.get() == 1:
                arr.append("concave points_se")
            if var19.get() == 1:
                arr.append("symmetry_se")
            if var20.get() == 1:
                arr.append("fractal_dimension_se")
            if var21.get() == 1:
                arr.append("radius_worst")
            if var22.get() == 1:
                arr.append("texture_worst")
            if var23.get() == 1:
                arr.append("perimeter_worst")
            if var24.get() == 1:
                arr.append("area_worst")
            if var25.get() == 1:
                arr.append("smoothness_worst")
            if var26.get() == 1:
                arr.append("compactness_worst")
            if var27.get() == 1:
                arr.append("concavity_worst")
            if var28.get() == 1:
                arr.append("concave points_worst")
            if var29.get() == 1:
                arr.append("symmetry_worst")
            if var30.get() == 1:
                arr.append("fractal_dimension_worst")

            if arr == []:
                warn = tk.messagebox.showwarning(
                    title="Warning", message="Choose at least one attribute")
            else:
                plot_chart('input_Data.csv', arr)
                load = Image.open('plot.png')
                load = load.resize((950, 500), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                img = Label(self, image=render)
                img.image = render
                img.place(x=20, y=275)

        btn = tk.Button(self, text='Show Regression Graph', command=show_graph)
        btn.place(x=820, y=240)

        btn2 = tk.Button(self, text="Return",
                         command=lambda: appController.showPage(StartPage))
        btn2.place(x=20, y=240)


class StatsPage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        visual_title = tk.Label(
            self, text="Choose attribute:", bg="sky blue", font=(50))
        visual_title.place(x=400, y=30)

        dfstats = pd.read_csv(
            'input_Data.csv', sep='\t')

        listvar = list(dfstats.columns)
        cb = Combobox(self, font=(30))
        cb['value'] = listvar
        cb.place(x=370, y=70)

        def show_statistic():
            value = cb.get()
            # gọi hàm ở đây
            xstat = stats_columns(
                'input_Data.csv', value)
            stat = tk.Label(self, text=xstat, background='#F0FFFF', font=(30))

            stat.place(x=405, y=230)

        btn = tk.Button(self, text='Statistic',
                        font=(30), command=show_statistic)
        btn.place(x=440, y=120)

        btn2 = tk.Button(self, text="Return", font=(30),
                         command=lambda: appController.showPage(StartPage))
        btn2.place(x=445, y=175)


class ModelPage(tk.Frame):
    def __init__(self, parent, appController):
        tk.Frame.__init__(self, parent)

        title = tk.Label(
            self, text="Enter value of attributes:", bg='sky blue')
        title.place(x=20, y=15)

        btn2 = tk.Button(self, text="Return",
                         command=lambda: appController.showPage(StartPage))
        btn2.place(x=310, y=550)

        l1 = tk.Label(self, text="radius_mean")
        l1.place(x=20, y=40)
        e1 = Entry(self, width=18)
        e1.place(x=187, y=40)

        l2 = tk.Label(self, text="texture_mean")
        l2.place(x=20, y=70)
        e2 = Entry(self, width=18)
        e2.place(x=187, y=70)

        l3 = tk.Label(self, text="perimeter_mean")
        l3.place(x=20, y=100)
        e3 = Entry(self, width=18)
        e3.place(x=187, y=100)

        l4 = tk.Label(self, text="area_mean")
        l4.place(x=20, y=130)
        e4 = Entry(self, width=18)
        e4.place(x=187, y=130)

        l5 = tk.Label(self, text="smoothness_mean")
        l5.place(x=20, y=160)
        e5 = Entry(self, width=18)
        e5.place(x=187, y=160)

        l6 = tk.Label(self, text="compactness_mean")
        l6.place(x=20, y=190)
        e6 = Entry(self, width=18)
        e6.place(x=187, y=190)

        l7 = tk.Label(self, text="concavity_mean")
        l7.place(x=20, y=220)
        e7 = Entry(self, width=18)
        e7.place(x=187, y=220)

        l8 = tk.Label(self, text="concave points_mean")
        l8.place(x=20, y=250)
        e8 = Entry(self, width=18)
        e8.place(x=187, y=250)

        l9 = tk.Label(self, text="symmetry_mean")
        l9.place(x=20, y=280)
        e9 = Entry(self, width=18)
        e9.place(x=187, y=280)

        l10 = tk.Label(self, text="fractal_dimension_mean")
        l10.place(x=20, y=310)
        e10 = Entry(self, width=18)
        e10.place(x=187, y=310)

        l11 = tk.Label(self, text="radius_se")
        l11.place(x=20, y=340)
        e11 = Entry(self, width=18)
        e11.place(x=187, y=340)

        l12 = tk.Label(self, text="texture_se")
        l12.place(x=20, y=370)
        e12 = Entry(self, width=18)
        e12.place(x=187, y=370)

        l13 = tk.Label(self, text="perimeter_se")
        l13.place(x=20, y=400)
        e13 = Entry(self, width=18)
        e13.place(x=187, y=400)

        l14 = tk.Label(self, text="area_se")
        l14.place(x=20, y=430)
        e14 = Entry(self, width=18)
        e14.place(x=187, y=430)

        l15 = tk.Label(self, text="smoothness_se")
        l15.place(x=20, y=460)
        e15 = Entry(self, width=18)
        e15.place(x=187, y=460)

        l16 = tk.Label(self, text="compactness_se")
        l16.place(x=400, y=40)
        e16 = Entry(self, width=18)
        e16.place(x=567, y=40)

        l17 = tk.Label(self, text="concavity_se")
        l17.place(x=400, y=70)
        e17 = Entry(self, width=18)
        e17.place(x=567, y=70)

        l18 = tk.Label(self, text="concave points_se")
        l18.place(x=400, y=100)
        e18 = Entry(self, width=18)
        e18.place(x=567, y=100)

        l19 = tk.Label(self, text="symmetry_se")
        l19.place(x=400, y=130)
        e19 = Entry(self, width=18)
        e19.place(x=567, y=130)

        l20 = tk.Label(self, text="fractal_dimension_se")
        l20.place(x=400, y=160)
        e20 = Entry(self, width=18)
        e20.place(x=567, y=160)

        l21 = tk.Label(self, text="radius_worst")
        l21.place(x=400, y=190)
        e21 = Entry(self, width=18)
        e21.place(x=567, y=190)

        l22 = tk.Label(self, text="texture_worst")
        l22.place(x=400, y=220)
        e22 = Entry(self, width=18)
        e22.place(x=567, y=220)

        l23 = tk.Label(self, text="perimeter_worst")
        l23.place(x=400, y=250)
        e23 = Entry(self, width=18)
        e23.place(x=567, y=250)

        l24 = tk.Label(self, text="area_worst")
        l24.place(x=400, y=280)
        e24 = Entry(self, width=18)
        e24.place(x=567, y=280)

        l25 = tk.Label(self, text="smoothness_worst")
        l25.place(x=400, y=310)
        e25 = Entry(self, width=18)
        e25.place(x=567, y=310)

        l26 = tk.Label(self, text="compactness_worst")
        l26.place(x=400, y=340)
        e26 = Entry(self, width=18)
        e26.place(x=567, y=340)

        l27 = tk.Label(self, text="concavity_worst")
        l27.place(x=400, y=370)
        e27 = Entry(self, width=18)
        e27.place(x=567, y=370)

        l28 = tk.Label(self, text="concave points_worst")
        l28.place(x=400, y=400)
        e28 = Entry(self, width=18)
        e28.place(x=567, y=400)

        l29 = tk.Label(self, text="symmetry_worst")
        l29.place(x=400, y=430)
        e29 = Entry(self, width=18)
        e29.place(x=567, y=430)

        l30 = tk.Label(self, text="fractal_dimension_worst")
        l30.place(x=400, y=460)
        e30 = Entry(self, width=18)
        e30.place(x=567, y=460)

        def diag():
            inp = dict()
            inp['radius_mean'] = e1.get()
            inp['texture_mean'] = e2.get()
            inp['perimeter_mean'] = e3.get()
            inp['area_mean'] = e4.get()
            inp['smoothness_mean'] = e5.get()
            inp['compactness_mean'] = e6.get()
            inp['concavity_mean'] = e7.get()
            inp['concave points_mean'] = e8.get()
            inp['symmetry_mean'] = e9.get()
            inp['fractal_dimension_mean'] = e10.get()
            inp['radius_se'] = e11.get()
            inp['texture_se'] = e12.get()
            inp['perimeter_se'] = e13.get()
            inp['area_se'] = e14.get()
            inp['smoothness_se'] = e15.get()
            inp['compactness_se'] = e16.get()
            inp['concavity_se'] = e17.get()
            inp['concave points_se'] = e18.get()
            inp['symmetry_se'] = e19.get()
            inp['fractal_dimension_se'] = e20.get()
            inp['radius_worst'] = e21.get()
            inp['texture_worst'] = e22.get()
            inp['perimeter_worst'] = e23.get()
            inp['area_worst'] = e24.get()
            inp['smoothness_worst'] = e25.get()
            inp['compactness_worst'] = e26.get()
            inp['concavity_worst'] = e27.get()
            inp['concave points_worst'] = e28.get()
            inp['symmetry_worst'] = e29.get()
            inp['fractal_dimension_worst'] = e30.get()

            inp = pd.DataFrame.from_dict(inp, orient='index')

            predict = model_result('cancer_pipeline.joblib', inp.T)
            if predict == 1:
                out = tk.Label(self, text="Diagnosis: Maglignant",
                               bg='sky blue', font=(20))
            else:
                out = tk.Label(self, text="Diagnosis: Benign",
                               bg='sky blue', font=20)
            out.place(x=310, y=640)

        btn = tk.Button(self, text='Diagnosis')
        btn['command'] = diag
        btn.place(x=310, y=510)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Cancer Diagnosis")
        self.geometry("1000x870")
        self.resizable(width=False, height=False)

        container = tk.Frame()
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, VisualizePage, StatsPage, ModelPage):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[F] = frame

        self.frames[StartPage].tkraise()

    def showPage(self, FrameClass):
        self.frames[FrameClass].tkraise()


app = App()
app.mainloop()
