from urlparse import urljoin, parse_qs
from django.utils.http import urlencode

def build_url(request, page_number, hashtag):
    """
    Build urls for pagination. First page haven`t page param.
    Page url: /some/path/?attr1=a&attr2=b&page=3&hashtag
    """
    query_params = request.GET.copy()
    # page 1, without page parameter
    if 'page' in query_params:
        del query_params['page']
    if page_number != 1:
        query_params['page'] = page_number
    url = request.path
    if query_params:
        url += '?'+ urlencode(query_params) + hashtag
    return url