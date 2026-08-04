# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_21:13:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 21:13:07 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.086 |  |
| 2026-08-04 21:10:54 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-08-04 21:10:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:09:56 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 21:09:00 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | -0.019 |  |
| 2026-08-04 21:08:03 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-08-04 21:07:29 | Glencourse (Kelani Ganga) | 13.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-04 21:06:59 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:06:56 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.057 |  |
| 2026-08-04 21:06:22 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.074 |  |
| 2026-08-04 21:05:51 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.109 |  |
| 2026-08-04 21:05:42 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-04 21:05:42 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:05:21 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-04 21:05:14 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-08-04 21:05:07 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:04:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:04:34 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.036 |  |
| 2026-08-04 21:03:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:03:46 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-08-04 21:03:42 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:03:37 | Deraniyagala (Kelani Ganga) | 2.69 | 🟢 Normal | -0.403 |  |
| 2026-08-04 21:03:36 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-08-04 21:03:13 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.024 |  |
| 2026-08-04 21:03:10 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.042 |  |
| 2026-08-04 21:03:04 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:02:49 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.034 |  |
| 2026-08-04 21:02:41 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-08-04 21:02:28 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:02:27 | Peradeniya (Mahaweli Ganga) | 4.66 | 🟢 Normal | -0.021 |  |
| 2026-08-04 21:02:11 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.100 |  |
| 2026-08-04 21:01:42 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 21:01:32 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:01:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-08-04 21:00:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 21:06:56 | Rathnapura (Kalu Ganga) | 5.98 | 🟡 Alert | -0.057 |  |
| 2026-08-04 21:11:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.086 |  |
| 2026-08-04 21:07:29 | Glencourse (Kelani Ganga) | 13.10 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-04 21:05:42 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-04 21:01:42 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 21:09:56 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 21:00:23 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:05:42 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:02:28 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:13:07 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:04:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:02:50 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:03:04 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:10:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:03:42 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-04 21:10:54 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-08-04 21:05:21 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-04 21:03:46 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:06:59 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:01:32 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-04 21:01:15 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-08-04 21:09:00 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | -0.019 |  |
| 2026-08-04 21:03:46 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-08-04 21:05:14 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-08-04 21:02:27 | Peradeniya (Mahaweli Ganga) | 4.66 | 🟢 Normal | -0.021 |  |
| 2026-08-04 21:03:36 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-08-04 21:03:13 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.024 |  |
| 2026-08-04 21:02:41 | Nawalapitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.030 |  |
| 2026-08-04 21:02:49 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.034 |  |
| 2026-08-04 21:04:34 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.036 |  |
| 2026-08-04 21:08:03 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.040 |  |
| 2026-08-04 21:03:10 | Panadugama (Nilwala Ganga) | 3.70 | 🟢 Normal | -0.042 |  |
| 2026-08-04 21:06:22 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.074 |  |
| 2026-08-04 21:02:11 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.100 |  |
| 2026-08-04 21:05:51 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.109 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-04 21:03:37 | Deraniyagala (Kelani Ganga) | 2.69 | 🟢 Normal | -0.403 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)