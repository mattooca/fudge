#!/usr/bin/env python
# encoding: utf-8

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
test fudge/core/utilities
cmattoon, 3/24/2011
"""

import unittest
from fudge.core import utilities

class brb_test(unittest.TestCase):
    def setUp(self):
        self.brb = utilities.brb
    
    def test1(self):
        # ???
        pass

class testReactionStrings(unittest.TestCase):
    def setUp(self):
        self.RS = utilities.reactionStrings
    
    def test1(self):
        for reac in ("n + Th232 -> Th233 + gamma",
            "n + Th232 -> n + (Th232_e2 -> He4 + (Ra228 -> He4 + Rn224))",
            "H2 + H3 -> n + He4",
            "n + C11 -> (C12 -> He4 + (Be8 -> He4[multiplicity:'2']))",
            "n + Fe56 -> n + Fe56 [compound]",
            "gamma + Pu239 -> n[multiplicity:'energyDependent', decayRate:'1.45210000e-02'] + Pu238",
            "n + Cl35 -> n + Cl35_s",
            "n + Pu239 -> n[multiplicity:'energyDependent', emissionMode:'prompt'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'1.32710000e-02'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'3.08810000e-02'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'1.13370000e-01'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'2.92500000e-01'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'8.57490000e-01'] + n[multiplicity:'energyDependent', emissionMode:'delayed', decayRate:'2.72970000e+00'] + gamma[multiplicity:'energyDependent'] [total fission]"
            ):
            self.assertEqual( reac, str(self.RS.parseReaction(reac)) )
    
    def test2(self):
        # should handle extra spaces, etc:
        string = "H2+Rb87  ->n[multiplicity: 'energyDependent'][fake string]"
        parsed = self.RS.parseReaction(string)
        self.assertEqual( str(parsed.target), "Rb87" )
        self.assertEqual( parsed.info, "fake string" )
        self.assertEqual( str(parsed), "H2 + Rb87 -> n[multiplicity:'energyDependent'] [fake string]" )
        pass
if __name__ == '__main__':
    unittest.main()
