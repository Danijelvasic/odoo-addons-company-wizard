## Odoo Company Creation Wizard: Modular Extensions

#### Description

This repository contains a collection of Odoo modules that extend the core functionality of the company creation process by providing a dynamic wizard interface. The base module offers an intuitive wizard that simplifies the process of creating new companies within the Odoo ecosystem. Additional glue modules ensure seamless integration and handling of extra settings required when other modules, such as Account or Product, are installed. These enhancements streamline the configuration process, making it more efficient for end users and system administrators.

### Features and Modules

1. Base Company Creation Wizard

* Module: `company_wizard_base`

* Version: 12.0.1.1.3

* Description: Provides the foundational wizard interface for creating a new company in Odoo. This module introduces a new menu item and streamlines the company creation process by offering a guided step-by-step interface.

* Technology: Developed using Odoo’s form views and server-side business logic (Python), the module leverages Odoo’s ORM framework to handle company data creation and validation. The wizard UI is built using Odoo’s form view and action handling system.

2. Account Integration for Company Wizard

* Module: `company_wizard_account`

* Version: 12.0.1.1.1

* Description: A glue module that extends the base company creation wizard by integrating the Account module. When the Account module is installed, this extension ensures that any required accounting configurations are properly set up during the company creation process.

* Technology: Uses Odoo’s module dependency and inheritance mechanisms to ensure compatibility with the Account module. It automates the setup of financial settings such as fiscal years, chart of accounts, and tax configurations.

3. Product Integration for Company Wizard

* Module: `company_wizard_product`

* Version: 12.0.1.1.1

* Description: A glue module that enables the creation of new companies when the Product module is installed. This module ensures that the necessary product-related settings, such as default product categories, units of measure, and product templates, are pre-configured during the company creation process.

* Technology: Built on Odoo’s ORM and extension mechanisms, it allows seamless integration with the Product module. The module uses the product.template model to ensure correct setup of product-related entities when a new company is created.

4. Account Wizard Test Module

* Module: `company_wizard_account_test`

* Version: 12.0.1.1.1

* Description: A dedicated testing module for the company_wizard_account module. This module is designed to validate the correct behavior of the account integration during the company creation process. It ensures that all accounting features are set up properly when a new company is created.

* Technology: Uses Odoo’s testing framework and unittest module to automate the verification of accounting configurations. The module includes test cases for creating companies with accounting setups and validates that the correct configurations are applied.

### Installation

To install the modules, follow the standard Odoo module installation process:

1. Clone or download this repository into your Odoo addons directory.

2. Update the module list by navigating to Apps > Update Apps List in Odoo.

3. Search for the modules in the Apps menu and install the necessary modules based on your configuration needs.

### Usage

Once installed, the wizard will appear under a new menu item for creating companies. Depending on the installed modules (Account, Product), the corresponding glue modules will handle the additional settings during the company creation process.

#### Technical Information

* Framework: Odoo ERP
* Version Compatibility: Odoo 12.0
* Languages Used: Python, XML
* License: GNU AGPL-3

#### Contribution

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. Be sure to follow the coding standards and include test cases where applicable.
