import sys
import requests
from lxml import html


def get_stock_info(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Failed to fetch data from Yahoo Finance.")
        return

    tree = html.fromstring(response.content)

    # Extracting data using XPath
    open_price = tree.xpath(
        '//div[@data-testid="quote-statistics"]//span[contains(text(), "Open")]/following-sibling::span/fin-streamer/text()')
    if open_price:
        open_price = open_price[0]
    else:
        open_price = "N/A"
    high_price = tree.xpath(
        '//div[@data-testid="quote-statistics"]//span[contains(text(), "Day\'s Range")]/following-sibling::span/fin-streamer/text()')
    if high_price:
        high_price = high_price[0]
    else:
        high_price = "N/A"

    low_price = tree.xpath(
        '//div[@data-testid="quote-statistics"]//span[contains(text(), "Day\'s Range")]/following-sibling::span/fin-streamer/text()')
    if low_price:
        low_price = low_price[0]
    else:
        low_price = "N/A"

    latest_price = tree.xpath(
        '//div[@data-testid="quote-statistics"]//span[contains(text(), "Open")]/following-sibling::span/fin-streamer/text()')
    if latest_price:
        latest_price = latest_price[0]
    else:
        latest_price = "N/A"

    volume = tree.xpath(
        '//div[@data-testid="quote-statistics"]//span[contains(text(), "Volume")]/following-sibling::span/fin-streamer/text()')
    if volume:
        volume = volume[0]
    else:
        volume = "N/A"

    # Yahoo Finance doesn't provide timestamp in the HTML, so we skip it for now
    # You can consider using another API or source for this information

    print("URL:", url)
    print("Open:", open_price)
    print("High:", high_price)
    print("Low:", low_price)
    print("Latest:", latest_price)
    print("Volume:", volume)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <stock_symbol>")
        sys.exit(1)

    symbol = sys.argv[1]
    get_stock_info(symbol)
