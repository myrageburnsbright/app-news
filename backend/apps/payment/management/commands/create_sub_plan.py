from django.core.management.base import BaseCommand
from apps.subscribe.models import SubscriptionPlan
class Command(BaseCommand):
    help = "Описание команды"

    def handle(self, *args, **options):
        premium_plan = SubscriptionPlan.objects.create(
            name="Premium Monthly Plan",
            price=12.00,
            duration_days=30,
            stripe_price_id="price_1SguSpIA8BzQl8H1tlj4q1pw",
            features={
                "priority_support": True,
                "unlimited_projects": True,
                "advanced_analytics": True,
                "no_ads": True
            },
            is_active=True
        )
        premium_plan.save()
        self.stdout.write("premium plan created!")