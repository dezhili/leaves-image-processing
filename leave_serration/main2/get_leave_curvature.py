from scipy.interpolate import UnivariateSpline
import numpy as np


def curvature_splines(x, y=None, error=0.1):
    if y is None:
        x, y = x.real, x.imag

    t = np.arange(x.shape[0])
    std = error * np.ones_like(x)

    fx = UnivariateSpline(t, x, k=4, w=1 / np.sqrt(std))
    fy = UnivariateSpline(t, y, k=4, w=1 / np.sqrt(std))

    xˈ = fx.derivative(1)(t)
    xˈˈ = fx.derivative(2)(t)
    yˈ = fy.derivative(1)(t)
    yˈˈ = fy.derivative(2)(t)
    curvature = abs((xˈ* yˈˈ - yˈ* xˈˈ)) / np.power(xˈ** 2 + yˈ** 2, 3 / 2)
    return curvature
