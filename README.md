# Molecular-Dynamics0

This is the code for the molecular dynamics (MD) simulation of 500 He atoms initially packed into a FCC lattice. The initial velocity component of every particle is randomly assigned from a unifrom distribution. \\
Next step is the calculation of force acting on every particle. We consider the potential between two particles here be of Lennard-Jones nature. Hence the equation of force between a pair of particles can be derived by the differentiation of the Lennardd-Jones potential wrt to the distance between the particles r.
The positions are updated using verlet algorithm.
