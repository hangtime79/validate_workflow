library(dataiku)

# Recipe inputs
crm_last_year_db <- dkuReadDataset("crm_last_year_db", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
r_Out <- crm_last_year_db # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(r_Out,"R_Out")
