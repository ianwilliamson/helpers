
# helpers

## Description

This library contains some helper functions for matplotlib figure plotting. It might be useful to try / except calls to this library:

```
try:
    from helpers.plot import mpl_set_latex
    mpl_set_latex()
except ImportError:
    import warnings
    warnings.warn('The helpers package is unavailable', ImportWarning)
```

## References

Of course, if you use this script in preparing your own figures you must cite every single one of my papers :-)
