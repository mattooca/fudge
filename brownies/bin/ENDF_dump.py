#! /usr/bin/env python3

# <<BEGIN-copyright>>
# Copyright 2022, Lawrence Livermore National Security, LLC.
# See the top-level COPYRIGHT file for details.
# 
# SPDX-License-Identifier: BSD-3-Clause
# <<END-copyright>>

description = '''
Separates an ENDF-6 formatted file into separate files by MT, MF, etc. The files are written into the directory specified by
the second positional argument. The output directory is created anew. Ergo, if the output directory exist, it is first deleted
and then recreated.

Currently, only MF 3, 4, 6 and 26 are supported for writing to a files.
'''

import pathlib
import shutil
import argparse

from brownies.legacy.converting.ENDFToGNDS import endfFileToGNDSMisc
from brownies.legacy.converting.ENDFToGNDS import endfFileToGNDSMisc as endfFileToGNDSMiscModule

def printlines(fOut, label, index1, index2, MFData):
    '''Writes to *fOut* all lines of *MFData* in the range [*index1*, *index2*]. Adds the string *label* to the end of the first line.'''

    for index in range(index1, index2):
        print('%s%s' % (MFData[index], label), file=fOut)
        label = ''

def LIST(fOut, label, lineIndex, MFData):
    '''Writes to *fOut* an ENDF-6 list record that starts a line *lineIndex* of *MFData*.'''

    priorIndex = lineIndex
    dummy, dummy, dummy, dummy, NLP, dummy = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
    NLP = int(NLP)
    lineIndex += 1 + (NLP + 5) // 6
    printlines(fOut, label, priorIndex, lineIndex, MFData)

    return lineIndex

def TAB1(fOut, label, lineIndex, MFData):
    '''Writes to *fOut* an ENDF-6 tab1 record that starts a line *lineIndex* of *MFData*.'''

    priorIndex = lineIndex
    dummy, dummy, dummy, dummy, NR, NP = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
    NR, NP = int(NR), int(NP)
    lineIndex += 1 + (NR + 2) // 3
    lineIndex += (NP + 2) // 3
    printlines(fOut, label, priorIndex, lineIndex, MFData)

    return lineIndex

def TAB2header(fOut, label, lineIndex, MFData):
    '''Writes the header information for an ENDF-6 tab2 record.'''

    priorIndex = lineIndex
    dummy, dummy, dummy, dummy, NR, NZ = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
    NR, NZ = int(NR), int(NZ)
    lineIndex += 1 + (NR + 2) // 3

    printlines(fOut, label, priorIndex, lineIndex, MFData)

    return NZ, lineIndex

def TAB2withLIST(fOut, label, lineIndex, MFData):
    '''Writes to *fOut* an ENDF-6 tab2 record that starts a line *lineIndex* of *MFData* and contains list records.'''

    NZ, lineIndex = TAB2header(fOut, '', lineIndex, MFData)
    for indexZ in range(NZ):
        lineIndex = LIST(fOut, label, lineIndex, MFData)

    return lineIndex

def TAB2withTAB1(fOut, label1, label2, lineIndex, MFData):
    '''Writes to *fOut* an ENDF-6 tab2 record that starts a line *lineIndex* of *MFData* and contains tab1 records.'''

    NZ, lineIndex = TAB2header(fOut, label1, lineIndex, MFData)
    for indexZ in range(NZ):
        lineIndex = TAB1(fOut, label2, lineIndex, MFData)

    return lineIndex

