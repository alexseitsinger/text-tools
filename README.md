# Find Best String

## Description

Finds the best matching string in a larger string. Returns either the first match or all matches, and their match value.

## Installation

```
pip install find-best-string
```

or

```
pipenv install find-best-string
```

## Arguments

1. query - String of text to find matches of in corpus.
2. corpus - String of text to scan for matches of query.
3. step - Step size of first match-value scan through corpus. Can be thought of as a sort of "scan resolution". Should not exceed length of query.
4. flex - Max left/right substring position adjustment value. Should not exceed length of query / 2.
5. case_sensitive - If false, converts corpus and query to lowercase before fiding matches.

## Usage

```python
from find_best_string import find_best_string

corpus = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
query = "Ipsum"

first_match = find_best_string(query, corpus)
```