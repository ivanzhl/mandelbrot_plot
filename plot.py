import numpy as np
import matplotlib.pyplot as plt
import subprocess

class Plotter():


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

        process = subprocess.Popen(['./mandelbrot'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return np.fromstring(output, sep=' ').reshape((800, 800))

    #plot data with matplotlib
    def plot_data(self,data):

        plt.figure(frameon=False)  # Erstelle ein neues Figure-Objekt ohne Rahmen
        ax = plt.imshow(data, cmap='magma', extent=[-2.5, 1.0, -1.0, 1.0], aspect='equal')
        plt.axis('off')  # Achsen ausschalten
        plt.title('Mandelbrot Set')
        plt.show()

    #run methode
    def run(self):
        self.compile_cpp('mandelbrot.cpp','mandelbrot')
        data = self.run_cpp()
        self.plot_data(data)

