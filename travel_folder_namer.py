# travel_folder_namer.py

"""
This script generates structured folder names for travel bookings,
following the SOC format used by Siam On Cloud.

Format:
SOC-YYMMDD-MMDD-YYYY-ROUTING-HK00-[Free text]
"""

from datetime import datetime

def format_date(date_str):
    """Convert DDMMMYYYY to YYMMDD or MMDD"""
    date_obj = datetime.strptime(date_str, "%d%b%Y")
    return date_obj.strftime("%y%m%d"), date_obj.strftime("%m%d")

def generate_folder_name(depart_date, return_date, outbound_airline, return_airline, routing, pax_count, note):
    dep_YYMMDD, _ = format_date(depart_date)
    _, ret_MMDD = format_date(return_date)
    airline_code = outbound_airline + return_airline if return_airline else outbound_airline + "XX"
    routing_code = routing.replace("-", "").upper()
    pax_code = f"HK{int(pax_count):02d}"
    note_sanitized = note.replace(" ", "-").replace("--", "-")

    folder_name = f"SOC-{dep_YYMMDD}-{ret_MMDD}-{airline_code}-{routing_code}-{pax_code}-{note_sanitized}"
    return folder_name

# Example usage
if __name__ == "__main__":
    print(generate_folder_name(
        "23JUN2025", "05JUL2025", "EK", "EK", "BKK-DXB-CDG-DXB-BKK", 4, "Paris-trip-family"
    ))
