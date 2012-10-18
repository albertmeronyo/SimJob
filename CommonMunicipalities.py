#!/usr/bin/env python

"""CommonMunicipalities.py: A column-wide, common-municipality comparator."""

import csv
from Levenshtein import ratio

class CommonMunicipalities:
    """A per column CSV common-string comparator"""

    def __init__(self, inputDataFile):
        # Struct initialization
        self.municipalitiesPerYear = {}
        self.municipalitiesPerYear["1899"] = []
        self.municipalitiesPerYear["1889"] = []
        self.municipalitiesPerYear["1909"] = []

        self.commonMunicipalities = []
        

        # Read data
        with open(inputDataFile, 'rb') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=',', quotechar='\'')
            for row in csvReader:
                if row[0].strip() != "":
                    self.municipalitiesPerYear["1899"].append(row[0])
                if row[1].strip() != "":                    
                    self.municipalitiesPerYear["1889"].append(row[1])
                if row[2].strip() != "":
                    self.municipalitiesPerYear["1909"].append(row[2])


    def doStringMatch(self):
        """Extract a list of common municipalities"""

        print "Extracting common municipalities..."

        for municipality in self.municipalitiesPerYear["1899"]:
            if municipality in self.municipalitiesPerYear["1889"] and municipality in self.municipalitiesPerYear["1909"]:
                self.commonMunicipalities.append(municipality)

        print len(self.commonMunicipalities)

    def doStringSimilarity(self):
        """Extract a list of fuzzy-common municipalities"""

        print "Extracting similar municipalities..."

        for municipality in self.municipalitiesPerYear["1899"]:
            max_r1 = 0
            mostSimilarMunicipality1 = ""
            for m2 in self.municipalitiesPerYear["1889"]:
                r = ratio(municipality.lower(), m2.lower())
                if r > max_r1:
                    max_r1 = r
                    mostSimilarMunicipality1 = m2

            max_r2 = 0
            mostSimilarMunicipality2 = ""
            for m2 in self.municipalitiesPerYear["1909"]:
                r = ratio(municipality.lower(), m2.lower())
                if r > max_r2:
                    max_r2 = r
                    mostSimilarMunicipality2 = m2

            
            if max_r1 > 0.9 and max_r2 > 0.9:
                print "{},{},{}".format(municipality, mostSimilarMunicipality1, mostSimilarMunicipality2)


if __name__ == "__main__":
    commonMunicipalitiesInstance = CommonMunicipalities('municipality-index.csv')
    commonMunicipalitiesInstance.doStringMatch()
    commonMunicipalitiesInstance.doStringSimilarity()
    #commonMunicipalitiesInstance.serialize('output.csv')


__author__ = "Albert Meronyo-Penyuela"
__copyright__ = "Copyright 2012, VU University Amsterdam"
__credits__ = ["Albert Meronyo-Penyuela"]
__license__ = "LGPL v3.0"
__version__ = "0.1"
__maintainer__ = "Albert Meronyo-Penyuela"
__email__ = "albert.merono@vu.nl"
__status__ = "Prototype"

