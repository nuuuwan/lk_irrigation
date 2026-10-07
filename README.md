# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_22:31:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 22:31:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.007 |  |
| 2026-10-07 22:08:39 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-07 22:08:39 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:08:22 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.018 |  |
| 2026-10-07 22:07:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.476 | 🔺 Rising |
| 2026-10-07 22:07:03 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:06:57 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:06:56 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:06:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:06:16 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.065 |  |
| 2026-10-07 22:05:36 | Holombuwa (Kelani Ganga) | 3.12 | 🟡 Alert | 0.658 | 🔺 Rising |
| 2026-10-07 22:05:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:04:39 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-07 22:04:35 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:04:24 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-07 22:03:57 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-10-07 22:03:50 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-07 22:02:59 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:02:43 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-07 22:02:42 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-10-07 22:02:31 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-07 22:02:30 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:02:25 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 22:02:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:02:12 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-07 22:01:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-07 22:01:45 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:01:25 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:01:15 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 22:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:00:53 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:51 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:00:32 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:06 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 22:05:36 | Holombuwa (Kelani Ganga) | 3.12 | 🟡 Alert | 0.658 | 🔺 Rising |
| 2026-10-07 22:07:15 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.476 | 🔺 Rising |
| 2026-10-07 22:02:31 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-10-07 22:02:12 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-07 22:01:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-07 22:04:39 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-07 22:03:50 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-07 22:01:15 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-07 22:08:39 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-07 22:02:25 | Ellagawa (Kalu Ganga) | 5.46 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 22:06:56 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:08:39 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:01:45 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:06:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:02:30 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:32 | Panadugama (Nilwala Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:06:57 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:06 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:05:26 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:00:53 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:08:22 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:02:21 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-07 22:31:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.007 |  |
| 2026-10-07 22:04:24 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-10-07 22:00:51 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:01:25 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:01:10 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-10-07 22:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.018 |  |
| 2026-10-07 22:03:57 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-10-07 22:02:43 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.019 |  |
| 2026-10-07 22:02:59 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:07:03 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:04:35 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-10-07 22:02:42 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-10-07 22:06:16 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)