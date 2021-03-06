# Copyright Aleksey Gurtovoy 2001-2006
#
# Distributed under the Boost Software License, Version 1.0. 
# (See accompanying file LICENSE_1_0.txt or copy at 
# http://www.boost.org/LICENSE_1_0.txt)
#
# See http://www.boost.org/libs/mpl for documentation.

# $Id$
# $Date$
# $Revision$

import os.path

import preprocess

preprocess.main(
    ["plain"]
    , "list"
    , os.path.join("boost", "mpl", "list", "aux_", "preprocessed")
)
