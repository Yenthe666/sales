# sales
Apps related to Odoo it's sales features:
- [sale_order_product_price_update](#sale_order_product_price_update): allow updating prices of quotation (lines) to quickly reflect price changes.
- [update_product_prices_by_category](#update_product_prices_by_category): allow updating sales and cost prices for all products in a product category.
- [quotation_template_automatic_description](#quotation_template_automatic_description): automatically update quotation template lines their description if the product description is changed
- [quotation_template_customer](#quotation_template_customer): allow configuring customer(s) on a quotation template and filtering it for specific customers
- [sale_order_transport_cost](#sale_order_transport_cost): allow configuring an extra fee for orders with a total under a specific threshold.

## sale_order_product_price_update
This app adds support to quickly update the sale prices of order lines in bulk through a button/wizard.<br/>
In current times sale prices are going up rapidly and quite often. By using the button "Update product" prices on a quotation (form view) you can quickly<br/>
get an overview of if prices increased, decreased or had no changes:
![image](https://user-images.githubusercontent.com/6352350/173044321-3b237805-2ee9-4441-a6ba-6363ec9f903f.png)

For every order line in the wizard you will see fur fields. Let's go over them:
- "Product": the link to the product for visual information,
- "Old price": the current price per piece on the order line (before applying these changes),
- "New public price": the sale price per piece without any discounts or pricelists applied. This is the public sale price (sale price set on the product),
- "New price customer": the automatically computed new sale price by taking the sale price of the product and applying the pricelist set on the order

- For the product "Office lamp" went from a (public!) sale price of 145.00 to 135.00. If you would keep this line and click on the "Apply" button the line would be changed to 121.50 because the current quotation has a pricelist with a discount rule set.
- For the product "Office Chair" we had a price increase from 65.00 per piece to 90.00 per piece (public price). If you would keep this line and click on the "Apply" button the line would be changed to 81.00 because the current quotation has a pricelist with a discount rule set.
- For the product "Accoustic Bloc Screens" you see no line as there is no price change.

You can simply go through all the lines and choose to remove them, keep them, or even set a manual (new) price per piece.<br/>
When you are done click on "Apply" and all lines on the quotation will be automatically updated.

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

After clicking on "Update prices" all products will be updated and in the chatter of the product(s) a notification will be logged showing the price changes:<br/>
![image](https://user-images.githubusercontent.com/6352350/172600974-16e1eaf2-8d4b-4669-b26c-e7baacfc6468.png)

**Tip:** The wizard will give a visual warning if a recent price update has been done on the current category:
![image](https://user-images.githubusercontent.com/6352350/172582335-f8dafb31-2657-455d-8558-fe97d24ac893.png)
This warning is shown based on comparing the current date with the time the last price update was done for this category.<br/>
If the amount of days is smaller than the `ir.config_param` with the key `update_product_prices_by_category.product_price_update_days_for_warning` this warning is shown.<br/>
This is configurable through Settings > Technical > Parameters > System Parameters

## quotation_template_automatic_description
Adds support to configure which quotation template lines their description should be, or shouldn't be, automatically updated.<br/>
On every quotation template line there is now a checkbox "Auto update description?". If this box is checked on and somebody changes the description on the product we will automatically update the quotation template line it's description. <br/>
If this box is not checked on when somebody changes the description on the related product we will not update the quotation template line.<br/>
This app is especially handy in a database where you have a lot of quotation template (lines) and do not want to manage their descriptions on the lines.
![image](https://user-images.githubusercontent.com/6352350/217465745-1fd19322-d6ba-484c-8840-47b00e188168.png)


## quotation_template_customer
Adds support to configure customer(s) on the quotation templates.<br/>
When the field is left empty the quotation template is shown/available on any quotation.<br/>
When a customer (or customers) are set the quotation template will only be selectable on quotations where the customer on the quotation is within the list of customers set on the quotation template.<br/>
<b>Tip:</b> If the customer set on the quotation template is a company we will also consider contacts under the company.<br/>
This functionality is configurable under Sales > Configuration > Sales Orders > Quotation Templates:
![image](https://user-images.githubusercontent.com/6352350/217323066-019a4326-95ce-423b-af41-ab08dba82f52.png)


## sale_order_transport_cost
Adds support to configure an extra transport cost if an order is under a specific amount.<br/>
The amount is configurable under Sales > Configuration > Settings:
![image](https://user-images.githubusercontent.com/16624719/196438626-dd52bc01-45f7-44f4-a9af-28dffa7f131a.png)


The price added on the order(s) is defined on the product "Transport cost":
![image](https://user-images.githubusercontent.com/16624719/196438634-35aabb95-de90-4eac-9c77-d88c71b32d85.png)

Odoo will automatically add or remove the cost on the sale order the moment is it saved.<br/>
We decided to do this on the save operation to safe computations/delays as we only need it to update automatically once really.
