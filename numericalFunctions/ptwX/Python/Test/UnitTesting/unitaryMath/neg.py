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

import listOfDoubles_C
import os, random

if( 'CHECKOPTIONS' in os.environ ) :
    options = os.environ['CHECKOPTIONS'].split( )
    if( '-e' in options ) : print __file__

def compareLists( list1, CList ) :

    CList2 = [ item for item in CList ]
    Pylist = [ -x  for x in list1 ]
    if( Pylist != CList2 ) :
        print list1
        print Pylist
        print CList2
        raise Exception( 'List differ' )

def check( list1 ) :

    CList1 = listOfDoubles_C.listOfDoubles_C( list1 )
    CList2 = -CList1
    compareLists( list1, CList2 )

values1 = xrange( -3, 5 )
values2 = xrange( -300, 5000 )
for i1 in xrange( 100 ) :
    check( [ float( random.choice( values1 ) ) for j1 in xrange( random.choice( values1 ) ) ] )
    check( [ float( random.choice( values2 ) ) for j1 in xrange( random.choice( values2 ) ) ] )