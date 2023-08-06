from django.contrib import admin

from .models import (
    daily_spending,
    desired_non_req_spending,
    desired_required_spending,
    desired_saving,
    income,
    user_account,
)

admin.site.register(user_account.UserAccount)
admin.site.register(income.Income)
admin.site.register(daily_spending.DailySpending)
admin.site.register(desired_non_req_spending.DesiredNonrequiredSpending)
admin.site.register(desired_saving.DesiredRequiredSaving)
admin.site.register(desired_required_spending.DesiredRequiredSpending)
