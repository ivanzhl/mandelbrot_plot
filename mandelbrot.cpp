#include <iostream>
#include <complex>
#include <numeric>

const int WIDTH = 800;
const int HEIGHT = 800;
const double MIN_RE = -2.5;
const double MAX_RE = -2.6;
const double MIN_IM = -1.0;
const double MAX_IM = -1.2;

 


//algorithm for checking if c is in mandelbrot set
int is_in_set(std::complex<double> c, int max_iter = 25){

    std::complex<double> z(0,0);
    for(int i = 0; i<max_iter; i++){
        
        // z(n+1) = z(n)² + c
        z = std::pow(z,2) + c;

        if(std::norm(z) > 10){
            return i;
        }
    }
    return 0;
}

int main() {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            double re = -2.5 + x * (3.5 / WIDTH);
            double im = -1.0 + y * (2.0 / HEIGHT);
            std::complex<double> c(re, im);
            std::cout << is_in_set(c,100) << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}