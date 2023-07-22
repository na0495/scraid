from setuptools import setup, find_packages

# -----------------------------------------

setup(
    name='scraid',
    version='0.12',
    packages=find_packages(),
    install_requires=[
        'scrapy',
        'fake_useragent',
    ],
    author='na0495',
    author_email='saad.mrabet@example.com',
    description='A package for advanced Scrapy functionality and utilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/na0495/scraid',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

    ],
)
