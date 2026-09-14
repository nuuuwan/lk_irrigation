# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_13:19:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,675 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 13:19:23 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:12:15 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.152 |  |
| 2026-09-14 13:07:51 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:07:17 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:07:15 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:06:50 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:06:32 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-09-14 13:05:36 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:05:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 13:04:54 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 13:04:17 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:04:01 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:57 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:40 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-14 13:03:36 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:03:18 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-09-14 13:03:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:07 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.049 |  |
| 2026-09-14 13:03:06 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:45 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:26 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:02:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:09 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 13:02:09 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 13:02:07 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 13:01:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-09-14 13:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:53 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:44 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-09-14 13:01:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 13:01:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:00:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:40 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:12 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 13:01:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-09-14 13:04:54 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-14 13:03:40 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-14 13:02:07 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 13:05:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 13:01:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 13:02:09 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 13:02:09 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 12:01:41 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:26 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:55 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:04:01 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:19:23 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:08 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:07:17 | Glencourse (Kelani Ganga) | 9.37 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:45 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:12 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:06 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:06:50 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:02:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:01:53 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:40 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:07:51 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:03:57 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:04:17 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:01:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:05:36 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:03:36 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-14 11:01:27 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-14 13:03:18 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-09-14 13:06:32 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.011 |  |
| 2026-09-14 12:07:37 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.011 |  |
| 2026-09-14 13:01:44 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-09-14 13:03:07 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.049 |  |
| 2026-09-14 13:12:15 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)