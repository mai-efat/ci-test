from setuptools import setup, find_packages

setup(
    name='jformat',
    version='0.1',
    description='يحول أي ملف لـ JSON',
    entry_points={
        'console_scripts': [
            'jformat=jformat.main:main',
        ],
    },
    install_requires=['click'],
    packages=find_packages()
)