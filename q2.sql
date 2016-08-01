SELECT Salesperson.Name 
FROM Salesperson, Orders
WHERE
Salesperson.ID = Orders.salesperson_id
GROUP BY Orders.salesperson_id
HAVING COUNT(Orders.salesperson_id) > 1
;