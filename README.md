# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_06:34:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,966 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 06:34:08 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 06:17:28 | Pitabeddara (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-08 06:13:14 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:13:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:12:50 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-11-08 06:11:18 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.185 |  |
| 2026-11-08 06:09:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-08 06:06:12 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.043 |  |
| 2026-11-08 06:06:08 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 06:05:49 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.013 |  |
| 2026-11-08 06:05:37 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-11-08 06:05:28 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:05:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.085 |  |
| 2026-11-08 06:04:56 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-08 06:04:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:04:04 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-08 06:03:50 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.142 |  |
| 2026-11-08 06:03:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:03:27 | Dunamale (Aththanagalu Oya) | 3.75 | 🟡 Alert | -0.026 |  |
| 2026-11-08 06:03:22 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 06:03:17 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-08 06:03:16 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 06:03:11 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.562 |  |
| 2026-11-08 06:03:10 | Moraketiya (Walawe Ganga) | 3.70 | 🟡 Alert | -0.382 |  |
| 2026-11-08 06:03:08 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.068 |  |
| 2026-11-08 06:02:53 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-11-08 06:02:35 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-08 06:02:19 | Kuda Oya (Kirindi Oya) | 2.63 | 🟢 Normal | -0.588 |  |
| 2026-11-08 06:02:19 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-08 06:02:05 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 06:02:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-11-08 06:01:56 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | -0.119 |  |
| 2026-11-08 06:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.597 | 🔺 Rising |
| 2026-11-08 06:01:35 | Wellawaya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.400 |  |
| 2026-11-08 06:01:21 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:01:17 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.031 |  |
| 2026-11-08 06:01:14 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:00:41 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-08 05:53:38 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 06:12:50 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | 0.073 | 🔺 Rising |
| 2026-11-08 06:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.597 | 🔺 Rising |
| 2026-11-08 06:03:27 | Dunamale (Aththanagalu Oya) | 3.75 | 🟡 Alert | -0.026 |  |
| 2026-11-08 06:03:50 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.142 |  |
| 2026-11-08 06:03:10 | Moraketiya (Walawe Ganga) | 3.70 | 🟡 Alert | -0.382 |  |
| 2026-11-08 06:17:28 | Pitabeddara (Nilwala Ganga) | 2.97 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-11-08 06:04:04 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-08 06:00:41 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-08 06:03:16 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 06:04:56 | Ellagawa (Kalu Ganga) | 7.15 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-08 06:02:19 | Putupaula (Kalu Ganga) | 1.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-08 06:06:08 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 06:34:08 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 06:02:05 | Baddegama (Gin Ganga) | 2.88 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 06:03:17 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-11-08 06:02:35 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-08 06:03:22 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 06:13:11 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:13:14 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:05:28 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:03:43 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:01:14 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:01:21 | Thalgahagoda (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-08 06:09:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 06:02:53 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-11-08 06:05:49 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.013 |  |
| 2026-11-08 06:01:17 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.031 |  |
| 2026-11-08 06:05:37 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-11-08 06:06:12 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.043 |  |
| 2026-11-08 06:02:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.053 |  |
| 2026-11-08 06:03:08 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.068 |  |
| 2026-11-08 06:05:20 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.085 |  |
| 2026-11-08 06:01:56 | Giriulla (Maha Oya) | 3.28 | 🟢 Normal | -0.119 |  |
| 2026-11-08 06:11:18 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | -0.185 |  |
| 2026-11-08 06:01:35 | Wellawaya (Kirindi Oya) | 1.93 | 🟢 Normal | -0.400 |  |
| 2026-11-08 06:03:11 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.562 |  |
| 2026-11-08 06:02:19 | Kuda Oya (Kirindi Oya) | 2.63 | 🟢 Normal | -0.588 |  |
| 2026-11-08 05:11:38 | Thanamalwila (Kirindi Oya) | 2.70 | 🟢 Normal | -0.964 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)