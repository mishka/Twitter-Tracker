import json
from time import sleep
from requests import post
from datetime import datetime
from urllib.parse import quote as qt
from twitter_scraper import Profile

JSON_FILENAME = 'db.json'
SLEEP_INTERVAL = 90 # how often you want it to check in seconds

USERNAME = '' # enter twitter username here
USERID =  0000 # enter twitter userID here, see --> https://tweeterid.com/

CHAT_ID = 'your telegram chat id'
TOKEN = 'telegram api bot token'


def telegram(text):
    log(f'Sending --> {text}')
    post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={qt(text)}&parse_mode=markdown')


def log(text):
    time = datetime.now().strftime('%H:%M:%S')
    print(f'| {time} | {text}')


def json_rw(read, content = None):
    file_mode = 'r+' if read else 'w'

    try:
        with open(JSON_FILENAME, file_mode) as f:
            if not read:
                json.dump(content, f, indent = 4, sort_keys = True, ensure_ascii=False)
                return

            if not f.read(1):
                return json.loads('{}')

            f.seek(0)
            return json.loads(f.read())
    except FileNotFoundError:
        open(JSON_FILENAME, 'w').close()
        return json.loads('{}')


def get_username(user_id):
    r = post("https://tweeterid.com/ajax.php", data = {'input': user_id}).text
    return r[1:]


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
        msg = ''
        for template, name, is_diff in values:
            value = getattr(profile, name)

            if name == 'birthday' or name == 'is_private' or name == 'website':
                value = str(value)

            if value == db[name]:
                continue

            if is_diff:
                diff = str(value - db[name])
                
                if not '-' in diff:
                    diff = f'+{diff}'
                
                diff = f'{value} ({diff})'

            db[name] = value

            msg += f'`{template}:` {diff}\n' if is_diff else f'`{template}:` {value}\n'

        if msg:
            telegram(msg)

    json_rw(0, db)

USERNAME = get_username(USERID) if not USERNAME else USERNAME

while(1):
    try:
        log('Fetching..')
        fetch(username = USERNAME)
        log('Sleeping..')

        sleep(SLEEP_INTERVAL)
    except Exception as e:
        telegram(f'`{e}`')
        sleep(60)
