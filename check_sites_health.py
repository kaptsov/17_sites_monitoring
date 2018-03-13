import argparse
import whois
import http1
import datetime


MONTH = 31
GOOD_SERVER_ANSWER = 200


def get_commandline_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath')
    return parser.parse_args()


def load_urls4check(filepath):
    with open(filepath) as text_file:
        filedata = text_file.read().splitlines()
    return filedata


def is_server_respond_200(url):
    return http1.head(url).status == GOOD_SERVER_ANSWER


def get_domain_expire_date(url):
    try:
        json_answer = whois.whois(url)
        date_answer = json_answer.get('expiration_date', 0)
        try:
            return date_answer[0]
        except TypeError:
            return date_answer
    except whois.parser.PywhoisError:
        print('Cant find', url)


def get_domain_status(expiration_date):
    if (expiration_date is not None):
        now = datetime.datetime.now()
        expiration = expiration_date - now
        domain_status = expiration.days > MONTH
    else:
        expiration = None
        domain_status = False
    return expiration, domain_status


if __name__ == '__main__':
    try:
        url_list_file = get_commandline_args('filepath')
        url_list = load_urls4check(url_list_file)
    except(FileNotFoundError, TypeError):
        exit('File not found or empty')

    for url in url_list:
        expiration, domain_status = get_domain_status(
            get_domain_expire_date(url))
        if (expiration is not None):
            print(url, 'responds with status 200:', is_server_respond_200(url))
            print('Status is OK:', domain_status,
                  'domain will expire in', expiration.days, 'days.')
