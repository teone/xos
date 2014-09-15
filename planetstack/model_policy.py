from django.db.models.signals import post_save
from django.dispatch import receiver
import pdb
from core.models import *
import model_policies

@receiver(post_save)
def post_save_handler(sender, **kwargs):
	sender_name = sender.__name__
	policy_name = 'model_policy_%s'%sender_name
	try:
		policy_handler = getattr(model_policies, policy_name)
		policy_handler.handle(sender)
	except:
		pass
