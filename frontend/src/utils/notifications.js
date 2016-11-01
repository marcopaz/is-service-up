function isNotificationSupported() {
  return ("Notification" in window);
}

export function requestNotificationPermission() {
  if (!isNotificationSupported()) {
    return;
  }
  Notification.requestPermission();
}

export function spawnNotification(title, options) {
  if (!isNotificationSupported()) {
    return;
  }
  return new Notification(title, options);
}

