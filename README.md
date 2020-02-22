# Pilgen - (WIP: optimizing) 

Python Image-Label dataset Generator for OCR

## Generate

```bash
python3 generate.py --lang ug --count 100 --out-dir data/
```

This command will output `100` images into folder `data/images/`, filename pattern is `'word_{}.jpg'.format(line_num)`, exmaple:
```
data/images/word_1.jpg
data/images/word_2.jpg
...
data/images/word_100.jpg
```

and a `gt.txt` file, its content pattern is `'{}\t{}'.format(filepath, word)`, like below:

```
data/images/word_1.jpg	ئانا
data/images/word_2.jpg	تىلىم
...
data/images/word_100.jpg	گۈللە

```

## Supported languages

* [x] ug - Uyghur (Uighur)
* [ ] other langs may will come

## Test

```bash
python3 test.py
```

## Develop environment

* Ubuntu 18.04.1
* Python 3.6.9

## Author

Salam Hiyali

## Contirubute

> Feel free

## License

MIT
