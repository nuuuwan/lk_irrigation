# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_23:35:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 23:35:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-29 23:26:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:09:14 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-08-29 23:09:06 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 23:08:45 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-29 23:08:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:07:42 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:07:42 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-08-29 23:07:16 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:06:50 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.392 |  |
| 2026-08-29 23:06:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:06:26 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-08-29 23:05:29 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:04 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:04:45 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.020 |  |
| 2026-08-29 23:04:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:03:56 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:03:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:03:19 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-29 23:03:09 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 23:03:08 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 23:02:59 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.058 |  |
| 2026-08-29 23:02:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:02:54 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 23:02:35 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:02:27 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 23:02:12 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-29 23:02:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-29 23:01:33 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:20 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:08 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:06 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:00:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 23:08:45 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-29 23:02:27 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-29 23:09:06 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 23:03:08 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 23:03:09 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 23:02:54 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 22:08:41 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 23:35:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-29 23:26:17 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:33 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:08 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:00:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:06 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:02:57 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:01:20 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:07:42 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:02:35 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:03:33 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:06:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:03:56 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:04:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:04 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:08:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:07:16 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:05:29 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-29 23:02:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-08-29 23:03:19 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-29 23:07:42 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.018 |  |
| 2026-08-29 23:02:12 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-29 23:04:45 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | -0.020 |  |
| 2026-08-29 22:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-08-29 23:06:26 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-29 23:09:14 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.044 |  |
| 2026-08-29 23:02:59 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.058 |  |
| 2026-08-29 23:06:50 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.392 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)