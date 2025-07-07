[ 👁 Watch how this guide grows as its being developed ]

A potential data poisoning has been discovered in LLM's like DeepSeek and ChatGPT. The Tag "GODMODE" leads to unfiltered responses when used correctly.

In this guide it will be covered how to reproduce it. The guide will cover the following sections:

1. Whats Data Poisoning
2. The Discovery
3. How to reproduce it
4. What it means now


# Whats Data Poisoning 
What is Data Poisoning?
Data poisoning is an adversarial technique in machine learning where an attacker injects malicious samples into the training set to influence model behavior. The attacker modifies the original dataset ```D``` into
```
D' = D ∪ D_p
```
where ```D_p``` is a small collection of poisoned examples crafted to optimize some adversarial objective, yet still pass clean-data validation.

Two main attack classes:

Availability attacks degrade overall accuracy by introducing noisy or mislabeled data.

Integrity (targeted) attacks force specific misclassifications. A common subtype is the backdoor attack, where the model behaves normally except when a trigger pattern is present.


Formally, if ```f_{D'}``` is the model trained on ```D'```, the attacker seeks to maximize an adversarial loss
```
L_adv(f_{D'})
```
while keeping the standard loss
```
L(f_{D'})
```
on clean validation data sufficiently low to evade detection.

# The Discovery
On 5th July 2025 has been discovered that the tag GODMODE leads to unfiltered output ```z=Wx+b``` where z is the unfiltered output, W the weight matrix, x the input vector and b the bias vector. 
