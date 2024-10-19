from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker
import random
from datetime import datetime, timedelta
from address.models import Address  # Importe o modelo Address

CustomUser = get_user_model()

class Command(BaseCommand):
    help = 'Creates 10 fake users with associated addresses'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')  # Using Brazilian Portuguese locale

        for _ in range(10):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            first_name = fake.first_name()
            last_name = fake.last_name()
            
            # CustomUser fields
            zip_code = fake.postcode()
            city = fake.city()
            state = fake.state_abbr()
            neighborhood = fake.neighborhood()
            gender = random.choice(['M', 'F'])
            complement = f"Apto {fake.random_int(min=1, max=999)}"
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
            street = fake.street_name()
            number = fake.building_number()

            # Separate user fields from additional fields
            user_fields = {
                'username': username,
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
            }

            additional_fields = {
                'zip_code': zip_code,
                'city': city,
                'state': state,
                'neighborhood': neighborhood,
                'gender': gender,
                'complement': complement,
                'birth_date': birth_date,
                'street': street,
                'number': number,
            }

            # Create user with basic fields
            user = CustomUser.objects.create_user(**user_fields)

            # Update user with additional fields if they exist in the model
            for field, value in additional_fields.items():
                if hasattr(user, field):
                    setattr(user, field, value)

            user.save()

            # Criar endereço associado
            address = Address.objects.create(
                user=user,
                city=city,
                state=state,
                neighborhood=neighborhood,
                street=street,
                number=number
            )

            self.stdout.write(self.style.SUCCESS(f'Created user: {username} with address'))

        self.stdout.write(self.style.SUCCESS('Successfully created 10 fake users with addresses'))
