# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_18:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 18:08:00 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-14 18:07:54 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:06:16 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-05-14 18:06:10 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 18:05:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-14 18:05:22 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-05-14 18:05:04 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-14 18:04:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-05-14 18:04:52 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-14 18:04:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.085 |  |
| 2026-05-14 18:04:17 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-14 18:04:15 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-14 18:04:02 | Rathnapura (Kalu Ganga) | 4.83 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-14 18:03:55 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 18:03:49 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.050 |  |
| 2026-05-14 18:03:40 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 18:03:27 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:03:26 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:17 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:11 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:02:51 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-14 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.51 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-14 18:02:42 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.308 | 🔺 Rising |
| 2026-05-14 18:02:34 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:02:12 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:01:35 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-14 18:01:35 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-05-14 18:01:34 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:01:24 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:01:23 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-14 18:01:14 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:57 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-14 18:00:56 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:13 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:09 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.51 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-14 18:02:42 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.308 | 🔺 Rising |
| 2026-05-14 18:06:16 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.036 | 🔺 Rising |
| 2026-05-14 18:05:22 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | 0.616 | 🔺 Rising |
| 2026-05-14 18:04:17 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-14 18:01:35 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.388 | 🔺 Rising |
| 2026-05-14 18:02:51 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-05-14 16:04:04 | Deraniyagala (Kelani Ganga) | 3.81 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-14 18:08:00 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-05-14 18:01:35 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-05-14 18:05:04 | Thawalama (Gin Ganga) | 2.44 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-14 18:04:15 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-14 18:04:02 | Rathnapura (Kalu Ganga) | 4.83 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-14 18:04:52 | Ellagawa (Kalu Ganga) | 8.39 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-14 18:01:23 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-14 18:03:40 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-14 18:00:09 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-14 18:03:55 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:17 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:56 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:00:13 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:26 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:01:14 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:02:12 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:07:54 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:01:24 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:05:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-05-14 18:06:10 | Katharagama (Menik Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:02:34 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:03:27 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:01:34 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:03:11 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-14 18:00:57 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-14 18:03:49 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | -0.050 |  |
| 2026-05-14 18:04:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.085 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 18:04:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)