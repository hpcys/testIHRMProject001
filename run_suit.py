import os
import time
import unittest

from BeautifulReport import BeautifulReport

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

suite = unittest.TestLoader().discover(BASE_DIR + '/script', 'test*.py')

# file = 'ihrm_{}.html'.format(time.strftime('%Y%m%d%H%M%S'))
file = 'ihrm.html'
BeautifulReport(suite).report(filename=file, description='完美报告', log_path=BASE_DIR + '/report')
print("--"*100)
print("aaaaaaaa")
