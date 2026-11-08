from enum import Enum

class TransferType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"