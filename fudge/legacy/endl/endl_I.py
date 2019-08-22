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
This module contains a set of routines that return information about ENDL I-values.
"""

endl_ILabels = (
    (  0,  2, "cross section" ), \
    (  1,  3, "angular dist." ), \
    (  3,  4, "E-angle dist." ), \
    (  4,  4, "l-order E-angle dist." ), \
    (  7,  2, "n_bar / fission" ), \
    (  8,  0, "histogram E dist." ), \
    (  9,  2, "multiplicity" ), \
    ( 10,  2, "secondary ave. E" ), \
    ( 11,  2, "residual ave. E" ), \
    ( 12,  2, "Q(E)" ), \
    ( 13,  2, "momentum" ), \
    ( 20,  4, "URR(E,T)" ), \
    ( 21,  3, "P(E|E_out)" ), \
    ( 22,  3, "angular dist. in (1-mu)" ), \
    ( 80,  0, "Maxwell reaction rate" ), \
    ( 81,  0, "Doppler x-sec." ), \
    ( 84,  0, "Maxwell E dist." ), \
    ( 89,  0, "Maxwell multiplicity" ), \
    ( 90,  0, "Maxwell secondary ave. E" ), \
    ( 91,  0, "Maxwell residual ave. E" ), \
    ( 92,  0, "Maxwell E of reaction part." ) )

def endl_ILabel( I ) :
    """Returns a mnemonic string for the specified I-value. If I-value is not defined than 'None' is returned."""

    for i in endl_ILabels :
        if ( i[0] == I ) : return i[2]
    return None

def endl_ILabelMaxWidth( ) :
    """Returns the maximum length of a string returned by endl_ILabel."""

    w = 0
    for i in endl_ILabels :
        if ( w < len( i[2] ) ) : w = len( i[2] )
    return w

def endl_IColumns( I ) :
    """Returns the number of columns of data for the specified I-value. If I-value is not defined than 'None' is returned."""

    for i in endl_ILabels :
        if ( i[0] == I ) : return i[1]
    return None