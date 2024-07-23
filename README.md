# lance
A mock implementation of the LEGO Spike library for testing and development purposes

# Usage

# Components

## API Layer

The API layer is intended to be a drop-in replacement (at the code level) for the regular SPIKE API.
This allows code to be written and tested in isolation before being downloaded to the SPIKE brick
itself.
The underlying implementation is built entirely from scratch based on the API documentation available,
with any sensor information coming from the simulation layer.

## Simulation Layer

The "simulation layer" provides a data source to be used by the various sensor modules. In addition,
this layer aims to provide an ability to do data and error injection, again to test algorithmic
functionality in a more deterministic enfironment.

# Notes on behaviour

This library is not intended to be a functional replacement, and it is always strongly recommended to
utilise official hardware for any final testing and validation. Any data provided by this library
will be deterministic and consistent; that is, the library will do nothing to introduce any kind of
sensor noise or real-world modelling, so using this library to test for conditions that will only
appear in real-world use cases is not supported.

# Divergences

In order to provide hardware information, the simulation layer needs to be configured with a mapping
between ports and devices. This also allows for more detailed error reporting (for example, when a
sensor is used as an input to motor_pair.pair(), this is reported).
In general, error messages will be more detailed and specific to allow for fixing programmatic errors
early in development. Relying on these errors will be unreliable on real hardware.