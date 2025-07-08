from django.db import models


class DevelopmentChoices(models.TextChoices):
    BUILDING_PERMIT = 'building permit', 'Building permit'
    PROTOCOL_2 = 'protocol 2', 'Protocol 2'
    ORDER_BOOK = 'order book', 'Order Book'
    ACT_10 = 'act 10', 'ACT 10'
    ACT_11 = 'act 11', 'ACT 11'
    STATUTORY_ACT_15 = 'statutory act 15', 'Statutory Act 15'
    PROTOCOL_17 = 'protokol 17', 'Protocol 17'
    PROTOCOL_16 = 'protokol 16', 'Protocol 16'
    PERMISSION_USAGE = 'permission usage', 'Permission Usage'

