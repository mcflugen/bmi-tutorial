#! /usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt

from heat_utils import solve_2d_heat_eqn, read_params_from_file


class Heat(object):
    _input_var_names = ('temperature', )
    _output_var_names = ('temperature', )

    def __init__(self):
        self._spacing = (1., 1.)
        self._alpha = 1.
        self._time_step = 1.

        self.time = 0.
        self.end_time = 20.
        self.temperature = None

    def initialize(self, fname):
        params = read_params_from_file('input.yaml')

        dy, dx = params['spacing']
        n_rows, n_cols = params['shape']
        alpha = params['alpha']

        time_step = ((dx ** 2. * dy ** 2.) /
                     (2. * alpha * (dx ** 2. + dy ** 2.)))
        time_step *= 0.9

        self.temperature = np.zeros((n_rows, n_cols))
        self.temperature[n_rows / 2, n_cols / 2] = 100.

        self._alpha = alpha
        self._spacing = (dy, dx)
        self._time_step = time_step
        self.time = 0.
        self.end_time = params['end_time']

    def update(self):
        self.temperature[:] = solve_2d_heat_eqn(self.temperature, self._spacing,
                                                alpha=self._alpha,
                                                time_step=self._time_step)
        self.time += self._time_step

    def finalize(self):
        pass

    def get_input_var_names(self):
        raise NotImplementedError('implement this!')

    def get_output_var_names(self):
        raise NotImplementedError('implement this!')

    def get_var_grid(self, name):
        raise NotImplementedError('implement this!')

    def get_var_itemsize(self, name):
        raise NotImplementedError('implement this!')

    def get_var_nbytes(self, name):
        raise NotImplementedError('implement this!')

    def get_var_type(self, name):
        raise NotImplementedError('implement this!')

    def get_var_units(self, name):
        raise NotImplementedError('implement this!')

    def get_value(self, name):
        raise NotImplementedError('implement this!')

    def set_value(self, name):
        raise NotImplementedError('implement this!')

    def get_grid_type(self, grid):
        raise NotImplementedError('implement this!')

    def get_grid_shape(self, grid):
        raise NotImplementedError('implement this!')

    def get_grid_spacing(self, grid):
        raise NotImplementedError('implement this!')

    def get_grid_origin(self, grid):
        raise NotImplementedError('implement this!')

    def get_grid_rank(self, grid):
        raise NotImplementedError('implement this!')


def main():
    model = Heat()
    model.initialize('input.yaml')

    while model.time < model.end_time:
        model.update()

        print 'time: %f' % model.time
        np.savetxt(sys.stdout, model.get_value('temperature'), fmt='%.3f')

    model.finalize()

    plt.imshow(model.get_value('temperature'))
    plt.show()


if __name__ == '__main__':
    main()
