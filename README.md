# Molecular-Dynamics

This is the code for the molecular dynamics (MD) simulation of 500 He atoms initially packed into a FCC lattice. The initial velocity component of every particle is randomly assigned from a unifrom distribution. 

Next step is the calculation of force acting on every particle. We consider the potential between two particles here be of Lennard-Jones nature.

<!--**Lennard-Jones Potential**
$$ V = 4\epsilon \left ( \left( \frac{\sigma}[r} \right)^12 - \left( \frac{1}{r^6} \right)^6 \right) $$-->
Hence the equation of force between a pair of particles can be derived by the differentiation of the Lennardd-Jones potential wrt to the distance between the particles r. 


The positions are updated using verlet algorithm.
<!--More details have to be added>
