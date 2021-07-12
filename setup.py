import sys

from setuptools import setup

if sys.version_info < (3, 6, 0):
    sys.exit("Python 3.6+ required but lower version found. Aborted.")

install_requires = ["click", "requests"]

setup(
    name="click_pkg_demo_atx_python",
    author="Chris Leonard (@cleonard)",
    author_email="ccl@chrisleonard.com",
    description="A demonstration of the Python Click package",
    py_modules=["weather_click"],
    entry_points="""
        [console_scripts]
        get_weather=weather_api:cli
     """,
    include_package_data=True,
    install_requires=install_requires,
    version="0.0.1",
    url="https://github.com/cleonard/click_pkg_demo_atx_python",
)
