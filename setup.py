from setuptools import setup, find_packages

setup(
    name='cradmin-legacy',
    description='Legacy 1.x fork of django_cradmin.',
    version='1.3.0',
    url='https://github.com/appressoas/cradmin_legacy',
    author='Espen Angell Kristiansen, Tor Johansen, Vegard Angell, Magne Westlie',
    author_email='post@appresso.no',
    license='BSD',
    packages=find_packages(
        exclude=[
            'ez_setup',
            'tasks'
        ]),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'django-crispy-forms>=1.6.0',
        'Django>=1.8',
        'django-multiupload',
        'Jinja2',
        'pytz',
        'future',
        'html2text',
        'htmls',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
