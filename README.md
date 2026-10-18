# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_07:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,056 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 07:22:58 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-18 07:19:36 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.170 |  |
| 2026-10-18 07:15:56 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.081 |  |
| 2026-10-18 07:13:23 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:10:00 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-10-18 07:09:59 | Thalgahagoda (Nilwala Ganga) | 2.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-18 07:09:43 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-10-18 07:08:35 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-18 07:08:01 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-18 07:08:00 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-10-18 07:06:29 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.171 |  |
| 2026-10-18 07:06:12 | Thawalama (Gin Ganga) | 3.46 | 🟢 Normal | -0.186 |  |
| 2026-10-18 07:05:32 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-10-18 07:05:25 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.178 |  |
| 2026-10-18 07:05:09 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-18 07:04:35 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.202 |  |
| 2026-10-18 07:04:30 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.151 |  |
| 2026-10-18 07:04:17 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.087 |  |
| 2026-10-18 07:04:01 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.054 |  |
| 2026-10-18 07:03:54 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.053 |  |
| 2026-10-18 07:03:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:03:45 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-10-18 07:03:34 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.135 |  |
| 2026-10-18 07:03:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:03:21 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:02:58 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 07:02:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.040 |  |
| 2026-10-18 07:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:02:40 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-18 07:02:36 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-10-18 07:02:27 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-10-18 07:02:12 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 07:02:09 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-18 07:01:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-18 07:01:10 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 07:09:59 | Thalgahagoda (Nilwala Ganga) | 2.04 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-18 07:22:58 | Panadugama (Nilwala Ganga) | 6.03 | 🟠 Minor Flood | -0.037 |  |
| 2026-10-18 07:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | -0.040 |  |
| 2026-10-18 07:05:09 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-18 07:08:35 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-18 07:02:09 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-18 07:08:01 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-18 07:02:12 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 07:02:58 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 07:02:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:13:23 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:03:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:03:21 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:01:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 07:02:54 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:03:25 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:01:10 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-18 07:02:27 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-10-18 07:02:40 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-10-18 07:05:32 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-10-18 07:02:36 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-10-18 07:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-10-18 07:03:45 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-10-18 07:10:00 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-10-18 07:08:00 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.040 |  |
| 2026-10-18 07:09:43 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-10-18 07:03:54 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.053 |  |
| 2026-10-18 07:04:01 | Holombuwa (Kelani Ganga) | 1.29 | 🟢 Normal | -0.054 |  |
| 2026-10-18 07:15:56 | Urawa (Nilwala Ganga) | 1.48 | 🟢 Normal | -0.081 |  |
| 2026-10-18 07:04:17 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.087 |  |
| 2026-10-18 07:03:34 | Weraganthota (Mahaweli Ganga) | -2.36 | 🟢 Normal | -0.135 |  |
| 2026-10-18 07:04:30 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.151 |  |
| 2026-10-18 07:19:36 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.170 |  |
| 2026-10-18 07:06:29 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.171 |  |
| 2026-10-18 07:05:25 | Glencourse (Kelani Ganga) | 11.96 | 🟢 Normal | -0.178 |  |
| 2026-10-18 07:06:12 | Thawalama (Gin Ganga) | 3.46 | 🟢 Normal | -0.186 |  |
| 2026-10-18 07:04:35 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.202 |  |
| 2026-10-18 06:06:17 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.286 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)