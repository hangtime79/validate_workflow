# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
new_customers_prepared = dataiku.Dataset("new_customers_prepared")
new_customers_prepared_df = new_customers_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

python_Out_df = new_customers_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
python_Out = dataiku.Dataset("Python-Out")
python_Out.write_with_schema(python_Out_df)
