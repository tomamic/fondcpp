#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def py_f(x: float) -> float:
    return x * x + x

def py_integral(a: float, b: float, n: int) -> float:
    """
    Estimate the area beneath the curve py_f, between the
    abscissas a and b; the region is approximated as n rectangles.
    """
    total = 0.0
    dx = (b - a) / n
    for i in range(n):
        total += dx * py_f(a + dx * i)
    return total

def main():
    import subprocess, time
    subprocess.run(["g++", "-O3", "integral.cpp", "-o", "_integral"])

    t0 = time.time()
    result = subprocess.run(["./_integral", "1", "10", "100000000"],
                            capture_output=True, text=True)
    t_cpp = time.time() - t0
    print(result.stdout)
    i = float(result.stdout.split()[1])
    print(f"C++\t{i:10.4f}\t{t_cpp:10.4f}")

    t0 = time.time()
    i = py_integral(1, 10, 100_000_000)
    t_py = time.time() - t0
    print(f"Python\t{i:10.4f}\t{t_py:10.4f}")
    print(t_py / t_cpp)

main()
