# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_00:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,293 measurements** from **39** stations.
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
| 2026-08-09 00:10:18 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-09 00:08:05 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -35.169 |  |
| 2026-08-09 00:06:59 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2026-08-09 00:06:58 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:06:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.079 |  |
| 2026-08-09 00:06:30 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:06:04 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 00:05:56 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 00:05:18 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:05:18 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.023 |  |
| 2026-08-09 00:05:10 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 00:04:51 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:04:50 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:04:21 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-08-09 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -2.250 |  |
| 2026-08-09 00:04:18 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:56 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 00:03:48 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-08-09 00:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -2.250 |  |
| 2026-08-09 00:03:43 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-09 00:03:28 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.040 |  |
| 2026-08-09 00:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:45 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 00:02:40 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-09 00:02:33 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:25 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-09 00:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:35 | Hanwella (Kelani Ganga) | 6.00 | 🟢 Normal | -35.169 |  |
| 2026-08-09 00:01:18 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:14 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:05 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:00:56 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 23:01:13 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-09 00:10:18 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-08-09 00:03:43 | Peradeniya (Mahaweli Ganga) | 3.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-09 00:05:56 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-09 00:05:10 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 00:03:56 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 00:02:45 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 23:07:37 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 00:06:04 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 00:02:25 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:05:18 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-08 23:02:29 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:05 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:33 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 23:06:40 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:06:30 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:00:56 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:20 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:04:51 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:40 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:04:18 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:14 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:01:18 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:06:58 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:48 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-08-09 00:06:59 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.011 |  |
| 2026-08-09 00:05:18 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.023 |  |
| 2026-08-09 00:02:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-09 00:03:28 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | -0.040 |  |
| 2026-08-09 00:04:21 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-08-09 00:06:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.079 |  |
| 2026-08-09 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | -2.250 |  |
| 2026-08-09 00:08:05 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -35.169 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)