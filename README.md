Poshmark Search Automation for fashion lovers with limited time! 

This project uses Selenium to automate searching for products on Poshmark. Specifically, it navigates to the women’s category on Poshmark and searches for “Prada Black Brushed Leather loafers size 9”.  It can be done via input, but I hard coded the search. Installation instructions follow. You can refactor the code to take input instead.  

Prerequisites

Before running the script, you need to have the following installed:

	•	Python 3.x
	•	Selenium
	•	ChromeDriver

Installation

	1.	Clone the Repository:
 git clone https://github.com/yourusername/poshmark-search-automation.git
cd poshmark-search-automation
	2.	Install Dependencies:
Make sure you have Selenium installed. You can install it using pip:
pip install selenium
3.	Download ChromeDriver:
Download the appropriate version of ChromeDriver for your operating system from ChromeDriver.
4.	Move ChromeDriver:
Move the ChromeDriver executable to a known location, e.g., /Users/marciprescott/Downloads/chromedriver-mac-arm64 2/chromedriver.

Usage

  1.	Update Path to ChromeDriver:
Ensure the path variable in the script points to the location of your ChromeDriver:
path = "/Users/marciprescott/Downloads/chromedriver-mac-arm64 4/chromedriver"
2.	Run the Script:
Execute the Python script:
python poshmark.py

Notes
You might have some issues with getting the chromedriver to work if you are on a mac, but if you search the error on google you should find a workaround.  AI might help as well. 

	•	Ensure that your Chrome browser is updated to the same version as your ChromeDriver.
	•	You can adjust the search term in the script to search for different products.
