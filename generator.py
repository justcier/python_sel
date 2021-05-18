import random
import string
import string_utils


class Generator:

    def __init__(self):
        self.upper_letters_list = "".join([string.ascii_uppercase])
        self.upper_letters_list2 = [string.ascii_uppercase]
        self.lower_letters_list = "".join([string.ascii_lowercase])
        self.digits_list = "".join([string.digits])
        self.special_characters_list = "".join([string.punctuation])
        self.email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com", "live.com"]

    def generate_string(self, amount_of_lower, amount_of_upper=0, amount_of_digits=0, amount_of_special=0):
        letters_to_use = [''.join(random.choice(self.upper_letters_list) for x in range(amount_of_upper)),
                          ''.join(random.choice(self.lower_letters_list) for x in range(amount_of_lower)),
                          ''.join(random.choice(self.digits_list) for x in range(amount_of_digits)),
                          ''.join(random.choice(self.special_characters_list) for x in range(amount_of_special))]

        letters_to_use_str = "".join(letters_to_use)
        return string_utils.shuffle(letters_to_use_str)

    def generate_email(self, amount_of_lower, amount_of_upper=0, amount_of_digits=0, amount_of_special=0):
        local_part = self.generate_string(amount_of_lower, amount_of_upper, amount_of_digits, amount_of_special)
        email_domain = random.choice(self.email_domains)
        email_gen = local_part + "@" + email_domain
        return email_gen

    def generate_password(self, amount_of_lower, amount_of_upper=0, amount_of_digits=0, amount_of_special=0):
        return self.generate_string(amount_of_lower, amount_of_upper, amount_of_digits, amount_of_special)
