import yaml
import numpy as np
from scipy import ndimage, random


def solve_2d_heat_eqn(temp, spacing, out=None, alpha=1., time_step=1.):
    """Solve the 2D Heat Equation on a uniform mesh.

    Parameters
    ----------
    temp : ndarray
        Temperature.
    spacing : array_like
        Grid spacing in the row and column directions.
    out : ndarray (optional)
        Output array.
    alpha : float (optional)
        Thermal diffusivity.
    time_step : float (optional)
        Time step.

    Returns
    -------
    result : ndarray
        The temperatures after time *time_step*.

    Examples
    --------
    >>> from heat import solve_2d
    >>> z0 = np.zeros((3, 3))
    >>> z0[1:-1, 1:-1] = 1.
    >>> solve_2d(z0, (1., 1.), alpha=.125)
    array([[ 0. ,  0. ,  0. ],
           [ 0. ,  0.5,  0. ],
           [ 0. ,  0. ,  0. ]])
    """
    dy2, dx2 = spacing[0] ** 2, spacing[1] ** 2
    stencil = np.array([[0., dy2, 0.],
                        [dx2, -2. * (dx2 + dy2), dx2],
                        [0., dy2, 0.]]) * alpha * time_step / (dx2 * dy2)

    if out is None:
        out = np.empty_like(temp)

    ndimage.convolve(temp, stencil, output=out)
    out[(0, -1), :] = 0.
    out[:, (0, -1)] = 0.
    return np.add(temp, out, out=out)


def read_params_from_file(fname):
    """Read model parameters from a file.

    Parameters
    ----------
    fname : str
        Name of YAML-formatted parameters file.

    Returns
    -------
    dict
        A dict of parameters for the heat model.
    """
    with open(fname, 'r') as fp:
        params = yaml.load(fp)

    params.setdefault('shape', (10, 20))
    params.setdefault('spacing', (1., 1.))
    params.setdefault('alpha', 1)
    params.setdefault('end_time', 100.)

    return params
