
import json
import os
import sys
from pprint import pprint

import requests
from dotenv import load_dotenv

from sms_common import build_body, build_headers


# Optional. API callback address  of the user for receiving the SMS
# status report, for example, "http://example.com/receiveSMSReport"
STATUS_CALLBACK = ""


def main():
    # load configurations from .env file
    load_dotenv()

    if len(sys.argv) < 6:
        usage = r'Usage: python send_notification.py "{receiver}" "{date}" '
        usage += r'"{time}" "{people}" "{code}"'
        print()
        exit(-1)

    receiver = sys.argv[1]
    date = sys.argv[2]
    time = sys.argv[3]
    people = sys.argv[4]
    code = sys.argv[5]

    template_params = f'["{date}","{time}","{people}","{code}"]'

    headers = build_headers()

    body = build_body(
        receiver=receiver,
        template_id=os.getenv('NOTIFICATION_TEMPLATE_ID'),
        template_params=template_params,
        status_callback=STATUS_CALLBACK)

    # SMS Sending API (single template, multiple users)
    # https://support.huaweicloud.com/intl/en-us/api-msgsms/sms_05_0001.html
    url = os.getenv('APP_ACCESS_ADDRESS') + '/sms/batchSendSms/v1'

    # Ignore the certificate trust issues to prevent API calling
    # failures caused by HTTPS certificate authentication failures
    verify = False

    response = requests.post(url, data=body, headers=headers, verify=verify)

    pprint(json.loads(response.text))


if __name__ == '__main__':
    main()
