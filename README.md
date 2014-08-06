Just Crawl is a scrapy project which demonstrates how to scrape data from html pages.This project is strictly for education purpose and should not be used for commercialisation.

Pre requisites:

    Python 2.7
    lxml. Most Linux distributions ships prepackaged versions of lxml
    OpenSSL. This comes preinstalled in all operating systems except Windows 
    pip or easy_install Python package managers

Installation: 

	To install using pip:

		pip install Scrapy

	To install using easy_install:

		easy_install Scrapy


Running the project:
	
    For output in json format:
		scrapy crawl jobdetails -o items.json

	For output in csv format:
		scrapy crawl jobdetails -o items.csv

	For the ouput in xml format:
		scrapy crawl jobdetails -o items.xml


References:

  http://doc.scrapy.org/en/latest/
