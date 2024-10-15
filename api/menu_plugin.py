from typing import Annotated
from semantic_kernel.functions import kernel_function
from database.menu import menu
import json


class MenuPlugin:

    pizzaMenu = menu

    @kernel_function(
        name="get_pizza_menu_filtered",
        description="Gets a list of pizza names. Will try to evaluate based on criteria what the best selection is",
    )
    def get_pizza_menu_filtered(
        self,
        pizzaNames: list[str],
    ) -> Annotated[str, "returns a list of pizza names in json format"]:
        """Returns list of pizzas."""
        filteredMenu = []
        for pizza in self.pizzaMenu:
            if pizza["name"] in pizzaNames:
                filteredMenu.append(pizza)

        # Convert to json string
        jsonMenu = json.dumps(filteredMenu)
        return jsonMenu
