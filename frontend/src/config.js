export var API_HOST = 'http://localhost:8000';
export var SERVICES_REFRESH_INTERVAL = 30;

export var STATUS_DESCRIPTION = {
  ok: 'Operational',
  minor: 'Degraded Performance',
  major: 'Partial Outage',
  critical: 'Major Outage',
  maintenance: 'Maintenance',
  unavailable: 'Status Unavailable',
};

export var STATUS_COLOR = {
  ok: 'green',
  minor: 'yellow',
  major: 'orange',
  critical: 'red',
  maintenance: 'blue',
  unavailable: 'gray',
};

export var STATUS_ICON = {
  ok: 'fa-check',
  minor: 'fa-minus-square',
  major: 'fa-exclamation-triangle',
  critical: 'fa-times',
  maintenance: 'fa-wrench',
  unavailable: 'fa-question',
};
