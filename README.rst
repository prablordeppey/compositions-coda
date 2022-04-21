Compositions
============

An extensive package for compositional data analysis. The major implementations are presented as follows.

Various transformation functions along with their inverses have been implemented to aid in compositional data analysis (CoDA).

Install
-------

.. code:: python
	pip install compositions-coda

Usage
-----

1. Transformations:

	- Centered Log Ratio (clr)
		- ```transform.clr``` for the forward transformation S :sup:`D` $Hello$ R<sup>D</sup>.
		- ```transform.clrInv``` for the inverse transform R<sup>D</sup> &#8594; S<sup>D</sup>.

	- Isometric Log Ratio (ilr)
		- ```transform.ilr``` for forward transformation S<sup>D</sup> &#8594; R<sup>D-1</sup>.
		- ```transform.ilrInv``` for the inverse transform R<sup>D-1</sup> &#8594; S<sup>D</sup>.

	- Additive Log Ratio (alr)
		- ```transform.alr``` for forward transform S<sup>D</sup> &#8594; R<sup>D-1</sup>.
		- ```transform.alrInv``` for the inverse transform R<sup>D-1</sup> &#8594; S<sup>D</sup>.

### Example

.. code:: python
	>> import numpy as np
	>> from compositions import transform
