# Hahaha - awesome - http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454

from lxml import html
import requests
import jsondict
import urllib

da = {}

def td_text_after(label, tree):
    """ retrieves text from first td following a td containing a label e.g.:"""
    a = tree.xpath("//*[contains(text(), '" + label + "')]/following-sibling::td//text()")#.extract_first()
    # return single element
    if len(a) == 1:
        return a[0]
    # return nothing
    elif len(a) == 0:
        return None
    # return the array
    return a
        
def parse_da_page(tree):
    """ Retrieve DA information from its detail page, labels must match """        
    labels = { 'date_lodged': 'Date Lodged:', 'desc_full': 'Description:', 
               'est_cost': 'Estimated Cost:', 'status': 'Status:',
               'date_determined': 'Date Determined:', 'decision': 'Decision:',
               'officer': 'Responsible Officer:' }
    # map DA fields with those in the following <td> elements on the page
    for i in labels:
        da[i] = td_text_after(labels[i], tree)
    return da

def get_da_by_url(url):
    # request url and form XML tree
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return parse_da_page(tree)


def get_da_by_da_no(da_no):
    # urlencode the DA no., it contains a '/'
    da_no_url = urllib.parse.quote_plus(da_no)
    url = "http://datrack.canterbury.nsw.gov.au/cgi/datrack.pl?ref=" + da_no_url + "&desc=&lodgefrom=&lodgeto=&statusfrom=&statusto=&search=search&activetab=2"
    print(url + '\n')
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # get the address info from the individual DA listing page
    da['da_no'] = tree.xpath('//td[@class="datrack_danumber_cell"]//text()')[0]#.extract_first()
    da['house_no'] = tree.xpath('//td[@class="datrack_houseno_cell"]//text()')[0]#.extract_first()
    da['street'] = tree.xpath('//td[@class="datrack_street_cell"]//text()')[0]#.extract_first()
    da['town'] = tree.xpath('//td[@class="datrack_town_cell"]//text()')[0]#.extract_first()"""
    da['url'] = tree.xpath('//td[@class="datrack_danumber_cell"]//@href')[0]
    return get_da_by_url(da['url'])
