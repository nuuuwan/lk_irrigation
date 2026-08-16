# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_14:10:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,085 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 14:10:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:09:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-16 14:09:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:08:31 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 14:08:19 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-08-16 14:07:55 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.062 |  |
| 2026-08-16 14:07:10 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-16 14:06:18 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:05:49 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:05:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-08-16 14:05:10 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-08-16 14:05:07 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.030 |  |
| 2026-08-16 14:04:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:04:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-16 14:04:15 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-08-16 14:04:13 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:04:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-08-16 14:03:51 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:03:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-16 14:02:59 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-08-16 14:02:46 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:18 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-16 14:02:00 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-16 14:01:52 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:01:33 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:01:31 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 14:01:11 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:00:10 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 14:04:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-16 14:02:52 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-08-16 14:09:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-08-16 14:03:43 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-16 14:07:10 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-16 14:01:31 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 14:08:31 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 14:02:46 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:00:10 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-16 13:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:59 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-16 13:10:04 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:01:33 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:37 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:04:13 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:06:18 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-16 13:03:16 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:10:48 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:03:51 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:09:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:05:49 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:04:56 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-16 13:12:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-16 13:13:21 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:01:52 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-16 14:08:19 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-08-16 14:02:00 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-08-16 14:02:18 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-16 14:05:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-08-16 13:04:40 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-08-16 14:05:10 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-08-16 14:04:15 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-08-16 14:05:07 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.030 |  |
| 2026-08-16 13:04:50 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.032 |  |
| 2026-08-16 14:04:12 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-08-16 13:21:17 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.045 |  |
| 2026-08-16 14:07:55 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)