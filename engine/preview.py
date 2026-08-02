class RoadbookPreview:

    def show_day(self, day):

        print("=" * 40)

        print(f"Dag {day.day}")
        print(day.title)

        print()

        print(f"Sträcka: {day.distance_km} km")
        print(f"Körtid: {day.ride_time}")

        print()

        print("Tankstopp:")

        for stop in day.fuel_stops:
            print(
                f"- {stop['name']} ({stop['km']} km)"
            )

        print()

        print("Lunch:")

        if day.lunch:
            print(
                f"- {day.lunch['place']}"
            )

        print()

        print("Sevärdheter:")

        for sight in day.sights:
            print(
                f"- {sight}"
            )

        print()

        print("Tips:")

        for tip in day.tips:
            print(
                f"- {tip}"
            )

        print("=" * 40)