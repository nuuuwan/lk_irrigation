# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_12:09:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 12:09:04 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 12:08:52 | Rathnapura (Kalu Ganga) | 5.94 | 🟡 Alert | 0.184 | 🔺 Rising |
| 2026-09-24 12:07:18 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 12:07:05 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 12:06:58 | Peradeniya (Mahaweli Ganga) | 4.41 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-24 12:06:58 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 12:05:49 | Baddegama (Gin Ganga) | 4.31 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 12:05:20 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 12:05:03 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 12:03:54 | Urawa (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.102 |  |
| 2026-09-24 12:03:52 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:52 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-24 12:03:49 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-24 12:03:45 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 12:03:37 | Holombuwa (Kelani Ganga) | 2.08 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-09-24 12:03:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:22 | Deraniyagala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-24 12:03:22 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-24 12:03:21 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:15 | Nawalapitiya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-24 12:03:11 | Glencourse (Kelani Ganga) | 13.29 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-24 12:03:03 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 12:02:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:27 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-09-24 12:02:19 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-24 12:02:14 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:02 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-24 12:01:48 | Pitabeddara (Nilwala Ganga) | 4.61 | 🟡 Alert | -0.139 |  |
| 2026-09-24 12:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:34 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-09-24 12:01:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:08 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:06 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 12:01:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-09-24 12:00:48 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 12:00:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 12:07:18 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 12:05:49 | Baddegama (Gin Ganga) | 4.31 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-24 12:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 12:08:52 | Rathnapura (Kalu Ganga) | 5.94 | 🟡 Alert | 0.184 | 🔺 Rising |
| 2026-09-24 12:02:19 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-24 12:07:05 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-24 12:02:27 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-09-24 12:01:48 | Pitabeddara (Nilwala Ganga) | 4.61 | 🟡 Alert | -0.139 |  |
| 2026-09-24 12:03:37 | Holombuwa (Kelani Ganga) | 2.08 | 🟢 Normal | 0.364 | 🔺 Rising |
| 2026-09-24 12:03:22 | Deraniyagala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-24 12:03:15 | Nawalapitiya (Mahaweli Ganga) | 3.10 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-24 12:03:22 | Kithulgala (Kelani Ganga) | 2.73 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-24 12:06:58 | Peradeniya (Mahaweli Ganga) | 4.41 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-24 12:03:11 | Glencourse (Kelani Ganga) | 13.29 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-24 12:06:58 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-24 12:05:20 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-24 12:03:49 | Ellagawa (Kalu Ganga) | 7.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-24 12:03:52 | Dunamale (Aththanagalu Oya) | 2.66 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-24 12:09:04 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-24 12:02:02 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-24 12:03:45 | Moraketiya (Walawe Ganga) | 1.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 12:00:48 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-24 12:02:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 12:01:06 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 12:03:21 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:00:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:08 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:03 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:05:03 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:32 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:03:52 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:02:14 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-24 12:01:04 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-09-24 12:01:34 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.030 |  |
| 2026-09-24 12:03:54 | Urawa (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)