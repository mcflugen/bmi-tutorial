#! /usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

from heat_utils import solve_2d_heat_eqn, read_params_from_file


def initialize(fname):
    """Initialize the heat model.

    Parameters
    ----------
    fname : str
        Name of the YAML-formatted input file.

    Returns
    -------
    dict
        Parameters for the heat model as a dict.
    """
    params = read_params_from_file('input.yaml')

    dy, dx = params['spacing']
    n_rows, n_cols = params['shape']
    alpha = params['alpha']

    time_step = (dx ** 2. * dy ** 2.) / (2. * alpha * (dx ** 2. + dy ** 2.))
    time_step *= 0.9

    temperature = np.zeros((n_rows, n_cols))
    temperature[n_rows / 2, n_cols / 2] = 100.

    time = 0.

    params['time_step'] = time_step
    params['time'] = time
    params['temperature'] = temperature

    return params


def update(params):
    """Update the heat model one time step.

    Parameters
    ----------
    params : dict
        Heat model parameters as a dict.
    """
    temperature = solve_2d_heat_eqn(params['temperature'], params['spacing'],
                                    alpha=params['alpha'],
                                    time_step=params['time_step'])
    params['temperature'] = temperature
    params['time'] += params['time_step']


def finalize():
    """Finalize the heat model."""
    pass


def main():
    params = initialize('input.yaml')

    while params['time'] < params['end_time']:
        update(params)

        print 'time: %f' % params['time']
        np.savetxt(sys.stdout, params['temperature'], fmt='%.3f')

    finalize()

    plt.imshow(params['temperature'])
    plt.show()


if __name__ == '__main__':
    main()
