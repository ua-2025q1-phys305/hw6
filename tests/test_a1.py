from phys305_hw6 import Grids
import numpy as np
import pytest

def test_grids():

    grids = Grids(4, 4)

    assert grids.x == pytest.approx(np.array([
        [-2., -1.,  0.,  1.],
        [-2., -1.,  0.,  1.],
        [-2., -1.,  0.,  1.],
        [-2., -1.,  0.,  1.],
    ]))

    assert grids.y == pytest.approx(np.array([
        [-2., -2., -2., -2.],
        [-1., -1., -1., -1.],
        [ 0.,  0.,  0.,  0.],
        [ 1.,  1.,  1.,  1.],
    ]))

    assert grids.kx == pytest.approx(np.array([
        [ 0.,  1., -2., -1.],
        [ 0.,  1., -2., -1.],
        [ 0.,  1., -2., -1.],
        [ 0.,  1., -2., -1.],
    ]) * np.pi / 2)

    assert grids.ky == pytest.approx(np.array([
        [ 0.,  0.,  0.,  0.],
        [ 1.,  1.,  1.,  1.],
        [-2., -2., -2., -2.],
        [-1., -1., -1., -1.],
    ]) * np.pi / 2)

    assert grids.kk == pytest.approx(np.array([
        [ 0.,  1.,  4.,  1.],
        [ 1.,  2.,  5.,  2.],
        [ 4.,  5.,  8.,  5.],
        [ 1.,  2.,  5.,  2.],
    ]) * np.pi * np.pi / 4)

    assert grids.ikk == pytest.approx(np.array([
        [ 0.,   1.0,  0.25, 1.0],
        [ 1.,   0.5,  0.2,  0.5],
        [ 0.25, 0.2,  0.125,0.2],
        [ 1.,   0.5,  0.2,  0.5],
    ]) / np.pi / np.pi * 4)
