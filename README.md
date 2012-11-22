python-dataimport
=================

Python script to import millions of xml files into SOLR

Q: Why not use the FileListEntityProcessor in combination with the XPathEntityProcessor?
A: line 217 in http://svn.apache.org/viewvc/lucene/dev/trunk/solr/contrib/dataimporthandler/src/java/org/apache/solr/handler/dataimport/FileListEntityProcessor.java?revision=1411366&view=markup
   Trying to cram millions of filepaths into memory is sub-optimal at best, out-of-memory at worst.

Included in the requests directory is the python requests package (http://docs.python-requests.org/). This package allows us to do http requests in a sane manner.

