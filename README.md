# Click package Demo

From [https://click.palletsprojects.com/en/8.0.x/][1]:

> "Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box."

- [Click website][1]
- [Click on GitHub][2]
- [Weatherbit current weather API docs][3]

## Get code and set up

- `git clone https://github.com/cleonard/click_pkg_demo_atx_python.git`
- `cd click_pkg_demo_atx_python`
- Create a virtual environment using your tool of choice (`virtualenv`, `pipenv`
  , `conda`) and activate it
- Installation requires the `setuptools` package. Install using pip or conda.
- Run `pip install --editable .`

## Usage

- Run `get_weather --help` to see the documentation that `click` generates
- Run command with no options (it has default values): `get_weather`
- Run with options: `get_weather -c Austin,TX -u I -l es`.  `I` means "Imperial"
  (Fahrenheit (F, mph, in)) and `es` is for Spanish results.

## License

***********************************************************  
"THE BEER-WARE LICENSE" (Revision 42):  
Chris Leonard <<ccl@chrisleonard.com>> wrote this file.  As long as you retain
this notice you can do whatever you want with this stuff. If we meet some day,
and you think this stuff is worth it, you can buy me a beer in return.  
***********************************************************

[1]: https://click.palletsprojects.com/en/8.0.x/
[2]: https://github.com/pallets/click/
[3]: https://www.weatherbit.io/api/weather-current
