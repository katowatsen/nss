import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Analysis():
    def __init__(self, graphs):

        dirname = os.path.dirname(__file__)
        parent_dirname = os.path.dirname(dirname)
        grandparent_dirname = os.path.dirname(parent_dirname)
        self.fileName = os.path.join(grandparent_dirname, "results.csv")
        
        #removes preexisting data
        if os.path.exists(self.fileName):
            os.remove(self.fileName)

        self.graphs = graphs

    def writeHeaders(self, data):

        keys = data[0].keys()

        with open(self.fileName, 'w') as CSV_out:

            dict_writer = csv.DictWriter(CSV_out, keys)
            dict_writer.writeheader()
            #dict_writer.writerows(data)

    def writeRow(self, data):
        keys = data[0].keys()

        with open(self.fileName, 'a') as CSV_out:
            dict_writer = csv.DictWriter(CSV_out, keys)
            dict_writer.writerows(data)


    def read(self):
        try:

            self.df = pd.read_csv(self.fileName)

        except(EOFError):
            print("No file found.")

    def parse_DF(self):

        self.data = self.df.to_numpy()
        self.keys = list(self.df.keys())

    def createFigure(self, x, y):
        self.parse_DF()

        for key in self.keys:
            if key == x:
                x_pos = self.keys.index(key)

            if key == y:
                y_pos = self.keys.index(key)

        x_axis = self.data[:,x_pos]
        y_axis = self.data[:,y_pos]
        fig = plt.figure(dpi=2000)
        red = "#cc2529"

        if x == "cycle":
            x  = "time"
            title = str(x) + "-" + str(y)
            fig, ax = plt.subplots()
            fig.suptitle(title)
            ax.set_xlabel(x)
            ax.set_ylabel(y)

            ax.plot(x_axis, y_axis, red)
        else: 
            title = str(x) + "-" + str(y)
            fig, ax = plt.subplots()
            fig.suptitle(title)
            ax.set_xlabel(x)
            ax.set_ylabel(y)

            plt.scatter(x_axis, y_axis, c=red)
            plt.plot(np.unique(x_axis), np.poly1d(np.polyfit(x_axis, y_axis, 1))(np.unique(x_axis)), "#3969b1")


        plt.savefig("output/"+title+".pdf")

    def createFigures(self):
        for pair in self.graphs:
            print(pair)
            self.createFigure(pair[0], pair[1])
        print("Produced graphs")
