select count(*) from customers_dialogs
where customers_dialogs.traffic_source_name = 'vk_easycode' and customers_dialogs.not_answered = 'yes'
