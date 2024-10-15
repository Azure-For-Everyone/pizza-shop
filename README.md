# Microsoft's Pizza Shop

Welcome to the Pizza Ordering Web Application! This project is built using React for the frontend and Python for the backend. The idea is to provide a seamless experience for users to order pizzas and search for their favorite pizzas using a smart search powered by Semantic Kernel and OpenAI.

## Concept

The main concept of this project is to create a user-friendly web application where users can browse a pizza menu, add pizzas to their cart, create orders, and track their orders. The application leverages Semantic Kernel and OpenAI to enable a smart search feature, allowing users to search for pizzas using natural language.

## Features

- **Menu Browsing:** Browse the delicious pizza menu and choose your favorite items.
- **Cart Management:** Add pizzas to the cart, view cart contents, and remove items if needed.
- **Order Creation:** Create a new pizza order, provide your contact information, and choose delivery priority.
- **Order Tracking:** Track the status of your order and view the estimated delivery time.
- **Smart Search:** Use natural language to search for pizzas using Semantic Kernel and OpenAI.

## Screenshots

<img src="https://github.com/JoseAlbDR/react-pizza-shop/assets/128265706/3368925b-462b-4eef-81f3-c5c6bccdade2" height="200px" width="300px"/>
<img src="https://github.com/JoseAlbDR/react-pizza-shop/assets/128265706/e288326b-1a21-4902-bb7c-5e7ee1b358fa" height="200px" width="300px"/>
<img src="https://github.com/JoseAlbDR/react-pizza-shop/assets/128265706/8d9a1468-814a-485e-b8a7-0d7d6bc92c58" height="200px" width="300px"/>
<img src="https://github.com/JoseAlbDR/react-pizza-shop/assets/128265706/0dd2b61d-39db-4d00-9c25-66c9eebfd763" height="200px" width="300px"/>
<img src="https://github.com/JoseAlbDR/react-pizza-shop/assets/128265706/b2ababf4-262b-42fc-86a5-086ace15d539" height="200px" width="300px"/>

## Usage

To use the Pizza Ordering Web Application, follow these steps:

### Frontend

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/react-pizza-shop.git
   ```

2. Change into the project directory:

   ```sh
   cd react-pizza-shop
   ```

3. Install dependencies:

   ```sh
   npm install
   ```

4. Start the development server:

   ```sh
   npm run dev
   ```

5. Open your web browser and navigate to the provided URL to access the app.

### Backend

1. Change into the backend directory:

   ```sh
   cd api
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

4. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

5. Create a [`.env`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fcedricverstraeten%2FProjects%2Fmicrosoft%2Fpizza-shop%2Fapi%2Fpizza_assistant.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A34%7D%7D%5D%2C%22db473f0e-ee0c-4418-baee-ab32216784ae%22%5D "Go to definition") file in the [api](http://_vscodecontentref_/#%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fcedricverstraeten%2FProjects%2Fmicrosoft%2Fpizza-shop%2Fapi%22%2C%22path%22%3A%22%2FUsers%2Fcedricverstraeten%2FProjects%2Fmicrosoft%2Fpizza-shop%2Fapi%22%2C%22scheme%22%3A%22file%22%7D%7D) directory and add your Azure OpenAI credentials:

   ```env
   AZUREOPENAI_API_ENDPOINT=<your-api-endpoint>
   AZUREOPENAI_API_KEY=<your-api-key>
   AZUREOPENAI_API_VERSION=<your-api-version>
   AZUREOPENAI_DEPLOYMENT_NAME=<your-deployment-name>
   ```

6. Start the backend server:

   ```sh
   python main.py
   ```

## How to Order Pizza

### Home Page

When you first access the app, you will be greeted with the home page. If you are a new user, you will be prompted to create an account by providing your name. If you are an existing user, your name will be displayed.

### Menu Page

After creating an account or if you are an existing user, you can proceed to the menu page. Here, you can browse the available pizza options. Each pizza will display its name, description, and price.

### Adding Pizzas to Cart

To add a pizza to the cart, simply click the "Add to Cart" button on the pizza card. The pizza will be added to your cart with a default quantity of 1. If the same pizza is already in the cart, its quantity will be increased.

### Viewing Cart

To view your cart, click the "Cart" button in the navigation bar. The cart page will display the pizzas you have added along with their quantities and total prices. From here, you can proceed to order or remove items from the cart.

### Order Creation

Click the "Order Pizzas" button on the cart page to proceed to order creation. You will be asked to provide your contact information, including your name and phone number. You can also choose whether you want to give your order priority. The total price for your order will be displayed.

### Order Tracking

Once you have created an order, you will be redirected to the order tracking page. Here, you can track the status of your order and view the estimated delivery time.

## Contributing

We welcome contributions to improve the Pizza Ordering Web Application. If you'd like to contribute, please follow the standard GitHub workflow of forking the repository, making changes on a feature branch, and opening a pull request to merge your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
