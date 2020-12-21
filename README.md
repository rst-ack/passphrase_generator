# passphrase_generator

Leverages Python's [secrets](https://docs.python.org/3/library/secrets.html) module to generate a secure passphrase from a wordlist

## Installation

Other than cloning this repo, no installation is required.

All of `genpass.py` dependencies are Python 3.6 built-in libraries.

## Usage

### Wordlists

By default, `genpass.py` uses the [`words.txt` file](https://github.com/dwyl/english-words/blob/master/words.txt) (from commit [11735d0](https://github.com/dwyl/english-words/commit/11735d0d68f051b817ad224e14d999acc94fcf00) of [dwyl's english-words repo](https://github.com/dwyl/english-words)) to generate a passphrase.

`words.txt` contains words that may include numbers and/or symbols. If you don't want to use words with numbers/symbols in them to generate your password, you can instead use [`words_alpha.txt`](https://github.com/dwyl/english-words/blob/master/words_alpha.txt) by calling `genpass.py` with the `-w` option, like this:

```bash
./genpass.py -w ./wordlists/words_alpha.txt
```

If you need, you can update `words.txt` and/or `words_alpha.txt` with a later commit from dwyl's repo.

Otherwise, if you so wish, you can create your own wordlist to generate passphrases from, and use them the same way you specify to use `words_alpha.txt` instead of `words.txt`.

### Generating passphrases

By default, `genpass.py` generates a single, 4-word-long passphrase without spaces.

If you want to generate more than one passphrase at once, you can use the `-n` option to specify an integer value of the number of passphrases you want to generate.

Similarly, if you want to generate a passphrase of custom length, simply use the `-l` option to specify an integer value of the number of words you want your passphrase to include.

Finally, if you want your passphrase to include spaces (although I don't necessarily recommend this - a surprising number of systems don't support spaces in passwords), simply use `--spaces` when calling `genpass.py`.

## Contributing

Pull requests are welcome for this project. Please include as much detail as possible about the changes, including:

* What they are
* Why you've made them or why you think they're needed

