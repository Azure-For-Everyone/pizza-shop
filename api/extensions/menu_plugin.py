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

    @kernel_function(
        name="filter_pizza_based_on_price",
        description="When a user is looking a specific price range for a pizza.",
    )
    def filter_pizza_based_on_price(self,
                                    min_price: int,
                                    max_price: int
                                    ) -> Annotated[str, "returns a list of pizzas in json format"]:
        """Returns a list of pizzas based on price range."""

        print("Planner called: filter_pizza_based_on_price")
        query = f"min_price={min_price} - max_price={max_price}"
        print(query)

        # Filter the menu based on the query
        filteredMenu = [
            item for item in self.pizzaMenu
            if min_price <= item['unitPrice'] <= max_price
        ]

        # Convert to json string
        jsonMenu = json.dumps(filteredMenu)
        return jsonMenu
