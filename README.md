 #ClothingStore Using Django

ClothingStore Django is a  web application built with the Django framework. This application provides an online platform for browsing, and managing a variety of teas, complete with user authentication, and a product catalog.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Product Catalog:** Browse a wide range of teas with detailed descriptions, images, and prices.
- **Admin Panel:** Comprehensive backend for managing inventory, orders, and user data.

## Installation

Follow these steps to set up on your local machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/02PaulSneha/ClothingStore_Django.git
   cd moreofdjango

2. Create a Virtual Environment

python3 -m venv env
Activate the virtual environment:

On macOS/Linux:

source env/bin/activate

On Windows:

env\Scripts\activate


3) Install Dependencies

pip install -r requirements.txt

4) Apply Database Migrations

python manage.py migrate
python manage.py makemigrations


5) Create a Superuser

python manage.py createsuperuser

Follow the prompts to set up an admin account.

6) Run the Development Server

python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

##Usage

Home Page: Explore featured clothes and categories.

Product Details: Click on a tea product to view detailed information, reviews, and pricing.


## Contributing
Contributions are welcome! If you would like to contribute to ClothingStore Django, please follow these steps:

## Fork the Repository

First, Create a New Branch :

git checkout -b feature/YourFeature
Commit Your Changes
git commit -m "Add new feature: [Your Feature]"

Now, Push to Your Branch :


git push origin feature/YourFeature

## Open a Pull Request

Please ensure your contributions adhere to the project's coding standards and include tests where appropriate.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or suggestions, feel free to reach out:


## Screenshots :

# Welcome Page :
![image](https://github.com/user-attachments/assets/b42e02a5-d17f-4bba-a988-d95df7d341f0)

# Home Page Listing product catalog :
![image](https://github.com/user-attachments/assets/334fc122-94b0-4b7d-94bb-5bae2db88cba)

# Description for each tea showing its' details, implemented using CSS cards :
![image](https://github.com/user-attachments/assets/77bb8e99-90c9-4559-b317-2f1a0ac10792)

# Store Locator, implemented using django forms.
![image](https://github.com/user-attachments/assets/5ad48fb5-6fde-4df2-8ef0-9151a91d5a8d)









