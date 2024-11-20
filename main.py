import maxminddb

database = "20241119"

print("Enter the country code (e.g. US):")
country = input().upper()

with maxminddb.open_database(f"./data/{database}-Country.mmdb") as reader:
    for network, record in reader:
        if record.get("country") is not None and record.get("country").get("iso_code") == country:
            print(f"{country}: {network}")
            with maxminddb.open_database(f"./data/{database}-ASN.mmdb") as reader:
                    ip = str(network).split("/")[0]
                    data = reader.get(ip)
                    if data is None:
                        asn, org = "N/A", "N/A"
                    else:
                        asn = data["autonomous_system_number"]
                        org = data["autonomous_system_organization"]

                    open(f"./dist/{country}-{database}-ASN.txt", "a").write(f"{network}\t{country}\tAS{asn}\t{org}\n")
