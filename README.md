# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_17:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-08-29 16:22:32 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:20:22 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-29 16:18:05 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 16:17:14 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.008 |  |
| 2026-08-29 16:15:22 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:14:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:14:15 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 16:20:22 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-29 16:11:13 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-29 17:01:56 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-29 16:03:38 | Thawalama (Gin Ganga) | 1.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 17:02:53 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 16:11:28 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 17:01:32 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-29 16:06:53 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 17:01:30 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 17:01:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 17:01:22 | Weraganthota (Mahaweli Ganga) | -3.48 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:29 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:23 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:05:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:06:03 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:02:14 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:15:22 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:03:09 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:09:06 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:00:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:04:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:05:23 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:07:51 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:01:15 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:00:24 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:00 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 17:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 16:17:14 | Rathnapura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.008 |  |
| 2026-08-29 17:03:20 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:25 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:01:01 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.010 |  |
| 2026-08-29 17:03:19 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.019 |  |
| 2026-08-29 17:02:36 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-08-29 17:02:52 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-29 16:04:50 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.059 |  |
| 2026-08-29 16:06:12 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.059 |  |
| 2026-08-29 16:05:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.075 |  |
| 2026-08-29 17:02:43 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)