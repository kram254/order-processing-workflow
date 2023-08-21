import requests
from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add more fields as needed
    
    @classmethod
    def get_new_orders(cls):
        return cls.query.filter_by(processed=False).all()
    
    def generate_shipping_label(self):
        # Use the carrier's API to generate shipping label and get tracking code
        api_url = 'https://api.shippingcarrier.com/ship'
        payload = {
            'order_id': self.id,
            'address': self.address,
            # Add more necessary data
            'api_key': 'your-api-key'
        }
        
        response = requests.post(api_url, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            self.tracking_code = data['tracking_code']
            self.processed = True
            db.session.commit()
            return True
        else:
            return False
        
def send_order_status_email(self):
        msg = Message('Your Order Status', sender='your@email.com', recipients=[self.email])
        msg.body = f'Your order with tracking code {self.tracking_code} has been processed and shipped.'
        mail.send(msg)        

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    # Add more fields as needed
