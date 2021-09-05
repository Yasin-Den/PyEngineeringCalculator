from setuptools import find_packages, setup

long_description = '''
An Engineering Calculator for Windows. Specifically designed for Electrical & IT Engineering at the moment.
'''

requirements = [
    'PyQt5',
    'numpy',
    'matplotlib'
]
# requirements = [
#     line.strip()
#     for line in open('requirements.txt').readlines()
# ]

setup(
    name='PyEngineeringCalculator',
    version='1.0.0',
    author='Yasin Khosh manesh',
    author_email='eayeay33g@gmail.com',
    url='https://github.com/eayeay33/PyEngineeringCalculator',
    install_requires=requirements,
    keywords=[
        'PyEngineeringCalculator', 'Engineering Calculator', 'Engineering',
        'Calculator', 'engineering calculator'
    ],
    description='This engineering calculator developed with python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
