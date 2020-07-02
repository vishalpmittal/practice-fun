from app import errors
from app import settings
from app.fake import fake_primary_external_api
from .base import BaseSmsProvider
from app.errors import (
    InvalidContentLength,
    InvalidPhoneNumber,
    ContentNotSet
)


class PrimarySmsApiProvider(BaseSmsProvider):
    """Primary SMS API Provider"""
    API_KEY = settings.PRIMARY_API_KEY

    def _validate_set_recipient(self, *args):
        """Validate recipient using the same logic as defined in `old.py` file.
        Throw appropriate exception or return a boolean"""
        # Implement it
        for arg in args:
            if not arg or not arg.isdigit():
                raise InvalidPhoneNumber('Invalid phone number')
        return True

    def _validate_set_content(self, *args):
        """Validate content.
        Throw appropriate exception or return a boolean"""
        # Implement it
        for arg in args:
            if not arg or len(arg) > 70:
                raise InvalidContentLength('Invalid content length')
        return True

    def _validate_before_sending(self):
        """Check if content and recipient are set.
        Throw appropriate exception from `app.errors` module"""
        # Implement it
        if not self.content:
            raise ContentNotSet("Content are not set yet")
        if not self.recipient:
            raise InvalidPhoneNumber("Receipient is not set")

    def _process_response(self, resp):
        """Check response content.
        Return (boolean, resp)"""
        # Implement it
        return resp.get('status') == 'SENT', resp

    def _prepare_payload(self):
        """Construct and return payload - check `old.py` for the implementation details"""
        # Implement it
        msg = {
            'content': self.content,
            'phone': self.recipient,
            'sender': self.SENDER_NAME,
            'api_key': self.API_KEY,
        }
        return msg

    def send(self):
        """Send the message"""
        self._validate_before_sending()
        payload = self._prepare_payload()
        response = fake_primary_external_api(payload)
        return self._process_response(response)
