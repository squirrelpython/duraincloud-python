from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Beta',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='duraincloud-python',
    version='1.0.0',
    description='A simple Python API for mm.duraincloud.com',
    long_description=open('README.md').read() + '\n\n',
    long_description_content_type='text/markdown',
    url='https://github.com/squirrelpython/duraincloud-python',
    author='Emrecan Ayas',
    author_email='emrecanayas06@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='duraincloud duraincloud-sms free number',
    packages=find_packages(),
    install_requires=['requests']
)