import pandas as pd
import getpass
import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.dialects import registry

registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

ACCOUNT = 'volvocars-manufacturinganalytics'
SAML_USERNAME = f'{getpass.getuser()}@volvocars.com'  # or SAML_USERNAME = 'cds-id@volvocars.com'

query = """
    SELECT * FROM VCG.INFORMATION_SCHEMA.TABLES
    """

engine = create_engine(
    'snowflake://' + ACCOUNT ,
    connect_args={
        'user': SAML_USERNAME,
        'authenticator': 'externalbrowser',
    }
)

# Test the connection by querying available tables and schemas
connection = engine.connect()
try:
    df_in_smart = pd.read_sql_query(query, connection)
finally:
    connection.close()
    engine.dispose()



st.write(df_in_smart)