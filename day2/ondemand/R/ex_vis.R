library(readr)

data <- read_csv("plant_growth.csv", col_names = TRUE)

print(data)

plot(data$week, data$height, xlab="Week", ylab="Height", main="Table")