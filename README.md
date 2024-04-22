```markdown
# Real Estate Web Scraper

This project is a Python script that scrapes real estate websites and generates PDFs of the property details. It uses data from an Excel spreadsheet to determine which URLs to scrape.

## Getting Started

These instructions will guide you on how to use this script.

### Prerequisites

You need to have the following installed on your machine:
- Python
- Selenium WebDriver
- ChromeDriver
- Openpyxl
- Requests

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip:
   ```
   pip install selenium openpyxl requests webdriver_manager
   ```

### Usage

1. Update the `house_list.xlsx` file with the URLs of the real estate properties you want to scrape. The URLs should be placed in the first column, starting from the second row.
2. Run the script:
   ```
   python main.py
   ```
3. The script will visit each URL in the spreadsheet, scrape the property details, and generate a PDF. The PDFs are saved in the `./company data/` directory.

## How It Works

The script uses Selenium WebDriver to automate a Chrome browser. It visits each URL in the spreadsheet and uses the `print_page()` function to generate a PDF of the page. The PDF is saved as a base64 string, which is then decoded and written to a file.

The filename of the PDF is derived from the URL of the property, with certain characters replaced for compatibility with file systems.

## Built With

- [Python](https://www.python.org/) - The programming language used.
- [Selenium WebDriver](https://www.selenium.dev/) - Used to automate the browser.
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) - The WebDriver for Chrome.
- [Openpyxl](https://openpyxl.readthedocs.io/) - Used to read data from the Excel spreadsheet.
- [Requests](https://requests.readthedocs.io/) - Used to send HTTP requests.

## Author
👤 Joao Melo

- Github: [@johnmelodev](https://github.com/johnmelodev)
- LinkedIn: [@joao-melo-dev](https://www.linkedin.com/in/joao-melo-dev)

## Show Your Support
Give a ⭐️ if this project helped you!
```