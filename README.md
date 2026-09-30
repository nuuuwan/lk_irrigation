# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_22:31:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 22:31:20 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:13:04 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:11:53 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-09-30 22:09:27 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:09:02 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:08:37 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.018 |  |
| 2026-09-30 22:07:40 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.009 |  |
| 2026-09-30 22:07:16 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:06:13 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-09-30 22:05:56 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:36 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-09-30 22:05:13 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:09 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:09 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-09-30 22:05:06 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:00 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 22:04:14 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-09-30 22:04:01 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:41 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:03:41 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:34 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:30 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:18 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-30 22:02:45 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -36.000 |  |
| 2026-09-30 22:02:44 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -36.000 |  |
| 2026-09-30 22:02:37 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:02:24 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:02:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-09-30 22:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-09-30 22:01:34 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-30 22:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:01:12 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:00:37 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-30 22:00:34 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:00:10 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 22:00:37 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-30 22:03:18 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 22:01:34 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-30 22:05:00 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 21:11:52 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-30 22:00:10 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:31:20 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:13:04 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:09 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:04:01 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:13 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:07:16 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:02:24 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:30 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:00:34 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:41 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:03:34 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:09:27 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:05:56 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 22:07:40 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.009 |  |
| 2026-09-30 22:09:02 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:03:41 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:02:37 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:01:12 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-09-30 22:08:37 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.018 |  |
| 2026-09-30 21:03:25 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-30 22:04:14 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | -0.021 |  |
| 2026-09-30 22:05:09 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.029 |  |
| 2026-09-30 22:02:10 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2026-09-30 22:06:13 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-09-30 22:05:36 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.031 |  |
| 2026-09-30 22:11:53 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-09-30 22:02:45 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)