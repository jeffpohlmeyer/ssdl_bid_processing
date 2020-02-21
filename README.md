# Process
- Create a new file for the raw bids for the current division (FYI it *must* match the `division` variable in line 59 
of `main.py`) and call it SSDL Raw Bids - <division>.csv.
- For example, for the NL East auction on Feb 22, the file would be called SSDL Raw Bids - NL East.csv and the 
`division` variable would be called `NL East`
- You'll likely want to input the initial bids into SSDL Raw Bids.xlsx as there are formulas in there that check 
legality of the bids (min, max, average matching breakdown, etc) as well as auto-incrementing the order.
- Then copy over columns A-J (by value) into your new csv file and save and close the file.
- Then simply run main.py and the Proboards-friendly bb code format should be generated in two csv files: NL East by 
Player.csv and NL East by Team.csv
