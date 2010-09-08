from distutils.core import setup
import fabtastic

long_description = open('README.md').read()

setup(
    name='django-fabtastic',
    version=fabtastic.VERSION,
    packages=['fabtastic', 
              'fabtastic.db', 
              'fabtastic.fabric',
              'fabtastic.fabric.commands', 
              'fabtastic.management',
              'fabtastic.management.commands'],
    description='A Django app that uses Django manage.py extension commands with Fabric for deployment.',
    author='Gregory Taylor',
    author_email='gtaylor@duointeractive.com',
    license='BSD License',
    url='http://github.com/duointeractive/django-fabtastic',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)