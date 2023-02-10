setwd("~/Desktop/WorkArea/GitHub/pf-dashboard")
# install.packages("DBI")
options(scipen=999) # turn off scientific notation like 1e+06
library(DBI)  # To access DB
library(ggplot2) # To build graph
library(plotly) # To have interactive graph
library(htmlwidgets) # To save graph as HTML

colorSepia <- "#fff1e5"

con <- dbConnect(RSQLite::SQLite(), dbname = "data/mutual-fund.db")
dbListTables(con)

queryResult <- dbGetQuery(con, "select yearqtr, sum(invested) as invested from v_fund_qtr_txn group by yearqtr order by yearqtr ;")

print(is.data.frame(queryResult))

ggplot(data = queryResult, aes(x = yearqtr, y = invested)) +
  geom_point() 


investedOverQtr <- ggplot(data = queryResult, 
                          aes(x = yearqtr, y = invested/1000,
                              text = paste('₹', invested))) +
  geom_line(colour = "DarkBlue", group=1) +
  labs(x= "Year - Quarter",
       y="Invested Amount (₹ 1000)",
       title = "Invested Amount over Quarters",
       subtitle = "",
       caption = "Source - Github/dheepakg: pf-dashboard/src/r/chart.r"
       
  ) +
  theme(
    plot.title = element_text(face = "bold"),  
    plot.title.position = "panel",
    axis.text.x=element_text(angle=45,hjust=1),
    axis.line = element_line(colour = "black"),
    axis.title.y = element_text(color = "DarkBlue"),
    axis.title.y.right = element_text(color = "Brown"),
    plot.background = element_rect(fill = colorSepia),
    panel.background = element_rect(fill = colorSepia),
    panel.grid.minor.x = element_blank(),
    panel.grid.major.x = element_blank(),
    
  )

investedOverQtr

# ggplotly(,tooltip = c("y",'text'))
interactive_graph <- ggplotly(,tooltip = c('text'))

saveWidget(widget=interactive_graph, 
           file = "output/invested-over-quarters.html",  # Output file name
           selfcontained=TRUE) # Remove folder after HTML file is generated




