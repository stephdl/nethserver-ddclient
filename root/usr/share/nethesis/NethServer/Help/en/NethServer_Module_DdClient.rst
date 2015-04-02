===========
Dynamic DNS
===========

Dynamic DNS (DDNS or DynDNS) is a method of automatically updating a name server
in the Domain Name System (DNS), often in real time, with the active DNS configuration
of its configured hostnames, addresses or other information.

End users of Internet access receive an allocation of IP addresses, often only a single address, by their Internet service provider.
The assigned addresses may either be fixed (or static), or may change from time to time, a situation called dynamic.
Dynamic addresses are generally given only to residential customers and small businesses, as most enterprises specifically require static addresses.

Dynamic IP addresses present a problem if the customer wants to provide a service to other users on the Internet, such as a web service.
As the IP address may change frequently, corresponding domain names must be quickly re-mapped in the DNS, to maintain accessibility using a well-known URL.

Many providers offer commercial or free Dynamic DNS service for this scenario. The automatic reconfiguration is implemented here by the software 'ddclient'.


DDNS
====

Create / Modify
---------------

Click Create to add a new Dynamic DNS Hostname


Dynamic DNS Hostname
    The dynamic dns hostname must be a full qualified hostname for your dynamic dns provider, for example arthur-rimbaud.dyndns.org. 
    It can contain only letters, numbers and hyphens, and must begin with a letter or a number.

    
Description 
    An optional comment for the host name.

Login
    The login must be a valid login for your dynamic dns provider.

Password
    The password must be a valid password for your dynamic dns provider.

Mail Exchanger hostname
    You can here your MX field, not available for all DynDNS providers.

Custom Dynamic Provider
    Here you can enter your custom settings. It is possible that your dynamic dns provider uses
    specific settings not available here.

    * Server Address (FQDN) : This field is the fully qualified domain name of your  provider server
    * Ddclient protocol : this field is the ddclient protocol you must use with your provider.

Dynamic DNS Providers
    You can choose between these providers, if yours are not available, please ask to add it.
