from lxml import html
import requests
import jsondict
import da_scrape

da = {}
def test_get_da_by_url(url):
    # test url        
    url = 'http://datrack.canterbury.nsw.gov.au/cgi/datrack.pl?cmd=download&id=ZiFfLxV6W1xHWBN1UwR5SVVSAV0GXUZUcGFGHhAyTykQAG5CWVADRQg='
    da = da_scrape.get_da_by_url(url)
    da_json = jsondict.record(da)
    """
    da['officer'] = ['B1', 'B2']
    da['status'] = 'bodged'
    """# print(jsondict.json_serial(da))
    print(jsondict.json_pretty(da))


def test_get_da_by_da_no(da_no):
    # da_no = 'DA-465/2016'
    da = da_scrape.get_da_by_da_no(da_no)
    print(jsondict.json_pretty(da))
