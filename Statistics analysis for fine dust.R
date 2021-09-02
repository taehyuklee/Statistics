install.packages("moonBook")
install.packages("mice")
install.packages("moonBook")
install.packages("VIM")
install.packages("Amelia")

library("ggplot2")  #graphic
library("Amelia")   #missing map
library("VIM")      #missing map과 
library("moonBook") #na.count 함수 
library("mice")     #Imputation 함수

x.1=read.csv("C:/Read/Jongro.csv")
x.1=read.csv("C:/Read/imputed1.csv")

head(x.1)

#x.1 = x[,-13 ]

#str(x.1)

########################### 데이터 개수 총 데이터 개수의 50% 미만 걸러내기 ########################


# 1. missing map으로 (mice VIM package)
miss <- aggr(x.1, col=c('navyblue','red'),
             numbers=TRUE, sortVars=TRUE,
             labels=names(x.1), cex.axis=.5,
             gap=3, ylab=c("Missing data","Pattern"))


# 2. Data frame으로 Data의 형태들을 Check# 

str(x.1) #total 'data.frame': 94224 obs. of 37 variables

head(is.na(x.1))

sum(is.na(x.1)) #x.1의 총 결측값 662640

#Total 31 variables

# 3. Data 개수 25% 미만인 것들 걸러내기 (제거)
for(i in (4:32)){
  # c = names(x.1[i])
   b = sum(is.na(x.1[,i]))
  # sprintf("%s:%d", (x.1[1,i]), sum(is.na(x.1[,i])))
  
         if (b>(94224*0.5)){
          
       {print(names(x.1[i]))
         } #last man removal
          
         }
}
#Reuslt "precipitation", "Drifted.snow", "3 hr Drifted snow", "the lowset cloud altitude", "State of ground", 현상번호 국내식"

head(x.1)

#데이터 부족한 것 제거 이후
x.1=x.1[, c(-14, -24, -29, -25, -31, -32 )]

## 제거된 데이터 data.frame 확인
str(x.1)


########################### variable name: sum of NA #############################

sprintf("%s:%d", names(x.1[28]), sum(is.na(x.1[,28])))

# NA numbers: 
# SO2: 2855, CO: 2674, O3: 2664, NO2: 2611, PM10: 3124, PM2.5: 5363 
# Temperature: 6, Precipitation: 84913, Wind.Speed:48, Wind Direction: 48, 
# Relative.humidity:25, Vapor.pressure:1850, Dew.point:1850, Spot.pressure:1855
# Sea.level.pressure:1852, #22 Sunshine.hour:42576, # 23 Solar.radiation:42770, #24: Drifted.snow:89100
# #25: 3hour drifted.snow:93895, Total.Cloudy:20417, middle and low cloudy:17168, cloud form:
# #29: the lowest cloud.altitude:49179, Visibility:13969, #31: State.of.ground:81785, #32: code num: 60099
# Ground.surface.temp:2387, earth.temp.5cm: 9368, 10cm: 9370, 20cm: 9382, 30cm:9447

# removal target: Drifted.snow, 3hour drifted.snow, State.of.ground, code num, Precipitation 


########################### 운형 다시 한 번 보기 ###############################

table(x.1$cloud.form)
summary(x.1$cloud.form)

as.data.frame(table(x.1$cloud.form)) # 41166개 
94224-41166 #out 인

x.1=x.1[, -25] #--> Total 28 varaibles
str(x.1)
################################################################################


# 4. 제거된 데이터 정리후 NA결측값 정리하고 처리하기 

x.final=na.omit(x.1) #Complete.cases (listwisedeletion)

str(x.final) # Final 형태의 dataset 형성하기 


#50% 이상이면 제거 한 것
write.csv(x.1, file="processed.csv", row.names = FALSE)

missing2= read.csv("processed.csv")

str(missing2)

# 5. 최종데이터 Missing map으로 확인하기

