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

import sys
sys.path.insert( 0, '../../../../../lib' )

import os, copy
import pointwiseXY_C

verbose = False
if( 'CHECKOPTIONS' in os.environ ) :
    options = os.environ['CHECKOPTIONS'].split( )
    if( '-e' in options ) : print __file__
    if( '-v' in options ) : verbose = True

def printXYIfVerbose( XYs, xMin = None, xMax = None, fill = None ) :

    if( verbose ) :
        if( not( xMin is None ) ) :
            print '# xMin =', xMin
            print '# xMax =', xMax
            print '# fill =', fill
        print '# length =', len( XYs )
        print XYs
        print

def checkSlicing( XYs_base, xMin, xMax, fill, length ) :

    XYs = XYs_base.domainSlice( domainMin = xMin, domainMax = xMax, fill = fill )
    printXYIfVerbose( XYs, xMin, xMax, fill )
    if( len( XYs ) != length ) : raise Exception( "%s: len( XYs ) = %d != length = %d: %g %d %d" % \
        ( __file__, len( XYs ), length, xMin, xMax, fill ) )
    xMin_ = max( xMin, XYs_base.domainMin( ) )
    xMax_ = min( xMax, XYs_base.domainMax( ) )
    if( fill ) :
        if( xMin_ != XYs.domainMin( ) ) : raise Exception( "%s: xMin_ = %g != XYs.domainMin( ) = %g: %g %d %d" % ( __file__, xMin_, XYs.domainMin( ), xMin, xMax, fill ) )
        if( xMax_ != XYs.domainMax( ) ) : raise Exception( "%s: xMax_ = %g != XYs.domainMax( ) = %g: %g %d %d" % ( __file__, xMax_, XYs.domainMax( ), xMax, xMax, fill ) )
    else :
        if( xMin_ > XYs.domainMin( ) ) : raise Exception( "%s: xMin_ = %g > XYs.domainMin( ) = %g: %g %d %d" % ( __file__, xMin_, XYs.domainMin( ), xMin, xMax, fill ) )
        if( xMax_ < XYs.domainMax( ) ) : raise Exception( "%s: xMax_ = %g < XYs.domainMax( ) = %g: %g %d %d" % ( __file__, xMax_, XYs.domainMax( ), xMin, xMax, fill ) )

if( verbose ) :
    doc = pointwiseXY_C.pointwiseXY_C.domainSlice.__doc__.split( '\n' )
    for d in doc : print "#", d

XYs = pointwiseXY_C.gaussian( .1, -10, domainMax = 8, sigma = 2.2 )
printXYIfVerbose( XYs )

checkSlicing( XYs, -100, 100, 0, 61 )
checkSlicing( XYs, -100, 100, 1, 61 )

checkSlicing( XYs, -100, 3.3, 0, 43 )
checkSlicing( XYs, -100, 3.3, 1, 44 )

checkSlicing( XYs, -7, 3.3, 0, 19 )
checkSlicing( XYs, -7, 3.3, 1, 21 )

checkSlicing( XYs, 3.3, 100, 0, 18 )
checkSlicing( XYs, 3.3, 100, 1, 19 )