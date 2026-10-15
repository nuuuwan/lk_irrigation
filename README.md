# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_17:06:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 17:06:32 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-15 17:06:21 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:06:11 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.041 |  |
| 2026-10-15 17:05:41 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 17:05:37 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 17:05:31 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.657 |  |
| 2026-10-15 17:05:30 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:04:21 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-15 17:04:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.022 |  |
| 2026-10-15 17:04:11 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.068 |  |
| 2026-10-15 17:03:51 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-10-15 17:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 17:03:41 | Urawa (Nilwala Ganga) | 3.22 | 🟡 Alert | -0.098 |  |
| 2026-10-15 17:03:36 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-10-15 17:03:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 17:03:14 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 17:03:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:02:55 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:02:44 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:02:10 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.010 |  |
| 2026-10-15 17:02:05 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:32 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:02 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:00:48 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:00:45 | Pitabeddara (Nilwala Ganga) | 4.20 | 🟡 Alert | 0.268 | 🔺 Rising |
| 2026-10-15 17:00:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 16:55:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 16:17:01 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 17:00:45 | Pitabeddara (Nilwala Ganga) | 4.20 | 🟡 Alert | 0.268 | 🔺 Rising |
| 2026-10-15 16:06:01 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-10-15 16:08:36 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |
| 2026-10-15 17:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.010 |  |
| 2026-10-15 17:03:41 | Urawa (Nilwala Ganga) | 3.22 | 🟡 Alert | -0.098 |  |
| 2026-10-15 17:03:51 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-10-15 16:04:22 | Thawalama (Gin Ganga) | 3.46 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-15 17:04:21 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-15 16:06:20 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-15 17:06:32 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-15 17:02:10 | Thanthirimale (Malwathu Oya) | 1.41 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 17:05:37 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 17:03:14 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 17:03:32 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 17:05:41 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-15 17:00:20 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 15:03:41 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 17:03:51 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 17:01:02 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:16:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:02:05 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:05:30 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:03:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:03:45 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:14 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:01:18 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-15 17:06:21 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:01:32 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:02:55 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-15 17:02:44 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-15 16:16:10 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.017 |  |
| 2026-10-15 16:05:07 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.020 |  |
| 2026-10-15 17:03:36 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-10-15 17:04:11 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.022 |  |
| 2026-10-15 17:06:11 | Badalgama (Maha Oya) | 3.47 | 🟢 Normal | -0.041 |  |
| 2026-10-15 17:04:11 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.068 |  |
| 2026-10-15 17:05:31 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | -0.657 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)