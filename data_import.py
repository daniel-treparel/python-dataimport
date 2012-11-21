import os
import sys

import requests
import logging

LOCATION = '/mnt/Data/irec/IREC'
URL = 'http://localhost:8983/solr/collection1/dataimport?optimize=false&clean=false&commit=false&verbose=false&entity=patent&command=full-import'

'''
POST individual xml docs like so:
curl "http://localhost:8983/solr/collection1/dataimport?optimize=false&clean=false&commit=true&verbose=false&entity=patent&command=full-import" --data-binary @./EP-0010210-A1.xml -H 'Content-type:text/xml; charset=utf-8'

commit with:
curl http://localhost:8983/solr/update?commit=true
'''


def _post_file(fn, hdrs={'Content-type': 'text/xml; charset=utf-8'}):
    with open(fn, 'rb') as fo:
        try:
            data = fo.read()
            res = requests.post(URL, data=data, headers=hdrs) 
            print "%r %r" % (res, fn)
            if res.status_code != 200:
                raise RuntimeError('status_code != 200\nstatus: %r\nfn: %r' % (res.status_code, fn))
        except:
            logging.exception("error while posting file")

def main():
    for dirpath, dirnames, filenames in os.walk(LOCATION):
        for fn in filenames:
            if fn.endswith('.xml'):
                filepath = os.path.join(dirpath, fn)
                _post_file(filepath)


if __name__=='__main__':
    log_fn = './import.log'
    log_format = '%(created)f '+logging.BASIC_FORMAT
    logging.basicConfig(filename=log_fn, level=logging.WARNING, format=log_format)

#    h = logging.StreamHandler(sys.stdout)
#    h.setLevel(logging.DEBUG)
#    h.setFormatter(logging.Formatter(log_format))
#    logging.root.addHandler(h)

    main()
