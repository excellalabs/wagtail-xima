/**
 * Created by Nick on 9/22/2015.
 */

function graph(data) {
    AmCharts.makeChart("chartdiv",
        {
            "type": "serial",
            "categoryField": "date",
            "dataDateFormat": "YYYY-MM",
            "theme": "light",
            "categoryAxis": {
                "minPeriod": "MM",
                "parseDates": true
            },
            "chartCursor": {
                "categoryBalloonDateFormat": "MMM YYYY"
            },
            "chartScrollbar": {},
            "trendLines": [],
            "graphs": [
                {
                    "fillAlphas": 0.7,
                    "fillColors": "#3865B7",
                    "id": "AmGraph-1",
                    "lineAlpha": 0,
                    "title": "Quantity Stocked",
                    "valueField": "Stocked"
                },
                {
                    "fillAlphas": 0.7,
                    "fillColors": "#6DCB4C",
                    "id": "AmGraph-2",
                    "lineAlpha": 0,
                    "title": "Quantity Sold",
                    "valueField": "Sold"
                }
            ],
            "guides": [],
            "valueAxes": [
                {
                    "id": "ValueAxis-1",
                    "title": "Units"
                }
            ],
            "allLabels": [],
            "balloon": {},
            "legend": {},
            "titles": [
                {
                    "id": "Title-1",
                    "size": 15,
                    "text": "Monthly Product Metrics"
                }
            ],
            "dataProvider": data
        }
    );
};
