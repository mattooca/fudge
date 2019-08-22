# <<BEGIN-copyright>>
# Copyright (c) 2011, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
# Written by the LLNL Computational Nuclear Physics group
#         (email: mattoon1@llnl.gov)
# LLNL-CODE-494171 All rights reserved.
# 
# This file is part of the FUDGE package (For Updating Data and 
#         Generating Evaluations)
# 
# When citing FUDGE, please use the following reference:
#   C.M. Mattoon, B.R. Beck, N.R. Patel, N.C. Summers, G.W. Hedstrom, D.A. Brown, "Generalized Nuclear Data: A New Structure (with Supporting Infrastructure) for Handling Nuclear Data", Nuclear Data Sheets, Volume 113, Issue 12, December 2012, Pages 3145-3171, ISSN 0090-3752, http://dx.doi.org/10. 1016/j.nds.2012.11.008
# 
# 
#     Please also read this link - Our Notice and Modified BSD License
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Lawrence Livermore National Security, LLC. nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL LAWRENCE LIVERMORE NATIONAL SECURITY BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# <<END-copyright>>

"""
This module contains a set of routines that return the symbol or name for an ENDL 
incident, yi, or outgoing, yo, particle designator.
"""

endl_yLabels = (
    (  1, "n", "neutron" ), \
    (  2, "p", "proton" ), \
    (  3, "d", "deuteron" ), \
    (  4, "t", "triton" ), \
    (  5, "He3", "helium3" ), \
    (  6, "He", "alpha" ), \
    (  7, "g", "gamma" ), \
    (  8, "e+", "positron" ), \
    (  9, "e-", "electron" ), \
    ( 10, "EC", "electron capture" ), \
    ( 11, "n as residual", "n as residual" ), \
    ( 12, "p as residual", "p as residual" ), \
    ( 13, "d as residual", "d as residual" ), \
    ( 14, "t as residual", "t as residual" ), \
    ( 15, "He3 as residual", "He3 as residual" ), \
    ( 16, "He as residual", "He as residual" ), \
    ( 18, "positron as residual", "positron as residual" ), \
    ( 19, "electron as residual", "electron as residual" ) )

def endl_yLabel( y ) :
    """Returns the symbol for the specified y or 'None' if y is out-of-bounds."""

    for i in endl_yLabels :
        if ( i[0] == y ) : return i[1]
    return None

def endl_yLongLabel( y ) :
    """Returns the label (i.e., name) for the specified y or 'None' if y is out-of-bounds."""

    for i in endl_yLabels :
        if ( i[0] == y ) : return i[2]
    return None

def endl_yLabelMaxWidth( ) :
    """Returns the maximum length of a string returned by endl_yLabel."""

    w = 0
    for i in endl_yLabels :
        if ( w < len( i[1] ) ) : w = len( i[1] )
    return w

def endl_yLongLabelMaxWidth( ) :
    """Returns the maximum length of a string returned by endl_yLongLabel."""

    w = 0
    for i in endl_yLabels :
        if ( w < len( i[2] ) ) : w = len( i[2] )
    return w