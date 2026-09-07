# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_23:31:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 23:31:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-07 23:26:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-07 23:14:07 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:12:47 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:11:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-07 23:10:52 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:09:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:08:18 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:07:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:06:03 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:54 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-07 23:05:51 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:42 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:25 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:15 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-07 23:04:50 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:22 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.987 | 🔺 Rising |
| 2026-09-07 23:04:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:07 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-07 23:03:52 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:03:47 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:03:40 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-07 23:03:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:03:00 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-07 23:02:28 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 23:02:09 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:52 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:48 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-07 23:01:42 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:11 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:01 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 23:00:31 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 23:04:22 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.987 | 🔺 Rising |
| 2026-09-07 23:01:48 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-07 23:26:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-07 23:02:28 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 23:01:01 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 23:03:40 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-07 23:05:54 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-07 23:31:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-07 23:04:07 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-07 23:01:11 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:00:31 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:03:52 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:36 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:02:03 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:25 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:00:46 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:08:41 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:14:07 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-07 22:02:52 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:05:51 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:10:52 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:52 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:01:42 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:03:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:07:41 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:40 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:50 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:04:16 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:06:03 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:08:18 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-07 23:09:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:02:09 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:12:47 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:03:47 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-07 23:11:18 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-09-07 23:05:15 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)