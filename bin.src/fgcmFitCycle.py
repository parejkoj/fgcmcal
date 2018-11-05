#!/usr/bin/env python
# See COPYRIGHT file at the top of the source tree.
import matplotlib
matplotlib.use("Agg")  # noqa

from lsst.fgcmcal.fgcmFitCycle import FgcmFitCycleTask

FgcmFitCycleTask.parseAndRun()
