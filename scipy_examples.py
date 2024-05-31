import numpy as np
from scipy.integrate import quad
from scipy.special import jn
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def main(argv=None) -> int:
    print("NumPy version: " + str(np.__version__))

    # Vier Besselfunktionen geplottet
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots()
    for alpha in range(4):
        ax.plot(x, jn(alpha, x), label=r"J$_{}(x)$".format(alpha))
        ax.legend()
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Bessel Functions")
    plt.show()

    # Integration
    a = 0
    b = np.pi / 2.0
    integral_value, absolute_error = quad(func=np.cos, a=a, b=b)
    print("Integralwert: " + str(integral_value))
    print("Absoluter Fehler: " + str(absolute_error))

    n = np.arange(0, 10)
    x = np.linspace(0, 9, 100)
    y_actual = np.cos(x)
    y_experiment = np.cos(n) + 0.12 * np.random.randn(len(n))
    # lineare Interpolation durchführen
    linear_interpolation = interp1d(n, y_experiment, kind="linear")
    y_linear_interpolation = linear_interpolation(x)
    # kubische Interpolation
    cubiic_interpolation = interp1d(n, y_experiment, kind="cubic")
    y_cubic_interpolation = cubiic_interpolation(x)
    # Vergleichsplot erzeugen
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(n, y_experiment, "bs", label="experiment data")
    ax.plot(x, y_actual, "k", lw=2, label="actual function")
    ax.plot(x, y_linear_interpolation, "r", label="linear interpolation")
    ax.plot(x, y_cubic_interpolation, "g", label="cubic interpolation")
    ax.legend(loc=3)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Functions Interpolation Example")
    plt.show()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
