#!/usr/bin/env python3

import argparse
import os.path

def main():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', nargs='+', help='Geonames dump (tab-delimited); obtain from http://download.geonames.org/export/dump/ ')
    parser.add_argument('-o','--outputdir', type=str,help="Output directory", action='store',default=".",required=False)
    args = parser.parse_args()

    for filename in args.files:
        country = filename.split('.')[0].upper()
        outfile = {
            'A': open('geonames.' + country + '.A.region.txt','w',encoding='utf-8'), #country, state,region
            'H': open('geonames.' + country + '.H.water.txt','w',encoding='utf-8'),
            'H-LK': open('geonames.' + country + '.H-LK.lakes.txt','w',encoding='utf-8'),
            'H-STM': open('geonames.' + country + '.H-STM.rivers.txt','w',encoding='utf-8'),
            'H-SEA': open('geonames.' + country + '.H-SEA.seas.txt','w',encoding='utf-8'),
            'L': open('geonames.' + country + '.L.parks.txt','w',encoding='utf-8'),
            'P': open('geonames.' + country + '.P.cities.txt','w',encoding='utf-8'),
            'R': open('geonames.' + country + '.R.roads.txt','w',encoding='utf-8'),
            'R-ST': open('geonames.' + country + '.R-ST.streets.txt','w',encoding='utf-8'),
            'S': open('geonames.' + country + '.S.buildings.txt','w',encoding='utf-8'),
            'T': open('geonames.' + country + '.T.mountains.txt','w',encoding='utf-8'),
            'U': open('geonames.' + country + '.U.undersea.txt','w',encoding='utf-8'),
            'V': open('geonames.' + country + '.V.forests.txt','w',encoding='utf-8')
        }
        with open(filename,'r',encoding='utf-8') as f:
            for line in f:
                fields = line.split("\t")
                featcls = fields[6]
                feat = fields[7] #this can be used for a more specific subdivision
                if featcls + '-' + feat in outfile:
                    print(fields[1], file=outfile[featcls + '-' + feat])
                else:
                    print(fields[1], file=outfile[featcls])

if __name__ == '__main__':
    main()
