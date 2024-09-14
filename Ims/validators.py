import re
from rest_framework import serializers


def validate_video_url(value):
    """ Валидация ссылки на видео (только youtube) """
    if value == "https://www.youtube.com/" or value == "https://youtube.com/":
        raise serializers.ValidationError(
            "Это корневая ссылка на YouTube, она не содержит в себе конкретного видео об уроке.")
    if not re.match(r'^https?://(www\.)?youtube\.com(/.+)?$', value):
        raise serializers.ValidationError('Ссылки на сторонние ресурсы запрещены. Используйте только youtube.com.')
