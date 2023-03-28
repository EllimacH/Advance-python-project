import random

def create_sample_accounts(num_accounts):
    """
    Creates `num_accounts` sample accounts with easy to remember passwords and usernames.
    """
    common_words = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'welcome', 'football', 'iloveyou', 'admin', 'monkey']
    for i in range(num_accounts):
        username = f"user{i}"
        password = random.choice(common_words)
        print(f"Username: {username}, Password: {password}")

def main():
    create_sample_accounts(10)

if __name__ == "__main__":
    main()