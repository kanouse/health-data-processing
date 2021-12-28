# health-data-processing
Utilities for processing Apple Health data

## Notes
* After obtaining the Apple Health data from iOS export, extract `export.zip` and place extracted `apple_health_export` folder into `/data`folder. You should then have a path to apple health data which is: `/data/apple_health_export`


## Categories
I found 52 `type` attribute values in my `Records`. The full list in in the file `apple-health-record-types.txt`. The 15 that I care about are listed below:
```
HKQuantityTypeIdentifierDietaryCarbohydrates  
HKCategoryTypeIdentifierAppleStandHour  
HKQuantityTypeIdentifierDietaryCholesterol  
HKQuantityTypeIdentifierActiveEnergyBurned  
HKQuantityTypeIdentifierDietaryEnergyConsumed  
HKQuantityTypeIdentifierDietaryFatSaturated  
HKCategoryTypeIdentifierSleepAnalysis  
HKQuantityTypeIdentifierBasalEnergyBurned  
HKQuantityTypeIdentifierDietarySugar  
HKQuantityTypeIdentifierRestingHeartRate  
HKQuantityTypeIdentifierDietaryFiber  
HKQuantityTypeIdentifierStepCount  
HKQuantityTypeIdentifierBodyMass  
HKQuantityTypeIdentifierDietaryProtein  
HKQuantityTypeIdentifierDietaryFatTotal  
HKQuantityTypeIdentifierBodyFatPercentage  
```
