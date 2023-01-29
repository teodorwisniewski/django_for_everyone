import pandas as pd

from unesco.models import Site, Iso, Category, State, Region



def run():

    df = pd.read_csv("whc-sites-2018-clean.csv")


    Site.objects.all().delete()
    Iso.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for index, row in df.iterrows():
        print(index, row)

        iso, created = Iso.objects.get_or_create(name=row["iso"])
        category, created = Category.objects.get_or_create(name=row["category"])
        state, created = State.objects.get_or_create(name=row["state"])
        region, created = Region.objects.get_or_create(name=row["region"])

        site_name = row["name"]
        site_year = row["year"]
        site_latitude = row["latitude"]
        site_longitude = row["longitude"]
        site_description = row["description"]
        site_justification = row["justification"]
        site_area_hectares = row["area_hectares"]

        site = Site(
                    name=site_name,
                    description=site_description,
                    year=site_year,
                    latitude=site_latitude,
                    longitude=site_longitude,
                    area_hectares=site_area_hectares,
                    justification=site_justification,
                    category=category,
                    region=region,
                    iso=iso,
                    state=state
                    )
        site.save()


print("end")
