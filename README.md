# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_21:07:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,486 measurements** from **39** stations.
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
| 2026-09-29 21:07:51 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:06:38 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.058 |  |
| 2026-09-29 21:06:21 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-09-29 21:06:20 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:06:03 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-09-29 21:04:50 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-29 21:04:22 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:12 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:05 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:04:04 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:03 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:01 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:03:57 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:03:51 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:51 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-09-29 21:03:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:42 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:38 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 21:02:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:22 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:15 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.031 |  |
| 2026-09-29 21:01:58 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:01:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 21:01:19 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:01:18 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-29 21:01:08 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:00:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.099 |  |
| 2026-09-29 21:00:11 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:58:28 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 21:04:50 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-29 21:01:18 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-29 21:01:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-29 21:02:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:01:08 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:31 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:58:28 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:01:19 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:51 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:22 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:12 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:06:20 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:38 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:00:11 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-29 20:02:20 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:03 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:04:04 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:03:42 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:01:58 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:02:22 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 21:07:51 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:03:57 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:04:01 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:04:05 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.010 |  |
| 2026-09-29 21:03:51 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-09-29 21:06:03 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-09-29 20:04:10 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-09-29 21:06:21 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-09-29 21:02:15 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.031 |  |
| 2026-09-29 21:06:38 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.058 |  |
| 2026-09-29 21:00:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)