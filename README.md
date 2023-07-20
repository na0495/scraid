# Scraid

scraid is a Python library that provides advanced utilities for Scrapy, including an advanced features and utilities.

## Installation

You can install scraid from PyPI:

```bash
pip install scraid
```

## Usage

Here's a basic example of how to use the AdvancedRequest class:


```python
from scraid.advanced_request import advancedRequest

request = AdvancedRequest('http://example.com')
print(request.headers['User-Agent'])  # prints the random User-Agent
```

## License
[MIT](https://choosealicense.com/licenses/mit/)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## TODO

- [ ] Add more scrapy most common utilities (middlewares, pipelines, etc.)
- [ ] Add more advanced request features
- [ ] Add more documentation
