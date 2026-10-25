# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_02:29:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,050 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 02:29:50 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.115 |  |
| 2026-10-26 02:21:56 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:09:45 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 02:09:35 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:08:38 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-26 02:08:33 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-26 02:07:45 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 02:07:05 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.068 |  |
| 2026-10-26 02:07:02 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-26 02:06:31 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-26 02:06:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:06:11 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 02:05:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-26 02:05:08 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.208 |  |
| 2026-10-26 02:04:02 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-26 02:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.068 |  |
| 2026-10-26 02:03:02 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-26 02:02:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:02:01 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 02:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 02:01:46 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.112 |  |
| 2026-10-26 02:01:41 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-26 02:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:01:19 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-10-26 02:01:17 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-26 02:01:15 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 02:00:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 02:00:40 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-10-26 01:55:33 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 01:49:40 | Norwood (Kelani Ganga) | 1.57 | 🟡 Alert | -0.023 |  |
| 2026-10-26 02:07:05 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.068 |  |
| 2026-10-26 02:00:40 | Moragaswewa (Deduru Oya) | 2.47 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-10-26 02:01:41 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-26 02:08:33 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 02:06:31 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-26 02:01:17 | Ellagawa (Kalu Ganga) | 7.95 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-26 02:04:02 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-26 02:05:36 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-26 02:09:45 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-26 02:08:38 | Dunamale (Aththanagalu Oya) | 3.10 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-26 02:07:45 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 02:07:02 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-26 01:55:33 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-26 02:01:15 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 02:02:01 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 01:05:48 | Putupaula (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 02:00:41 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 02:06:11 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 02:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 01:07:39 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:06:23 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:09:35 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:02:48 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:01:28 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 01:03:29 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-26 02:21:56 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:55 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-26 02:03:02 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-26 02:01:19 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-10-26 02:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.068 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 02:01:46 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.112 |  |
| 2026-10-26 02:29:50 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.115 |  |
| 2026-10-26 01:04:47 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.138 |  |
| 2026-10-26 02:05:08 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)