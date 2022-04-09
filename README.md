# NLP Benchmark

A simple benchmark for NLP tools.

## Tested features

In this repository, we benchmarked:
- Language detection tools
- Sentiment analysis tools
- Date extraction tools

You can find some results we obtained in the `resources` folder.

## Installation

To run the benchmark yourself, just install the dependencies and run `main.py`:

```bash
pip install -r requirements.txt
python3 main.py
```

The total execution time for the whole benchmark can be very long (a few hours).

## Developing a new Runner

This benchmark aims to be easily extensible. 
It works with what we call runners.
A runner corresponds to one NLP tool you want to benchmark

A runner is just a class that returns the information required for the
benchmark.
You can have a look at the `runners` folder to see examples of existing runners.
