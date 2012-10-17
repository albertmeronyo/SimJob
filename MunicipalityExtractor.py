#!/usr/bin/env python

"""MunicipalityExtractor.py: A municipality label extractor for XLS files."""

import csv
from xlrd import open_workbook

class MunicipalityExtractor:
    """An XLS municipality-label extractor"""

    def __init__(self):
        # Struct initialization
        self.municipalitiesPerSheet = {}
        

    def doMunicipalityExtraction(self, inputDataFile, col, row, lim):
        """Extract municipality names from specified location, column 
        top-bottom until lim"""

        # print "Harvesting data from input file {}...".format(inputDataFile)

        # Open workbook for input data
        self.inputDataFile = inputDataFile
        self.sourceData = open_workbook(self.inputDataFile, formatting_info=True)
        self.sourceSheet = self.sourceData.sheet_by_index(0)

        self.municipalitiesPerSheet[self.inputDataFile] = set()

        for i in range(row-1, lim):
            self.cell = self.sourceSheet.cell(i, col)
            if str(self.cell.value).strip() != "":
                self.municipalitiesPerSheet[self.inputDataFile].add(self.cell.value)


    def serialize(self, outputDataFile):
        """Write municipalities found in specified output"""

        # print "Serializing to output file..."

        with open(outputDataFile, 'wb') as csvfile:
            self.csvwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            for key in self.municipalitiesPerSheet.keys():
                self.csvwriter.writerow([key] + list(self.municipalitiesPerSheet[key]))
                print key
                for m in list(self.municipalitiesPerSheet[key]):
                    print m

        print len(self.municipalitiesPerSheet)


if __name__ == "__main__":
    munExtractorInstance = MunicipalityExtractor()
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_03_T1.xls', 0, 8, 6678)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_04_T1.xls', 0, 8, 11127)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_05_T1.xls', 0, 8, 2781)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_06_T1.xls', 0, 8, 6762)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_07_T1.xls', 0, 8, 10855)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_08_T1.xls', 0, 8, 8607)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_09_T1.xls', 0, 8, 10410)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_10_T1.xls', 0, 8, 2402)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_11_T1.xls', 0, 9, 2507)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_12_T1.xls', 0, 8, 8011)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1889_13_T1.xls', 0, 8, 2698)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_01_T.xls', 0, 9, 9596)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_02_T.xls', 0, 9, 11462)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_03_T.xls', 0, 9, 17843)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_04_T.xls', 0, 9, 13757)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_05_T.xls', 0, 9, 3240)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_06_T.xls', 0, 9, 4888)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_07_T.xls', 0, 9, 9500)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_08_T.xls', 0, 9, 9081)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_09_T.xls', 0, 9, 6577)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_10_T.xls', 0, 9, 2767)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1899_11_T.xls', 0, 9, 5775)
    munExtractorInstance.doMunicipalityExtraction('data/BRT_1909_01_T.xls', 0, 6, 36935)
    munExtractorInstance.serialize('output.csv')


__author__ = "Albert Meronyo-Penyuela"
__copyright__ = "Copyright 2012, VU University Amsterdam"
__credits__ = ["Albert Meronyo-Penyuela"]
__license__ = "LGPL v3.0"
__version__ = "0.1"
__maintainer__ = "Albert Meronyo-Penyuela"
__email__ = "albert.merono@vu.nl"
__status__ = "Prototype"

