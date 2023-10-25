import datetime

from src.domain.entity.calendar import Calendar, Week


class TestCalendar:
    def test_create(self):
        name = "고도"
        birthday = datetime.date(1988, 6, 21)
        lifespan = 80
        calendar = Calendar.create(name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan
        assert len(calendar.years) == lifespan + 1
        assert len(calendar.years[0].weeks) == 52

    def test_update_basic_info(self):
        calendar = Calendar.create("고도", datetime.date(1988, 6, 21), 80)

        name = "뉴고도"
        birthday = datetime.date(2000, 6, 21)
        lifespan = 100
        calendar.update_basic_info(name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan
        assert len(calendar.years) == lifespan + 1
        assert len(calendar.years[0].weeks) == 52

    def test_age(self):
        calendar = Calendar.create("고도", datetime.date(1988, 6, 21), 80)
        assert calendar.age == 35

        calendar = Calendar.create("고도", datetime.date(1988, 12, 31), 80)
        assert calendar.age == 34


class TestWeek:
    def test_time_type_before_born(self):
        week = Week(
            yearnum=1987,
            weeknum=1,
            today=datetime.date.today(),
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "before_born"

        week = Week(
            yearnum=1988,
            weeknum=1,
            today=datetime.date.today(),
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "before_born"

    def test_time_type_after_death(self):
        week = Week(
            yearnum=2089,
            weeknum=1,
            today=datetime.date.today(),
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "after_death"

        week = Week(
            yearnum=2088,
            weeknum=30,
            today=datetime.date.today(),
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "after_death"

    def test_time_type_past(self):
        today = datetime.date(2023, 6, 21)
        week = Week(
            yearnum=2023,
            weeknum=1,
            today=today,
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "past"

    def test_time_type_now(self):
        today = datetime.date(2023, 6, 21)
        week = Week(
            yearnum=2023,
            weeknum=today.isocalendar().week,
            today=today,
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "now"

    def test_time_type_future(self):
        today = datetime.date(2023, 6, 21)
        week = Week(
            yearnum=2023,
            weeknum=52,
            today=today,
            birthday=datetime.date(1988, 6, 21),
            lifespan=100,
        )
        assert week.time_type == "future"
