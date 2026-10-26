# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_13:16:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🔴 Holombuwa — Major Flood; 🟠 Rathnapura — Minor Flood; 🟡 Kithulgala — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 13:16:25 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:11:17 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:11:16 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 13:10:51 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.018 |  |
| 2026-10-26 13:08:52 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-26 13:08:02 | Rathnapura (Kalu Ganga) | 7.78 | 🟠 Minor Flood | 0.165 | 🔺 Rising |
| 2026-10-26 13:07:38 | Hanwella (Kelani Ganga) | 4.44 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-26 13:06:44 | Urawa (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-10-26 13:06:21 | Peradeniya (Mahaweli Ganga) | 4.98 | 🟢 Normal | 0.591 | 🔺 Rising |
| 2026-10-26 13:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-10-26 13:05:54 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-10-26 13:05:49 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 13:05:47 | Kithulgala (Kelani Ganga) | 3.46 | 🟡 Alert | 0.330 | 🔺 Rising |
| 2026-10-26 13:05:32 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-26 13:04:44 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 13:04:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:04:36 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:04:34 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:04:17 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 13:04:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:03:50 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -228.000 |  |
| 2026-10-26 13:03:15 | Holombuwa (Kelani Ganga) | 5.05 | 🔴 Major Flood | 0.388 | 🔺 Rising |
| 2026-10-26 13:03:12 | Galgamuwa (Mee Oya) | 3.46 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-10-26 13:03:12 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.162 |  |
| 2026-10-26 13:03:11 | Panadugama (Nilwala Ganga) | 5.05 | 🟡 Alert | -228.000 |  |
| 2026-10-26 13:03:09 | Deraniyagala (Kelani Ganga) | 4.02 | 🟢 Normal | 0.675 | 🔺 Rising |
| 2026-10-26 13:03:04 | Nawalapitiya (Mahaweli Ganga) | 3.67 | 🟡 Alert | -0.257 |  |
| 2026-10-26 13:02:42 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 13:02:38 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-26 13:02:12 | Norwood (Kelani Ganga) | 2.23 | 🟡 Alert | -0.030 |  |
| 2026-10-26 13:01:17 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 13:01:13 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:01:09 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:01:08 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-26 13:01:03 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-10-26 13:00:57 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 13:00:47 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:00:14 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:00:09 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 13:03:15 | Holombuwa (Kelani Ganga) | 5.05 | 🔴 Major Flood | 0.388 | 🔺 Rising |
| 2026-10-26 13:08:02 | Rathnapura (Kalu Ganga) | 7.78 | 🟠 Minor Flood | 0.165 | 🔺 Rising |
| 2026-10-26 13:05:47 | Kithulgala (Kelani Ganga) | 3.46 | 🟡 Alert | 0.330 | 🔺 Rising |
| 2026-10-26 13:01:03 | Dunamale (Aththanagalu Oya) | 3.54 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-10-26 13:05:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-10-26 13:10:51 | Magura (Kalu Ganga) | 4.16 | 🟡 Alert | -0.018 |  |
| 2026-10-26 13:02:12 | Norwood (Kelani Ganga) | 2.23 | 🟡 Alert | -0.030 |  |
| 2026-10-26 13:03:04 | Nawalapitiya (Mahaweli Ganga) | 3.67 | 🟡 Alert | -0.257 |  |
| 2026-10-26 13:03:09 | Deraniyagala (Kelani Ganga) | 4.02 | 🟢 Normal | 0.675 | 🔺 Rising |
| 2026-10-26 13:06:21 | Peradeniya (Mahaweli Ganga) | 4.98 | 🟢 Normal | 0.591 | 🔺 Rising |
| 2026-10-26 13:05:54 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | 0.508 | 🔺 Rising |
| 2026-10-26 13:03:12 | Galgamuwa (Mee Oya) | 3.46 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-10-26 12:06:01 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-10-26 13:06:44 | Urawa (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-10-26 13:08:52 | Giriulla (Maha Oya) | 3.31 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-10-26 13:01:08 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-26 13:04:44 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 13:07:38 | Hanwella (Kelani Ganga) | 4.44 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-26 13:00:57 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 13:04:17 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 13:02:42 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 13:11:16 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 13:05:49 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 13:04:34 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:04:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:04:36 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 13:01:17 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 13:05:32 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-26 13:00:14 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:01:09 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:16:25 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:01:13 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:04:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:00:47 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:11:17 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 13:02:38 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-26 13:00:09 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | -0.010 |  |
| 2026-10-26 13:03:12 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.162 |  |
| 2026-10-26 13:03:50 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -228.000 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)