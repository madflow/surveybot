from setuptools import setup, find_packages
import sys, os

version = '0.1'

def _read(fn):
    path = os.path.join(os.path.dirname(__file__), fn)
    return open(path).read()

setup(name='surveybot',
      version=version,
      description="A friendly online-survey bot",
      long_description=_read('README.md'),
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='online-surveys',
      author='madflow',
      author_email='',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'mechanize'
      ],
      entry_points={
          'console_scripts': [
              'surveybot = surveybot.ui:main',
          ],
      }
      )
