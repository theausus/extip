from distutils.core import setup

setup(
        description = 'External IP parser',
        author = 'Austin Garrigus',
        url = 'https://github.com/theausus/extip',
        download_url = 'https://github.com/theausus/extip/archive/master.zip',
        author_email = 'theausus@gmail.com',
        version = '0.9',
        packages = ['extip'],
        scripts = ['scripts/extip'],
        name = 'extip',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Topic :: Utilities',
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
            ],
)
