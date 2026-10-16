# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_05:20:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,179 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 05:20:45 | Moraketiya (Walawe Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-10-16 05:15:30 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.016 |  |
| 2026-10-16 05:14:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-10-16 05:14:02 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 05:12:39 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-16 05:11:30 | Dunamale (Aththanagalu Oya) | 3.73 | 🟡 Alert | -0.019 |  |
| 2026-10-16 05:10:31 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-10-16 05:10:01 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 05:08:36 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 05:08:27 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:08:13 | Urawa (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-10-16 05:07:44 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 05:07:05 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-10-16 05:07:03 | Pitabeddara (Nilwala Ganga) | 4.30 | 🟡 Alert | -0.039 |  |
| 2026-10-16 05:06:06 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:06:00 | Thawalama (Gin Ganga) | 3.98 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-16 05:05:50 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.113 |  |
| 2026-10-16 05:05:36 | Magura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.095 |  |
| 2026-10-16 05:05:32 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.023 |  |
| 2026-10-16 05:05:29 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 05:05:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:04:53 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-10-16 05:04:40 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 05:04:39 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.021 |  |
| 2026-10-16 05:03:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-16 05:03:39 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 05:03:24 | Rathnapura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.013 |  |
| 2026-10-16 05:03:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-16 05:02:56 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-16 05:02:46 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.043 |  |
| 2026-10-16 05:02:33 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-16 05:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-16 05:02:08 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-16 05:02:08 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 05:03:39 | Panadugama (Nilwala Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 05:10:01 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 05:14:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2026-10-16 05:11:30 | Dunamale (Aththanagalu Oya) | 3.73 | 🟡 Alert | -0.019 |  |
| 2026-10-16 05:07:03 | Pitabeddara (Nilwala Ganga) | 4.30 | 🟡 Alert | -0.039 |  |
| 2026-10-16 05:06:00 | Thawalama (Gin Ganga) | 3.98 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-16 05:03:09 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 05:12:39 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-16 05:03:41 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-16 05:14:02 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 05:08:36 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 05:04:40 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 05:07:44 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:06:06 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:01:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:05:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:00:18 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:08:27 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 05:07:05 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-10-16 05:05:29 | Glencourse (Kelani Ganga) | 11.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 05:02:08 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-16 05:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-16 05:02:56 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-10-16 05:03:24 | Rathnapura (Kalu Ganga) | 3.66 | 🟢 Normal | -0.013 |  |
| 2026-10-16 05:15:30 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.016 |  |
| 2026-10-16 05:10:31 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-10-16 05:02:33 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-16 05:04:39 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.021 |  |
| 2026-10-16 05:05:32 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | -0.023 |  |
| 2026-10-16 05:04:53 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-10-16 05:20:45 | Moraketiya (Walawe Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-10-16 05:08:13 | Urawa (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.030 |  |
| 2026-10-16 05:02:46 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.043 |  |
| 2026-10-16 05:02:08 | Moragaswewa (Deduru Oya) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-10-16 05:05:36 | Magura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.095 |  |
| 2026-10-16 05:05:50 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)