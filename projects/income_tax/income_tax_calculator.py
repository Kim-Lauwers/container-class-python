class :
    @staticmethod
    def calculate_tax(income: int) -> float:
        __tax_payable: int = 0
        if income <= 10000:
            __tax_payable = 0
        elif income <= 20000:
            # no tax on first 10,000
            x = income - 10000
            # 10% tax
            __tax_payable = x * 10 / 100
        else:
            # first 10,000
            __tax_payable = 0

            # next 10,000 10% tax
            __tax_payable = 10000 * 10 / 100

            # remaining 20%tax
            __tax_payable += (income - 20000) * 20 / 100

        return __tax_payable
