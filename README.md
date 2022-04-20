# Compositions

An extensive package for compositional data analysis. The major implementations are presented as follows.

Various transformation functions along with their inverses have been implemented to aid in compositional data analysis (CoDA).

## Install

<pre><code> pip install compositions-coda</code></pre>

## Usage

Import ```transforms```:

<pre><code>from compositions import transform</code></pre>

- Centered Log Ratio (clr)
  - ```transform.clr``` for the forward transformation $S^D\rightarrow \mathbb{R}^D$.
  - ```transform.clrInv``` as the inverse function $\mathbb{R}^D\rightarrow S^D$.

- Isometric Log Ratio (ilr)
  - ```transform.ilr``` for forward transformation $S^D\rightarrow \mathbb{R}^{D-1}$.
  - ```transform.ilrInv``` for inverse transform $\mathbb{R}^{D-1}\rightarrow S^D$.
  
- Additive Log Ratio (alr)
  - ```transform.alr``` for forward transform $S^D\rightarrow \mathbb{R}^{D-1}$.
  - ```transform.alrInv``` for inverse transform R^D-1 &#8594; S^D.

## Example
