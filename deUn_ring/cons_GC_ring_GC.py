import gdshelpers
import numpy as np
from gdshelpers.geometry.chip import Cell
from gdshelpers.parts.resonator import RingResonator
from gdshelpers.parts.port import Port
from gdshelpers.parts.waveguide import Waveguide
from gdshelpers.parts.coupler import GratingCoupler
from gdshelpers.helpers.positive_resist import convert_to_positive_resist


class GC_ring_GC(object):

    pi = np.pi

    def __init__(self, username, wg_length, radius, wg_width, ring_width, gap, resist_type):
        self.username = username
        self.wg_length = wg_length
        self.radius = radius
        self.wg_width = wg_width
        self.ring_width = ring_width
        self.gap = gap
        self.resist_type = resist_type

    def microringL(self):
        return self.radius * self.radius * self.pi

    def deUn_ring(self):
        period = 550

        center_x = [0, 2 * period, 4 * period, 6 * period, 8 * period]
        center_y = [0, period, 2 * period, 3 * period, 4 * period]

        # center_y = 0
        waveguide_width = 0.850
        waveguide_length = 500
        coupling_length = 20
        Gap = [.700, .800, .900, 1, 1.2]
        Radius = [25, 50, 75, 125, 150]
        bend_radius = 30
        cell = Cell('CELL')

        coupler_params = {
            'width': waveguide_width,
            'full_opening_angle': np.deg2rad(36),
            'grating_period': 1.2,
            'grating_ff': 1 - 0.4,
            'n_gratings': 20,
            'ap_max_ff': 1 - 0.04,
            'n_ap_gratings': 20,
            'taper_length': 48.
        }

        for k in range(5):
            for i in range(5):
                wg_1 = Waveguide.make_at_port(Port((center_x[k], center_y[i]), angle=0, width=waveguide_width))
                wg_1.add_straight_segment(waveguide_length / 2)
                wg_2 = Waveguide.make_at_port(Port((center_x[k], center_y[i]), angle=self.pi, width=waveguide_width))
                wg_2.add_straight_segment(waveguide_length / 2)
                left_coupler = GratingCoupler.make_traditional_coupler_at_port(wg_2.current_port, angle=self.pi,
                                                                               **coupler_params)
                right_coupler = GratingCoupler.make_traditional_coupler_at_port(wg_1.current_port, angle=0,
                                                                                **coupler_params)
                resonator_1 = RingResonator.make_at_port(wg_2.in_port, gap=Gap[i], radius=Radius[k])

                # Negative Resist
                # cell.add_to_layer(1,wg_1,mzi_1,wg_2,left_coupler,right_coupler)
                # Positive Resist
                if (self.resist_type == 'positive'):

                    cell.add_to_layer(1, convert_to_positive_resist(parts=[wg_1, wg_2, left_coupler, right_coupler],
                                                                buffer_radius=3))
                    cell.add_to_layer(2, convert_to_positive_resist(parts=[resonator_1], buffer_radius=3))
                else:
                    print(self.username, 'you should set the resist type to "positive"')


        cell.show()
        cell.save('GC_ring_GC_test_Mar23rd.gds')



ring1 = GC_ring_GC('Zizheng', 1.55, np.array([25, 50, 75, 125, 150]), 0.800, 0.800, np.array([.700, .800, .900, 1, 1.2]), 'positive')
perimeter = ring1.microringL()
print(perimeter)
construct_ring_matrix = ring1.deUn_ring()
