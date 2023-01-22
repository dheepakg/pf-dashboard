setwd("~/Desktop/WorkArea/GitHub/pf-dashboard/")
install.packages("RSQLite")
library(dplyr)
library(dbplyr)
library(ggplot2)

# Connect to sqlite
ppfas_db <- DBI::dbConnect(RSQLite::SQLite(), "data/mutual-fund.db")

# Read from sqlite DB
txn_data <- tbl(ppfas_db, sql("SELECT * FROM txn_dim"))
# Chart
typeof(txn_data)

# TODO Chart it. 
# Make the chart extendable to other funds
# Include marker for top-ups

