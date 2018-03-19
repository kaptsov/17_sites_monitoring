import argparse
import whois
import http1
import datetime


def get_commandline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()


def load_urls4check(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read().splitlines()
    return filedata


def is_server_respond_200(url):
    good_server_answer = 200
    return http1.head(url).status == good_server_answer


def get_domain_expire_date(url):
    server_answer = whois.whois(url)
    expiration_date = server_answer.get('expiration_date', 0)
    if type(expiration_date) == list:
        return expiration_date[0]
    return expiration_date


def get_expiration_days(expiration_date):
    now = datetime.datetime.now()
    expiration = expiration_date - now
    return expiration


if __name__ == '__main__':
    try:
        url_list_file = get_commandline_args().filepath
        url_list = load_urls4check(url_list_file)
    except(FileNotFoundError, TypeError):
        exit('File not found or empty')

    month = 31
    for url in url_list:
        try:
            expire_date = get_domain_expire_date(url)
            expiration = get_expiration_days(expire_date).days
            domain_status = expiration > month
            print(url, 'responds with status 200:', is_server_respond_200(url))
            print('Status is OK:', domain_status,
                  'Domain will expire in', expiration, 'days.')
        except whois.parser.PywhoisError:
            print('Cant find', url)
