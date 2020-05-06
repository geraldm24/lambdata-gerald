import pandas 
from sklearn.model_selection import train_test_split
class Learning():
    def __init__(self, df):
        self.data = df
    """ Using self as a constructor for data in datframe
    The goal is to wrangle some data below we turn all string to upper and 
    also make a train test split
    """
    def case(self,X):        
        self.data[X] = self.data[X].str.upper()
        
    def split(self, target):
        self.y = self.data[target]
        self.X = self.data.drop(target,axis=1)   
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y)


if __name__ == "__main__":
    hardware_cnames = ['Vendor_name', 'Model_name', 'MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX', 'PRP', 'ERP']
    df = pandas.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/cpu-performance/machine.data',
                        names=hardware_cnames)


    mylearning = Learning(df)
    print(mylearning.data)
    mylearning.case("Vendor_name")
    print(mylearning.data)
    mylearning.split("ERP")
    print(mylearning.X_train)




        