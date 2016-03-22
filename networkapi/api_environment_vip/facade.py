# -*- coding:utf-8 -*-
import logging

from networkapi.api_environment_vip.models import OptionVipCombinate, OptionVipCombinateItem, \
    OptionVipCombinateItemPermitted
from networkapi.requisicaovips.models import OptionVip, OptionVipEnvironmentVip

log = logging.getLogger(__name__)


def get_option_vip_by_environment_vip_ids(environment_vip_ids):
    """
    Return option vip list by ids of environment vip
    param environment_vip_ids: ids list of environment vip
    example: [<environment_vip_id>,...]
    """
    options_vip = list()
    for environment_vip_id in environment_vip_ids:
        option_environment_vips = OptionVipEnvironmentVip.objects.filter(environment=environment_vip_id)

        options_vip.append(option_environment_vips)
    return options_vip


def get_option_vip_by_environment_vip_type(search_list):
    """
    Return option vip list by ids of environment vip and option vip type
    param environment_vip_ids: ids list of environment vip
    param type_option: option vip type
    example: [{
        environment_vip_id:<environment_vip_id>
        type_option:<type_option>
    ]}
    """
    options_vip = list()
    for item in search_list:

        option_environment_vips = OptionVip.objects.filter(
            optionvipenvironmentvip__environment__id=int(item['environment_vip_id']),
            tipo_opcao=item['type_option'])

        options_vip.append(option_environment_vips)
    return options_vip

