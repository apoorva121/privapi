from privapi.fakers import (
    _full_name_, _date_, _id_, _key_, _company_business_id_, _company_, _bank_account_, _first_name_, _last_name_,
    _address_, _bban_, _city_, _country_, _country_code_, _ssn_, _email_, _phone_number_, _gender_,
    _building_number_, _iban_, _postal_code_, _state_, _street_, _province_, _amount_, _credit_score_,
    _credit_card_number_, _alphanumeric_, _location_, _latitude_, _longitude_, _timestamp_, _latitude_str_,
    _longitude_str_, _timestamp_str_, _amount_str_, _credit_score_str_)

name_type_to_gen = {'string':
                        {'[uU]ser': _full_name_,
                         '[fF]ullName': _full_name_,
                         'firstname': _first_name_,
                         'lastname': _last_name_,
                         '[aA]ddress': _address_,
                         '[nN]ationality': _country_,
                         '[dD]ate': _date_,
                         '[tT]axId': _company_business_id_,
                         '[sS]erial': _id_,
                         '[oO]rganization': _company_,
                         '[cC]ompany': _company_,
                         '[dD]ba': _company_,
                         '[dD]oingBusinessAs': _company_,
                         '[bB]usinessName': _company_,
                         '[aA]ccount': _bank_account_,
                         '[uU]UID': _id_,
                         '[sS]hareholder': _full_name_,
                         '[pP]ostalCode': _postal_code_,
                         '[zZ]ip': _postal_code_,
                         '[bB]ic': _bban_,
                         '[bB]ankCity': _city_,
                         '[bB]usinessContact': _full_name_,
                         '[cC]ity': _city_,
                         '[cC]ountryCode': _country_code_,
                         '[cC]country': _country_,
                         '[dD]ateOfBirth': _date_,
                         '[dD]ob': _date_,
                         '[dD]ocumentNumber': _ssn_,
                         '[pP]assport': _ssn_,
                         '[iI]dentityDocument': _ssn_,
                         '[iI]dNumber': _ssn_,
                         '[iI]dCard': _ssn_,
                         '[dD]rivingLicense': _ssn_,
                         '[cC]reditCard': _credit_card_number_,
                         '[eE]mail': _email_,
                         '[pP]hone': _phone_number_,
                         '[pP]honeCountryCode': _country_code_,
                         '[gG]ender': _gender_,
                         '[hH]ouse': _building_number_,
                         '[bB]uilding': _building_number_,
                         '[aA]partment': _building_number_,
                         '[aA]pt': _building_number_,
                         '[iI]ban': _iban_,
                         '[sS]tate': _state_,
                         '[pP]rovince': _province_,
                         '[sS]treet': _street_,
                         '[rR]ecordLocator': _alphanumeric_,
                         '[rR]eservationCode': _alphanumeric_,
                         '[lL]ocation': _location_,
                         '[lL]atitude': _latitude_str_,
                         '[lL]ongitude': _longitude_str_,
                         '[lL]at': _latitude_str_,
                         '[lL]on': _longitude_str_,
                         "[tT]imestamp": _timestamp_str_,
                         "[sS]ignature_sha1": _id_,

                         },
                    'number':
                        {
                            "[tT]imestamp": _timestamp_str_,
                            "[dD]ate": _timestamp_str_,
                            "[bB]alance": _amount_str_,
                            "[aA]mount": _amount_str_,
                            "[cC]redit": _amount_str_,
                            "[cC]reditScore": _credit_score_str_,
                            "[sS]core": _credit_score_str_,
                            "[lL]atitude": _latitude_str_,
                            "[lL]ongitude": _longitude_str_
                        }
                    }

exclusions = [".*amazonaws.com"]