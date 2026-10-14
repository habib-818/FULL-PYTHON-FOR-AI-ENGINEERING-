## THIS EXAMPLE GIVEN USING OPEN AI 'API' CONFIG

class APIconfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_token=100):
        self.api_key = api_key
        self.model = model
        self.max_token = max_token
        self.url = "https://api.openai.com/v1"


# Using positional for arg, named for optional
dev_config = APIconfig("sk-dev-key", max_token=50)


# Using all named arguments (clearest)
prod_config = APIconfig(api_key="sk-dev-key", model="gpt-4", max_token=1000)


# Access the configuration
print(dev_config.model)
print(prod_config.model)
print(prod_config.max_token) 