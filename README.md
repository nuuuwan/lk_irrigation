# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--08_23:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,637 measurements** from **39** stations.
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
| 2026-09-08 23:02:51 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:43 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.079 |  |
| 2026-09-08 23:02:20 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:17 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:12 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:01:09 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:00:49 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 23:00:13 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:21:33 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-08 22:01:25 | Peradeniya (Mahaweli Ganga) | 2.39 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-09-08 22:04:14 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-08 22:01:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-08 22:05:09 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-08 22:12:06 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-08 22:00:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-08 23:00:49 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-08 22:02:07 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 22:07:13 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-08 22:00:19 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-08 21:03:02 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:00:13 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:04:01 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:01:04 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:12:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:02:28 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:12 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:07:01 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:05:37 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:20 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:06:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:21:33 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:03:21 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:02:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:51 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:02:17 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-08 20:04:45 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:11:27 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-08 23:01:09 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-08 22:09:37 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-09-08 22:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-09-08 22:07:20 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-08 22:00:18 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.023 |  |
| 2026-09-08 22:01:49 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.031 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-08 23:02:43 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)