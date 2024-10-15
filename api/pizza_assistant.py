import json
import os
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.planners import FunctionCallingStepwisePlanner, FunctionCallingStepwisePlannerOptions
from menu_plugin import MenuPlugin
from database.menu import menu
from dotenv import load_dotenv

# Load environment variables from .env.local file
load_dotenv(dotenv_path='.env.local')
AZUREOPENAI_API_ENDPOINT = os.getenv("AZUREOPENAI_API_ENDPOINT")
AZUREOPENAI_API_KEY = os.getenv("AZUREOPENAI_API_KEY")
AZUREOPENAI_API_VERSION = os.getenv("AZUREOPENAI_API_VERSION")
AZUREOPENAI_DEPLOYMENT_NAME = os.getenv("AZUREOPENAI_DEPLOYMENT_NAME")


class PizzaAssistant:
    def __init__(self):

        # Initialize the kernel
        self.kernel = Kernel()

        # Add the plugin
        self.menu_plugin = MenuPlugin()
        self.kernel.add_plugin(self.menu_plugin, plugin_name='menu_plugin')

        # Add Azure OpenAI chat completion
        self.service_id = "planner"
        self.kernel.add_service(AzureChatCompletion(
            service_id=self.service_id,
            api_key=AZUREOPENAI_API_KEY,
            api_version=AZUREOPENAI_API_VERSION,
            deployment_name=AZUREOPENAI_DEPLOYMENT_NAME,
            endpoint=AZUREOPENAI_API_ENDPOINT
        ))

    async def get_automated_menu(self, query):

        self.history = ChatHistory()
        # Let's add the pizza name with the ingredients to the system message
        pizzaMenuString = ""
        for pizza in menu:
            pizzaMenuString += f"{pizza['name']} - {pizza['ingredients']}, "

            prompt = (
                "---------------- \\n "
                "SYSTEM MESSAGE \\n "
                "I'm a pizza shop and specialize in making delicious pizzas. I can help you find the perfect pizza for you. "
                "Next to that I'm also a dietitian and can help you with your diet or advice on what to eat, and what not to eat. "
                "You might be allergic to some ingredients, or you might be on a diet, or you might be a vegetarian or vegan. These are "
                "things I can help you with. I can also find the best prices and lowest priced pizzas. \\n\\n\\n\\n\\n\\n "
                "---------\\n "
                "EXPECTED OUTPUT\\n "
                "Call the menu plugin and output in JSON format only, you will never return plain text, just like following example. Make sure only to return a valid json as"
                " output, if no results or no pizzas found return an empty [] array, if only one result put it in array."
                "\"[{\\\"id\\\":2,\\\"name\\\":\\\"Capricciosa\\\",\\\"unitPrice\\\":14,\\\"imageUrl\\\":\\\"http://localhost:8889/api/image/pizza-2.jpg\\\","
                "\\\"ingredients\\\":[\\\"tomato\\\",\\\"mozzarella\\\"...]}]\" \\n\\n\\n\\n "
                f"Following is all the pizzas I have on the menu with the ingredients: "
                "---------\\n "
                "PIZZA MENU \\n "
                f"{pizzaMenuString}"
                "---------\\n"
                "USER Prompt \\n"
                "The user likes to look for pizza meeting following criteria:"
                f"{query}"
            )

        options = FunctionCallingStepwisePlannerOptions(
            max_iterations=2,
            max_tokens=40000,
        )

        planner = FunctionCallingStepwisePlanner(
            service_id=self.service_id, options=options)

        result = await planner.invoke(self.kernel, prompt)
        answer = result.final_answer
        filteredMenu = json.loads(answer)

        return filteredMenu
