# Pyadina Python based Order Management

Need to run this one before doing some analysis:
``` sql
delete from orders where date = '16.08.2023';
update orders set date = '18.08.2023' where date = '17.08.2023';
update orders set timestamp=TIME(timestamp, '+480 minutes') where date='18.08.2023';
```