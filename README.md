# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_19:28:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,014 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 19:28:00 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.007 |  |
| 2026-09-13 19:20:34 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:20:32 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:14:39 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.042 |  |
| 2026-09-13 19:13:01 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-13 19:12:07 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 19:11:40 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.089 |  |
| 2026-09-13 19:08:44 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:07:14 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 19:07:03 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-13 19:06:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-09-13 19:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 19:06:06 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:05:55 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.048 |  |
| 2026-09-13 19:05:07 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.058 |  |
| 2026-09-13 19:05:02 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:04:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:04:33 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.142 |  |
| 2026-09-13 19:04:32 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-09-13 19:04:01 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:03:54 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:03:02 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:56 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:52 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 19:02:36 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -1.884 |  |
| 2026-09-13 19:02:34 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-13 19:02:31 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:13 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-09-13 19:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:29 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:26 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:25 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:16 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |
| 2026-09-13 19:01:05 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 19:00:47 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 19:06:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-09-13 19:13:01 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-13 19:01:05 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-13 19:12:07 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 19:02:52 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 19:06:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 19:07:14 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:56 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:00:47 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:20:32 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:20:34 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:03:54 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:26 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:31 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:05:02 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:02:16 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:04:01 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:04:44 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:06:06 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:08:44 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:16 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:01:25 | Thanamalwila (Kirindi Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 19:28:00 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.007 |  |
| 2026-09-13 19:07:03 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-09-13 19:02:34 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-09-13 19:04:32 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.028 |  |
| 2026-09-13 19:02:13 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | -0.030 |  |
| 2026-09-13 19:14:39 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.042 |  |
| 2026-09-13 19:05:55 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.048 |  |
| 2026-09-13 19:05:07 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.058 |  |
| 2026-09-13 19:11:40 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | -0.089 |  |
| 2026-09-13 19:04:33 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.142 |  |
| 2026-09-13 19:01:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.153 |  |
| 2026-09-13 19:02:36 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -1.884 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)