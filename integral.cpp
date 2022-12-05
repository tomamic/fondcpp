/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include <chrono>
#include <iostream>

double f(double x) {
    return x * x + x;
}

double integral(double a, double b, int n) {
    /**
     * Estimate the area beneath the curve f, between the
     * abscissas a and b; the region is approximated as n rectangles.
     */
    auto total = 0.0;
    auto dx = (b - a) / n;
    for (auto i = 0; i < n; ++i) {
        total += dx * f(a + dx * i);
    }
    return total;
}

int main() {
    auto start = std::chrono::steady_clock::now();

    std::cout << "integral: " << integral(1, 10, 100'000'000) << std::endl;

    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> elapsed_seconds = end-start;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";
}
