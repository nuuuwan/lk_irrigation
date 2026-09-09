# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_09:07:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,032 measurements** from **39** stations.
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
| 2026-09-09 09:07:33 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 09:07:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:07:06 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 09:07:04 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.180 |  |
| 2026-09-09 09:06:10 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:05:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-09 09:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:04:58 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:04:57 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:04:48 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-09 09:04:35 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.039 |  |
| 2026-09-09 09:04:25 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 09:04:24 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-09 09:04:19 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-09-09 09:03:57 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-09-09 09:03:55 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.057 |  |
| 2026-09-09 09:03:20 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:15 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:07 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:03:01 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:02:54 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:48 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.126 |  |
| 2026-09-09 09:02:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:37 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 09:01:32 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:23 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:00 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-09 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:25 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:25 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 09:01:00 | Nagalagam Street (Kelani Ganga) | 0.38 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-09 09:04:24 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-09 09:05:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-09 09:07:33 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-09 09:07:06 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 09:04:25 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-09 09:04:48 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-09 09:01:37 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 08:05:00 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 09:00:40 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:02:19 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:20 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:25 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:55 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:06 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:54 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:06:10 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:04:58 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:23 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:01:32 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:02:48 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:15 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:07:10 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:20 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-09 08:08:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:00:25 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-09 09:03:07 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:03:01 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:04:57 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-09-09 09:03:57 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-09-09 09:04:35 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.039 |  |
| 2026-09-09 09:04:19 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.048 |  |
| 2026-09-09 09:03:35 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.057 |  |
| 2026-09-09 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.126 |  |
| 2026-09-09 09:07:04 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)