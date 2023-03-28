# HUAWEI CLOUD Message & SMS example

This repository contains basic SMS sending scripts to demonstrate the
Messages & SMS service of HUAWEI CLOUD (International SMS).

## Installation (Python)

1. Install Miniconda if not already installed: <https://docs.conda.io/en/latest/miniconda.html>
2. Create a Conda virtual environment using Python 3.10 (`msgsms` is used as
   the environment name): `conda create -n msgsms python=3.10 -y`
3. Activate the virtual environment: `conda activate msgsms`
4. Install Python requirements with pip: `pip install -r requirements.txt`

## HUAWEI CLOUD preparation

Please check the overall usage flow in the Help Center:
[How to Use International SMS][usage-flow].

1. Create SMS application - <https://support.huaweicloud.com/intl/en-us/usermanual-msgsms/sms_03_0013.html>
2. Create SMS Template - <https://support.huaweicloud.com/intl/en-us/usermanual-msgsms/sms_03_0016.html>

For the examples of this repository, two templates were created:

**Notification template**, used in the `send_notification.py` script:

```plain
Reservation confirmed at ${DATE} ${TIME} for ${NUM_3} people.
Show the following code at the reservation day: ${TXT_20}.
```

**Verification code template**, used in the `send_verification_code.py` script:

```plain
${NUM_8} is your verification code on our demo app.
```

## Usage

1. Make a copy of `.env.example` named `.env`, and set `APP_KEY`, `APP_SECRET`,
   `APP_ACCESS_ADDRESS` and `CHANNEL_NO`. All those values are obtained from
   Application Management page;
2. Get the notification template ID and update `TEMPLATE_ID` inside
   `send_notification.py` script;
3. Get the verification code template ID and update `TEMPLATE_ID` inside
   `send_verification_code.py` script;
4. Follow one of the examples below.

### Send verification code example

```plain
python send_verification_code.py "+5511912345678" "123456"
```

The expected output is the following:

```plain
{'code': '000000',
 'description': 'Success',
 'result': [{'createTime': '2023-03-28T20:07:20Z',
             'from': 'msg...',
             'originTo': '+5511912345678',
             'smsMsgId': '98c...939',
             'status': '000000'}]}
```

### Send notification example

```plain
python send_notification.py "+5511912345678" "2023/3/30" "10:30" "25" "ABCD1234"
```

The expected output is the following:

```plain
{'code': '000000',
 'description': 'Success',
 'result': [{'createTime': '2023-03-28T20:07:20Z',
             'from': 'msg...',
             'originTo': '+5511912345678',
             'smsMsgId': '98c...939',
             'status': '000000'}]}
```

[usage-flow]: <https://support.huaweicloud.com/intl/en-us/qs-msgsms/sms_02_0002.html>
