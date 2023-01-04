from upkeep import upkeep

u = upkeep('user','password')
locations = u.locations.get_all_locations()

location_lut = {}
for l in locations:
    location_lut[l["name"]] = l["id"]

# https://developers.onupkeep.com/#create-an-asset
u.assets.create_asset("DF-20221212-00", serial="1EC4-1-2149-00080", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address: ", area="")
u.assets.create_asset("DF-20221212-01", serial="1EC4-1-2149-00132", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address: ", area="")
u.assets.create_asset("DF-20221212-02", serial="1EC4-1-2149-00276", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address: ", area="")
u.assets.create_asset("DF-20221212-03", serial="1EC4-1-2149-00077", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-00", serial="1EC4-1-2149-00335", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-01", serial="1EC4-1-2149-00152", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-02", serial="1EC4-1-2149-00354", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-03", serial="1EC4-1-2149-00139", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-04", serial="1EC4-1-2149-00175", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")
u.assets.create_asset("DF-20221219-05", serial="1EC4-1-2149-00142", location=location_lut["Terawatt HQ"],
                      description="WIFI MAC Address:", area="")

# Manually delete assets from the UI
