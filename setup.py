from setuptools import setup

setup(name='cryptocompy',
      packages=['cryptocompy'],
      version='0.1.1.dev2',
      description='Simple wrapper for the public Cryptocompare API.',
      keywords = '',
      author='Titian Steiger',
      author_email='titian.steiger@gmail.com',
      url='https://github.com/wildsmileofbutterfly/cryptocompy',
      download_url='https://github.com/wildsmileofbutterfly/cryptocompy/archive/0.1.1.dev2.tar.gz',
      license='MIT',
      python_requires='>=3',
      install_requires=['requests'],)