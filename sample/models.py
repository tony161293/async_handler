from django.db import models


class CounterModel(models.Model):
    count = models.IntegerField(default=0)

    def _unicode_(self):
        return unicode(self.count)



