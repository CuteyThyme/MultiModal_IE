"""
##################################################################################################
# Copyright Info :    Copyright (c) Davar Lab @ Hikvision Research Institute. All rights reserved.
# Filename       :    __init__.py
# Abstract       :

# Current Version:    1.0.0
# Date           :    2020-05-31
##################################################################################################
"""
from .davar_common import *
from .davar_det import *
from .davar_rcg import *
from .davar_spotting import *
from .davar_ie import *
from .mmcv import *
from .version import __version__

__all__ = ['__version__']
