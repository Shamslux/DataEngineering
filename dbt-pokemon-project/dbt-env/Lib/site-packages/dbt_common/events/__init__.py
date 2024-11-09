from dbt_common.events.base_types import EventLevel
from dbt_common.events.event_manager_client import get_event_manager
from dbt_common.events.functions import get_stdout_config
from dbt_common.events.logger import LineFormat

# make sure event manager starts with a logger
get_event_manager().add_logger(
    get_stdout_config(LineFormat.PlainText, True, EventLevel.INFO, False)
)
