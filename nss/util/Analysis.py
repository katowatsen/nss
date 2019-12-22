import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Analysis():
    def __init__(self):

        dirname = os.path.dirname(__file__)
        parent_dirname = os.path.dirname(dirname)
        grandparent_dirname = os.path.dirname(parent_dirname)
        self.fileName = os.path.join(grandparent_dirname, "results.csv")
        
        #removes preexisting data
        if os.path.exists(self.fileName):
            os.remove(self.fileName)

    def write(self, data):

        keys = data[0].keys()

        with open(self.fileName, 'w') as CSV_out:

            dict_writer = csv.DictWriter(CSV_out, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def read(self):
        try:

            self.data = pd.read_csv(self.fileName)

        except(EOFError):
            print("No file found.")

        print(self.data.head())

    def parse_CSV(self):

        major_data = []

        for sub_data in data:
            row = []

            for k in sorted(sub_data.keys()):
                row.append(sub_data[k])

            major_data.append(row)

            
        self.data = np.array(major_data)

    def createFigure(self):

        fig = plt.figure()

