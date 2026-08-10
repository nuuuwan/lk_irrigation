# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_16:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,788 measurements** from **39** stations.
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
| 2026-08-10 16:08:00 | Peradeniya (Mahaweli Ganga) | 3.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 16:06:14 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:05:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:05:47 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:05:06 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:04:40 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:04:38 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-08-10 16:04:05 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:04 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.049 |  |
| 2026-08-10 16:04:03 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-10 16:03:54 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:03:47 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.021 |  |
| 2026-08-10 16:03:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 16:03:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-08-10 16:02:52 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.061 |  |
| 2026-08-10 16:02:36 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:02:28 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:02:27 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 16:02:17 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-08-10 16:01:56 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.076 |  |
| 2026-08-10 16:01:42 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:08 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:49 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:34 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:00:32 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.070 |  |
| 2026-08-10 16:00:14 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.035 |  |
| 2026-08-10 15:59:09 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:26:05 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 15:03:38 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-08-10 15:11:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-08-10 16:02:17 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-08-10 16:03:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 16:02:27 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 16:08:00 | Peradeniya (Mahaweli Ganga) | 3.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 16:04:03 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-10 16:00:55 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:02:28 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:05:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:05 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:05:47 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:06:14 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:02:36 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:38 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:49 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:00:32 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 15:59:09 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:01:08 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 16:04:40 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:03:54 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:01:56 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:01:42 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:05:06 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-08-10 16:00:34 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-10 15:09:12 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.018 |  |
| 2026-08-10 16:03:47 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.021 |  |
| 2026-08-10 16:03:18 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.029 |  |
| 2026-08-10 16:04:30 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-08-10 16:00:14 | Panadugama (Nilwala Ganga) | 3.73 | 🟢 Normal | -0.035 |  |
| 2026-08-10 15:11:01 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-08-10 16:04:04 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.049 |  |
| 2026-08-10 16:02:52 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.061 |  |
| 2026-08-10 16:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.070 |  |
| 2026-08-10 16:01:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)