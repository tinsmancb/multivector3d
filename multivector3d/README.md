# Multivector3D
Basic python class for a 3D multivector, implemented using numpy for efficient
numerical computation. The following operations are implemented:

```python
from multivector3d import Multivector3D

a = Multivector3D(vector=[1,2,3])
b = Multivector3D(bivector=[4,5,6])
c = 2.0
```

* `a+b` Addition
* `a*c` Scalar multiplication (limitation: scalar must be on the right)
* `a/c` Scalar division
* `a*b` Geometric product
* `a.dot(b)` Dot product
* `a^b` Wedge product
* `~a` Dual multivector (multiplication by unit pseudoscalar)

The multivector attributes for the four grades, each of which can be specified
in the constructor:

* `a.scalar` Scalar
* `a.vector` Vector, in the canonical `{e_1, e_2, e_3}` basis
* `a.bivector` Bivector, in the `{e_2 e_3, e_3 e_1, e_1 e_2}` basis
* `a.pscalar` Pseudoscalar `e_1 e_2 e_3`.

This project is more of an academic exercise than anything production ready at
this point. If you want to do computations with the geometric algebra in python,
check out the [clifford](https://clifford.readthedocs.io/en/latest/) package.

## Installation

The package can be installed from pip: `pip install multivector3d`. The only 
dependency is numpy.
