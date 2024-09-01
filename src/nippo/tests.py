from django.test import TestCase
from .models import NippoModel
from django.urls import reverse


class NippoTestCsse(TestCase):
    def setUp(self):
        obj = NippoModel(title="testのタイトル", content="testcontenです。")
        obj.save()

# データが正しく保存されているか
    def test_saved_signal_object(self):
        qs_counter = NippoModel.objects.count()
        self.assertEqual(qs_counter, 1)
    
    # ４０４を返すか。
    def test_response(self):
        detail_url = reverse('nippo-detail', kwargs = {"pk": 100})
        detail_response = self.client.get(detail_url)
        update_url = reverse('nippo-detail', kwargs = {"pk": 100})
        update_response = self.client.get(detail_url)
        delete_url = reverse('nippo-detail', kwargs = {"pk": 100})
        delete_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(update_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)

    def test_sreate_on_createView(self):
        url = reverse("nippo-create")
        cereate_data = {"title":"title_from_test", "content":"content_from_test"}
        response = self.client.post(url, cereate_data)
        qs_counter2 = NippoModel.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(qs_counter2, 2)


