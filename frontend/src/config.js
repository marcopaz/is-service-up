var API_HOST = 'http://localhost:8000';
var SERVICES_REFRESH_INTERVAL = 3;

var STATUS_DESCRIPTION = {
  ok: 'Operational',
  minor: 'Degraded Performance',
  major: 'Partial Outage',
  critical: 'Major Outage',
  maintenance: 'Maintenance',
  unavailable: 'Status Unavailable',
};

var STATUS_COLOR = {
  ok: 'green',
  minor: 'yellow',
  major: 'orange',
  critical: 'red',
  maintenance: 'blue',
  unavailable: 'gray',
};

var STATUS_ICON = {
  ok: 'fa-check',
  minor: 'fa-minus-square',
  major: 'fa-exclamation-triangle',
  critical: 'fa-times',
  maintenance: 'fa-wrench',
  unavailable: 'fa-question',
};

export {
  API_HOST,
  SERVICES_REFRESH_INTERVAL,
  STATUS_DESCRIPTION,
  STATUS_COLOR,
  STATUS_ICON,
};
