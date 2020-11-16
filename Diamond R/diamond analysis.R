# Diamond Analysis
# Rick Scavetta
# 29.09.2020
# A small case study for EDA and stats

# load packages
library(tidyverse)
library(ggplot2)

# Read in the data (csv format):
# Newer methods from tidyr package
jems <- read_csv("data/diamonds.csv")

# super convenient way
# library(rio) # R i/o
# jems2 <- import("data/diamonds.csv")

# Get familiar with our data:
summary(jems)
names(jems)
glimpse(jems)

# more detail:
attributes(jems)
typeof(jems)

#How many diamonds with a clarity of category “IF” are present in the data-set? - 
#What fraction of the total do they represent?

jems %>%
  filter(clarity == "IF")%>%
   nrow()

#What proportion of the whole is made up of each category of clarity?

length(jems$clarity)
#What is the cheapest diamond price overall? 
min(jems$price)

#What is the range of diamond prices? 
range(jems$price)
#What is the average diamond price in each category of cut and color?
mean(jems$price)

#Make a scatter plot that shows the price of a diamond as described 
# by another continous variable,like the carat.

cut_price <- ggplot(jems, aes(x = cut, y = price))
              + geom_point()
              cut_price + geom_point()

carat_price <- ggplot(jems, aes(x = carat, y = price))
              + geom_point()

# Exercise 8.11 (Displaying models)
carat_price <- ggplot(jems, aes(x = carat, y = price))
                   + 
              geom_point()
              geom_smooth()
