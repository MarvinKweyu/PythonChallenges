## Background
An administrator wants to create a test with multiple choices along with 
difficulty levels and marks for the said questions. Questions are allowed to
have a difficulty level from 1 to 5. Marks are calculated from multiplying the
difficulty by 2. 

## Bunsiness Rules 

### Problem at hand
We need to get the total marks from each question based on the difficulty level. At the start, we assume there
is no test file, and hence a new one is created.

## Inputs and Output

We need file to store the test. This will contain a list of all test questions.
An example test with one question would look as below:

```
[
  {
    "question": "When was the Olympics?",
    "answers": [
      "zero",
      "2016",
      "2000",
      "yesterday"
    ],
    "difficulty": 3
  }
]
```
As well, display the questions currently created and as a list of questions and 
show the detail of the questions as well. We also need an option to delete these questions
as selected and search across all  of those in the test.

## 
## Pseudocode and calculation

The marks for a question may be calculated as below:
```
makrs = difficulty * 2
```