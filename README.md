# PHYS305 Homework Set #6

Welcome to the repository for **Homework Set #6** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we've covered.
The submission cutoff time is at **Thursday May 8th, 11:59pm** Arizona
time.
Please use [this link](https://classroom.github.com/a/6aVUKkGd) to
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

Each Python file in `src/phys305_hw6/` corresponds to one assignment.
The notebook will call your implementations directly, so ensure your
functions are correct and match the required interface.
Use `pytest` to validate outputs and spot common mistakes.


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


### Assignment 2: Velocity Field, Jacobian, and Dealiasing (2 points)

Implement the functions in `src/phys305_hw6/a2.py` that construct key
spectral operations required to evolve 2D incompressible fluid flow.

You will define the following three functions:

1. `vel(grids, Psi)`: Compute the velocity components from a
   streamfunction `Psi` in spectral space.

   **Inputs:**
   * `grids`: an instance of your `Grids` class from Assignment 1, which provides `kx`, `ky`.
   * `Psi`: 2D NumPy array in spectral space.

   **Returns:**
   * `ux`, `uy`: real-space velocity fields computed via spectral derivatives:

2. `Jdet(grids, Psi, W)`: Compute the Jacobian determinant $J(\psi,
   w)$ in spectral space, which captures the nonlinear advection term.

   **Inputs:**
   * `grids`: the Grids object.
   * `Psi`: streamfunction in spectral space.
   * `W`: vorticity in spectral space.

   **Returns:**
   * A 2D NumPy array representing the Jacobian determinant in spectral space.

3. `dealiasing(F)`: Apply the 2/3 rule to remove high-frequency modes
   from a 2D Fourier array F.

   **Input:**
   * `F`: a 2D NumPy array in spectral space (Fourier-transformed).

   **Returns:**
   * A new array where all modes with indices beyond (`N/3`) in either
     dimension have been set to zero:

**Hints and Testing:**
* Review `tests/test_a2.py` to understand how correctness is verified.
* The test initializes streamfunction $\psi = -\sin(x) + \sin(y)$ and
  vorticity $w = \sin(x) - \sin(y)$.
  The corresponding velocity and Jacobian are known analytically.
* The dealiasing test checks that Fourier modes in the excluded band
  are zero.

### Assignment 3: Initialization and Visualization (2 points)

In this assignment, you will implement `init()` and `plot()` functions
in `src/phys305_hw6/a3.py` to set up an initial vorticity field and
visualize the fluid flow using the streamfunction and velocity field.

1. `init(grids, scale)`: This function initializes the vorticity field
   in spectral space based on a **special initial condition**:
   * Horizontal velocity `ux`: random noise generated from a normal
     distribution with zero mean and specified standard deviation
     `scale`.
   * Vertical velocity `uy`: a **step function** that is +1 when `x >=
     0` and -1 otherwise.

   **Inputs:**
   * `grids`: an instance of the `Grids` class from Assignment 1.
   * `scale`: standard deviation for generating the random velocity
     field.

   **Returns:**
   * `W`: the initial vorticity in spectral space, with high-frequency
     modes suppressed using the 2/3 de-aliasing rule.

2. `plot(grids, W, L, skip=4)`: This function visualizes the
   streamfunction and velocity field using matplotlib.

   **Inputs:**
   * `grids`: the Grids object.
   * `W`: the vorticity in spectral space.
   * `L`: the size of the domain.
   * `skip`: how many grid points to skip when plotting velocity
     vectors (default is 4).

   Behavior:
   * Solve for the streamfunction using the inverse Laplacian: `Psi =
     grids.ikk * W`.
   * Convert `Psi` to real space using inverse FFT.
   * Plot the streamfunction using `plt.imshow()`.
   * Compute velocity field using `vel()` and overlay arrows using
     `plt.quiver()`.


### Assignment 4: Time-Stepping the Vorticity Field (2 points)

In this assignment, you will implement a spectral time-stepper in
`src/phys305_hw6/a4.py` using a semi-implicit update scheme for the 2D
vorticity equation.

1. `Stepper` Class: Create a class `Stepper` that inherits from the
   `Grids` class you built in Assignment 1.
   This means `Stepper` **extends** the grid structure with additional
   physical parameters and a time-stepping method.

   **Why subclass `Grids`?**
   The `Grids` class already provides all the spatial and spectral
   arrays (like `x`, `kx`, `ikk`) needed to evolve the vorticity.
   By subclassing it, `Stepper` can directly access those arrays,
   making the code cleaner and modular.

2. Class Signature:

   ```python
   class Stepper(Grids):
       def __init__(self, L, N, nu, mu, beta):
       	   ...
       def __call__(self, W, dt):
           ...
   ```

   Constructor Inputs:
   * `L`: domain size.
   * `N`: number of grid points per dimension.
   * `nu`: kinematic viscosity.
   * `mu`: Ekman damping coefficient.
   * `beta`: strength of Coriolis variation ($\beta$-plane).

   These parameters are saved as attributes inside the object.

   `__call__(self, W, dt)`:
   This method makes the Stepper object behave like a function: when
   you call `step(W, dt)`, it advances the vorticity `W` by one time
   step `dt`.


### Assignment 5: Full Simulation Driver (2 points)

In this final assignment, you will implement a complete simulation
pipeline that brings together everything from the previous
assignments.
Your goal is to evolve a 2D incompressible fluid using spectral
methods and output a series of visualization frames.

1. `main()` Function: Implement the function `main()` in
   `src/phys305_hw6/a5.py`.

   This function sets up and runs the simulation.
   The default arguments control time step size, resolution,
   viscosity, and other physical or numerical parameters.

   **Default Parameters:**
   ```python
   dt   = 0.001     # Time step
   Nt   = 10000     # Number of time steps
   skip = 10        # Output frequency
   L    = 2 * np.pi # Domain size
   N    = 128       # Grid resolution
   nu   = 0.001     # Kinematic viscosity
   mu   = 0.0       # Ekman damping
   beta = 0.0       # Coriolis parameter
   ```

2. Steps to Implement:
   1. Create a Stepper object: `step = Stepper(L, N, nu, mu, beta)`
   2. Initialize the vorticity field: `W = init(step, 0.5)`
   3. Loop through the time steps:
      * Save a visualization every skip steps using `plot()`.
      * Advance the simulation by calling `step(W, dt)` repeatedly.
   4. Save the final frame after the loop ends.

3. Make the script executable by adding:
   ```python
   if __name__ == "__main__":
       main()
   ```

**Hints and Testing**

* It is very difficult to automatically test graphic output so we are
  not checking the output of `main()`.
  Nevertheless, the test still requires `main()` runs without
  problems; and we will manually inspect your output for full credits.
* The test runs `main(Nt=10,skip=1)`, which should generate 11 PNG
  files (`0000.png` to `0010.png`).
* These files must be created in the current directory, so make sure
  `plot()` and `plt.savefig()` are called correctly.
* Use `plt.close()` after each plot to avoid memory issues.

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
