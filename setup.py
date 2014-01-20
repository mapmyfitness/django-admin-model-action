import os
from setuptools import setup, find_packages

from adminmodelaction import VERSION

import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version(".".join(map(str, VERSION)), __file__, git_format='%h')
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='django-admin-model-action',
    version=version,
    description='adds the hability to have action buttons on the admin chage view',
    long_description=readme,
    author='Arthur Debert',
    author_email='arthur@stimuli.com.br',
    url='http://github.com/arthur-debert/django-admin-model-action',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

