#ggmap
#ggplot2
pkgs = c("ggmap","ggplot2")

loadPackages <- function(x){
    new.x <- x[!(x %in% installed.packages()[, "Package"])]
    if (length(new.x))
        install.packages(new.x, dependencies = TRUE)
    sapply(x, require, character.only = TRUE)
}
loadPackages(pkgs)
Df <- read.csv(file="/home/sankarshan/Documents/Work/NYCTaxi/plot_with_R/16_1lat_long_popularity_surcharge.csv", header=TRUE, sep=",")
names(Df)<-c("latitude", "longitude","popularity","surcharge")
lat <- c(40.6155, 40.9301)                
lon <- c(-74.0733, -73.8192) 
#map = get_map(location = c(-74.001555,40.74108),source="google",maptype="roadmap",zoom=12,color=c("bw"))
map = get_map(location = c(lon = mean(lon), lat = mean(lat)),source="google",maptype="roadmap",zoom=12,color=c("bw"))
ggmap(map) + geom_point(
  aes(x=longitude, y=latitude, show_guide = TRUE, colour=surcharge), 
  data=Df, alpha=.8, na.rm = T)  + 
  scale_color_gradient(low="beige", high="red")
