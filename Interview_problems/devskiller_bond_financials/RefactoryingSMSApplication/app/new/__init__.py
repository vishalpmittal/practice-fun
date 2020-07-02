"""New SMS module"""
from .providers import PrimarySmsApiProvider, SecondarySmsApiProvider


def sms_factory(api):
    """Implement a factory that creates appropriate objects based on the `api` argument.
    When `api` is unknown, throw NotImplementedError exception."""
    # Implement it
    sms_providers = {'primary', 'secondary'}
    if not api or api not in sms_providers:
        raise NotImplementedError
    if api == 'primary':
        return PrimarySmsApiProvider()
    elif api == 'secondary':
        return SecondarySmsApiProvider()


