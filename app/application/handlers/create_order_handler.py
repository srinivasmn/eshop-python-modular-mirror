class CreateOrderHandler:
    def handle(self, command):
        # Stubbed business logic
        return {
            "order_id": 1,
            "status": "Created",
            "customer_id": command.customer_id
        }
