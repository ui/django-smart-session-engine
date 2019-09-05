# -*- coding: utf-8 -*-
import sys
from setuptools import setup

setup(
    name='django-smart-session-engine',
    version='0.0.1',
    author='Stamps Indonesia',
    author_email='hello@stamps.co.id',
    packages=['smart_session_engine'],
    url='https://github.com/ui/django-smart-session-engine',
    license='MIT',
    description='Django session engine on steroids.',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.md']},
    install_requires=['django>=2', 'django-redis>=4'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
