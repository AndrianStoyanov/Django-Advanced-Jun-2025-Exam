from typing import Optional
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible


def validate_name(name):
    for ch in name:
        if not ch.isalnum() and ch != '-' and ch != ' ':
            raise ValidationError('The company name is invalid!')


def validator_phone(value):
    if not value.isdigit():
        raise ValidationError('Your phone number is invalid!')


@deconstructible
class SizeValidator:
    def __init__(self, file_size: int, message: Optional[str]=None):
        self.file_size = file_size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        self.__message = value or f"File size must be less than {self.file_size}MB"

    def __call__(self, value: UploadedFile) -> None:
        if value.size > self.file_size * 1024 * 1024:
            raise ValidationError(self.message)