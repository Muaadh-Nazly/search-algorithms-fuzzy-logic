# Fuzzy Logic - Error Likelihood Prediction

## 📋 Overview

Implementation of a **Fuzzy Logic System** for predicting error likelihood and determining appropriate mitigation strategies based on system parameters. Built using Python and scikit-fuzzy library.

## 🎯 Objectives

- Design fuzzy inference system for error prediction
- Implement membership functions for input variables
- Create rule-based decision making system
- Determine error mitigation strategies based on fuzzy logic

## 🧠 Fuzzy Logic System Design

### Input Variables (Antecedents)

1. **Data Redundancy**
   - Range: 0-10
   - Membership Functions: Low, Medium, High
   - Description: Level of data redundancy in the system

2. **Degradation Level**
   - Range: 0-10
   - Membership Functions: Low, Medium, High
   - Description: System degradation level

3. **Error History**
   - Range: 0-25
   - Membership Functions: Low, Medium, High
   - Description: Historical error frequency

### Output Variables (Consequents)

1. **Error Likelihood**
   - Range: 0-30
   - Membership Functions: Low, Medium, High
   - Description: Probability of error occurrence

2. **Error Mitigation**
   - Range: 0-30
   - Membership Functions: Replication, Masking
   - Description: Recommended mitigation strategy

## 📊 Membership Functions

### Triangular Membership Functions

All input and output variables use **triangular membership functions** (trimf):

```python
# Example for Data Redundancy
data_redundancy['low'] = fuzz.trimf([0, 0, 15])
data_redundancy['medium'] = fuzz.trimf([0, 15, 30])
data_redundancy['high'] = fuzz.trimf([15, 30, 30])
```

### Membership Function Parameters

| Variable | Low | Medium | High |
|----------|-----|--------|------|
| Data Redundancy | [0, 0, 15] | [0, 15, 30] | [15, 30, 30] |
| Degradation Level | [0, 0, 15] | [0, 15, 30] | [15, 30, 30] |
| Error History | [0, 0, 15] | [0, 15, 30] | [15, 30, 30] |
| Error Likelihood | [0, 0, 15] | [0, 15, 30] | [15, 30, 30] |

### Mitigation Strategies

- **Replication:** [0, 0, 20] - Data replication strategy
- **Masking:** [0, 20, 45] - Error masking strategy

## 🔄 Fuzzy Inference Process

### 1. Fuzzification
- Convert crisp input values to fuzzy sets
- Determine membership degrees for each linguistic variable

### 2. Rule Evaluation
- Apply fuzzy rules to determine output membership
- Combine multiple rules using fuzzy operators

### 3. Aggregation
- Combine outputs from all rules
- Create unified fuzzy output set

### 4. Defuzzification
- Convert fuzzy output to crisp value
- Use center of gravity (centroid) method

## 🛠️ Implementation

### Technology Stack
- **Language:** Python 3
- **Library:** scikit-fuzzy (skfuzzy)
- **Dependencies:** numpy


## 📝 Code Structure

### Cell 1: Imports
```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
```

### Cell 2: Fuzzification
- Define input variables (antecedents)
- Set universe of discourse ranges

### Cell 3: Membership Functions
- Define triangular membership functions
- Assign linguistic labels (Low, Medium, High)

### Cell 4: Output Variables
- Define output variables (consequents)
- Set output ranges

### Cell 5: Output Membership Functions
- Define membership functions for outputs
- Define mitigation strategies

### Cell 6: Fuzzy Rules
- Create rule base
- Define IF-THEN rules

### Cell 7: Control System
- Create fuzzy control system
- Set up inference engine

### Cell 8: Simulation
- Input crisp values
- Run fuzzy inference
- Get defuzzified outputs

## 🎯 Application Domain

This fuzzy logic system is designed for:
- **System Reliability:** Predicting error likelihood
- **Quality Control:** Assessing system degradation
- **Risk Management:** Determining mitigation strategies
- **Decision Support:** Automated decision making under uncertainty


## 🔍 Key Concepts

### Fuzzy Sets
- Allow partial membership (0 to 1)
- Handle uncertainty and vagueness
- Natural language representation

### Linguistic Variables
- Human-readable descriptions
- Low, Medium, High categories
- Intuitive interpretation

### Rule-Based System
- IF-THEN rules
- Multiple conditions
- Combined outputs

## 📈 Advantages of Fuzzy Logic

1. **Handles Uncertainty:** Works with imprecise data
2. **Human-Like Reasoning:** Mimics human decision making
3. **Robust:** Handles noisy or incomplete data
4. **Interpretable:** Rules are understandable
5. **Flexible:** Easy to modify rules


