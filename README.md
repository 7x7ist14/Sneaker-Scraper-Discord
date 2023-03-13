# All-in-one-Sneaker-Scraper-Discord
A sneaker scraper that can scrape all prices and payout prices for every size of a sneaker on different marketplace websites.
The scraper will react on a command that you send in your discord channel and will return a list with all prices and sizes of the choosen website.
Supported sites are:
+ Restocks --> Payout and listed prices
+ Hypeboost --> Payout and listed prices
+ Sneakit --> listed prices


# Requirements:

Check if you have all the needed Python libraries.

-->To install all needed libraries just do this:
+ open the folder that contains all files (the folder name should be "Sneaker-Scraper-Discord") in your file Explorer.
+ click on the path and write "cmd" --> now click enter
+ you should now see a cmd window, you just have to type "pip install -r requirements.txt" 
+ all needed libraries should now be installed and your good to go :)

# Chrome Driver
Please Check that you have the same version of the chrome driver in the folder with the scraper files as your main chrome is!
To check that go to "chrome://settings/help" and click on "About Chrome".
After that go to https://chromedriver.chromium.org/downloads and download the right version.
If your version isn't the same as in the Folder, just download your version and replace the chrome-driver file.
In the folder is the version: ChromeDriver 111.0.5563.65

--> automation for the chrome driver updates will be added in the future

# How to use

1. install all files and extract the zip file. --> check if you have all needed files in the folder. (main.py, embed.py, config.py, chromedriver.exe, requirements.txt)

2. install requirements.txt --> go to #requirements section to see how

3. Open the config.py file and input your Discord Bot Token and the name of the discord channel were you want to use the scraper in.

4. Check or change the commands in the config.py file if you want to.
--> The commands can be changed if you want to, here are all default commands:

+ COMMAND_PREFIX_ALL = "$scrape"    (Scraper for all sites at the same time --> only listing prices)
+ COMMAND_PREFIX_RESTOCKS = "$restocks" (Scraper for Restocks only --> listing prices only)
+ COMMAND_PREFIX_HYPEBOOST = "$hypeboost" (Scraper for Hypeboost only --> listing prices only)
+ COMMAND_PREFIX_SNEAKIT = "$sneakit" (Scraper for Sneakit only --> listing prices only)
+ COMMAND_PREFIX_PAYOUT_ALL = "$payout" (Scraper for all sites at the same time --> only payout prices)
+ COMMAND_PREFIX_RESTOCKS_PAYOUT = "$r" (Scraper for Restocks only --> payout prices only)
+ COMMAND_PREFIX_HYPEBOOST_PAYOUT = "$h" (Scraper for Hypeboost only --> payout prices only)

5. Open and run the "discord_embed" file. (best for this is VS-Code in my opinion)
--> updated running process will be added soon.

6. Write the keyword / commadnd with the SKU of a sneaker in your discord channel. You can change all commands if you want to in the config.py file.
Format examples:
+ $scrape DD1503-101
+ $payout DD1503-101
+ .... and so on

7. The Scraper will now collect all the data and will return you a message with all sizes and prices in your discord channel.

# Features:
+ Product URL's of your scraped product for multiple marketplace websites in the return message. (StockX, Restocks, GOAT, Hypeboost, Sneakit)
+ Payout and listing prices for all listed sites directly and fast back in your discord channel
+ Product image of the scraped product in the return message 
+ multiple differen scraping modes. (look at How to use command list)

# Return message examples:

![image](https://user-images.githubusercontent.com/103487648/224563004-25393349-9909-4082-b6c0-5dc1bd3ceb42.png)

![image](https://user-images.githubusercontent.com/103487648/224563029-73f28597-7eb5-4a73-a6fc-10ab5afda2bd.png)

![image](https://user-images.githubusercontent.com/103487648/224563049-ae87b7f0-07aa-4bd3-87e3-498c5f1fef82.png)

![image](https://user-images.githubusercontent.com/103487648/224563062-9d6f630a-ead0-4a1f-a86b-84c696150d16.png)

![image](https://user-images.githubusercontent.com/103487648/224563083-ef76a39c-5a2c-4a60-a30d-3fce8ce75662.png)




