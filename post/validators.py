from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date


def validate_password(value):
    if len(value) < 8:
        raise ValidationError(_("Пароль должен содержать минимум 8 символов."))
    if not any(char.isdigit() for char in value):
        raise ValidationError(_("Пароль должен содержать минимум одну цифру."))


def validate_email_domain(value):
    allowed_domains = ["mail.ru", "yandex.ru"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValidationError(_("Домен почты должен быть mail.ru или yandex.ru."))


def validate_age(value):
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )
    if age < 18:
        raise ValidationError(_("Автор поста должен быть старше 18 лет."))


def validate_prohibited_words(value):
    prohibited_words = ["ерунда", "глупость", "чепуха"]
    for word in prohibited_words:
        if word in value.lower():
            raise ValidationError(_(f'Заголовок не должен содержать слово "{word}".'))
