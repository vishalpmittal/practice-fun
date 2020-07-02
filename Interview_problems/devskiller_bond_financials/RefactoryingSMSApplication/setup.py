import sys
from setuptools import find_packages, setup

# TODO: ugly hack for old nosetests runner
if '--with-xunit' in sys.argv:
    sys.argv.remove('--with-xunit')

packages = [
  'pytest==4.6.4',
  'pytest-timeout==1.3.3',
  'pytest-runner',
]

setup(
    name='sms_provider_refactor',
    version='1.0.0',
    author='Devskiller',
    author_email='support@devskiller.com',
    packages=find_packages(),
    python_requires='>=3.5',
    include_package_data=True,
    zip_safe=False,
    install_requires=packages + [
        'wheel',
        'setuptools==41.0.1',
    ],
    setup_requires=packages,
    tests_require=packages,
)
