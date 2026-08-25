# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_17:22:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 17:22:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:22:01 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 17:13:36 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-25 17:13:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:09:18 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-08-25 17:08:47 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-25 17:08:01 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:07:58 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.055 |  |
| 2026-08-25 17:07:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:07:16 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 17:06:54 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.083 |  |
| 2026-08-25 17:06:18 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:04:57 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 17:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:04:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 17:04:15 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:04:06 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:04:02 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:58 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:03:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:30 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-25 17:03:02 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:01 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-25 17:02:56 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:42 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:26 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.122 |  |
| 2026-08-25 17:02:05 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-25 17:01:54 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:01:45 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:28 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:22 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:05 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:00:24 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:00:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:00:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 17:13:36 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-25 17:02:58 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-25 17:08:47 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-25 17:04:57 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-25 17:02:05 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-25 17:02:42 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 17:04:43 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 17:04:06 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:01:54 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:03:58 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:07:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:13:26 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 17:07:16 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 17:22:01 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-25 17:01:22 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:00:21 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:26 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:22:30 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:56 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:08 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:02 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 16:05:10 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:28 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:04:15 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:06:18 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:08:01 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:04:02 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:45 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:01:05 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:00:24 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-08-25 17:03:30 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-08-25 17:09:18 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-08-25 17:07:58 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.055 |  |
| 2026-08-25 17:06:54 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.083 |  |
| 2026-08-25 17:02:23 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)