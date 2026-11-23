# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_02:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 02:17:01 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-24 02:15:16 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.008 |  |
| 2026-11-24 02:14:55 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:14:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:11:28 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.523 |  |
| 2026-11-24 02:09:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-11-24 02:08:43 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 02:07:11 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -18.000 |  |
| 2026-11-24 02:07:09 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -18.000 |  |
| 2026-11-24 02:06:42 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-24 02:05:07 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-24 02:04:20 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-24 02:04:08 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-24 02:03:17 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-11-24 02:03:05 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:02:33 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-24 02:02:21 | Giriulla (Maha Oya) | 4.49 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-11-24 02:02:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:02:07 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.113 |  |
| 2026-11-24 02:01:36 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -3.429 |  |
| 2026-11-24 02:01:26 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:01:19 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-24 02:01:15 | Urawa (Nilwala Ganga) | 1.99 | 🟢 Normal | -3.429 |  |
| 2026-11-24 02:01:09 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-11-24 02:00:59 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:00:31 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-11-24 02:00:31 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:00:27 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:00:09 | Peradeniya (Mahaweli Ganga) | 3.01 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 02:02:21 | Giriulla (Maha Oya) | 4.49 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-11-24 02:09:49 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-11-24 02:05:07 | Glencourse (Kelani Ganga) | 11.86 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-24 02:03:17 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-11-24 00:00:17 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-24 02:06:42 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-24 01:01:08 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-24 02:04:08 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-24 02:01:19 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-24 02:17:01 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-24 00:24:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-24 02:08:43 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 01:05:35 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 00:04:06 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.005 |  |
| 2026-11-24 02:00:31 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:03:05 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:00:59 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:01:26 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 01:02:30 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:14:36 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:02:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:00:27 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:14:55 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-24 02:15:16 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.008 |  |
| 2026-11-24 00:07:00 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-11-24 02:02:33 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-24 01:01:40 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.010 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-24 02:04:20 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-11-24 02:01:09 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 02:00:31 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-11-24 02:00:09 | Peradeniya (Mahaweli Ganga) | 3.01 | 🟢 Normal | -0.041 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 02:02:07 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.113 |  |
| 2026-11-24 02:11:28 | Holombuwa (Kelani Ganga) | 1.71 | 🟢 Normal | -0.523 |  |
| 2026-11-24 02:01:36 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -3.429 |  |
| 2026-11-24 02:07:11 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)