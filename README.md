# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_05:20:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,905 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 05:20:43 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:18:00 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:13:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 05:09:44 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 05:09:01 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -180.000 |  |
| 2026-11-26 05:09:00 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -180.000 |  |
| 2026-11-26 05:07:50 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:06:32 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-26 05:06:23 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:06:20 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-11-26 05:06:19 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-26 05:05:26 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:05:01 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.115 |  |
| 2026-11-26 05:05:01 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-11-26 05:04:55 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-26 05:04:51 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-11-26 05:04:29 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-26 05:03:29 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-26 05:03:26 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-26 05:03:24 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-11-26 05:03:12 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-26 05:03:07 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-26 05:02:44 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:02:22 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 05:02:20 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.144 |  |
| 2026-11-26 05:02:17 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-26 05:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-11-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-26 05:02:07 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.097 |  |
| 2026-11-26 05:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:01:15 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-11-26 05:00:55 | Thalgahagoda (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-26 05:00:40 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-26 05:00:32 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-11-26 05:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-26 04:56:11 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 05:02:22 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-11-26 05:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-11-25 20:05:34 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | 0.483 | 🔺 Rising |
| 2026-11-26 05:06:32 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.320 | 🔺 Rising |
| 2026-11-26 05:02:17 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-26 05:00:40 | Moragaswewa (Deduru Oya) | 3.06 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-26 05:06:19 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-26 05:03:26 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-26 05:03:29 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-26 05:04:55 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-26 05:04:29 | Hanwella (Kelani Ganga) | 3.93 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-26 05:09:44 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 05:13:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 05:02:44 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:01:24 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:06:23 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:20:43 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:07:50 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:18:00 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:05:26 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-26 05:06:20 | Katharagama (Menik Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-11-26 05:03:12 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-11-26 05:03:07 | Wellawaya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-26 04:56:11 | Panadugama (Nilwala Ganga) | 4.06 | 🟢 Normal | -0.023 |  |
| 2026-11-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-26 05:00:32 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.031 |  |
| 2026-11-26 05:03:24 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-11-26 05:00:28 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-11-26 05:04:51 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.043 |  |
| 2026-11-26 05:05:01 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.051 |  |
| 2026-11-26 05:01:15 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | -0.074 |  |
| 2026-11-26 05:02:07 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.097 |  |
| 2026-11-26 05:05:01 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.115 |  |
| 2026-11-26 05:02:20 | Glencourse (Kelani Ganga) | 11.87 | 🟢 Normal | -0.144 |  |
| 2026-11-26 05:09:01 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)