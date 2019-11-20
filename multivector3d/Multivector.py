import numpy as np


class Multivector3D():
    """Defines an 3-dimensional multivector, with
    components stored as numpy arrays.

    Attributes:
        dtype: data type of the underlying numpy arrays.
        scalar: scalar part.
        vector: vector part. The three components correspond
            to e_1, e_2, and e_3.
        bivector: bivector part. The three components correspond
            to e_2e_3, e_3e_1, and e_1e_2.
        pscalar: psuedoscalar (signed volume) part, corresponding
            to e_1e_2e_3.
    """

    def __init__(self,
                 scalar=0.0,
                 vector=[0.0, 0.0, 0.0],
                 bivector=[0.0, 0.0, 0.0],
                 pscalar=0.0):
        """Initialize a zero 3 dimensional multivector.

        Args:
            scalar: a floating point number.
            vector: a list of 3 floats, or a numpy array with shape (3,).
            bivector: a list of 3 floats, or a numpy array with shape (3,).
            pscalar: a floating point number.
        """

        self.scalar = scalar
        self.vector = np.array(vector)
        self.bivector = np.array(bivector)
        self.pscalar = pscalar

    def __add__(self, other):
        """Add two multivectors.

        Args:
            other: another Multivector3D.

        Returns:
            mv_sum: sum of the two multivectors.
        """

        return Multivector3D(scalar=self.scalar + other.scalar,
                             vector=self.vector + other.vector,
                             bivector=self.bivector + other.bivector,
                             pscalar=self.pscalar + other.pscalar)

    def __sub__(self, other):
        """Subtract two multivectors."""

        return self + (other*(-1))

    def __mul__(self, other):
        """Multiply two multivectors, or a multivector and a scalar.

        Args:
            other: another Multivector3D.

        Returns:
            mv_prod: geometric product of the two multivectors.
        """

        if isinstance(other, float) or isinstance(other, int):
            return Multivector3D(
                scalar=other*self.scalar,
                vector=other*self.vector,
                bivector=other*self.bivector,
                pscalar=other*self.pscalar)

        return Multivector3D(
            scalar=(self.scalar*other.scalar
                    - self.pscalar*other.pscalar
                    + np.dot(self.vector, other.vector)
                    - np.dot(self.bivector, other.bivector)),
            vector=(self.scalar*other.vector
                    + other.scalar*self.vector
                    - self.pscalar*other.bivector
                    - other.pscalar*self.bivector
                    - np.cross(self.vector, other.bivector)
                    + np.cross(other.vector, self.bivector)),
            bivector=(self.scalar*other.bivector
                      + other.scalar*self.bivector
                      + other.pscalar*self.vector
                      + self.pscalar*other.vector
                      + np.cross(self.vector, other.vector)
                      - np.cross(self.bivector, other.bivector)),
            pscalar=(self.scalar*other.pscalar
                     + self.pscalar*other.scalar
                     + np.dot(self.vector, other.bivector)
                     + np.dot(self.bivector, other.vector)))

    def __truediv__(self, other):
        """Scalar division of a multivector."""
        if isinstance(other, float) or isinstance(other, int):
            return self*(1/other)

        raise ValueError("Must divide by a float.")

    def dot(self, other):
        """Dot product of two Multivector3D.
        """

        return (self * other + other * self)/2

    def __xor__(self, other):
        """Wedge product with another Multivector3D.
        """

        return (self * other - other * self)/2

    def __invert__(self):
        """Dual Multivector of a Multivector."""
        return self * Multivector3D(pscalar=1)

    def __repr__(self):
        return 'Multivector with components:\nscalar: {}\n' \
               'vector: {}\nbivector: {}\npscalar: {}'.format(
                   self.scalar, self.vector, self.bivector, self.pscalar)


E1 = Multivector3D(vector=[1.0, 0.0, 0.0])
E2 = Multivector3D(vector=[0.0, 1.0, 0.0])
E3 = Multivector3D(vector=[0.0, 0.0, 1.0])
