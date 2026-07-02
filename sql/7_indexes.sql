CREATE INDEX idx_churn
ON customer_data(Churn);

CREATE INDEX idx_contract
ON customer_data(Contract);

CREATE INDEX idx_payment
ON customer_data(PaymentMethod);

CREATE INDEX idx_internet
ON customer_data(InternetService);

-- explain
-- select * from customer_data;

EXPLAIN
SELECT *
FROM customer_data
WHERE Contract='Month-to-month';