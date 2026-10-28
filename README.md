# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_14:29:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Urawa — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 14:29:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:13:31 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | 0.154 | 🔺 Rising |
| 2026-10-28 14:09:52 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.048 |  |
| 2026-10-28 14:09:46 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.026 |  |
| 2026-10-28 14:07:56 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 14:07:41 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | -0.057 |  |
| 2026-10-28 14:06:52 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-10-28 14:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.72 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-28 14:06:40 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-28 14:06:37 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 14:06:37 | Putupaula (Kalu Ganga) | 3.67 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 14:05:49 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:05:17 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:35 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:32 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:30 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-28 14:04:27 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:23 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 14:04:11 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | -0.010 |  |
| 2026-10-28 14:03:52 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:03:48 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 14:03:44 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:03:38 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-10-28 14:03:36 | Rathnapura (Kalu Ganga) | 6.15 | 🟡 Alert | -0.061 |  |
| 2026-10-28 14:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:02:57 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-10-28 14:02:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 14:02:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 14:02:36 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.039 |  |
| 2026-10-28 14:02:35 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 14:04:23 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 14:06:37 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 14:06:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.72 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-28 14:13:31 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | 0.154 | 🔺 Rising |
| 2026-10-28 14:06:52 | Panadugama (Nilwala Ganga) | 5.91 | 🟡 Alert | 0.053 | 🔺 Rising |
| 2026-10-28 14:06:37 | Putupaula (Kalu Ganga) | 3.67 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 14:04:11 | Ellagawa (Kalu Ganga) | 10.42 | 🟡 Alert | -0.010 |  |
| 2026-10-28 14:02:36 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.039 |  |
| 2026-10-28 14:03:36 | Rathnapura (Kalu Ganga) | 6.15 | 🟡 Alert | -0.061 |  |
| 2026-10-28 14:01:55 | Dunamale (Aththanagalu Oya) | 3.55 | 🟡 Alert | -0.073 |  |
| 2026-10-28 14:02:06 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-10-28 14:02:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 14:04:30 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-28 14:06:40 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-28 14:07:56 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 14:00:50 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 14:02:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 14:03:48 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 14:00:15 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:29:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:32 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:27 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:05:17 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:04:35 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:01:38 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:02:12 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-28 14:03:52 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:03:44 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:05:49 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-10-28 14:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-28 13:07:24 | Galgamuwa (Mee Oya) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-28 14:03:38 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-10-28 14:09:46 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.026 |  |
| 2026-10-28 14:02:35 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.032 |  |
| 2026-10-28 14:09:52 | Thawalama (Gin Ganga) | 3.36 | 🟢 Normal | -0.048 |  |
| 2026-10-28 14:02:34 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-10-28 14:07:41 | Thanthirimale (Malwathu Oya) | 2.06 | 🟢 Normal | -0.057 |  |
| 2026-10-28 14:02:57 | Horowpothana (Yan Oya) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-10-28 14:00:10 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)