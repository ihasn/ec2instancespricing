__author__ = 'ihasn'
from .. import ec2instancespricing

def test_t2med_linux():
    result = {'regions': [{'region': u'us-east-1','instanceTypes': [{'os': u'linux', 'price': 0.052,
             'type': u't2.medium'}]}], 'config': {'currency': 'USD', 'unit': 'perhr'}}

    assert ec2instancespricing.get_ec2_ondemand_instances_prices(filter_region='us-east-1', filter_instance_type='t2.medium',
                                             filter_os_type='linux') == result


def test_c48xlarge_mswin():
    result = {'regions': [{'region': u'us-east-1','instanceTypes': [{'os': u'mswin', 'price': 3.184,
             'type': u'c4.8xlarge'}]}], 'config': {'currency': 'USD', 'unit': 'perhr'}}

    assert ec2instancespricing.get_ec2_ondemand_instances_prices(filter_region='us-east-1', filter_instance_type='c4.8xlarge',
                                             filter_os_type='mswin') == result

def test_instance_types():
    result = ['t1.micro', 'm1.small', 'm1.medium', 'm1.large', 'm1.xlarge', 'm2.xlarge', 'm2.2xlarge', 'm2.4xlarge',
              't2.micro', 't2.small', 't2.medium', 'm3.medium', 'm3.large', 'm3.xlarge', 'm3.2xlarge', 'c1.medium',
              'c1.xlarge', 'c3.large', 'c3.xlarge', 'c3.2xlarge', 'c3.4xlarge', 'c3.8xlarge', 'cc2.8xlarge',
              'cg1.4xlarge', 'cr1.8xlarge', 'hi1.4xlarge', 'hs1.8xlarge', 'g2.2xlarge', 'r3.large', 'r3.xlarge',
              'r3.2xlarge', 'r3.4xlarge', 'r3.8xlarge', 'i2.xlarge', 'i2.2xlarge', 'i2.4xlarge', 'i2.8xlarge',
              'd2.xlarge', 'd2.2xlarge', 'd2.4xlarge', 'd2.8xlarge', 'c4.large', 'c4.xlarge', 'c4.2xlarge',
              'c4.4xlarge', 'c4.8xlarge']
    assert ec2instancespricing.EC2_INSTANCE_TYPES == result