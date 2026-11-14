class EventTicketBooker:
    def __init__(self, event_name):
        self.name = event_name # here self.name --> is the instance attribute bound/linked/connected to the object via self.
        self.tickets = []

    def add_ticket(self, ticket_type, price):
        self.tickets.append((ticket_type, price))
        return f"Booked: {ticket_type}"
    def total_revenue(self):
        return sum(p for _, p in self.tickets)

    def invoice(self):
        lines = [f'Event Invoice: {self.name}:']
        for name, price in self.tickets:
            lines.append(f" {name}: PKR {price:,}")
        lines.append(f"TOTAL REVENUE: PKR {self.total_revenue():,}")
        return '\n'.join(lines)

# Create the booking object
booking = EventTicketBooker("AI Automation Summit 2026")

# Add tickets
booking.add_ticket("VIP Pass", 15000)
booking.add_ticket("Standard Pass", 5000)
booking.add_ticket("Workshop Add-on", 3500)

# Print the final generated invoice
print(booking.invoice())