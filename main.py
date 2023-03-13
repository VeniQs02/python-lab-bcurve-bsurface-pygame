import matplotlib.pyplot as plt
import numpy as np
import scipy


def two_dimensional_initials():
    def bezier_curve(points, n_points=100):
        t = np.linspace(0, 1, n_points)
        n = len(points) - 1
        curve = np.zeros((n_points, 2))
        for i in range(n_points):
            for j in range(n + 1):
                curve[i] += points[j] * newton(n, j) * (1 - t[i]) ** (n - j) * t[i] ** j
        return curve

    def newton(n, k):
        return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

    l1 = np.array([[100, 50], [100, 100], [100, 100], [150, 100], [200, 150], [200, 200], [200, 400]])
    l2 = np.array([[100, 50], [200, 50], [250, 150], [250, 250], [250, 400]])
    l3 = np.array([[250, 400], [200, 400]])

    l4 = np.array([[300, 400], [300, 50]])
    l5 = np.array([[300, 400], [350, 400]])
    l6 = np.array([[350, 400], [350, 270]])
    l7 = np.array([[350, 270], [360, 330], [385, 380], [400, 400]])
    l8 = np.array([[400, 400], [450, 400]])
    l9 = np.array([[450, 400], [390, 295], [380, 225], [450, 50]])
    l10 = np.array([[450, 50], [400, 50]])
    l11 = np.array([[400, 50], [380, 100], [360, 160], [350, 220]])
    l12 = np.array([[350, 220], [350, 50]])
    l13 = np.array([[350, 50], [300, 50]])

    c1 = bezier_curve(l1)
    c2 = bezier_curve(l2)
    c3 = bezier_curve(l3)
    c4 = bezier_curve(l4)
    c5 = bezier_curve(l5)
    c6 = bezier_curve(l6)
    c7 = bezier_curve(l7)
    c8 = bezier_curve(l8)
    c9 = bezier_curve(l9)
    c10 = bezier_curve(l10)
    c11 = bezier_curve(l11)
    c12 = bezier_curve(l12)
    c13 = bezier_curve(l13)

    plt.plot(c1[:, 0], c1[:, 1], c2[:, 0], c2[:, 1], c3[:, 0], c3[:, 1], c4[:, 0], c4[:, 1], c5[:, 0], c5[:, 1], \
             c6[:, 0], c6[:, 1], c7[:, 0], c7[:, 1], c8[:, 0], c8[:, 1], c9[:, 0], c9[:, 1], c10[:, 0], c10[:, 1], \
             c11[:, 0], c11[:, 1], c12[:, 0], c12[:, 1], c13[:, 0], c13[:, 1])

    plt.xlim([0, 500])
    plt.ylim([0, 500])
    plt.show()
# two_dimensional_initials()

def three_dimensional_field():
    # Teapot data
    control_points = np.array([[1.4, 0.0, 2.4],
                               [1.4, -0.784, 2.4],
                               [0.784, -1.4, 2.4],
                               [0.0, -1.4, 2.4],
                               [1.3375, 0.0, 2.53125],
                               [1.3375, -0.749, 2.53125],
                               [0.749, -1.3375, 2.53125],
                               [0.0, -1.3375, 2.53125],
                               [1.4375, 0.0, 2.53125],
                               [1.4375, -0.805, 2.53125],
                               [0.805, -1.4375, 2.53125],
                               [0.0, -1.4375, 2.53125],
                               [1.5, 0.0, 2.4],
                               [1.5, -0.84, 2.4],
                               [0.84, -1.5, 2.4],
                               [0.0, -1.5, 2.4]])

    # Define Bezier patches
    patches = [
        (np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]), 3, 3),
        (np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]), 3, 2),
        (np.array([[0, 1, 2, 3], [4, 5, 6, 7]]), 2, 2),
        (np.array([[0, 1, 2, 3]]), 1, 2)
    ]

    # Evaluate Bezier patches
    def evaluate_patch(patch, u, v):
        points, degree_u, degree_v = patch
        result = np.zeros(3)
        for i in range(degree_u + 1):
            for j in range(degree_v + 1):
                point = control_points[points[i][j]]
                result += point * bernstein(degree_u, i, u) * bernstein(degree_v, j, v)
        return result

    def bernstein(n, i, t):
        return scipy.special.comb(n, i) * t ** i * (1 - t) ** (n - i)

    # Generate surface mesh
    u, v = np.linspace(0, 1, 20), np.linspace(0, 1, 20)
    U, V = np.meshgrid(u, v)
    points = np.array([evaluate_patch(patch, u, v) for patch in patches])
    x, y, z = points[:, :, 0], points[:, :, 1], points[:, :, 2]

    # Plot surface mesh
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_xlabel('X')
three_dimensional_field()





