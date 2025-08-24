# Python Utilities

A collection of reusable Python functions covering a wide range of tasks. The project is organized into folders by topic and includes unit tests for each module.

## Contents

- **asyncio_functions/** – helpers for asynchronous programming such as task throttling, retries and timeouts.
- **compression_functions/** – utilities for compressing and decompressing data with algorithms like BZ2, GZIP, LZMA, Snappy, Zlib and Zstandard.
- **decorators/** – decorator functions for caching, conditional execution and error handling.
- **file_functions/** – file system helpers for copying files, creating directories and parsing tabular data.
- **iterable_functions/** – operations for lists, sets and other iterables.
- **linux_functions/** – utilities for monitoring Linux processes and resources.
- **multiprocessing_functions/** – patterns for parallel processing using the `multiprocessing` module.
- **pandas_functions/** – simple wrappers around common `pandas` DataFrame tasks.
- **print_functions/** – print formatted messages and system information to the terminal.
- **statistics_functions/** – basic statistical calculations.
- **strings_utility/** – handy string manipulation helpers.
- **data_types/** – implementations of data structures such as graphs, heaps and queues.

## Installation

This project requires Python 3.10 or later.

```bash
# clone the repository
git clone https://github.com/MForofontov/python-utils
cd python-utils

# create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# install runtime dependencies
pip install -r requirements.txt

# install additional packages for development and testing
pip install -r requirements_dev.txt
# alternatively install the optional "dev" extras defined in `pyproject.toml`
pip install -e .[dev]
```
`tqdm` is used for progress bars. The runtime requirements file also installs
`aiohttp` for asynchronous HTTP helpers and `pandas` for the dataframe utilities.

## Running Tests

You **must** install the development dependencies before running tests. Use
`pip install -r requirements_dev.txt` or install the optional `dev` extras via
`pip install -e .[dev]`. These packages include `pytest` and
`pytest-asyncio` in addition to the runtime requirements. If they are missing,
tests will raise import errors. After installing the dependencies, you can run
all tests and generate an Allure report using the helper script:

```bash
bash pytest.sh
```

The script runs tests from `pytest/unit` and stores the report under `pytest_run_tests/`.
The Allure command-line tool is required to generate the reports. If you don't have it installed, follow the [official installation guide](https://docs.qameta.io/allure/#_installing_a_commandline).

## Example Usage

Import modules directly from the package. For example, to capitalize each word in a string:

```python
from python_utils.strings_utility.capitalize_words import capitalize_words

print(capitalize_words("hello world"))  # -> 'Hello World'
```

## Logging

Set up a logger once in your application and pass it to any decorator that
accepts the optional ``logger`` parameter.

```python
import logging

logger = logging.getLogger("python_utils")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

from python_utils.decorators.throttle import throttle

@throttle(0.5, logger=logger)
def my_function():
    ...
```

The `timeout` decorator is also thread-based so it works on all platforms,
including Windows. When the specified limit is reached a `TimeoutException` is
raised while the underlying thread may still finish in the background.

## Contributing

1. Fork the repository and create a new branch.
2. Make your changes and add tests when appropriate.
3. Commit your work and open a pull request.

## License

This project is licensed under the [GNU GPLv3](LICENSE).

