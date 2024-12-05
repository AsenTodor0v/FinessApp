from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Example: At least one uppercase letter, one digit, and one special character
        if not re.search(r'[A-Z]', password):  # At least one uppercase letter
            raise ValidationError('Password must contain at least one uppercase letter.')
        if not re.search(r'\d', password):  # At least one digit
            raise ValidationError('Password must contain at least one digit.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # At least one special character
            raise ValidationError('Password must contain at least one special character.')
        if len(password) < 8:  # Minimum length of 8 characters
            raise ValidationError('Password must be at least 8 characters long.')

    def get_help_text(self):
        return (
            "Your password must contain at least 8 characters, including one uppercase letter, one digit, "
            "and one special character (e.g., !@#$%^&*)."
        )
