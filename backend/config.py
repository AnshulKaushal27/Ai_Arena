from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # ── API ────────────────────────────────────────────────────────────
    AICREDITS_API_KEY: str
    AICREDITS_BASE_URL: str = "https://api.aicredits.in/v1"

    # ── Database ───────────────────────────────────────────────────────
    DATABASE_URL: str = "sqlite:///./arena.db"

    # ── Portfolio config ───────────────────────────────────────────────
    DEFAULT_CAPITAL: float = 100_000.0
    TOP_CANDIDATES: int = 15

    # ── Scheduler (IST 24h) ────────────────────────────────────────────
    MORNING_HOUR: int = 8
    MORNING_MINUTE: int = 40
    CLOSING_HOUR: int = 15
    CLOSING_MINUTE: int = 45

    UPSTOX_ANALYTICS_TOKEN:   str = ""
    TWELVE_DATA_API_KEY:  str = ""
    # ── NSE Universe ───────────────────────────────────────────────────
    NIFTY_200_TICKERS: List[str] = [
        # Financials
        "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "AXISBANK.NS", "KOTAKBANK.NS",
        "BAJFINANCE.NS", "BAJAJFINSV.NS", "INDUSINDBK.NS", "HDFCLIFE.NS",
        "SBILIFE.NS", "ICICIPRULI.NS", "CHOLAFIN.NS", "MUTHOOTFIN.NS",
        "RECLTD.NS", "PFC.NS", "BANDHANBNK.NS", "FEDERALBNK.NS",
        "PNB.NS", "BANKBARODA.NS", "CANBK.NS", "IDFCFIRSTB.NS",
        # Technology
        "TCS.NS", "INFOSYS.NS", "WIPRO.NS", "HCLTECH.NS", "TECHM.NS",
        "LTIM.NS", "PERSISTENT.NS", "MPHASIS.NS", "COFORGE.NS",
        # Energy / Oil & Gas
        "RELIANCE.NS", "ONGC.NS", "BPCL.NS", "IOC.NS", "HINDPETRO.NS",
        "ADANIENT.NS", "PETRONET.NS", "GAIL.NS", "OIL.NS",
        # Industrials / Capital Goods
        "BHEL.NS", "HAL.NS", "SIEMENS.NS", "ABB.NS", "POLYCAB.NS",
        "ADANIPORTS.NS", "ADANIGREEN.NS", "HAVELLS.NS", "VOLTAS.NS",
        "CUMMINSIND.NS", "THERMAX.NS", "BHARAT-ELEC.NS", "CGPOWER.NS",
        # Auto
        "MARUTI.NS", "TATAMOTORS.NS", "BAJAJ-AUTO.NS", "HEROMOTOCO.NS",
        "EICHERMOT.NS", "ASHOKLEY.NS", "MOTHERSON.NS", "BALKRISIND.NS",
        # Consumer Staples
        "HINDUNILVR.NS", "ITC.NS", "NESTLEIND.NS", "BRITANNIA.NS",
        "DABUR.NS", "MARICO.NS", "COLPAL.NS", "GODREJCP.NS",
        "TATACONSUM.NS", "VBL.NS", "MCDOWELL-N.NS",
        # Consumer Discretionary
        "TITAN.NS", "DMART.NS", "ASIANPAINT.NS", "BERGEPAINT.NS",
        "PIDILITIND.NS", "WHIRLPOOL.NS", "DIXON.NS", "KALYANKJIL.NS",
        # Healthcare
        "SUNPHARMA.NS", "CIPLA.NS", "DRREDDY.NS", "DIVISLAB.NS",
        "APOLLOHOSP.NS", "GLAND.NS", "TORNTPHARM.NS", "ALKEM.NS",
        "LALPATHLAB.NS", "METROPOLIS.NS", "MAXHEALTH.NS",
        # Basic Materials
        "TATASTEEL.NS", "JSWSTEEL.NS", "HINDALCO.NS", "GRASIM.NS",
        "ULTRACEMCO.NS", "AMBUJACEM.NS", "SHREECEM.NS", "SAIL.NS",
        "NMDC.NS", "JINDALSTEL.NS", "COALINDIA.NS", "DEEPAKNTR.NS",
        "SRF.NS", "PIIND.NS", "AARTIIND.NS", "COROMANDEL.NS", "UPL.NS",
        # Utilities / Power
        "POWERGRID.NS", "NTPC.NS", "NHPC.NS", "TATAPOWER.NS",
        "TORNTPOWER.NS", "CESC.NS",
        # Telecom
        "BHARTIARTL.NS",
        # Real Estate
        "DLF.NS", "PRESTIGE.NS", "OBEROIRLTY.NS", "GODREJPROP.NS",
        # Misc / New Economy
        "NAUKRI.NS", "ZOMATO.NS", "IRCTC.NS", "INDIGO.NS",
        "LICI.NS", "ADANIPOWER.NS",
    ]

    class Config:
        env_file = ".env"


settings = Settings()

