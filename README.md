# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_03:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,215 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 03:11:12 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-08-05 03:11:10 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.135 |  |
| 2026-08-05 03:11:10 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-08-05 03:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.053 |  |
| 2026-08-05 03:10:24 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-05 03:10:09 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | -0.107 |  |
| 2026-08-05 03:07:19 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:07:09 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:06:26 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.063 |  |
| 2026-08-05 03:06:04 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.180 |  |
| 2026-08-05 03:05:59 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:05:36 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.216 |  |
| 2026-08-05 03:05:18 | Kithulgala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 03:04:46 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-08-05 03:04:03 | Nawalapitiya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.595 | 🔺 Rising |
| 2026-08-05 03:04:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:03:34 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:03:19 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.048 |  |
| 2026-08-05 03:03:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-08-05 03:02:59 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 03:02:56 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 03:02:51 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:40 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:27 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:20 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.035 |  |
| 2026-08-05 03:02:00 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:53 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-05 03:01:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:21 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.070 |  |
| 2026-08-05 03:01:10 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:56:05 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.180 |  |
| 2026-08-05 02:46:07 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.216 |  |
| 2026-08-05 02:35:36 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.070 |  |
| 2026-08-05 02:23:44 | Nawalapitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.595 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 02:00:35 | Rathnapura (Kalu Ganga) | 5.51 | 🟡 Alert | -0.093 |  |
| 2026-08-05 03:11:12 | Ellagawa (Kalu Ganga) | 8.94 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-08-05 03:04:03 | Nawalapitiya (Mahaweli Ganga) | 3.38 | 🟢 Normal | 0.595 | 🔺 Rising |
| 2026-08-05 03:05:18 | Kithulgala (Kelani Ganga) | 2.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 03:02:56 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 03:01:53 | Peradeniya (Mahaweli Ganga) | 4.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-05 03:01:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:10 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:23 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 02:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:03:34 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:51 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:27 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:04:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 01:46:30 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:00 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:07:09 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:07:19 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:02:40 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:05:59 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:01:21 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 03:10:24 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-05 02:08:54 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-08-05 01:05:14 | Pitabeddara (Nilwala Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-08-05 03:02:59 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-08-05 03:03:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-08-05 03:04:46 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.012 |  |
| 2026-08-05 03:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.035 |  |
| 2026-08-05 03:03:19 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.048 |  |
| 2026-08-05 03:10:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | -0.053 |  |
| 2026-08-05 03:06:26 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | -0.063 |  |
| 2026-08-05 03:01:21 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.070 |  |
| 2026-08-05 03:10:09 | Glencourse (Kelani Ganga) | 13.15 | 🟢 Normal | -0.107 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-05 03:11:10 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.135 |  |
| 2026-08-05 03:06:04 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.180 |  |
| 2026-08-05 03:05:36 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)