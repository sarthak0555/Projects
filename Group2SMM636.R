##Question 1
library(corrplot)
## Import data
movie<- read.csv("C:/Users/Desktop/IMDB-Movies.csv", header = TRUE, sep = ",")
dim(movie)
movie<-na.omit(movie)
dim(movie)
numerical<-movie[,c(8:11)]
head(numerical)

##Data summary
summary(numerical)
corr<-cor(numerical)
corrplot(corr,add=TRUE, type="lower", method="number",order="AOE", col="black",diag=FALSE,tl.pos="n", cl.pos="n")

##PCA
library(ggplot2)
pca <- prcomp(numerical, center = TRUE,scale = TRUE)
summ1 <- summary(pca)
summ1

loadings <-pca$rotation[, 1:2]
loadings 

# Plot
df1 <- as.data.frame(pca$x[,1:2])
df1 <- data.frame(df1, Year= movie$Year)
xlab1 <- paste0("PC1(",round(summ1$importance[2,1]*100,2),"%)")
ylab1 <- paste0("PC2(",round(summ1$importance[2,2]*100,2),"%)")

ggplot(df1 ,aes(x=PC1,y=PC2,color=Year))+ geom_point()

### Cluster results
library(cluster)
kmeans_res <- kmeans(df1[,1:2], centers = 3, nstart = 10)
pca_cluster <- cbind(df1[,1:2], Cluster = as.factor(kmeans_res$cluster))


ggplot(pca_cluster, aes(x = PC1, y = PC2, color = Cluster)) +
  geom_point(size = 3) +
  labs(x = "PC1", y = "PC2") +
  stat_ellipse(size = 2, alpha = 0.2) +
  scale_color_manual(values = c("#E41A1C", "#377EB8", "#4DAF4A"))

