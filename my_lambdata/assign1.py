# my_lambdata/assignment1.py

from pandas import DataFrame
class Wrangler():
    """
    Wrangler takes a dataframe and manipulates it
    """
    def __init__(self, my_df): 
    # self is the constructor
    # my_df a pandas.DataFrame with a column called abbrev.
        self.df = my_df
    
    def add_state_names(self):
        """
        Converts a dataframe with a column of state abbreviations, adding a corresponding column of state names.
        Params:
            my_df a pandas.DataFrame with a column called "abbrev".
        Example:
            add_state_names(df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]}))
        Returns: a pandas.DataFrame with the original col as well as a "name" column.
        """

        

    # need a list or dict with the abbrev/name mappings
        names_map = {"CA": "Cali", "CO": "Colo",
                 "CT": "Conn", "DC": "District of Columbia"}

    # create a new column which maps the existing column using our names map
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    # breakpoint()
    # type(type(new_frame["abbrev"])) #> <class 'pandas.core.series.Series'>
    # dir(new_frame["abbrev"])
        self.df["name"] = self.df["abbrev"].map(names_map)

    def inspect_columns(self):
        print(self.df.columns)
if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    wrangler = Wrangler(df)
    wrangler.add_state_names()
    print(wrangler.df.head())