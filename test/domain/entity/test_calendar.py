import datetime
import uuid

from src.domain.entity.calendar import Calendar, Week


class TestCalendar:
    def test_create(self):
        user_id = uuid.uuid4()
        name = "고도"
        birthday = datetime.date(1988, 6, 21)
        lifespan = 80

        calendar = Calendar.create(user_id, name, birthday, lifespan)

        assert calendar.user_id == user_id
        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan
        assert len(calendar.years) == lifespan + 1
        assert len(calendar.years[0].weeks) == 52

    def test_update_basic_info(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
        name = "뉴고도"
        birthday = datetime.date(2000, 6, 21)
        lifespan = 100

        calendar.update_basic_info(name, birthday, lifespan)

        assert calendar.name == name
        assert calendar.birthday == birthday
        assert calendar.lifespan == lifespan
        assert len(calendar.years) == lifespan + 1
        assert len(calendar.years[0].weeks) == 52

    def test_this_year_percentage(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)

        assert calendar.this_year_percentage == 81.37

    def test_deathday(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)

        assert calendar.deathday == datetime.date(2068, 6, 21)

    def test_age(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
        assert calendar.age == 35

        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 12, 31), 80)
        assert calendar.age == 34

    def test_total_percentage(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
        assert calendar.total_percentage == 44.18

    def test_past_week_count(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
        assert calendar.past_week_count == 1787

    def test_future_week_count(self):
        calendar = Calendar.create(uuid.uuid4(), "고도", datetime.date(1988, 6, 21), 80)
        assert calendar.future_week_count == 2270


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
