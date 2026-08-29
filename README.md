# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_08:04:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 08:04:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.087 |  |
| 2026-08-29 08:04:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.139 |  |
| 2026-08-29 08:04:19 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-08-29 08:04:10 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 08:04:02 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.112 |  |
| 2026-08-29 08:03:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 08:03:40 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-29 08:03:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:03:16 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.065 |  |
| 2026-08-29 08:02:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 08:02:01 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:01:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:41 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:41 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 08:01:31 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-29 08:01:17 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-29 08:01:09 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:01:05 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:49:49 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:20:51 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-29 07:16:11 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-29 07:15:51 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.112 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 07:04:23 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-08-29 07:11:49 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-29 08:03:40 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-29 08:01:31 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-29 08:03:59 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 07:16:11 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-29 07:20:51 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-29 08:02:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 08:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 08:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 07:04:32 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 07:49:49 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:19 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:00:49 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:04:40 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:04:10 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:02:40 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:01:05 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:01:37 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:01:09 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 08:02:01 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 07:09:35 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-08-29 07:13:32 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-08-29 07:07:44 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-29 07:03:10 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:03:21 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:41 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:43 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-29 08:01:41 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-29 07:04:54 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-08-29 08:01:17 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-29 08:04:19 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.039 |  |
| 2026-08-29 08:03:16 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.065 |  |
| 2026-08-29 08:04:43 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.087 |  |
| 2026-08-29 08:04:02 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.112 |  |
| 2026-08-29 08:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.139 |  |
| 2026-08-29 07:03:20 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)