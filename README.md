jenkjobs
========

RSDT@UCL's extension to jenkins job builder.

Using it is as easy as installing it. Then [distribute](https://pypi.python.org/pypi/distribute) does the rest.


Doxygen publisher:
------------------

Requires the doxygen plugin. 

```yaml
publishers:
    - doxygen:
        doxyfile: path to doxyfile relative to workspace. Required.
        working_directory: path to working directory relative to workspace. Defaults to ""
        node: nodename. Defaults to "".
        keep: whether to keep previous docs. Defaults to false.
```

The doxygen files should be found in the input working directory. They must by some other process.
This plugins only publishes them.
