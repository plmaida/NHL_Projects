# NHL API - Playing with Pandas

## Overview
The first work done was completing a comparison between players. One of the difficulties of using this API is that there doesn't seem to be a way of getting PlayerIDs easily. 

## Parser
Using argparser we can add different arguments. They are the following:  
  --compare (True or False). This allows for us to set up the first dataframe.    
  --save (True or False). Will save the dataframe to "player_comparison.pkl"     
  --saveas (string). Will save the dataframe to a desired title, be sure to include .pkl       
  --load (string). Allows the user to load the dataframe, be sure to include .pkl     
  --add (integer). Allows the user to add to the dataframe     
  --remove (integer). Allows the user to remove from the dataframe     
  --visualize (True or False). Saves a visualization of the document to "comparison.png". This will currently overwrite the file (will     change to save to a chosen filename)          
  --players (True or False). Allows the user to show the players currently in the list.    

Therefore to initialize the project one must run ``` python nhl_comparison.py --compare True --save True ``` alternatively ``` python nhl_comparison.py --compare True --saveas filename ``` will also work if you want to input a different filename. 

In order to add to a specific dataframe use ``` --load filename --add # --save True ``` or  ```--load filename --add # --saveas filename2```. The second option will allow for the user to not save over the original dataframe and can create a new dataframe. 

## Adding and Comparing
As mentioned it is hard to find player IDs aside from using the link provided in the comments of the provided link: https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api. 

The process therefore asks the user to input a player name. Input the last name in lower case and a product code will be output. Using the product code will be input (find a way to make this more automatic). The difficulty here is, for example, if you want to look at "Kane" you can get the result for both Patrick Kane or Evander Kane. 

## Removing
Because the player name is saved into the dataframe, we simply input the name of the player, the player code is not needed to remove the player. 

## Visualizing
An example of a graph that shows Points/Game is shown here:
![comparison](https://user-images.githubusercontent.com/38801847/52666990-b45aa400-2edd-11e9-850d-e001d1040bc9.png)


