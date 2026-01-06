from lumibot.strategies import Strategy

class Strategy(Strategy):
    """
    QF5208 Portfolio Management – Strategy Assignment

    Your task:
      - Design and implement your own trading / portfolio strategy.
      - You will mainly work in `initialize` and `on_trading_iteration`.
      - You may use the strategy methods documented here:
        https://lumibot.lumiwealth.com/strategy_methods.html
    """

    def initialize(self):
        """
        Called once before the strategy starts trading.

        You should:
          - Choose how often your strategy runs by setting `self.sleeptime` (e.g. "1D" for once per day, "60M" for once per hour).
          - Initialize any state variables you need (e.g. target tickers, lookback windows).

        Useful attributes & methods:
          - self.sleeptime              (string like "1D", "60M")
          - self.cash, self.portfolio_value
          - self.get_parameters(), self.set_parameters()
        See: Strategy lifecycle docs & properties in LumiBot.
        """

        # TODO: Implement your own logic here
        #self.sleeptime = "1D"  # run once per trading day
        #self.target_assets = ["SPY", "QQQ"] # List of assets to consider in your portfolio (edit these)
        #self.max_weight_per_asset = 0.6   # e.g. no asset should be more than 60% of portfolio
        #self.min_cash_buffer = 0.05       # keep at least 5% in cash
        # etc...
        
        self.log_message("Initialized Strategy")

    def on_trading_iteration(self):
        """
        Main trading loop. This method is called every `self.sleeptime` during market hours.
        You can find relevant strategy methods in the docs: https://lumibot.lumiwealth.com/strategy_methods.html.
        Or check the example strategies in the strategies folder.
        """

        # TODO: Implement your own logic here

        self.log_message(
            f"[Strategy] "
            f"Portfolio=${self.get_portfolio_value():,.2f}, Cash=${self.get_cash():,.2f}, "
            f"Positions={self.get_positions()}"
        )



