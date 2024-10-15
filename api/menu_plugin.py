from typing import Annotated
from semantic_kernel.functions import kernel_function
from database.menu import menu
import json


class MenuPlugin:

    pizzaMenu = menu

    @kernel_function(
        name="get_automated_pizza_menu",
        description="Gets a list of pizza names. Will try to evaluate based on criteria what the best selection is",
    )
    def get_automated_pizza_menu(
        self,
        pizzaNames: list[str],
    ) -> Annotated[str, "returns a list of pizza names in json format"]:
        """Returns list of pizzas."""

        print("Planner called: get_automated_pizza_menu")
        print(pizzaNames)

        filteredMenu = []
        for pizza in self.pizzaMenu:
            if pizza["name"] in pizzaNames:
                filteredMenu.append(pizza)

        # Convert to json string
        jsonMenu = json.dumps(filteredMenu)
        return jsonMenu
