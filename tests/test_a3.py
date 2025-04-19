from phys305_hw6 import Grids, init, plot
import numpy as np
from matplotlib import pyplot as plt
import pytest

grids     = Grids(2 * np.pi, 8)
W_ref     = np.zeros(8, dtype=np.complex64)
W_ref[ 1] = -38.627417-16.j
W_ref[-1] = -38.627417+16.j

def test_step():

    W = init(grids, 0)

    assert W[0, :] == pytest.approx(W_ref)
    assert W[1:,:] == pytest.approx(0)

def test_plot():

    W = init(grids, 0.5)

    plot(grids, W, 2 * np.pi, skip=1)
    plt.savefig('test_plot.png')
    plt.close()
