#!/usr/bin/env python3
"""solve.py: Single model solver for openCEM"""
__version__ = "0.1.1"
__author__ = "José Zapata"
__copyright__ = "Copyright 2018, ITP Renewables, Australia"
__credits__ = ["José Zapata", "Dylan McConnell", "Navid Hagdadi"]
__license__ = "?GPL"
__maintainer__ = "José Zapata"
__email__ = "jose.zapata@itpau.com.au"
__status__ = "Development"

import argparse
import datetime
import os
import shutil
import subprocess
import time

from cemo.multi import SolveTemplate


def valid_file(param):
    base, ext = os.path.splitext(param)
    if ext not in ('.cfg'):
        raise argparse.ArgumentTypeError('File must have a cfg extension')
    return param


# start the clock on the run
start_time = time.time()

# create parser object
parser = argparse.ArgumentParser(description="openCEM multiyear model solver")

# Multi year simulation option using a configuration file
parser.add_argument(
    "config",
    help="Specify a configuration file for simulation" +
    " Note: Python configuration files named CONFIG.cfg",
    type=lambda f: valid_file(f),
    metavar='CONFIG')
# Obtain a solver name from command line, default cbc
parser.add_argument(
    "--solver",
    help="Specify solver used by model." +
    " For Pyomo supported solvers installed in your system ",
    type=str,
    metavar='SOLVER',
    default="cbc")

# Zip and upload result to custom directory
parser.add_argument(
    "--dir",
    help="Copy results to folder",
    type=str,
    metavar='DIR')

# parse arguments into args structure
args = parser.parse_args()

# Read configuration file name from
cfgfile = args.config
# create Multi year simulation
X = SolveTemplate(cfgfile, solver=args.solver)
# instruct the solver to launch the multi year simulation
print("openCEM msolve.py: Runtime %s (pre solver)" % str(
    datetime.timedelta(seconds=(time.time() - start_time))))
X.solve()
print("openCEM msolve.py: Runtime %s (post solver)" % str(
    datetime.timedelta(seconds=(time.time() - start_time))))

if args.dir:
    outname = X.Name + "_sol.json"
    subprocess.run(["gzip", outname])
    outname = outname + ".gz"
    shutil.copy2(outname, args.dir)
