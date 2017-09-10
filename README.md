# newrelicEmailUserList
A Python script that reads a (undocumented) New Relic REST API and creates a CSV file containing the emails for all users on the account. This script will ask the user for the REST API key for the account who's user emails should be reported. The output from this script is a CSV file, newrelicUserEmailList.csv, in the current directory. The format is suitable to copy the file contents into the clipboard and paste into the address line of an email or to create a distribution list in your Mail program.  

## Dependencies
  * This script requires Python 3 or higher

## Installation
  Edit this script file and add the New Relic REST API key for the default account to the head["X-API-Key"] item. 
