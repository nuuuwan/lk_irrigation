# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_19:30:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 19:30:45 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:15:12 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | -0.033 |  |
| 2026-10-20 19:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.009 |  |
| 2026-10-20 19:12:54 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.026 |  |
| 2026-10-20 19:10:22 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:09:27 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 19:09:21 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.027 |  |
| 2026-10-20 19:08:54 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:08:24 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.026 |  |
| 2026-10-20 19:06:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-20 19:06:04 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:05:52 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.066 |  |
| 2026-10-20 19:05:38 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-10-20 19:05:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:05:31 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 19:05:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.068 |  |
| 2026-10-20 19:04:37 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-20 19:04:33 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:04:28 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 19:04:15 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.022 |  |
| 2026-10-20 19:04:14 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-20 19:04:11 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.039 |  |
| 2026-10-20 19:04:03 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-20 19:03:55 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-10-20 19:03:45 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:03:36 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 19:03:01 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:02:52 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-20 19:02:42 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:02:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-20 19:02:28 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:01:50 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:01:30 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.040 |  |
| 2026-10-20 19:01:12 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-20 19:01:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 19:00:28 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:57:59 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 19:15:12 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | -0.033 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 19:01:12 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-10-20 19:04:14 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-20 19:02:52 | Moraketiya (Walawe Ganga) | 1.56 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-20 19:01:11 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-20 19:03:36 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-20 19:04:37 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-20 19:02:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-20 19:04:03 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-20 19:06:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-20 19:04:28 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 19:05:31 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 19:09:27 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 19:10:22 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:00:28 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:01:50 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:03:01 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:30:45 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:05:37 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:04:33 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:08:54 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:06:04 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-20 19:12:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.009 |  |
| 2026-10-20 19:02:28 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:03:45 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:02:42 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-20 19:03:55 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | -0.012 |  |
| 2026-10-20 19:05:38 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-10-20 19:04:15 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.022 |  |
| 2026-10-20 19:12:54 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.026 |  |
| 2026-10-20 19:08:24 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.026 |  |
| 2026-10-20 19:09:21 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.027 |  |
| 2026-10-20 19:04:11 | Hanwella (Kelani Ganga) | 2.54 | 🟢 Normal | -0.039 |  |
| 2026-10-20 19:01:30 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.040 |  |
| 2026-10-20 19:05:52 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.066 |  |
| 2026-10-20 19:05:21 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)