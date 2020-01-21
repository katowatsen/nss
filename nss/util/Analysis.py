import csv
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Analysis():
    def __init__(self):

        dirname = os.path.dirname(__file__)
        parent_dirname = os.path.dirname(dirname)
        grandparent_dirname = os.path.dirname(parent_dirname)
        self.fileName = os.path.join(grandparent_dirname, "results.csv")
        
        #removes preexisting data
        if os.path.exists(self.fileName):
            os.remove(self.fileName)

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

    def createFigure(self, x, y):
        self.parse_DF()

        time = self.data[:,0]
        alt = self.data[:,-2]
        fig = plt.figure()
        fig.suptitle("Altruism v.s. Time")
        fig, ax = plt.subplots()
        ax.plot(time, alt)

        canvas = plt.get_current_fig_manager().canvas

        agg = canvas.switch_backends(FigureCanvasAgg)
        agg.draw()
        s, (width, height) = agg.print_to_buffer()

        # Convert to a NumPy array.
        X = np.frombuffer(s, np.uint8).reshape((height, width, 4))

        # Pass off to PIL.
        from PIL import Image
        im = Image.frombytes("RGBA", (width, height), s)

        # Uncomment this line to display the image using ImageMagick's `display` tool.
        im.save("output/alt-time.png")
        im.show()
