from phys305_hw6 import main
from os.path import exists
import os

def test_main():

    main(Nt=10, skip=1)

    for n in range(10+1):
        assert exists(f'{n:04d}.png')
