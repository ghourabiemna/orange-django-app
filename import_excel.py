import os
import django
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orange.settings')
django.setup()
from interface_resource.models import Interface

# Load Excel file
df = pd.read_excel(r'C:\Users\Emna\Downloads\Interface_Resource_05-20-2025_11-27-16.xlsx')
# Clean and import rows
for _, row in df.iterrows():
    rate_cleaned = int(str(row['Rate (bit/s)']).replace(',', '').strip() or 0)
    Interface.objects.create(
        interface_name=row['Interface Name'],
        description=row['Description'],
        ne_name=row['NE Name'],
        ipv4_address=row['IPv4 Address'] if row['IPv4 Address'] != '-' else None,
        subnet_mask=row['IPv4 Address SubnetMask'] if row['IPv4 Address SubnetMask'] != '-' else None,
        mac_address=row['MAC Address'],
        rate=rate_cleaned,
        admin_status=row['Administrative Status'],
        ipv4_status=row['IPv4 Operating Status']
    )
