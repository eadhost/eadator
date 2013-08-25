from setuptools import setup, find_packages
setup(
    name = "eadator",
    version = "0.1",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['lxml'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        'eadator': ['ents/*.dtd', 'ents/*.xsd', 'ents/*.xml', 'ents/*.ent', 'ents/*.dcl' ],
    },
    zip_safe = False,

    # metadata for upload to PyPI
    author = "Brian Tingle",
    author_email = "brian.tingle.cdlib.org@gmail.com",
    description = "This is an Example Package",
    license = "BSD",
    keywords = "validate ead 2002 xml xsd dtd",
    url = "https://github.com/tingletech/eadator",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
    entry_points = {
        'console_scripts': [
            'eadator = eadator.eadator:main',
        ]
    },
    test_suite = "tests.test_eadator"
)
