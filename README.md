# Surfs Up 

## Overview of the analysis
W. Avy assigned another challenge to us requesting more information about temperature trends before opening his surf shop. He specifically requested temperature data for the months of June and December to determine if the business is sustainable year round. In order to retrieve temperature data, we used Python, Pandas, and SQLAlchemy to filter the data column of the Measurements table in the hawaii.sqlite database. The retrieved data was first converted into a list. We then created a DataFrame from the list and generated the summary statistics. 

## Results 
* The June data shows a larger amount of temperature counts compared to the December data. June shows a count of 2753 while December has 1597 counts. 
* Although there was a large difference in temperature counts between both months, the average temperatures for June and December are very close in numbers. June has a mean temperature of 75.01 while December has a mean temperature of 73.76.
* The 2016 data for months June and December have the same maximum temperature of 87 degrees. 

![june_data](https://github.com/echuung94/surfs_up/blob/main/Resources/june%20data.png)

![december_data](https://github.com/echuung94/surfs_up/blob/main/Resources/december%20data.png)


## Summary
While reviewing the temperature data for June and December, I noticed that there was a higher amount of temperatures recorded in the month of June than in December. It is possible that there could be similar temperatures in different days of the month, but it was interesting to see that the mean temperatures recorded were reported very close in numbers. Although the two months are in different seasons, there could be days that are warmer in the winter or cooler in the summer. The data given shows that in December there was a max temperature of 87 degrees while in June, the lowest temperature was recorded to be 58 degrees. </br>
The Measurement.prcp could be used to retrieve precipitation data for both months so that W. Avy could see the amount of precipitation in the area so that too much or too little will not affect his business so much. Measurement.station could also be used so that W. Avy so that he knows how many stations were used to collect the data for the months of June and December. 
