import requests, subprocess, sys
ACCESS_TOKEN = 'XXXXXXXX'

def main():
    result = subprocess.run(['tail', '-n', '1', './log/check_reservation.log'], encoding='utf-8', stdout=subprocess.PIPE)
    result = result.stdout
    if not('FINISH check_reservation.py' in result):
        notice_error()
        sys.exit()
    else:
        sys.exit()

def notice_error():
    line_notify_token = ACCESS_TOKEN
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {
        'message': (None, '\nERROR : check_reservation.py don\'t work'),
    }
    requests.post(line_notify_api, headers = headers, data = data)

if __name__ == '__main__':
    main()