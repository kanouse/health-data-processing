from datetime import date
import xml.etree.ElementTree as ET
import sqlite3

# where is the data?
EXPORT_FILENAME = "data/apple_health_export/export.xml"
root = ET.parse(EXPORT_FILENAME).getroot()
conn = sqlite3.connect("health-data.db")
cursor = conn.cursor()

# when to we start counting?
START_DATE = date.fromisoformat("2021-10-19")


def main():

    for item in root.iter('Record'):
        # make sure we care about the record type
        t = item.get("type")
        if t not in preferred_types:
            continue

        # make sure it's from a date that matters
        d = date.fromisoformat(item.get("creationDate")[:10])
        if d < START_DATE:
            continue

        unit = item.get("unit")
        value = item.get("value")

        sql = """
            insert into main.health_data
            (type, unit, value, creation_date)
            values
            (?, ?, ?, ?)
        """

        print(sql, (t, unit, value, d))
        cursor.execute(sql, (t, unit, value, d))



def list_health_metric_types(root):
    """
    Finds all the distinct type values used in the health records

    :param root: the XML root
    :return: pass
    """
    types = []
    for item in root.iter('Record'):
        types.append(item.get("type"))

    types_distinct = list(set(types))
    for t in types_distinct:
        print(t)

    pass

preferred_types = [
"HKQuantityTypeIdentifierDietaryCarbohydrates",
"HKCategoryTypeIdentifierAppleStandHour",
"HKQuantityTypeIdentifierDietaryCholesterol",
"HKQuantityTypeIdentifierActiveEnergyBurned",
"HKQuantityTypeIdentifierDietaryEnergyConsumed",
"HKQuantityTypeIdentifierDietaryFatSaturated",
"HKCategoryTypeIdentifierSleepAnalysis",
"HKQuantityTypeIdentifierBasalEnergyBurned",
"HKQuantityTypeIdentifierDietarySugar",
"HKQuantityTypeIdentifierRestingHeartRate",
"HKQuantityTypeIdentifierDietaryFiber",
"HKQuantityTypeIdentifierStepCount",
"HKQuantityTypeIdentifierBodyMass",
"HKQuantityTypeIdentifierDietaryProtein",
"HKQuantityTypeIdentifierDietaryFatTotal",
"HKQuantityTypeIdentifierBodyFatPercentage"
]

main()