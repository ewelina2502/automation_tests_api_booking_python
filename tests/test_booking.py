import pytest

from models import booking
from models.booking import Bookings


def test_get_ids():
    get_ids = booking
    get_ids.get_ids_booking()


def test_get_id_fixture(new_booking):
    get_id_fixture = booking
    get_id_fixture.get_id_fixture(new_booking)


def test_get_id_details_from_fixture_return_json(new_booking):
    get_id_details = booking
    get_id_details.get_id_details_from_fixture(new_booking)


def test_add_booking():
    add_booking = Bookings()
    add_booking.add_booking()


def test_get_token():
    get_token = booking
    get_token.get_token()


def test_delete_newbooking(new_booking, new_token):
    delete_nb = booking
    delete_nb.delete_booking(new_booking, new_token)


def test_put_booking(new_booking, new_token):
    put_nb = booking
    put_nb.put_booking(new_booking, new_token)


def test_patch_booking(new_booking, new_token):
    patch_nb = booking
    patch_nb.patch_booking(new_booking, new_token)


@pytest.fixture
def new_booking():
    new_booking_one = Bookings()
    return new_booking_one.add_booking()


@pytest.fixture
def new_token():
    new_token_code = booking
    return new_token_code.get_token()
