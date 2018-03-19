import argparse
import whois
import http1
import datetime


def get_url_list():
    try:
        url_list_file = get_commandline_args().filepath
        return load_urls4check(url_list_file)
    except(FileNotFoundError, TypeError):
        return None


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


def get_domain_status(url, month=31):
    try:
        expire_date = get_domain_expire_date(url)
        now = datetime.datetime.now()
        expiration = (expire_date - now).days
        state = expiration > month
        return expiration, state
    except whois.parser.PywhoisError:
        return None, None


def print_results(url_list):
    for url in url_list:
        domain_expiration, domain_state = get_domain_status(url)
        if domain_state is not None:
            print(url, 'responds with status 200:', is_server_respond_200(url))
            print('Status is OK:', domain_state,
                  'Domain will expire in', domain_expiration, 'days.')
        else:
            print('Cant find', url)


if __name__ == '__main__':
    url_list = get_url_list()
    if url_list:
        print_results(url_list)
    else:
        print('File not found or empty')
