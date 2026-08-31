# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_22:14:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 22:14:43 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-08-31 22:12:55 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:12:32 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:10:35 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-08-31 22:09:56 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 22:09:22 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 22:08:35 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:08:08 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.062 |  |
| 2026-08-31 22:08:06 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:07:01 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.012 |  |
| 2026-08-31 22:06:52 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.021 |  |
| 2026-08-31 22:06:34 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:06:08 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:57 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:35 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:10 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:53 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-08-31 22:04:47 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:40 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:24 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:20 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:03:01 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-31 22:02:36 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-31 22:02:35 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:02:31 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:02:19 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:02:10 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:02:07 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.036 |  |
| 2026-08-31 22:01:47 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:01:19 | Manampitiya (Mahaweli Ganga) | -0.54 | 🟢 Normal | -0.011 |  |
| 2026-08-31 22:01:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:00:57 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:00:39 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:00:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 22:02:36 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-31 22:09:56 | Glencourse (Kelani Ganga) | 9.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 22:09:22 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:00:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:02:35 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 21:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-08-31 21:04:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:40 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:00:39 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:12:55 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:12:32 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:06:34 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:02:31 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:06:08 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:24 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:10 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:08:06 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:35 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:19 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:04:47 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:05:57 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:08:35 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:01:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 22:10:35 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-08-31 22:03:01 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-31 22:04:53 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-08-31 22:01:19 | Manampitiya (Mahaweli Ganga) | -0.54 | 🟢 Normal | -0.011 |  |
| 2026-08-31 22:07:01 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.012 |  |
| 2026-08-31 22:14:43 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-08-31 22:02:19 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:02:10 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:01:47 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-08-31 22:06:52 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.021 |  |
| 2026-08-31 22:02:07 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.036 |  |
| 2026-08-31 21:17:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.050 |  |
| 2026-08-31 22:08:08 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)