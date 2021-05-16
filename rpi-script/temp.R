library(ggplot2)
raw_data <- read.csv("temp.log", header = FALSE)
colnames(raw_data) <- c("Date", "Temperature")
raw_data$Date <- as.POSIXct(raw_data$Date, format = "%Y-%m-%d_%H:%M:%S")
raw_data$Daytime <- format(raw_data$Date,"%H")
raw_data$Daytime[raw_data$Daytime == "09" | raw_data$Daytime == 10] <- "morning"
raw_data$Daytime[raw_data$Daytime == 15 | raw_data$Daytime == 16] <- "afternoon"
raw_data$Month <- format(raw_data$Date,"%B")
raw_data$Year <- format(raw_data$Date,"%Y")


ggplot(raw_data, aes(Date, Temperature, color = Daytime)) + geom_line()
