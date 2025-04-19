from phys305_hw6 import Stepper, init
import numpy as np
import pytest

step = Stepper(4 * np.pi, 8, 0.1, 0.01, 0.001)

W_ref     = np.zeros(8, dtype=np.complex64)
W_ref[ 1] = -18.64558213-7.76549871j
W_ref[-1] = -18.64558213+7.76549871j

def test_step():

    W = init(step, 0)
    W = step(W, dt=1)

    assert W[0, :] == pytest.approx(W_ref)
    assert W[1:,:] == pytest.approx(0)
