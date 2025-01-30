# Amazon Web Scrapper

*Web Scrapping is the process of extracting data or feed from webpages or websites.*

**Obejective:** The objective of this project is to learn the basics of web scrapping using BeautifulSoup and requests library provided by python. 

**Key Highlights**

1. **Title**: Extracted from the `<h2>` tag.  
2. **Price**: Extracted from the `<span>` tag with the class `a-price-whole` for the main price.  
3. **Reviews**: Extracted from the `<span>` tag with the class `a-icon-alt` for review ratings.  
4. **Product URL**: The link to the individual product page is extracted to gather additional details like availability.

**The script automatically scrapes multiple products from the search results page and fetches corresponding availability information from their individual product pages.**

**Data Storage**

Firstly all the product details are appended into the list, which is later on converted to the data frame.

The Data Frame is then saved as a CSV file, making it easy and manipualte the data on later stage. 

