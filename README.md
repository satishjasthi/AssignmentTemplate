# AssignmentTemplate
Repository to create a template to score the assignment

# Assignment submission structure:
## Directory Structure:
```
ProjectRoot
├── LICENSE
├── README.md
├── src
│   ├── score_model.py
│   └── test_model.py
└── test_data.csv
```

- All the source code should be placed in `src` dir
- `test_model.py` should contain the code to run the model on test data
- `score_model.py` assigns final score based for the assignment
- `test_data.csv` should have two columns 
    - `feature`
    - `label`

- Use python3.6 or above

# To test the model and score it run
```
python src/test_model.py test_data.csv && python src/score_model.py Predictions.csv
```
