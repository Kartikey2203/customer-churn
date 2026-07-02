-- 1 
SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1  END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1  end) * 100.0
        / COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY Contract
ORDER BY Churn_Rate DESC;
-- 2 
SELECT
    InternetService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        *100.0
        /COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY InternetService
ORDER BY Churn_Rate DESC;

-- 3 
SELECT
    InternetService,
    Contract AS Tenure,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        *100.0
        /COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY InternetService,Contract
ORDER BY Churn_Rate DESC;

-- 4
SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        *100.0
        /COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;


-- 5
SELECT
    SeniorCitizen,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        *100.0
        /COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY SeniorCitizen;


-- 6
SELECT
    TechSupport,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)
        *100.0
        /COUNT(*),
        2
    ) AS Churn_Rate
FROM customer_data
GROUP BY TechSupport
ORDER BY Churn_Rate DESC;

-- 7
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges),2) AS Avg_Monthly_Charges
FROM customer_data
GROUP BY Churn;


-- 8
SELECT
    Churn,
    ROUND(AVG(tenure),2) AS Avg_Tenure
FROM customer_data
GROUP BY Churn;

