from setuptools import setup, find_packages

setup(
    name="page-searcher",
    version="0.0.1",
    description="Command Line Tool to parse PDF and search for pages",
    install_requires= ["click==8.1.3","PyPDF2==3.0.1"],
    entry_points= """
    [console_scripts]
    page-searcher=page_searcher.main:main
    """,
    author="Kékéli Afonouvi",
    packages=find_packages()
)