import pandas as pd
import numpy as np

def main():

	source = raw_input('Data source: ')		

	data = pd.read_csv(source)
	data = pd.DataFrame(data)

	muni = raw_input('Town: ')
	muni = muni.upper()	
	beds = raw_input('Number of bedrooms: ')
	
	if muni == 'ALL' :
	    l = data
	else :
	    l = data[data['municipal'] == muni]
	
        if beds == 'all' :
	    beds == 'all'
        else :
 	    beds = int(beds)	
	    l = l[l['bedrooms'] == beds]
	
        l = l.reset_index(drop=True)

	print 'Median rent for ' + str(beds) + ' bedroom apartments in ' + muni + ' is ' + str(l['ask'].median())

	
main()
