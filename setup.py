from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="react_stats",
    version="0.86",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ahoy = react_stats.ahoy:main",
            "make-assets = react_stats.make_assets:main",
            "auto-assets = react_stats.auto_assets:main",
            "get-stats = react_stats.get_stats:main"
        ]
    },
    package_data={'react_stats': ['languages.json', 'assets.json']},
    install_requires=[
        'tabulate',
        'chardet',
        'pandas',
        'asciibars',
        'watchdog'
    ]
)