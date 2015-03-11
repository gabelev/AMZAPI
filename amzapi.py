# CODE to generate the specific request URL for the AMZ API. 
# Version 0.0



def amazon_test_url():
    import base64, hashlib, hmac, time
    from urllib import urlencode, quote_plus
    
    AWS_ACCESS_KEY_ID = 'insert' #Key ID associated with GABE's Account
    AWS_SECRET_ACCESS_KEY = 'insert'  #secret Key associated with Gabe's account
    TEST_ISBN = '0441569595' # will need to change this up so that this url function can take a list of ISBN args

    base_url = "http://ecs.amazonaws.com/onca/xml"
    url_params = dict(
        Service='AWSECommerceService', 
        Operation='ItemLookup', 
        IdType='ISBN', 
        ItemId=TEST_ISBN,
        SearchIndex='Books',
        AWSAccessKeyId=AWS_ACCESS_KEY_ID,  
        ResponseGroup='Images,ItemAttributes,EditorialReview,SalesRank')

    #Can add Version='2009-01-06'. What is it BTW? API version?


    # Add a ISO 8601 compliant timestamp (in GMT)
    url_params['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # Sort the URL parameters by key
    keys = url_params.keys()
    keys.sort()
    # Get the values in the same order of the sorted keys
    values = map(url_params.get, keys)

    # Reconstruct the URL parameters and encode them
    url_string = urlencode(zip(keys,values))

    #Construct the string to sign
    string_to_sign = "GET\necs.amazonaws.com\n/onca/xml\n%s" % url_string

    # Sign the request
    signature = hmac.new(
        key=AWS_SECRET_ACCESS_KEY,
        msg=string_to_sign,
        digestmod=hashlib.sha256).digest()

    # Base64 encode the signature
    signature = base64.encodestring(signature).strip()

    # Make the signature URL safe
    urlencoded_signature = quote_plus(signature)
    url_string += "&Signature=%s" % urlencoded_signature

    request_URL = "%s?%s\n\n%s\n\n%s" % (base_url, url_string, urlencoded_signature, signature)

    print request_URL

import requests
import pprint


endpoint = amazon_test_url()
response = requests.get(endpoint)

data = response.url
pprint.pprint(data)