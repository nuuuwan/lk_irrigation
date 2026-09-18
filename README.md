# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_01:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 01:03:31 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-19 01:03:14 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-19 01:03:12 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:02:50 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-09-19 01:02:38 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-09-19 01:02:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:02:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.100 |  |
| 2026-09-19 01:02:17 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-19 01:02:16 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:42 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:25 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:12 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:10 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 01:00:46 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 01:00:37 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 00:14:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-09-19 01:03:31 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-19 01:03:14 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-09-19 00:02:46 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-19 01:02:17 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-19 00:13:40 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-19 00:02:15 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-19 00:09:38 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-19 00:00:56 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-19 01:00:46 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 01:01:10 | Ellagawa (Kalu Ganga) | 4.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 01:00:37 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 00:10:18 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:02:01 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:03:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:12 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:02:31 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:10:58 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:25 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:39 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:09:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:03:12 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:02:16 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:05:41 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:04:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-19 01:01:42 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 00:09:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-19 01:02:50 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-09-19 00:11:55 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-19 00:07:34 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-09-19 00:07:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-09-19 00:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-09-19 01:02:38 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-09-19 00:03:01 | Baddegama (Gin Ganga) | 2.75 | 🟢 Normal | -0.031 |  |
| 2026-09-19 00:03:38 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.070 |  |
| 2026-09-19 01:02:25 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)