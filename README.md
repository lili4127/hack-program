
# hack-program

My program plays rock paper scissors lizard spock against the computer. It first learns
from sampling games so it can make better decisions, then plays the computer, and prints the result!

Install this package locally with:

```bash
cd mypackage/
pip install -e .
```

This will install a CLI tool that can be called as follows:

```bash
# run with default equal probabilities 1/5
mymodule --t 1000 
```
or

```bash
# run with default equal probabilities 1/5
mymodule --trials 1000 
```
```
I won 47.27% of 1000 trials (ties=194)
```

```bash
# run with biased probabilities
mymodule --t 1000 --p 0.6 0.1 0.1 0.1 0.1
```

or

```bash
# run with biased probabilities
mymodule --trials 1000 --probs 0.6 0.1 0.1 0.1 0.1
```

```
I won 64.2% of 1000 trials (ties=176)
```