import gudhi
import math as m
import matplotlib.pyplot as plt

L = []

for k in range(10):
    angle = 2*m.pi*k/10
    L.append([m.cos(angle), m.sin(angle)])

alpha = gudhi.AlphaComplex(points=L)
simplex = alpha.create_simplex_tree()
diag = simplex.persistence()
gudhi.plot_persistence_barcode(diag)
gudhi.plot_persistence_diagram(diag)
plt.show()
