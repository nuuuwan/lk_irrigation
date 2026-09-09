# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_15:07:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,273 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 15:07:44 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:07:06 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.047 |  |
| 2026-09-09 15:05:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:05:41 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:04:54 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-09 15:04:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:04:40 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 15:04:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 15:04:28 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:04:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-09 15:04:17 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-09 15:03:30 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:03:26 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |
| 2026-09-09 15:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.059 |  |
| 2026-09-09 15:03:21 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-09-09 15:03:19 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-09 15:03:02 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.020 |  |
| 2026-09-09 15:03:00 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:50 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 15:02:48 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:41 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:37 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:35 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:34 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-09 15:02:30 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:02:17 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:47 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:39 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:15 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:12 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 15:01:07 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:00:29 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-09 15:00:25 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-09-09 15:00:21 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:00:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 15:04:17 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-09 15:04:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-09 15:00:29 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-09 15:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-09 15:04:54 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-09 15:04:40 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 15:04:31 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-09 15:01:12 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 15:02:50 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 15:01:47 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:00:21 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:04:49 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 13:57:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:41 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:00:21 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:48 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:07 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:37 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:39 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:01:15 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:03:00 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:35 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:17 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:07:44 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:02:37 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:04:28 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-09 14:14:19 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 15:05:55 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:02:30 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:05:41 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-09 15:02:34 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-09-09 15:00:25 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-09-09 15:03:02 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.020 |  |
| 2026-09-09 15:03:19 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-09-09 15:03:21 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-09-09 15:07:06 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.047 |  |
| 2026-09-09 15:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.059 |  |
| 2026-09-09 15:03:26 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)