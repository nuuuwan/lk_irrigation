# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_17:16:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,606 measurements** from **39** stations.
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
| 2026-11-06 17:16:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:13:04 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:09:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:09:29 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:09:13 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.009 |  |
| 2026-11-06 17:08:46 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-06 17:07:45 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:07:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |
| 2026-11-06 17:07:21 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:06:59 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-06 17:05:28 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-11-06 17:04:38 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-06 17:04:35 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:04:32 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:04:11 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:47 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-06 17:03:47 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:41 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:03:40 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:38 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-11-06 17:03:14 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:03 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:55 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-11-06 17:02:54 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:51 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:02:50 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.062 |  |
| 2026-11-06 17:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-11-06 17:02:14 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:01:49 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.047 |  |
| 2026-11-06 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:01:42 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-06 17:01:35 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:27 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | -0.074 |  |
| 2026-11-06 17:01:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-06 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:04 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-06 17:00:57 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-06 17:00:14 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 17:02:46 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.386 | 🔺 Rising |
| 2026-11-06 17:02:55 | Holombuwa (Kelani Ganga) | 2.00 | 🟢 Normal | 0.363 | 🔺 Rising |
| 2026-11-06 17:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-11-06 17:01:42 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-06 17:04:38 | Magura (Kalu Ganga) | 1.97 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-06 17:00:57 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-06 17:01:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-06 17:01:04 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-06 17:03:47 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-06 17:04:35 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:07:21 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:04:32 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 17:06:59 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-06 17:01:35 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:16:54 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:02:54 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:09:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:07:45 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:03 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:47 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:14 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:09:29 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:04:11 | Rathnapura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:38 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:03:40 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 17:08:46 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-11-06 17:09:13 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.009 |  |
| 2026-11-06 17:13:04 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:03:41 | Giriulla (Maha Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:02:14 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-06 17:01:45 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:02:51 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-11-06 17:05:28 | Peradeniya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-11-06 17:00:14 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.032 |  |
| 2026-11-06 17:01:49 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.047 |  |
| 2026-11-06 17:02:50 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.062 |  |
| 2026-11-06 17:01:27 | Moragaswewa (Deduru Oya) | 2.51 | 🟢 Normal | -0.074 |  |
| 2026-11-06 17:07:43 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)