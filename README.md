# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_14:22:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 14:22:59 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-24 14:11:27 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.118 |  |
| 2026-09-24 14:10:06 | Thawalama (Gin Ganga) | 5.34 | 🟡 Alert | -0.009 |  |
| 2026-09-24 14:10:02 | Baddegama (Gin Ganga) | 4.37 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 14:09:44 | Pitabeddara (Nilwala Ganga) | 4.29 | 🟡 Alert | -0.107 |  |
| 2026-09-24 14:08:54 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.199 |  |
| 2026-09-24 14:08:41 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 14:07:38 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 14:07:33 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:06:45 | Panadugama (Nilwala Ganga) | 6.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 14:06:23 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:05:54 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-09-24 14:05:05 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 14:04:59 | Glencourse (Kelani Ganga) | 13.54 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-24 14:04:40 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:04:26 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-24 14:04:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:04:22 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.098 |  |
| 2026-09-24 14:04:01 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-09-24 14:03:25 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-09-24 14:03:25 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-24 14:03:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:03:18 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:03:14 | Nawalapitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-09-24 14:02:56 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:02:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 14:02:44 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-24 14:02:32 | Deraniyagala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.351 |  |
| 2026-09-24 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 14:02:21 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:33 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.026 |  |
| 2026-09-24 14:01:25 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 14:01:19 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:00:18 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 14:10:02 | Baddegama (Gin Ganga) | 4.37 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-09-24 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 14:06:45 | Panadugama (Nilwala Ganga) | 6.72 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 14:03:25 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-09-24 14:22:59 | Magura (Kalu Ganga) | 4.88 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-09-24 14:05:54 | Rathnapura (Kalu Ganga) | 6.01 | 🟡 Alert | 0.000 |  |
| 2026-09-24 14:10:06 | Thawalama (Gin Ganga) | 5.34 | 🟡 Alert | -0.009 |  |
| 2026-09-24 14:09:44 | Pitabeddara (Nilwala Ganga) | 4.29 | 🟡 Alert | -0.107 |  |
| 2026-09-24 14:04:59 | Glencourse (Kelani Ganga) | 13.54 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-24 14:04:26 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-24 14:08:41 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 14:03:25 | Hanwella (Kelani Ganga) | 5.02 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-24 14:02:44 | Dunamale (Aththanagalu Oya) | 2.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-24 14:07:38 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-24 14:05:05 | Ellagawa (Kalu Ganga) | 7.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 14:01:25 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 14:02:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 14:00:18 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 14:03:22 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:00:32 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:02:56 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:56 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:03:18 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 13:11:01 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:07:33 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:04:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:02:21 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:04:40 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:06:23 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:19 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 14:01:33 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.026 |  |
| 2026-09-24 13:01:03 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.030 |  |
| 2026-09-24 14:04:01 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-09-24 14:04:22 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.098 |  |
| 2026-09-24 14:03:14 | Nawalapitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.101 |  |
| 2026-09-24 14:11:27 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.118 |  |
| 2026-09-24 14:08:54 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.199 |  |
| 2026-09-24 14:02:32 | Deraniyagala (Kelani Ganga) | 2.42 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)