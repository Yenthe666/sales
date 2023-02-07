# sales
Apps related to Odoo it's sales features:
- [quotation_template_customer](#quotation_template_customer): allow configuring customer(s) on a quotation template and filtering it for specific customers
- [sale_order_transport_cost](#sale_order_transport_cost): allow configuring an extra fee for orders with a total under a specific threshold.

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
