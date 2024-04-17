#!/bin/bash

# Check if the user provided a stock symbol as a command-line argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <stock_symbol>"
    exit 1
fi

# Call the Python script with the provided stock symbol
python3 stock.py "$1"
