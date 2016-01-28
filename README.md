# Rental-Listings
Analyzing apartment rental listings in Greater Boston

3_month_avg.ipynb: Calculate monthly median rent using 3-month rolling average.

De-Duplicator.ipynb: Assign each listing a duplicate id based on some combination of listing title, number of bedrooms, asking price, location, and posting date.

de-duplicator_with_x,y.ipynb: Same as De-Duplicator but works for x, y coordinate locations. Also supports rounding coordinates to 2, 3, or 4 decimal places (assuming they are already included in the data)

median.py: Computes median rent for given town and number of bedrooms

Levenshtein.ipynb: de-duplicate listings data using text comparison via simhash and hamming distance. WARNING: not tested, contains errors in its current form. 
See:
https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
http://matpalm.com/resemblance/simhash/
