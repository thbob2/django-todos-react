#!! 
#!!     _  _   _   _____         _         __             _       _ _                                
#!!   _| || |_| | |_   _|__   __| | ___   / /__  ___ _ __(_) __ _| (_)_______ _ __ ___   _ __  _   _ 
#!!  |_  ..  _| |   | |/ _ \ / _` |/ _ \ / / __|/ _ \ '__| |/ _` | | |_  / _ \ '__/ __| | '_ \| | | |
#!!  |_      _|_|   | | (_) | (_| | (_) / /\__ \  __/ |  | | (_| | | |/ /  __/ |  \__ \_| |_) | |_| |
#!!    |_||_| (_)   |_|\___/ \__,_|\___/_/ |___/\___|_|  |_|\__,_|_|_/___\___|_|  |___(_) .__/ \__, |
#!!                                                                                     |_|    |___/ 

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')