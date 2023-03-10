import contextlib
from collections import namedtuple
import datetime
from decimal import Decimal
from functools import partial
import inspect
import io
from itertools import product
import platform
from types import SimpleNamespace

import dateutil.tz

import numpy as np
from numpy import ma
from cycler import cycler
import pytest

import matplotlib
import matplotlib as mpl
from matplotlib import rc_context
from matplotlib._api import MatplotlibDeprecationWarning
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import matplotlib.font_manager as mfont_manager
import matplotlib.markers as mmarkers
import matplotlib.patches as mpatches
import matplotlib.path as mpath
from matplotlib.projections.geo import HammerAxes
from matplotlib.projections.polar import PolarAxes
import matplotlib.pyplot as plt
import matplotlib.text as mtext
import matplotlib.ticker as mticker
import matplotlib.transforms as mtransforms
import mpl_toolkits.axisartist as AA
from numpy.testing import (
    assert_allclose, assert_array_equal, assert_array_almost_equal)
from matplotlib.testing.decorators import (
    image_comparison, check_figures_equal, remove_ticks_and_titles)


def test_boxplot_empty_string():
    data = np.random.rand(5, 3)
    fig, axs = plt.subplots(9)

    axs[0].boxplot(data, sym='')

    # Assert that the plot has no outlier symbols
    for line in axs[0].get_lines():
        assert line.get_marker() == ''


def test_boxplot_patchArtist_color():
    data = np.random.rand(5, 3)
    fig, axs = plt.subplots()
    boxprops = {'color': 'red'}
    bxp_handle = axs.boxplot(data, boxprops=boxprops, patch_artist=True)

    # Assert that the 'color' key is removed from the boxprops dict
    for bxp_artist in bxp_handle['boxes']:
        assert bxp_artist.get_edgecolor() != 'red' and bxp_artist.get_facecolor() != 'red'

