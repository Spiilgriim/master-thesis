from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

trefoil = np.array([(0, 1, 0.5), (-0.33, 0.33, 1), (0, -0.5, 0), (1, -0.5, 0.5),
                    (0.33, 0.33, 1), (-0.33, 0.33, 0), (-1, -0.5, 0.5), (0, -0.5, 1), (0.33, 0.33, 0)])

fig8 = np.array([(0, 1, 0.5), (-0.33, 0.66, 0), (0, 0, 1), (0.25, -0.5, 0.5), (0, -0.66, 0), (-1, 0, 0.5),
                 (-0.33, 0.66, 1), (0.33, 0.66, 0), (1, 0, 0.5), (0, -0.66, 1), (-0.25, -0.5, 0.5), (0, 0, 0), (0.33, 0.66, 1)])

#trajectory = trefoil
trajectory = fig8

ax = plt.axes(projection="3d")
ax.scatter3D([e[0] for e in trajectory], [e[1] for e in trajectory], [e[2]
                                                                      for e in trajectory], s=50, c=range(len(trajectory)), cmap="hsv")
plt.show()
