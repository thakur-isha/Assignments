## Webscraper

#### Using Object oriented code, implemented the web scraping from the URL provided.

1.) Created a class as webScaper which accept URL as parameter and which can be used for fetching the data.

2.) Class has a function getData() which crawl on the URL and fetch the data.

3.) Class has a function filterOperation() which will use the data fetched with getData() and apply the operation to filter the data.

4.) If the title word count is greater than 5 then it will sort the entries with comment count in filterOperation().

5.) If the title word count is less or equal to 5 then sort the entries with points in filterOperation().