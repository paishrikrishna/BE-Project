"""BE_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from homepage.views import home_index_page,qr_code
from calander.views import cal_index_page
from camera.views import cam_index_page
from requested_events.views import req_events_index_page
from login_page.views import login_index_page
from new_users.views import new_user_index_page
from notice_board.views import notice_index_page
from messaging_module.views import message_index_page
from sensors.views import sensors_index_page,read_water_tank_status,switch_status,water_level,device_initial_setup,read_light_switch_status,light_switch_status,lights_operation,all_lights_operation,read_floor_light_status,floor_and_light_status,date_and_time,lights_statu_s,turn_hrd,export_data
from entry_exit_timestamp.views import timestamp_index_page,export_timestamps,qr_code_scanner
from temp_rmv_access.views import temp_rmv_access
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_index_page),
    path('<str:user>/<str:auth>/homepage',home_index_page),
    path('<str:user>/<str:auth>/calander',cal_index_page),
    path('<str:user>/<str:auth>/camera',cam_index_page),
    path('<str:user>/<str:auth>/requested_events',req_events_index_page),
    path('<str:user>/<str:auth>/notice_board',notice_index_page),
    path('<str:user>/<str:auth>/message',message_index_page),
    path('<str:user>/<str:auth>/sensors',sensors_index_page),
    path('<str:user>/<str:auth>/timestamp_index_page',timestamp_index_page),
    path('new_user',new_user_index_page),
    path('read_water_tank_status/',read_water_tank_status),
    path('switch_status/',switch_status),
    path('water_level/',water_level),
    path('device_initial_setup/',device_initial_setup),
    path('read_light_switch_status/',read_light_switch_status),
    path('light_switch_status/',light_switch_status),
    path('lights_operation/',lights_operation),
    path('all_lights_operation/',all_lights_operation),
    path('read_floor_light_status/',read_floor_light_status),
    path('floor_and_light_status/',floor_and_light_status),
    path('date_and_time/',date_and_time),
    path('lights_statu_s/',lights_statu_s),
    path('turn_hrd/',turn_hrd),
    path('export_data/',export_data),
    path('<str:user>/qr_code/',qr_code),
    path('export_timestamps/',export_timestamps),
    path('<str:user>/<str:auth>/temp_rmv_access',temp_rmv_access),
    path('qr_code_scanner/',qr_code_scanner)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
