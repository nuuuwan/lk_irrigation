# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_12:19:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,937 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 12:19:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:10:19 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-09-21 12:09:26 | Rathnapura (Kalu Ganga) | 5.70 | 🟡 Alert | -0.027 |  |
| 2026-09-21 12:09:04 | Magura (Kalu Ganga) | 5.51 | 🟡 Alert | -0.019 |  |
| 2026-09-21 12:09:03 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:08:19 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.015 |  |
| 2026-09-21 12:06:37 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.078 |  |
| 2026-09-21 12:06:10 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-09-21 12:06:00 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-09-21 12:05:51 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.000 |  |
| 2026-09-21 12:05:50 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.000 |  |
| 2026-09-21 12:05:24 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-21 12:04:55 | Glencourse (Kelani Ganga) | 13.29 | 🟢 Normal | -0.183 |  |
| 2026-09-21 12:04:43 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-21 12:04:38 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.048 |  |
| 2026-09-21 12:04:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-21 12:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-09-21 12:04:08 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 12:04:02 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.031 |  |
| 2026-09-21 12:03:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:03:47 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.123 |  |
| 2026-09-21 12:03:37 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.072 |  |
| 2026-09-21 12:03:25 | Hanwella (Kelani Ganga) | 6.18 | 🟢 Normal | -0.148 |  |
| 2026-09-21 12:03:14 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 12:02:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:58 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 12:02:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 12:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:41 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.021 |  |
| 2026-09-21 12:02:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 12:01:38 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | -0.053 |  |
| 2026-09-21 12:01:27 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:01:25 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-09-21 12:01:25 | Weraganthota (Mahaweli Ganga) | 2.88 | 🟢 Normal | 5.695 | 🔺 Rising |
| 2026-09-21 12:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:00:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:00:40 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 12:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.87 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-09-21 12:05:51 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.000 |  |
| 2026-09-21 12:02:55 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 12:09:04 | Magura (Kalu Ganga) | 5.51 | 🟡 Alert | -0.019 |  |
| 2026-09-21 12:09:26 | Rathnapura (Kalu Ganga) | 5.70 | 🟡 Alert | -0.027 |  |
| 2026-09-21 12:01:38 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | -0.053 |  |
| 2026-09-21 12:01:25 | Weraganthota (Mahaweli Ganga) | 2.88 | 🟢 Normal | 5.695 | 🔺 Rising |
| 2026-09-21 12:02:58 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-21 12:04:38 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-09-21 12:02:13 | Nawalapitiya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 12:04:43 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-21 12:03:14 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 12:02:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 12:04:08 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 12:02:21 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:49 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:01:27 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:58 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:02:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:00:40 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:09:03 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:19:35 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:00:43 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:03:53 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 12:05:24 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-09-21 12:06:10 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-09-21 12:01:25 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-09-21 12:08:19 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.015 |  |
| 2026-09-21 12:10:19 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.017 |  |
| 2026-09-21 12:02:41 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -0.021 |  |
| 2026-09-21 12:04:02 | Dunamale (Aththanagalu Oya) | 3.20 | 🟢 Normal | -0.031 |  |
| 2026-09-21 12:06:00 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-09-21 12:04:38 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.048 |  |
| 2026-09-21 12:03:37 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.072 |  |
| 2026-09-21 12:06:37 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.078 |  |
| 2026-09-21 12:03:47 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.123 |  |
| 2026-09-21 12:03:25 | Hanwella (Kelani Ganga) | 6.18 | 🟢 Normal | -0.148 |  |
| 2026-09-21 12:04:55 | Glencourse (Kelani Ganga) | 13.29 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)