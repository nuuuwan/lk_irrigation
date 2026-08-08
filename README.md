# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_01:16:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 01:16:27 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-08-09 01:15:12 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:08:16 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 01:07:26 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:06:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.020 |  |
| 2026-08-09 01:05:55 | Peradeniya (Mahaweli Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-08-09 01:05:38 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:05:36 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:05:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 01:05:09 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-09 01:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-09 01:04:40 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.049 |  |
| 2026-08-09 01:04:33 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.060 |  |
| 2026-08-09 01:04:30 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-09 01:04:13 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 01:03:55 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:03:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:02:46 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:02:40 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:02:14 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-09 01:02:06 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:01:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:46 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-08-09 01:01:35 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-09 01:01:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:00:43 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 01:04:30 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-09 01:01:35 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-09 01:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-09 01:05:09 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-09 01:04:13 | Nawalapitiya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 01:00:43 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 01:02:14 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-09 00:02:45 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 01:08:16 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 01:05:26 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 00:02:25 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 23:02:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:02:46 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:57 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 23:06:40 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:46 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:15:12 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:03:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:02:40 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:04:51 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:05:38 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:18 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:16:27 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-08-09 01:07:26 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:05:36 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:02:06 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:03:55 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:05:55 | Peradeniya (Mahaweli Ganga) | 3.73 | 🟢 Normal | -0.019 |  |
| 2026-08-09 01:06:16 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.020 |  |
| 2026-08-09 01:01:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-08-09 01:04:40 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.049 |  |
| 2026-08-09 01:04:33 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | -0.060 |  |
| 2026-08-09 00:06:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)