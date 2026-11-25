# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_19:28:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,573 measurements** from **39** stations.
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
| 2026-11-25 19:28:18 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.007 |  |
| 2026-11-25 19:13:16 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.027 |  |
| 2026-11-25 19:13:11 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.052 |  |
| 2026-11-25 19:08:42 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-25 19:07:45 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:07:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-25 19:06:51 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-25 19:06:32 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-25 19:05:49 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.048 |  |
| 2026-11-25 19:05:42 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-25 19:05:33 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-11-25 19:04:56 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-25 19:04:48 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.067 |  |
| 2026-11-25 19:04:33 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-25 19:04:30 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-25 19:04:27 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.052 |  |
| 2026-11-25 19:04:04 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.211 |  |
| 2026-11-25 19:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 19:03:36 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-11-25 19:03:27 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.096 |  |
| 2026-11-25 19:03:24 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-25 19:03:06 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:03:00 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-25 19:02:41 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:02:26 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:02:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-25 19:01:57 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:01:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-25 19:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 19:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-11-25 19:01:23 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:01:09 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 19:01:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.085 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 19:05:33 | Glencourse (Kelani Ganga) | 10.64 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-11-25 19:08:42 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-11-25 19:01:40 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-11-25 19:03:24 | Magura (Kalu Ganga) | 2.90 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-25 19:04:30 | Dunamale (Aththanagalu Oya) | 2.90 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-25 18:02:46 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-25 19:03:00 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-25 19:02:10 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-25 19:04:33 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-25 19:06:32 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-25 18:02:35 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-25 19:07:01 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-25 18:00:42 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-25 19:01:09 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 19:04:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 19:01:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 18:15:44 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:01:57 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-25 19:28:18 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.007 |  |
| 2026-11-25 19:07:45 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:02:26 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:01:23 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-25 19:03:36 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-11-25 19:04:56 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-25 19:02:41 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-25 19:03:06 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 19:13:16 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.027 |  |
| 2026-11-25 19:06:51 | Giriulla (Maha Oya) | 2.17 | 🟢 Normal | -0.028 |  |
| 2026-11-25 19:05:42 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-25 19:01:09 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-11-25 19:05:49 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | -0.048 |  |
| 2026-11-25 19:01:29 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.051 |  |
| 2026-11-25 19:04:27 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.052 |  |
| 2026-11-25 19:13:11 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.052 |  |
| 2026-11-25 19:04:48 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.067 |  |
| 2026-11-25 19:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.085 |  |
| 2026-11-25 19:03:27 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.096 |  |
| 2026-11-25 19:04:04 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.211 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)