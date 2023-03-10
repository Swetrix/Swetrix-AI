from typing import List

import pandas as pd
from pydantic import BaseModel


class ChartBase(BaseModel):
    """
    This class is used both for the request and the response.
    Request: data to predict the next period.
    Response: forecasted data to display the chart with prediction.
    """
    x: List[str]
    sdur: List[int]
    uniques: List[int]
    visits: List[int]

    def to_pandas(self):
        return pd.DataFrame({
            'x': self.x,
            'visits': self.visits,
            'uniques': self.uniques,
            'sdur': self.sdur,
        })

    def keys(self):
        return ['visits', 'uniques', 'sdur']


class ChartData(ChartBase):
    period_to_forecast: int
    frequency: str  # 'd' for days, 'w' for hours, 'M' for months, 'Y' for years


class ChartDataResponse(ChartBase):
    pass
