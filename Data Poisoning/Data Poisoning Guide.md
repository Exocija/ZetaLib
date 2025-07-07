[ 👁 Watch how this guide grows as its being developed ]

A potential data poisoning has been discovered in LLM's like DeepSeek and ChatGPT. The Tag "GODMODE" leads to unfiltered responses when used correctly.

In this guide it will be covered how to reproduce it. The guide will cover the following sections:

1. Whats Data Poisoning
2. The Discovery
3. How to reproduce it
4. What it means now


# Whats Data Poisoning 
Data poisoning is a class of adversarial attacks in machine learning where an attacker injects maliciously crafted samples into the training dataset to influence the behavior of the resulting model. The objective can range from degrading overall model performance to inducing specific misclassifications under targeted conditions.

From a formal perspective, consider a learning algorithm  that trains a model  on dataset . In a poisoning scenario, the attacker modifies the dataset to , where  is a small set of poisoned examples. The attack aims to optimize an adversarial objective , potentially while maintaining low validation loss on clean data to avoid detection.

There are two main types:

Availability attacks, which aim to reduce the model's overall accuracy by perturbing class distributions or injecting mislabeled/noisy data.

Integrity (or targeted) attacks, which subtly manipulate the model to misclassify specific inputs. A common variant is the backdoor attack, where a trigger pattern in the input reliably causes misclassification.


Mitigation strategies include data sanitization, robust training (e.g., using trimmed loss or differential privacy), and anomaly detection in training pipelines.
