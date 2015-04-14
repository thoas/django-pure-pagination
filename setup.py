from distutils.core import setup


setup(
    name='django-pure-pagination',
    version='0.2.2',
    author='Florent Messa',
    long_description=open('README.rst').read(),
    license='BSD',
    keywords='pagination, django',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    author_email='florent.messa@gmail.com',
    url='https://github.com/thoas/django-pure-pagination/',
    packages=['pure_pagination'],
    include_package_data=True,
    zip_safe=False,
    package_data={
        'pure_pagination': [
            'pure_pagination/templates',
            'pure_pagination/templates/pure_pagination',
            'pure_pagination/templates/pure_pagination/index.html'
        ],
    },
)
