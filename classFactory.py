"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
                
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        
        # return DataRow
        def retrieve(self, curs, condition=None):
            # use internal cols and table to build query
            query = "select {0} from {1}".format(",".join(self.cols), self.table)
            if condition != None:
                query += " where " + condition
            curs.execute(query)
            for a in curs.fetchall():
                dr = DataRow(a)
                dr.table = table
                yield dr
        
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow

 
