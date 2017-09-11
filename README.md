# newrelicEmailUserList
A Python script that reads a (undocumented) New Relic REST API and creates a CSV file containing the emails for all users on the account. This script will ask the user for the REST API key for the account who's user emails should be reported. The output from this script is a CSV file, newrelicUserEmailList.csv, in the current directory. The format is suitable for copying to clipboard and pasting into your email address field or creating a distribution list.  

## Dependencies
  * Requires the 'request' module

## Installation
  The script will ask you to input the REST API key for the account. I recommend you add a default REST API key value in the headers dictionary,

    'X-Api-Key':'<Add_REST_API_Key_HERE>' # Default REST API Key 
