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

filename_mesh = data_dir + '/meshes/3d/cylinder.mesh'

regions = {
    'Omega': 'all', # or 'cells of group 6'
    'Gamma_Left': ('vertices in (x<0.00001)', 'facet'),
    'Gamma_Right': ('vertices in (x>0.099999)', 'facet'),
}

variables = {
't' : ('unknown field', 'temperature', 0),
's' : ('test field','temperature', 't'),
}
ebcs = {
't1' : ('Gamma_Left', {'t.0' : 2.0}),
't2' : ('Gamma_Right', {'t.0' : -2.0}),
}
