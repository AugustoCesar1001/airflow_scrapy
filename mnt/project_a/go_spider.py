from scrapy.crawler import CrawlerProcess
from bookscraper.spiders.bookspider import BookspiderSpider


#Run the spider
process = CrawlerProcess(settings = {
    # Adjusting the scraping behavior to rotate appropriately through proxies and user agents
    "CONCURRENT_REQUESTS": 3, # The maximum number of concurrent (i.e. simultaneous) requests that will be performed by the Scrapy downloader
    "DOWNLOAD_TIMEOUT": 60, # Setting the timeout parameter to 60 seconds as per the ScraperAPI documentation
    "RETRY_TIMES": 5, # Catch and retry failed requests up to 5 times
    "ROBOTSTXT_OBEY": False, # Saves one API call
})

process.crawl(BookspiderSpider)
process.start()   
