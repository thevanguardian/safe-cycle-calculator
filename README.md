# Safe Cycle Calculator

![Project Image](image.png)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-blue)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Safe Cycle Calculator is a tool designed to help you identify which IPs can be shut down while maintaining a specified capacity of their associated applications. This ensures that your system remains operational and efficient, even when certain IPs are taken offline.

## Features

- Identifies optimal IPs to shut down based on application capacity requirements
- Configurable retain percentage for strategic shutdown planning
- Generates test data for simulation and testing
- Provides detailed output in JSON format

## Installation

To install the necessary dependencies, run:

```sh
pip install -r requirements.txt
```
## Usage
### Generate Test Data
To generate the test data, run:
```sh
$ make data
```

### Run the Main Script
To run the main script, use the following command:
```sh
$ python main.py -f ip_app_data.json -r 50
```

### Arguments
The main script supports the following arguments:

- -f, --file: Path to the JSON file containing IP and application data (required).
- -r, --retain_percentage: Percentage of capacity to retain (default: 50).


### Run Unit Tests
To run the unit tests, use:
```sh
$ make test
```

## Contributing
We welcome contributions! Please see our CONTRIBUTING guidelines for more details.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.