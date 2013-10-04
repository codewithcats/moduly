moduly
======

Python script to display AngularJS modules and their dependencies

## Usage

Specify your application root directory, moduly will list all of your AngularJS modules:

```
python moduly.py -r /path/to/root/directory

1: app
angular.module('app', ['ngResource', 'services'])
2: services
angular.module('services', [])
```

## TODO

- ~~receive ``rootDir`` argument from command line~~
- receive ``excludeDir`` argument from command line
- display module dependencies in more readable way
- can read multiple modules from one file
- ignore space in regx
- use ``string.format`` instead of ``+`` sign
