import os
import urllib.request as req
from urllib.parse import urlparse


def download(url, to=None):
    """Download a remote file specified by a URL to a 
    local directory.

    :param url: str
        URL pointing to a remote file.

    :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """

    parsed_python_url = urlparse(url)
    if(to == None):
        to = os.path.basename(parsed_python_url.path)

    req.urlretrieve(url, to)