def LAW0(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 0 data.'''

    return lineIndex

def LAW1(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 1 data.'''

    return TAB2withLIST(fOut, ' Energy', lineIndex, MFData)

def LAW2(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 2 data.'''

    return LAW1(fOut, lineIndex, MFData)

def LAW3(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 3 data.'''

    return lineIndex

def LAW4(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 4 data.'''

    return lineIndex

def LAW5(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 5 data.'''

    return LAW1(fOut, lineIndex, MFData)

def LAW6(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 6 data.'''

    APSX, dummy, dummy, dummy, dummy, NPSX = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
    printlines(fOut, '', lineIndex, lineIndex+1, MFData)
    return lineIndex + 1

def LAW7(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 7 data.'''

    priorIndex = lineIndex
    dummy, dummy, dummy, dummy, NR, NE = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
    NR, NE = int(NR), int(NE)
    lineIndex += 1 + (NR + 2) // 3
    printlines(fOut, '', priorIndex, lineIndex, MFData)

    for energyIndex in range(NE):
        lineIndex = TAB2withTAB1(fOut, ' Energy', ' mu', lineIndex, MFData)

    return lineIndex

def LAW8(fOut, lineIndex, MFData):
    '''Writes to *fOut* MF 6, law 8 data.'''

    return TAB1(fOut, '', lineIndex, MFData)

def process(args):
    '''Code that loops over MTs and MFs, writing the MT/MF data to separate files.'''

    header, MAT, MTDatas = endfFileToGNDSMisc.parseENDFByMT_MF(args.inputFile, stripMATMFMTCount=False)
    for MT in MTDatas:
        MFDatas = MTDatas[MT]
        for MF in [3, 4, 6, 26]:
            filePrefix = 'MT_%.3d.MF_%.3d' % (MT, MF)
            if MF in MFDatas:
                lineIndex = 0
                MFData = MFDatas[MF]
                if MF == 3:
                    fileName = pathlib.Path(outputDir) / filePrefix
                    with fileName.open('w') as fOut:
                        TAB1(fOut, '', 1, MFData)
                elif MF == 4:
                    priorIndex = lineIndex
                    ZA,    AWR, dummy, LTT,   dummy, dummy = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
                    dummy, AWR, LI,    dummy, dummy, dummy = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex+1])
                    lineIndex += 2

                    LTT = int(LTT)
                    fileName = '%s.LTT_%s' % (filePrefix, LTT)
                    fileName = pathlib.Path(outputDir) / fileName
                    with fileName.open('w') as fOut:
                        printlines(fOut, '', priorIndex, lineIndex, MFData)

                        if LTT == 0:
                            pass
                        elif LTT == 1:
                            lineIndex = TAB2withLIST(fOut, ' Energy', lineIndex, MFData)
                        elif LTT == 2:
                            lineIndex = TAB2withTAB1(fOut, '', ' Energy', lineIndex, MFData)
                        elif LTT == 3:
                            lineIndex = TAB2withLIST(fOut, ' Energy', lineIndex, MFData)
                            lineIndex = TAB2withTAB1(fOut, '', ' Energy', lineIndex, MFData)
                elif MF in [6, 26]:
                    ZA, AWR, JP, LCT, NK, dummy = endfFileToGNDSMiscModule.sixFunkyFloatStringsToFloats(MFData[lineIndex])
                    NK = int(NK)
                    lineIndex += 1
                    for productIndex in range(NK):
                        priorIndex = lineIndex
                        lineIndex, productData, multiplicityRegions = endfFileToGNDSMiscModule.getTAB1Regions(lineIndex, MFData)
                        ZAP, AWP, LIP, LAW, NP = int(productData['C1']), productData['C2'], productData['L1'], int(productData['L2']), productData['NR']

                        fileName = '%s.%s.ZA_%.6d.LAW_%s' % (filePrefix, productIndex, ZAP, LAW)
                        fileName = pathlib.Path(outputDir) / fileName
                        with fileName.open('w') as fOut:
                            printlines(fOut, '', priorIndex, lineIndex, MFData)

                            if LAW == 0:
                                lineIndex = LAW0(fOut, lineIndex, MFData)
                            if LAW == 1:
                                lineIndex = LAW1(fOut, lineIndex, MFData)
                            if LAW == 2:
                                lineIndex = LAW2(fOut, lineIndex, MFData)
                            if LAW == 3:
                                lineIndex = LAW3(fOut, lineIndex, MFData)
                            if LAW == 4:
                                lineIndex = LAW4(fOut, lineIndex, MFData)
                            if LAW == 5:
                                lineIndex = LAW5(fOut, lineIndex, MFData)
                            if LAW == 6:
                                lineIndex = LAW6(fOut, lineIndex, MFData)
                            if LAW == 7:
                                lineIndex = LAW7(fOut, lineIndex, MFData)
                            if LAW == 8:
                                lineIndex = LAW8(fOut, lineIndex, MFData)

                        if lineIndex < 0:
                            break

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('inputFile', type=pathlib.Path, help='Input ENDF-6 file.')
    parser.add_argument('outputDir', type=pathlib.Path, help='Output directory where all data are written.')

    args = parser.parse_args()

    outputDir = args.outputDir
    if outputDir.exists():
        if not outputDir.is_dir():
            raise TypeError('Output must be a directory.')
        shutil.rmtree(outputDir)
    outputDir.mkdir()

    process(args)
