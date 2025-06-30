import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

## load the dataset
df=pd.read_csv('spamdetector/spambase.csv')
x=df.drop('spam', axis=1)
y=df['spam']

## split the dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2,random_state=42)

## create a logistic regression model
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Model trained successfully!")


## evaluate the model using accuracy, precision, recall, and F1 score

accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# create a confusion matrix
cm=confusion_matrix(y_test,y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Spam', 'Spam'], yticklabels=['Not Spam', 'Spam'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()  # Ensure labels don't get cut off
plt.savefig('confusion_matrix.png', bbox_inches='tight', dpi=150)
plt.close()  # Close the figure to free memory
print("Confusion matrix saved as 'confusion_matrix.png'")