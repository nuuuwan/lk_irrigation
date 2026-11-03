# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_01:25:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 01:25:44 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:21:55 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.025 |  |
| 2026-11-04 01:20:29 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-04 01:14:49 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-04 01:14:02 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.112 |  |
| 2026-11-04 01:13:45 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-04 01:10:29 | Urawa (Nilwala Ganga) | 2.52 | 🟡 Alert | -0.553 |  |
| 2026-11-04 01:08:32 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:08:07 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-04 01:07:51 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.190 |  |
| 2026-11-04 01:07:42 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-11-04 01:06:59 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-04 01:06:42 | Moraketiya (Walawe Ganga) | 3.25 | 🟡 Alert | -0.010 |  |
| 2026-11-04 01:05:19 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-11-04 01:04:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2026-11-04 01:04:23 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.400 |  |
| 2026-11-04 01:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 01:03:33 | Moragaswewa (Deduru Oya) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-11-04 01:03:31 | Giriulla (Maha Oya) | 3.61 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-04 01:03:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-04 01:03:06 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-11-04 01:02:46 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.070 |  |
| 2026-11-04 01:02:32 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:02:29 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -28.000 |  |
| 2026-11-04 01:02:20 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:01:35 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -28.000 |  |
| 2026-11-04 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-04 01:01:09 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-11-04 01:00:40 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | -0.051 |  |
| 2026-11-04 01:00:17 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 01:06:42 | Moraketiya (Walawe Ganga) | 3.25 | 🟡 Alert | -0.010 |  |
| 2026-11-04 01:10:29 | Urawa (Nilwala Ganga) | 2.52 | 🟡 Alert | -0.553 |  |
| 2026-11-04 00:04:12 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 9.474 | 🔺 Rising |
| 2026-11-04 00:03:29 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-04 01:05:19 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-11-04 01:14:49 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 01:07:42 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-11-04 01:03:31 | Giriulla (Maha Oya) | 3.61 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-11-04 01:06:59 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-04 01:13:45 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-04 01:08:07 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-04 01:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 01:20:29 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-04 01:00:17 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:49:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:08:32 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:25:44 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:02:20 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:16:27 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:02:32 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:03:19 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-11-04 01:03:14 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-11-04 01:03:33 | Moragaswewa (Deduru Oya) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-11-04 01:01:09 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-11-04 01:03:06 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-11-04 01:21:55 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.025 |  |
| 2026-11-04 01:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-04 01:00:40 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | -0.051 |  |
| 2026-11-04 01:04:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2026-11-04 01:02:46 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.070 |  |
| 2026-11-04 01:14:02 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.112 |  |
| 2026-11-04 00:02:14 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.141 |  |
| 2026-11-04 01:07:51 | Thanamalwila (Kirindi Oya) | 1.91 | 🟢 Normal | -0.190 |  |
| 2026-11-04 01:04:23 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.400 |  |
| 2026-11-04 01:02:29 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -28.000 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)