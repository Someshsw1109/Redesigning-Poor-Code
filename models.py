# models.py  

class UserType:  
    ADMIN = 'admin'  
    MEMBER = 'member'  
    GUEST = 'guest'  

class BookStatus:  
    AVAILABLE = 'available'  
    CHECKED_OUT = 'checked_out'  
    RESERVED = 'reserved'  
    LOST = 'lost'  
    DAMAGED = 'damaged'  

class TransactionType:  
    CHECKOUT = 'checkout'  
    CHECKIN = 'checkin'  
    RESERVE = 'reserve'  
    RENEW = 'renew'  

class TransactionStatus:  
    PENDING = 'pending'  
    COMPLETED = 'completed'  
    CANCELED = 'canceled'  
    OVERDUE = 'overdue'  

class DueDatePolicy:  
    STANDARD = 14  # Standard due date in days  
    SHORT_TERM = 7  # Short-term loan due date in days  
    EXTENDED = 21  # Extended loan due date in days  

class LateFee:  
    STANDARD = 0.50  # Standard late fee per day  
    EXTENDED = 1.00  # Extended late fee per day for longer loans  

class Genre:  
    FICTION = 'Fiction'  
    NON_FICTION = 'Non-Fiction'  
    SCIENCE_FICTION = 'Science Fiction'  
    FANTASY = 'Fantasy'  
    MYSTERY = 'Mystery'  
    BIOGRAPHY = 'Biography'  
    HISTORY = 'History'  
    CHILDREN = 'Children'  

class ReservationStatus:  
    ACTIVE = 'active'  
    COMPLETED = 'completed'  
    CANCELED = 'canceled'  

class NotificationType:  
    EMAIL = 'email'  
    SMS = 'sms'  
    PUSH = 'push'  

class NotificationStatus:  
    SENT = 'sent'  
    PENDING = 'pending'  
    FAILED = 'failed'  

class BorrowingLimit:  
    STANDARD_LIMIT = 5  # Standard number of books a member can borrow  
    GUEST_LIMIT = 2  # Number of books a guest can borrow  
    MAX_RENEWALS = 3  # Maximum number of times a book can be renewed  

# You can add more models or constants as needed for your application.