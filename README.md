# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_13:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,150 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 13:17:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:15:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.00 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-11-09 13:08:32 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:08:00 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:07:40 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-11-09 13:07:28 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-11-09 13:06:48 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-09 13:06:35 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-09 13:06:19 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 13:05:23 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.105 |  |
| 2026-11-09 13:05:13 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:04:59 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-09 13:03:54 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -0.053 |  |
| 2026-11-09 13:03:44 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | -0.128 |  |
| 2026-11-09 13:03:41 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:03:40 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.106 |  |
| 2026-11-09 13:03:40 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:03:38 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 13:03:26 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:03:25 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:03:25 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.039 |  |
| 2026-11-09 13:03:24 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 13:03:20 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2026-11-09 13:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-09 13:03:15 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 13:02:54 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | -0.030 |  |
| 2026-11-09 13:02:47 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.091 |  |
| 2026-11-09 13:02:47 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.054 |  |
| 2026-11-09 13:02:40 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.079 |  |
| 2026-11-09 13:02:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-09 13:02:19 | Giriulla (Maha Oya) | 2.79 | 🟢 Normal | -0.061 |  |
| 2026-11-09 13:02:06 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:01:31 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.022 |  |
| 2026-11-09 13:01:09 | Moragaswewa (Deduru Oya) | 2.69 | 🟢 Normal | -0.021 |  |
| 2026-11-09 13:00:51 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-11-09 13:00:43 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:00:42 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-11-09 13:00:27 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.146 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 13:04:59 | Dunamale (Aththanagalu Oya) | 4.45 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-11-09 13:15:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.00 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-11-09 12:07:57 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-11-09 13:03:24 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-09 13:03:54 | Panadugama (Nilwala Ganga) | 5.60 | 🟡 Alert | -0.053 |  |
| 2026-11-09 13:02:47 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.054 |  |
| 2026-11-09 13:02:38 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-09 13:03:38 | Nagalagam Street (Kelani Ganga) | 0.87 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-09 13:03:15 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 13:06:19 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-09 13:08:32 | Horowpothana (Yan Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-09 12:06:05 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:17:32 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:03:25 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:08:00 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-09 13:07:40 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-11-09 13:03:26 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:02:06 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:03:41 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:00:43 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:03:40 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-11-09 13:06:35 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-09 13:06:48 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.019 |  |
| 2026-11-09 13:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-09 13:01:09 | Moragaswewa (Deduru Oya) | 2.69 | 🟢 Normal | -0.021 |  |
| 2026-11-09 13:01:31 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.022 |  |
| 2026-11-09 13:00:42 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-11-09 13:03:20 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2026-11-09 13:07:28 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.028 |  |
| 2026-11-09 13:02:54 | Moraketiya (Walawe Ganga) | 1.74 | 🟢 Normal | -0.030 |  |
| 2026-11-09 13:00:51 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.032 |  |
| 2026-11-09 13:03:25 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.039 |  |
| 2026-11-09 13:02:19 | Giriulla (Maha Oya) | 2.79 | 🟢 Normal | -0.061 |  |
| 2026-11-09 13:02:40 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.079 |  |
| 2026-11-09 13:02:47 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.091 |  |
| 2026-11-09 13:05:23 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.105 |  |
| 2026-11-09 13:03:40 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.106 |  |
| 2026-11-09 13:03:44 | Hanwella (Kelani Ganga) | 4.24 | 🟢 Normal | -0.128 |  |
| 2026-11-09 13:00:27 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)