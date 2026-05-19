# Retrieves Phone code. Do not change
# File should be completely unchanged

# Checks if Routes is up and running. Do not change
def is_url_reachable(url):
    """Check if the URL can be reached. Pass the URL as a parameter.
    If it can be reached, it returns True, otherwise it returns False"""

    import ssl
    import urllib.request

    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            # print("Response Status Code:", response.status) #for debugging purposes
            if response.status == 200:
                return True
            else:
                return False
    except Exception as e:
        print (e)

    return False