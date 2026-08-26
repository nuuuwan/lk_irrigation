# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_08:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,781 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 08:19:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.024 |  |
| 2026-08-26 08:17:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:15:30 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 08:13:57 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-26 08:11:48 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-26 08:10:22 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 08:10:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:09:57 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.035 |  |
| 2026-08-26 08:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 08:08:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:07:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:07:15 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-26 08:07:01 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 08:06:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:06:40 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.012 |  |
| 2026-08-26 08:06:17 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-26 08:06:07 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:05:57 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 08:05:40 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-26 08:05:28 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:05:12 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:53 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.043 |  |
| 2026-08-26 08:03:37 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-26 08:03:27 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 08:03:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-08-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:39 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 08:02:28 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.111 |  |
| 2026-08-26 08:02:21 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:19 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.031 |  |
| 2026-08-26 08:02:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:58 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-26 08:01:45 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:42 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-26 08:00:42 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 08:06:17 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-26 08:13:57 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-26 08:03:37 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-26 08:01:58 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-26 08:11:48 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-26 08:15:30 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 08:09:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-26 08:05:40 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-26 08:02:39 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 08:10:22 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 08:07:01 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-26 08:05:57 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 08:03:27 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 08:01:45 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:17:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:10:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:07:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:05:12 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:06:07 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:06 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:05:28 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:21 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:03:22 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:00:42 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:06:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:08:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:42 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:01:12 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:02:08 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-26 08:07:15 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-26 08:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-26 08:06:40 | Rathnapura (Kalu Ganga) | 3.79 | 🟢 Normal | -0.012 |  |
| 2026-08-26 08:19:54 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.024 |  |
| 2026-08-26 08:02:19 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.031 |  |
| 2026-08-26 08:09:57 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.035 |  |
| 2026-08-26 08:03:53 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | -0.043 |  |
| 2026-08-26 08:03:18 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |
| 2026-08-26 08:02:28 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)