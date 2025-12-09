SQL_CHECKS = {
    "missing_values": """
        SELECT * FROM orders
        WHERE customer_id IS NULL OR order_date IS NULL;
    """,

    "duplicate_orders": """
        SELECT order_id, COUNT(*)
        FROM orders
        GROUP BY order_id
        HAVING COUNT(*) > 1;
    """,

    "timestamp_mismatch": """
        SELECT *
        FROM orders
        WHERE order_date > delivery_date;
    """,

    "invalid_relationships": """
        SELECT o.*
        FROM orders o
        LEFT JOIN customers c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """
}
