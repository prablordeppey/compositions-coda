Compositions
============

An extensive package for compositional data analysis. The major implementations are presented as follows.

Various transformation functions along with their inverses have been implemented to aid compositional data analysis (CoDA).

Installation
------------

::
	
	pip install compositions-coda

Usage
-----

1. **Transformations**:

	::
		
		from compositions import transform

	.. role::  raw-html(raw)
		:format: html
		
	- Centered Log Ratio (clr)
		- ``transform.clr`` for forward transformation S :sup:`D` :raw-html:`&rarr;` R :sup:`D`.
		- ``transform.clrInv`` for inverse transform R :sup:`D` :raw-html:`&rarr;` S :sup:`D`.

	- Isometric Log Ratio (ilr)
		- ``transform.ilr`` for forward transformation S :sup:`D` :raw-html:`&rarr;` R :sup:`D-1`.
		- ``transform.ilrInv`` for inverse transform R :sup:`D-1` :raw-html:`&rarr;` S :sup:`D`.

	- Additive Log Ratio (alr)
		- ``transform.alr`` for forward transform S :sup:`D` :raw-html:`&rarr;` R :sup:`D-1`.
		- ``transform.alrInv`` for inverse transform R :sup:`D-1` :raw-html:`&rarr;` S :sup:`D`.		
