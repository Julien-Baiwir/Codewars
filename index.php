<?php
SELECT *
FROM orders

WHERE total_amount > (SELECT AVG(total_amount) FROM orders WHERE customer_id = orders.customer_id);
?>
