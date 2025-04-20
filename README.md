# PHYS305 Homework Set #6

Welcome to the repository for **Homework Set #6** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we've covered.
The submission cutoff time is at **Thursday May 8th, 11:59pm** Arizona
time.
Please use [this link](https://classroom.github.com/a/___) to
accept it from GitHub Classroom.


## Structure and Grading

This homework set consists of **five assignments**, each contributing
equally to your overall grade.
The grading breakdown is as follows:

1. **Automated Evaluation (50%)**:
   * Each assignment will be graded using `pytest`, an automated
     testing framework.
   * The correctness of your solutions accounts for 1 point per
     assignment (5 points in total).
   * You can run `pytest` in GitHub Codespaces or your local
     development environment to verify your solutions before
     submission.

2. **Documentation and Coding Practices (50%)**:
   * The remaining 1 point per assignment (5 points total) will be
     based on documentation and coding practices.
   * Clear and concise **documentation** of your code, including
     meaningful comments.
   * Adherence to good **coding practices**, such as proper variable
     naming, modular design, and code readability.

By following the interface and prototypes provided in each assignment
template, you can ensure compatibility with the autograding system and
maximize your score.


## Assignments

A Jupyter notebook `demo/vis.ipynb` is provided to help you test and
visualize your code.
Use it frequently to debug and validate your solver.

Each Python file in `src/phys305_hw6/` corresponds to one assignment.
The notebook will call your implementations directly, so ensure your
functions are correct and match the required interface.
Use pytest to validate outputs and spot common mistakes.


### Assignment 1: Grid and Wavenumber Setup (2 points)

Implement a class `Grids(L, N)` in `src/phys305_hw6/a1.py` that sets
up the real-space grid and spectral wavenumbers for a square, periodic
domain of size $L\times L$ with $N\times N$ points.

Your class should:
* Generate real-space coordinates $x$, $y$ using `np.meshgrid()`, with
  values evenly spaced from $-L/2$ to $L/2$ (excluding the endpoint
  $L/2$).
* Generate 2D spectral wavenumber arrays $kx$, $ky$ using
  `np.fft.fftfreq()` and `np.meshgrid()` and convert to angular
  frequency (multiply by $2\pi$).
* Provide derived spectral arrays as cached properties:
  * `kk` : the squared wavenumber magnitude, i.e., `kx**2 + ky**2`.
  * `ikk`: its inverse, with the zero mode (`kx=ky=0`) set to zero to
    avoid division by zero in later part of the algorithm.

Looking into `tests/test_a1.py` and finding out how the tests are done
may help you implement `src/phys305_hw6/a1.py`.


## Additional Notes

* **Collaboration**:
  You are encouraged to discuss ideas with your peers, but your
  submission must reflect your own work.
* **Help and Resources**:
  If you encounter any difficulties, please refer to the course
  materials, consult your instructor, or seek help during office
  hours.
* **Deadlines**:
  Be mindful of the submission deadline, as late submissions will not
  be accepted.

Good luck, and have fun working on the assignments!
