# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_23:07:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,557 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 23:07:48 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | -0.028 |  |
| 2026-09-29 23:07:41 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:06:58 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-09-29 23:06:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:06:04 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:05:32 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:05:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:05:12 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-09-29 23:05:09 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:04:36 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-09-29 23:04:08 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:03:50 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:03:46 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:03:42 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 23:03:36 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:03:24 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 23:03:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:38 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:35 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:12 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:11 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:01:42 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:01:37 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-29 23:01:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:00 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:44 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:39 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:00:33 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-09-29 23:00:12 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-29 22:59:24 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-09-29 22:55:24 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 23:05:12 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-09-29 23:01:37 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-29 23:00:12 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-29 23:03:24 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 23:03:42 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 23:03:10 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:39 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:03:46 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:44 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:13:15 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:12 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:38 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:04:08 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:23 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:06 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:01:00 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:35 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:05:32 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:06:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:05:13 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:03:50 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:02:11 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:06:58 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-09-29 23:03:36 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:01:57 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-29 23:04:36 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-09-29 23:00:33 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.013 |  |
| 2026-09-29 23:06:04 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:01:42 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:07:41 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:05:09 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-09-29 23:07:48 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | -0.028 |  |
| 2026-09-29 22:13:24 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.037 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)