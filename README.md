# Compositions

An extensive package for compositional data analysis. The major implementations are presented as follows.

Various transformation functions along with their inverses have been implemented to aid in compositional data analysis (CoDA).

## Install

<pre><code> pip install compositions-coda</code></pre>

## Usage

Import ```transforms```:

<pre><code>from compositions import transform</code></pre>

- Centered Log Ratio (clr)
  - ```transform.clr``` for the forward transformation S<sup>D</sup> &#8594; R<sup>D</sup>.
  - ```transform.clrInv``` as the inverse function R<sup>D</sup> &#8594; S<sup>D</sup>.

- Isometric Log Ratio (ilr)
  - ```transform.ilr``` for forward transformation S<sup>D</sup> &#8594; R<sup>D-1</sup>.
  - ```transform.ilrInv``` for inverse transform R<sup>D-1</sup> &#8594; S<sup>D</sup>.
  
- Additive Log Ratio (alr)
  - ```transform.alr``` for forward transform S<sup>D</sup> &#8594; R<sup>D-1</sup>.
  - ```transform.alrInv``` for inverse transform R<sup>D-1</sup> &#8594; S<sup>D</sup>.

## Example
