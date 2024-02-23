# d.py - Dependency Inversion Principle (DIP) Example
# Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions.

from abc import ABC, abstractmethod

# Abstraction for different authentication methods
class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, username, password):
        pass

class BasicAuth(Authenticator):
    def authenticate(self, username, password):
        # Implement basic authentication
        print(f"BasicAuth: Authenticating user {username} with password {password}")

class OAuth(Authenticator):
    def authenticate(self, username, password):
        # Implement OAuth authentication
        print(f"OAuth: Authenticating user {username} with password {password}")

class GoogleAuth(Authenticator):
    def authenticate(self, username, password):
        # Implement Google authentication
        print(f"GoogleAuth: Authenticating user {username} with password {password}")

def main():
    # Initialize the BasicAuth authenticator
    basic_authenticator = BasicAuth()

    # Authenticate user using BasicAuth
    basic_authenticator.authenticate("user123", "password123")

    # Initialize the OAuth authenticator
    oauth_authenticator = OAuth()

    # Authenticate user using OAuth
    oauth_authenticator.authenticate("user456", "password456")

    # Initialize the GoogleAuth authenticator
    google_authenticator = GoogleAuth()

    # Authenticate user using GoogleAuth
    google_authenticator.authenticate("user789", "password789")

if __name__ == "__main__":
    main()
