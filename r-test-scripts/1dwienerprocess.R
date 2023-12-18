N <- 1000;
dis <- rnorm(N, 0, 1);
cumdis <- cumsum(dis);
plot(cumdis, type = "l", main = "Wiener process in One Dimension", xlab = "time", ylab = "displacement");