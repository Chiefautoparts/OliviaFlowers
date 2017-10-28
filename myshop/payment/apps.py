# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'myshop.payment'
    verbose_name = 'mpyshop.Payment'

    def ready(self):
    	import myshop.payment.signals
