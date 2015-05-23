#! /usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

from heat_utils import solve_2d_heat_eqn, read_params_from_file


def initialize(fname):
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
    temperature = solve_2d_heat_eqn(params['temperature'], params['spacing'],
                                    alpha=params['alpha'],
                                    time_step=params['time_step'])
    params['time'] += params['time_step']


def finalize():
    pass


def main():
    params = initialize('input.yaml')

    while params['time'] < params['end_time']:
        update(params)

        print 'time: %f' % time
        np.savetxt(sys.stdout, temperature, fmt='%.3f')

    finalize()

    plt.imshow(params['temperature'])
    plt.show()


if __name__ == '__main__':
    main()
