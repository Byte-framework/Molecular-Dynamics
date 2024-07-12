# Molecular-Dynamics

This is the code for the molecular dynamics (MD) simulation of 500 He atoms initially packed into a FCC lattice. The initial velocity component of every particle is randomly assigned from a unifrom distribution. 

Next step is the calculation of force acting on every particle. We consider the potential between two particles here be of Lennard-Jones nature. Then the equation of force between a pair of particles can be derived by the differentiation of the Lennard-Jones potential with respect to the distance between the particles (*r*). 

In order to simulate a large system, we use periodic boundary condition, with a cutoff distance equal to half the box (or lattice) length. This means, the distance in any direction (x, y or z ) between a particle *i* and the nearest image of a particle *j* is less than the cutoff distance.

The last step is updating the positions and velocities of the particles which are done using verlet algorithm.

<!--**Lennard-Jones Potential**
$$ V = 4\epsilon \left ( \left( \frac{\sigma}[r} \right)^12 - \left( \frac{1}{r^6} \right)^6 \right) $$-->
 


<!--More details have to be added>
