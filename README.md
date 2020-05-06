# lambdata-gerald

## Installation 

pip install -i https://test.pypi.org/simple/ lambdata-gerald
## Usage
This package allows you to train test split with 
from my_lambdata.dfpkg import Learning
It also allows you to make all string in a column upper case 
from my_lambdata.dfpkg import Learning

example for case method
instantiate the class Learning 
mylearn = Learning(df) name of dataframe
mylearn.case("Column_name")) use this syntax to invoke the case method upon a column for upper string data
print(mylearn.data)

example for split method
instantiate the class Learning
mylearning2 = Learning(df)
mylearn.split("target_name") place your y variable in the parenthesis
print(mylearn.X_test) or .X_train to see your split in data 

