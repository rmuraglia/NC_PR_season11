# pr_from_skout.r

library(tidyverse)

dat_all <- read.table('dat/season_11.csv', header=T, sep=',')

dat_trim <- dat_all %>% select(Name, Total.Played, Score)

min_match_req <- 20
dat_trim %>% filter(Total.Played >= min_match_req) %>% .[1:20,]