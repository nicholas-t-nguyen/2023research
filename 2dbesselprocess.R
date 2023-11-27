N <- 1000;
disx <- rnorm(N, 0, 1);
disy <- rnorm(N, 0, 1);
disz <- rnorm(N, 0, 1);
cumdisx <- cumsum(disx);
cumdisy <- cumsum(disy);
cumdisz <- cumsum(disz);
norm <- sqrt(cumdisx^2 + cumdisy^2 + cumdisz^2);
plot(norm, type="l", main="Bessel process of 3d Wiener process", xlab="time", ylab="norm");