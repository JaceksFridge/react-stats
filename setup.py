from setuptools import setup, find_packages

setup(
    name="react_stats",
    version="0.76",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "printr = react_stats.printr:main",
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