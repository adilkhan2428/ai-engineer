# Exercise  2: AI Confidence Score
import numpy as np
np.random.seed(25)
confidence_score = np.random.rand(10)
weight_values = np.random.randn(10)

print("Confidence Score: ")
print(confidence_score)

print("\nWeight Values: ")
print(weight_values)

print("Highest confidence score: ", np.max(confidence_score))

print("Lowest confidence score: ", np.min(confidence_score))

print("Average weight: ", np.mean(weight_values))