#!/usr/bin/env python
# coding: UTF-8
from __future__ import division

from pychebfun import *

import numpy as np
np.seterr(all='raise')
import numpy.testing as npt

import unittest

from .tools import *

plot_res = 200

class TestPlot(unittest.TestCase):
    def setUp(self):
        # Constuct the O(dx^-16) "spectrally accurate" chebfun p
        self.p = Chebfun.from_function(f)

    def test_plot(self):
        xs,ys,xi,yi,d = plot_data(self.p, plot_res)
        self.assertEqual(d, 1)
        npt.assert_allclose(ys, f(xs))
        plot(self.p)

    def test_plot_interpolation_points(self):
        plt.clf()
        plot(self.p, with_interpolation_points=True)
        a = plt.gca()
        self.assertEqual(len(a.lines),2)
        plt.clf()
        plot(self.p, with_interpolation_points=False)
        a = plt.gca()
        self.assertEqual(len(a.lines),1)

    def test_cheb_plot(self):
        compare(self.p, f)

    def test_chebcoeffplot(self):
        chebcoeffplot(self.p)

    def test_plot_circle(self):
        T = .5
        def cirper(x):
            return circle(x, period=T)
        c = Chebfun.from_function(cirper, domain=[0,T])
        xs,ys,xi,yi,d = plot_data(c, plot_res)
        self.assertEqual(d, 2,)
        for X,Y in [(xs,ys), (xi,yi)]:
            dist = np.square(X) + np.square(Y)
            npt.assert_allclose(dist, 1, err_msg="The plot should be a circle")
        plot(c)

    def test_plot_complex(self):
        c = np.exp(1j*Chebfun.identity(domain=[-np.pi,np.pi]))
        xs,ys,xi,yi,d = plot_data(c, plot_res)
        self.assertEqual(d, 2, "dimension is two for complex chebfun")
        for X,Y in [(xs,ys), (xi,yi)]:
            dist = np.square(X) + np.square(Y)
            npt.assert_allclose(dist, 1, err_msg="The plot should be a circle")
        plot(c)

    def test_too_many_dimensions(self):
        c = Chebfun.from_data(np.random.random_sample([3,4]))
        with self.assertRaises(ValueError):
            plot(c)

    def test_error(self):
        chebpolyplot(self.p)