mice_plot = aggr(missing2, col=c('light blue','white'), prop= FALSE,
                  numbers=TRUE, sortVars=TRUE,
                  labels=names(missing2), cex.axis=.55,
                  gap=3, ylab=c("Missing data","Pattern"))


mice_plot = aggr(x.final, col=c('light blue','white'), prop= FALSE,
                 numbers=TRUE, sortVars=TRUE,
                 labels=names(x.1), cex.axis=.7,
                 gap=3, ylab=c("Missing data","Pattern"))

md.pattern(x.1)

str(x.1)


####################### Regression imputation ############################ 

# Deterministic regression imputation

De.reg = mice(x.de.reg, method = "norm.predict", m = 1) # Impute data
De.reg.result = complete(De.reg) # Store data
str(De.reg.result)
head(De.reg.result)

write.csv(De.reg.result, file="De.reg.csv", row.names = FALSE)

# Stochastic regression imputation

St.reg = mice(x.1, method = "norm.nob", m = 1, maxit = 150) # Impute data
St.reg.result = complete(St.reg) # Store data
str(St.reg.result)
head(St.reg.result)



mice_plot = aggr(St.reg.result, col=c('light blue','white'), prop= FALSE,
                 numbers=TRUE, sortVars=TRUE,
                 labels=names(St.reg.result), cex.axis=.55,
                 gap=3, ylab=c("Missing data","Pattern"))


write.csv(St.reg.result, file="St.reg.it150.csv", row.names = FALSE)


################## multiple try imputation #################### 
dim(x.1)
x.2 = x.1[,5:28]
dim(x.2)
#time 
imputed.data = mice(x.2, m=5, method="pmm")



fit1=with(imp,lm(Sepal.Length~Petal.Length+Species))
summary(imputed.data)

imputed.data$imp$Wind.direction
imputed.data$imp$Total.cloudy
imputed.data$imp$middle.and.low.cloud
imputed.data$imp$Vapor.pressure
imputed.data$imp$Dew.point
imputed.data$imp$Visibility
imputed.data$imp$earth.temperature..10cm.
imputed.data$imp$earth.temperature..5cm.
imputed.data$imp$earth.temperature..20cm.
imputed.data$imp$earth.temperature..30cm.
imputed.data$imp$Sea.level.pressure
imputed.data$imp$spot.pressure

result1=complete(imputed.data)
result2=complete(imputed.data,2)
result3=complete(imputed.data,3)
result4=complete(imputed.data,4)
result5=complete(imputed.data,5)

impute1 = read.csv("imputed2.csv")


mice_plot = aggr(impute1, col=c('light blue','white'), prop= FALSE,
                 numbers=TRUE, sortVars=TRUE,
                 labels=names(impute1), cex.axis=.55,
                 gap=3, ylab=c("Missing data","Pattern"))


###################### After multiple Imputation, Anaylsis ##################

####### predictor (예측변수) Matrix
imputed.data$predictorMatrix


# Distribution #
xyplot(imputed.data, PM2.5 ~ Wind+Temp+Solar.R,pch=18,cex=1)


#convergence 확인
plot(imputed.data)

result_f = cbind(x.1[,1:4],result1)


write.csv(result_f, file="C:/Read/imputed2.csv", row.names = FALSE)

x.3=na.omit(result1[, -23])


fit= with(data=imputed.data, lm(Total.cloudy~NO2+SO2+O3+PM2.5+PM10+Dew.point+Visibility+Wind.direction))

result=pool(fit)
summary(result)




################################################### end Imputation ####################################################









######################################### Jongro-gu Time series ###########################################

## omit NA 1Area, 2Location, 3Code, 5Address, 12 Address
x.final=x.final[, c(-1, -2, -3, -5, -12)]

str(x.final) #61246, 23 variables 


## Mice ## imputated data
x.final.mi = x.3[, c(-1, -2, -3, -5, -12)]
str(x.final.mi)


