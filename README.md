# NHL_API
Projects to practice different coding skills using the NHL API using information provided at https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api.

The first work done was completing a comparison between players. One of the difficulties of using this API is that there doesn't seem to be a way of getting PlayerIDs easily. 

Using argparser we can add different arguments. They are the following:
--compare (True or False). This allows for us to set up the first dataframe 
--save (True or False). Will save the dataframe to "player_comparison.pkl"
--saveas (string). Will save the dataframe to a desired title
--load (string). Allows the user to load the dataframe
--add (integer). Allows the user to add to the dataframe
--remove (integer). Allows the user to remove from the dataframe
--visualize (True or False). Saves a visualization of the document to "comparison.png". This will currently overwrite the file (will change to save to a chosen filename)

Therefore to initialize the project one must run: 
python nhl_comparison.py --compare True --save True 
alternatively 
python nhl_comparison.py --compare True --saveas filename 
will work.

In order to add to a specific dataframe use --load filename --add # --saveas filename

