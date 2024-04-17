
**Stock Information Fetcher**

This is a Python application that fetches stock information from Yahoo Finance using web scraping techniques. It includes a shell script to simplify running the application with a stock symbol.

**Prerequisites**

Python environment (Python 3.x recommended)
Internet connection to fetch stock information from Yahoo Finance

**Installation**

Clone or download this repository to your local machine.

    git clone <repository_url>

Navigate to the project directory.
cd us-stock-info

**Install the required Python packages using pip.**

    pip install -r requirements.txt

This will install the necessary packages such as requests and lxml for web scraping.

**Usage**
Activate your Python environment if you're using a virtual environment.

    source <path_to_virtual_env>/bin/activate

Run the shell script stock.sh followed by the stock symbol you want to fetch information for.

    ./stock.sh <stock_symbol>

Replace <stock_symbol> with the symbol of the stock you're interested in (e.g., AAPL for Apple, MSFT for Microsoft).

**Example:**

    ./stock.sh AAPL

This will display the stock information for Apple Inc.
