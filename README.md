# sales
Apps related to Odoo it's sales features:
- [update_product_prices_by_category](#update_product_prices_by_category): allow updating sales and cost prices for all products in a product category.


## update_product_prices_by_category
Adds support to update the sales and cost prices of products in bulk through the product categories.<br/>
This can be done through a wizard from Purchase > Configuration > Products > Product Categories through the "Update product prices" button:
![image](https://user-images.githubusercontent.com/6352350/172580961-5478e5a6-b723-4221-80be-83198967d7b7.png)

Once this button has been clicked a wizard opens up with a set of options:
![image](https://user-images.githubusercontent.com/6352350/172582123-e57f9af9-0d85-4dab-8144-47e186da2080.png)

Let's go over them one by one:
- "Increase price by": configurable selection to define if you'd like to do a percentage price increase or a fixed price increase.
- "Purchase price": the percentage with which you want to increase the purchase price if the option "Increase price by" is set to percentage, otherwise the amount.<br/> Leave empty if you do not want to do an increase on the purchase price.
- "Sale price": the percentage with which you want to increase the sale price if the option "Increase price by" is set to percentage, otherwise the amount.<br/>Leave empty if you do not want to do an increase on the sale price.
- "Product Category": the category for which you want to update prices. It is by default set to the current category from which you opened the wizard.
- "Update underlying categories": If this option is checked on and the current product category has underlying categories all the products beloning to the subcategories will also get price updates. Use it with caution ;-)


**Tip:** The wizard will give a visual warning if a recent price update has been done on the current category:
![image](https://user-images.githubusercontent.com/6352350/172582335-f8dafb31-2657-455d-8558-fe97d24ac893.png)
This warning is shown based on comparing the current date with the time the last price update was done for this category.<br/>
If the amount of days is smaller than the `ir.config_param` with the key `update_product_prices_by_category.product_price_update_days_for_warning` this warning is shown.<br/>
This is configurable through Settings > Technical > Parameters > System Parameters
