import requests

def print_box(text):
    line = '+' + '-' * (len(text) + 2) + '+'
    print(line)
    print('| ' + text + ' |')
    print(line)

def check_header_security(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            headers = response.headers

            print_box("Response Code: " + str(response.status_code))
            print("Response Headers:")
            for header, value in headers.items():
                print(header + ":", value)

            check_content_security_policy(response)
            check_cross_domain_misconfiguration(response)
            check_anti_clickjacking_header(response)
            check_cookie_httponly(response)
            check_cookie_secure_flag(response)
            check_cookie_samesite_flag(response)
            check_strict_transport_security(response)
            check_x_content_type_options(response)
        else:
            print("Failed to reach", url, "- Response Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Failed to reach", url, "-", str(e))

def check_content_security_policy(response):
    headers = response.headers
    csp_header = headers.get('Content-Security-Policy')
    if csp_header:
        print_box("Content Security Policy (CSP) is present")
        print("Response Headers:")
        for header, value in headers.items():
            print(header + ":", value)
        print(csp_header)
        if 'script-src *' in csp_header or 'style-src *' in csp_header or 'img-src *' in csp_header:
            print_box("Cross-Domain Misconfiguration: Resource loading from any domain is allowed.")
        else:
            print_box("No Cross-Domain Misconfiguration detected.")
    else:
        print_box("Content Security Policy (CSP) is not present")

def check_cross_domain_misconfiguration(response):
    headers = response.headers
    csp_header = headers.get('Content-Security-Policy')
    if csp_header and ('script-src *' in csp_header or 'style-src *' in csp_header or 'img-src *' in csp_header):
        print_box("Cross-Domain Misconfiguration: Resource loading from any domain is allowed.")
    else:
        print_box("No Cross-Domain Misconfiguration detected.")

def check_anti_clickjacking_header(response):
    headers = response.headers
    x_frame_options = headers.get('X-Frame-Options')
    if x_frame_options:
        print_box("X-Frame-Options header is present: " + x_frame_options)
    else:
        print_box("Missing Anti-clickjacking header (X-Frame-Options) detected.")

def check_cookie_httponly(response):
    headers = response.headers
    cookies_header = headers.get('Set-Cookie')
    if cookies_header:
        print_box("Cookies:")
        for cookie in cookies_header.split(','):
            if 'httponly' not in cookie.lower():
                print("Cookie does not have the HttpOnly flag set:", cookie.strip())
    else:
        print_box("No cookies found.")

def check_cookie_secure_flag(response):
    headers = response.headers
    cookies_header = headers.get('Set-Cookie')
    if cookies_header:
        print_box("Cookies:")
        for cookie in cookies_header.split(','):
            if 'secure' not in cookie.lower():
                print("Cookie does not have the Secure flag set:", cookie.strip())
    else:
        print_box("No cookies found.")

def check_cookie_samesite_flag(response):
    headers = response.headers
    cookies_header = headers.get('Set-Cookie')
    if cookies_header:
        print_box("Cookies:")
        for cookie in cookies_header.split(','):
            if 'samesite' not in cookie.lower():
                print("Cookie does not have the SameSite attribute set:", cookie.strip())
    else:
        print_box("No cookies found.")

def check_strict_transport_security(response):
    headers = response.headers
    strict_transport_security = headers.get('Strict-Transport-Security')
    if strict_transport_security:
        print_box("Strict-Transport-Security header is present: " + strict_transport_security)
    else:
        print_box("Strict-Transport-Security header is not set.")

def check_x_content_type_options(response):
    headers = response.headers
    x_content_type_options = headers.get('X-Content-Type-Options')
    if x_content_type_options:
        print_box("X-Content-Type-Options header is present: " + x_content_type_options)
    else:
        print_box("X-Content-Type-Options header is missing.")

# Get URL from user input
url = input("Enter the website URL to check the header misconfigurations: ")
check_header_security(url)
