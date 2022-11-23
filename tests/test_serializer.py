from unittest import TestCase
from django.contrib.auth.models import User

from mainapp.serializers import *
from mainapp.models import *

class TestMijozSer(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id":5, "ism":"Ali",
            "tel":"+998916693704", "manzil":"Marg'ilon, markaz",
              "qarz":0,
            "user":User.objects.get(id=1)}

    def test_mijoz_ser(self):
        ser = MijozSerializer(self.data)
        assert ser.data['id'] == 5
        assert ser.data['ism'] == "Ali"
        assert ser.data['tel'] == "+998916693704"
        assert ser.data['manzil'] == "Marg'ilon, markaz"

class TestSuvSer(TestCase):
    def setUp(self) -> None:
        self.data = {
            "id":5, "brend":"Oltiariq",
            "narx":4000, "litr":1,
              "batafsil":"Yaxshi suv"}

    def test_suv_ser(self):
        ser = SuvSerializer(self.data)
        assert ser.data['id'] == 5
        assert ser.data['brend'] == "Oltiariq"
        assert ser.data['narx'] == 4000
        assert ser.data['litr'] == 1
