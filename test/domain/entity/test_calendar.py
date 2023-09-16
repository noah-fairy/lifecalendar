import datetime

from src.domain.entity.calendar import Calendar


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
