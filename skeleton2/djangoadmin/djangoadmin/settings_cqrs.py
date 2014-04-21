METEOR_MONGO_DATABASES = {
    'meteorapp': {
        'HOST': '127.0.0.1',
        'PORT': 3001,
        'DB': 'meteor',
    }
}

from mongoengine import connect
# connect(METEOR_MONGO_DATABASES["meteorapp"]["DB"], host=METEOR_MONGO_DATABASES["meteorapp"]["HOST"], port=METEOR_MONGO_DATABASES["meteorapp"]["PORT"])
connect("meteor", host="mongodb://127.0.0.1:3001/meteor")
