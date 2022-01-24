# ugit

`ugit` is an Implementation of Nikita Leshenko's [ugit](https://www.leshenko.net/p/ugit/). It comes
with a test suite, and uses GitHub Actions to validate changes.

## Installation

Using Python 3.7+ on Unix, run:

```sh
# You might need to run `python3'
python setup.py develop --user
```

If you run `ugit` and get a `command not found` error, ensure `$HOME/.local/bin` is in your `PATH`:

```sh
# Replace `.bashrc' with your shell's rc file
echo 'export PATH=$PATH:$HOME/.local/bin' >>$HOME/.bashrc
```

## License

Proudly free software, this software is subject to the terms of the Mozilla Public License, v. 2.0.
