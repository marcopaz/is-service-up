var REFRESH_INTERVAL = 30;

function updateServiceStatus(elm, service) {
    elm.data('status', service.status);

    // replace status icon
    var icon= elm.find('.icon-indicator');
    icon.removeClass(function(i, css) {
        return (css.match(/fa-.*/g) || []).join(' ');
    });
    icon.addClass(service.status_icon);

    // replace status color
    var cont = elm.find('.service-inner-container');
    cont.removeClass(function(i, css) {
        return (css.match(/status-.*/g) || []).join(' ');
    });
    cont.addClass('status-' + service.status_color);

    // replace status text
    elm.find('.service-status a').html(service.status_human);
}

function loadServicesData() {
    $.get('/status', function(json) {
        var services = json.data.services;
        var last_update = json.data.last_update;
        var elements = {};
        $('.service-container').each(function(i, elm){
            var name = $(elm).find('.service-name').text();
            elements[name] = $(elm);
        });
        $.each(services, function(i, service) {
            var elm = elements[service.name];
            if (!elm) {
                return;
            }
            var old_status = elm.data('status');
            if (service.status != old_status) {
                updateServiceStatus(elm, service);
            }
        });
        $('.last-update-seconds').html(last_update);
    });
}

function increaseLastUpdateTime() {
    var value = $('.last-update-seconds').html();
    $('.last-update-seconds').html(parseInt(value) + 1);
}

$(function(){
    setInterval(loadServicesData, REFRESH_INTERVAL * 1000);
    setInterval(increaseLastUpdateTime, 1000);
});
