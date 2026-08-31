# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_03:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,545 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 03:03:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:04 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:43 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:07 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.043 |  |
| 2026-09-01 03:01:37 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:08 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:01 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:00:56 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.225 |  |
| 2026-09-01 02:48:37 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:34:27 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.043 |  |
| 2026-09-01 02:26:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.123 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 00:11:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-09-01 02:26:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-09-01 02:06:34 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-01 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-01 02:03:15 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 03:03:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:01 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:00:47 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:04:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:43 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 00:00:55 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:07:25 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:07:25 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:05:49 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:01:11 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:01:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:02:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:02:23 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:48:37 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:03:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:04:42 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:37 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:07:06 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:28:33 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:04 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:02:55 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-09-01 01:47:46 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.018 |  |
| 2026-09-01 02:07:41 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.030 |  |
| 2026-09-01 02:11:30 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-09-01 01:09:09 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.036 |  |
| 2026-09-01 02:00:52 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.040 |  |
| 2026-09-01 03:02:07 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.043 |  |
| 2026-09-01 02:12:46 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.046 |  |
| 2026-09-01 03:00:56 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.225 |  |
| 2026-09-01 00:11:57 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.452 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)