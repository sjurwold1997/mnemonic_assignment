from django.test import TestCase, Client
from .models import Account, Transaction
from .views import transfer_money, see_all_transfers

class TransactionTestCase(TestCase):
    def setUp(self):
        self.acc_1 = Account.objects.create(name="TestAccount1", available_cash=1000)
        self.acc_2 = Account.objects.create(name="TestAccount2", available_cash=100)
        self.c = Client()
    
    def test_valid_transaction(self):
        """
        Runs a valid transaction between the two test accounts and checks if
        the behavior is as expected, i.e. that the amount is withdrawn from the
        source and transferred to the destination. Also checks the status of the 
        Transaction object created.
        """
        amount = 700
        before_amount_source, before_amount_destination = self.acc_1.available_cash, self.acc_2.available_cash
        self.c.post('/transfer/', {'source-id': self.acc_1.id, 'destination-id': self.acc_2.id, 'amount': amount}, follow=True)
        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(before_amount_source-amount, self.acc_1.available_cash)
        self.assertEqual(before_amount_destination+amount, self.acc_2.available_cash)
        self.assertTrue(Transaction.objects.first().success)
    
    def test_invalid_transaction(self):
        """
        Executes a invalid transaction and checks that no money is transferred between the 
        two test accounts. Also checks if the generated Transaction object is unsuccessful.
        """
        amount = 200
        before_amount_source, before_amount_destination = self.acc_2.available_cash, self.acc_1.available_cash
        self.c.post('/transfer/', {'source-id': self.acc_2.id, 'destination-id': self.acc_1.id, 'amount': amount}, follow=True)
        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(before_amount_source, self.acc_2.available_cash)
        self.assertEqual(before_amount_destination, self.acc_1.available_cash)
        self.assertFalse(Transaction.objects.first().success)
    
    


