
#Creating a scatter of fico and interst rate
png('Interest.Fico.png')
plot(data$Fico.Avg, data$Interest.Rate,pch=19,col=groupedInterest,ylab="",xlab="")
mtext("Fico Mean",side=1,line=2,at=max(data$Fico.Avg))
mtext("Interest Rate",side=2,las=1,line=-3,at=1.05*max(data$Interest.Rate))
abline(lm1,col='blue',lwd=3)
dev.off()