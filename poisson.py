r"""
Laplace equation using the short syntax of keywords.

See :ref:`diffusion-poisson` for the long syntax version.

Find :math:`t` such that:

.. math::
    \int_{\Omega} c \nabla s \cdot \nabla t
    = 0
    \;, \quad \forall s \;.
"""
from __future__ import absolute_import
from sfepy import data_dir
material={
   'coef':({'val':1.0},),
}
fields={
'temperature':('real',1,'Omega',1),
}
equations={
'Temperature':"""dw_laplace.i.Omega(coef.val, s,t)=0"""
}
integrals={
'i':2,
}

