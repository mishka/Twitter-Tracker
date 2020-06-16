import json
from time import sleep
from requests import post
from datetime import datetime
from urllib.parse import quote as qt
from twitter_scraper import Profile


# https://twitter.com/i/user/xxx
CHAD_ID = 'your telegram chat id'
USERNAME, USERID = 'username', 000000000000 # twitter username and userID
TOKEN = 'telegram api bot token'
SLEEP_INTERVAL = 90 # how often you want it to check in seconds
JSON_FILENAME = 'db.json'


def telegram(text):
    log(f'Sending --> {text}')
    post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAD_ID}&text={qt(text)}&parse_mode=markdown')


def log(text):
    time = datetime.now().strftime('%H:%M:%S')
    print(f'| {time} | {text}')


def json_rw(read, content = None):
    file_mode = 'r+' if read else 'w'

    with open(JSON_FILENAME, file_mode) as f:
        if not read:
            json.dump(content, f, indent = 4, sort_keys = True, ensure_ascii=False)
            return

        if not f.read(1):
            return json.loads('{}')

        f.seek(0)
        return json.loads(f.read())


def fetch(username = None, userID = None):
    user = username or userID
    profile = Profile(user)
    db = json_rw(1)

    values = (
        ('Name',          'name',            0),
        ('Website',       'website',         0),
        ('Birthday',      'birthday',        0),
        ('Username',      'username',        0),
        ('Biography',     'biography',       0),
        ('Private',       'is_private',      0),
        ('Profile Photo', 'profile_photo',   0),
        ('Banner Photo',  'banner_photo',    0),
        ('Likes',         'likes_count',     1),
        ('Tweets',        'tweets_count',    1),
        ('Following',     'following_count', 1),
        ('Followers',     'followers_count', 1)
    )

    if not db:
        for _, name, __ in values:
            value = getattr(profile, name)
            if name == 'birthday' or name == 'is_private' or name == 'website':
                value = str(value)

            db[name] = value
    else:
        for template, name, is_diff in values:
            value = getattr(profile, name)

            if name == 'birthday' or name == 'is_private' or name == 'website':
                value = str(value)

            if value == db[name]:
                continue

            if is_diff:
                diff = value - db[name]

            db[name] = value

            telegram(f'{template}: `{diff}`')

    json_rw(0, db)


while(1):
    try:
        log('Fetching..')
        fetch(username = USERNAME)
        log('Sleeping..')

        sleep(SLEEP_INTERVAL)
    except Exception as e:
        telegram(f'`{e}`')
        sleep(60)