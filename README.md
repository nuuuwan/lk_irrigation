# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_17:29:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,429 measurements** from **39** stations.
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
| 2026-08-29 17:29:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:14:57 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:13:57 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:11:53 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 17:11:27 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:10:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:09:54 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:09:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.113 |  |
| 2026-08-29 17:08:05 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-29 17:07:34 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 17:06:32 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:06:11 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 17:05:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:48 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:39 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:03:49 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.052 |  |
| 2026-08-29 17:03:25 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:20 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-08-29 17:03:09 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:53 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 17:02:52 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-29 17:02:43 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.092 |  |
| 2026-08-29 17:02:36 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-08-29 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:00 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:01:56 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 17:01:32 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-29 17:01:30 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 17:01:22 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:01:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:01:15 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:01:01 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:00:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:00:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 17:08:05 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-29 17:01:56 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 17:02:53 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 17:07:34 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 17:01:32 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-29 17:11:53 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 17:06:11 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 17:01:30 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 17:01:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:03:53 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:13:57 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:01:22 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:20 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:29:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:11:27 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:14:57 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:09 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:48 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:00:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:05:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:04:39 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:10:20 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:09:54 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:01:15 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:00:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:00 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:06:32 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:20 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:25 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:01:01 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-08-29 17:02:36 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-08-29 17:02:52 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-29 17:03:49 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.052 |  |
| 2026-08-29 17:02:43 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.092 |  |
| 2026-08-29 17:09:38 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)