# ── Sector map ──────────────────────────────────────────────────────────────
SECTOR_MAP: dict[str, str] = {
    # Financials
    "HDFCBANK.NS": "Financials", "ICICIBANK.NS": "Financials",
    "SBIN.NS": "Financials", "AXISBANK.NS": "Financials",
    "KOTAKBANK.NS": "Financials", "BAJFINANCE.NS": "Financials",
    "BAJAJFINSV.NS": "Financials", "INDUSINDBK.NS": "Financials",
    "HDFCLIFE.NS": "Insurance", "SBILIFE.NS": "Insurance",
    "ICICIPRULI.NS": "Insurance", "CHOLAFIN.NS": "Financials",
    "MUTHOOTFIN.NS": "Financials", "RECLTD.NS": "Financials",
    "PFC.NS": "Financials", "BANDHANBNK.NS": "Financials",
    "FEDERALBNK.NS": "Financials", "PNB.NS": "Financials",
    "BANKBARODA.NS": "Financials", "CANBK.NS": "Financials",
    "IDFCFIRSTB.NS": "Financials",
    # Technology
    "TCS.NS": "Technology", "INFOSYS.NS": "Technology",
    "WIPRO.NS": "Technology", "HCLTECH.NS": "Technology",
    "TECHM.NS": "Technology", "LTIM.NS": "Technology",
    "PERSISTENT.NS": "Technology", "MPHASIS.NS": "Technology",
    "COFORGE.NS": "Technology",
    # Energy
    "RELIANCE.NS": "Energy", "ONGC.NS": "Energy",
    "BPCL.NS": "Energy", "IOC.NS": "Energy",
    "HINDPETRO.NS": "Energy", "ADANIENT.NS": "Energy",
    "PETRONET.NS": "Energy", "GAIL.NS": "Energy", "OIL.NS": "Energy",
    # Industrials
    "BHEL.NS": "Industrials", "HAL.NS": "Industrials",
    "SIEMENS.NS": "Industrials", "ABB.NS": "Industrials",
    "POLYCAB.NS": "Industrials", "ADANIPORTS.NS": "Industrials",
    "ADANIGREEN.NS": "Industrials", "HAVELLS.NS": "Industrials",
    "VOLTAS.NS": "Industrials", "CUMMINSIND.NS": "Industrials",
    "THERMAX.NS": "Industrials", "CGPOWER.NS": "Industrials",
    # Auto
    "MARUTI.NS": "Auto", "TATAMOTORS.NS": "Auto",
    "BAJAJ-AUTO.NS": "Auto", "HEROMOTOCO.NS": "Auto",
    "EICHERMOT.NS": "Auto", "ASHOKLEY.NS": "Auto",
    "MOTHERSON.NS": "Auto", "BALKRISIND.NS": "Auto",
    # Consumer Staples
    "HINDUNILVR.NS": "Consumer Staples", "ITC.NS": "Consumer Staples",
    "NESTLEIND.NS": "Consumer Staples", "BRITANNIA.NS": "Consumer Staples",
    "DABUR.NS": "Consumer Staples", "MARICO.NS": "Consumer Staples",
    "COLPAL.NS": "Consumer Staples", "GODREJCP.NS": "Consumer Staples",
    "TATACONSUM.NS": "Consumer Staples", "VBL.NS": "Consumer Staples",
    "MCDOWELL-N.NS": "Consumer Staples",
    # Consumer Discretionary
    "TITAN.NS": "Consumer Discretionary", "DMART.NS": "Consumer Discretionary",
    "ASIANPAINT.NS": "Consumer Discretionary", "BERGEPAINT.NS": "Consumer Discretionary",
    "PIDILITIND.NS": "Consumer Discretionary", "DIXON.NS": "Consumer Discretionary",
    "KALYANKJIL.NS": "Consumer Discretionary",
    # Healthcare
    "SUNPHARMA.NS": "Healthcare", "CIPLA.NS": "Healthcare",
    "DRREDDY.NS": "Healthcare", "DIVISLAB.NS": "Healthcare",
    "APOLLOHOSP.NS": "Healthcare", "GLAND.NS": "Healthcare",
    "TORNTPHARM.NS": "Healthcare", "ALKEM.NS": "Healthcare",
    "LALPATHLAB.NS": "Healthcare", "METROPOLIS.NS": "Healthcare",
    "MAXHEALTH.NS": "Healthcare",
    # Basic Materials
    "TATASTEEL.NS": "Basic Materials", "JSWSTEEL.NS": "Basic Materials",
    "HINDALCO.NS": "Basic Materials", "GRASIM.NS": "Basic Materials",
    "ULTRACEMCO.NS": "Basic Materials", "AMBUJACEM.NS": "Basic Materials",
    "SHREECEM.NS": "Basic Materials", "SAIL.NS": "Basic Materials",
    "NMDC.NS": "Basic Materials", "JINDALSTEL.NS": "Basic Materials",
    "DEEPAKNTR.NS": "Basic Materials", "SRF.NS": "Basic Materials",
    "PIIND.NS": "Basic Materials", "AARTIIND.NS": "Basic Materials",
    "COROMANDEL.NS": "Basic Materials", "UPL.NS": "Basic Materials",
    # Utilities
    "POWERGRID.NS": "Utilities", "NTPC.NS": "Utilities",
    "NHPC.NS": "Utilities", "TATAPOWER.NS": "Utilities",
    "TORNTPOWER.NS": "Utilities", "CESC.NS": "Utilities",
    "COALINDIA.NS": "Utilities", "ADANIPOWER.NS": "Utilities",
    # Telecom
    "BHARTIARTL.NS": "Telecom",
    # Real Estate
    "DLF.NS": "Real Estate", "PRESTIGE.NS": "Real Estate",
    "OBEROIRLTY.NS": "Real Estate", "GODREJPROP.NS": "Real Estate",
    # Misc
    "NAUKRI.NS": "Technology", "ZOMATO.NS": "Consumer Discretionary",
    "IRCTC.NS": "Industrials", "INDIGO.NS": "Industrials", "LICI.NS": "Insurance",
    "WHIRLPOOL.NS": "Consumer Discretionary",
}