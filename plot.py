import numpy as np
import matplotlib.pyplot as plt
import subprocess

class Plotter():

    def __init__(self,fractal):
      self.fractal = fractal

    #compile cpp algorithm
    def compile_cpp(self,source_file, executable_name):

        #compile command
        command = ['g++', '-o', executable_name, source_file]
        
        #try to compile
        try:
            subprocess.run(command, check=True)
            print("compilation successful")
        except subprocess.CalledProcessError:
            print("compilation error")



    #run cpp algorithm
    def run_cpp(self):

        process = subprocess.Popen(['./algorithm'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return np.fromstring(output, sep=' ').reshape((800, 800))

    #plot data with matplotlib
    def plot_data(self,data):

        plt.figure(frameon=False)  
        plt.imshow(data, cmap='magma', extent=[-2.5, 1.0, -1.0, 1.0], aspect='equal')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.axis('off')  #
        plt.show()

    #run methode
    def run(self):
        self.compile_cpp(self.fractal,'algorithm')
        data = self.run_cpp()
        self.plot_data(data)

