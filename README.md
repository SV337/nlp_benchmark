# NLP Benchmark

A simple benchmark for NLP tools.

## Tested features

In this repository, we benchmarked:
- Language detection tools
- Sentiment analysis tools
- Date extraction tools

You can find some results we obtained in the `resources` folder.

## Developing a new Runner

This benchmark aims to be easily extensible. 
It works with what we call runners.
A runner corresponds to one NLP tool you want to benchmark

A runner is just a class that returns the information required for the
benchmark.
You can have a look at the `runners` folder to see examples of existing runners.
