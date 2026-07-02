USE customer_churn;

CREATE TABLE customer_data (

    gender VARCHAR(10),

    SeniorCitizen TINYINT,

    Partner VARCHAR(5),

    Dependents VARCHAR(5),

    tenure INT,

    PhoneService VARCHAR(5),

    MultipleLines VARCHAR(20),

    InternetService VARCHAR(20),

    OnlineSecurity VARCHAR(20),

    OnlineBackup VARCHAR(20),

    DeviceProtection VARCHAR(20),

    TechSupport VARCHAR(20),

    StreamingTV VARCHAR(20),

    StreamingMovies VARCHAR(20),

    Contract VARCHAR(20),

    PaperlessBilling VARCHAR(5),

    PaymentMethod VARCHAR(40),

    MonthlyCharges DECIMAL(8,2),

    TotalCharges DECIMAL(10,2),

    Churn VARCHAR(5)

);