
#### This is a Scrapy spider parsing jpg pictures from www.sfzd.cn.

Besides the settings, pipeline, middleware item files, chr.py is the spider file, and the ProcessMonitor.py is the spider control script, created to solve the no response issue.

A source file of characters waiting to be searched is not included here.
And the output files include a csv with urls matched with characters, a folder with all jpg files downloaded from the site, a txt keeping all successfully scraped characters, and a txt keeping all no-result characters.

The no response issue: the spider stops parsing any data while still keeps requesting after around 10-20 minutes.
So the process monitor script is written to control the restart of the spider to keep scraping data from the site.
