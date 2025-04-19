from phys305_hw6 import Grids, vel, Jdet, dealiasing
import numpy as np
from numpy.fft import fft2, ifft2
import pytest

grids = Grids(4 * np.pi, 128)
psi   = - np.sin(grids.x) + np.sin(grids.y)
w     = + np.sin(grids.x) - np.sin(grids.y)

ux_ref   = np.cos(grids.y)
uy_ref   = np.cos(grids.x)
jdet_ref = ux_ref * np.cos(grids.x) - uy_ref * np.cos(grids.y)

def test_vel():

    ux, uy = vel(grids, fft2(psi))

    assert ux == pytest.approx(ux_ref)
    assert uy == pytest.approx(uy_ref)

def test_Jdet():

    jdet = ifft2(Jdet(grids, fft2(psi), fft2(w))).real

    assert jdet == pytest.approx(jdet_ref)

def test_dealiasing():

    Nx, Ny = grids.x.shape
    Hx = Nx // 3
    Hy = Ny // 3

    u = np.random.uniform(size=(Nx, Ny))
    U = dealiasing(fft2(u))

    assert U[Hx:-Hx+1, :] == pytest.approx(0)
    assert U[:, Hy:-Hy+1] == pytest.approx(0)
