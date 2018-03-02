import argparse
import http1
import requests
import datetime


def get_commandline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()


def load_urls4check(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read().splitlines()
    return filedata


def get_server_respond_code(url):
    return http1.head(url).status


def get_domain_expire_status(url):
    params = {"apikey": 'fe7fa75b11aaf41fa205ba292787fd74',
              'r': 'whois', 'domain': url}
    request = requests.get('http://api.whoapi.com', params=params)
    answer = request.json()
    if answer["registered"]:
        expiration_date = datetime.datetime.strptime(
            answer["date_expires"], '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        time_untill_expire = expiration_date - now
        if time_untill_expire.days < 30:
            domain_status = 'Warning!'
        else:
            domain_status = 'OK'
    return (domain_status, time_untill_expire.days)


if __name__ == '__main__':
    try:
        url_list_file = get_commandline_args('filepath')
        url_list = load_urls4check(url_list_file)
        for url in url_list:
            print(url, ' responds with status:', get_server_respond_code(url))
            domain_status, expiration = get_domain_expire_status(url)
            print('Status is', domain_status,
                  'domain will expire in', expiration, ' days')
    except(FileNotFoundError):
        exit('File not found')
