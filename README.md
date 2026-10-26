# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_16:35:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,598 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Rathnapura — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Kithulgala — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 16:35:53 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.272 |  |
| 2026-10-26 16:14:06 | Urawa (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.046 |  |
| 2026-10-26 16:10:01 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-10-26 16:09:47 | Badalgama (Maha Oya) | 4.29 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 16:09:24 | Kithulgala (Kelani Ganga) | 3.03 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-10-26 16:08:13 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 16:08:10 | Peradeniya (Mahaweli Ganga) | 5.62 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-10-26 16:06:36 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-10-26 16:06:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:06:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:06:25 | Rathnapura (Kalu Ganga) | 8.07 | 🟠 Minor Flood | 0.105 | 🔺 Rising |
| 2026-10-26 16:05:48 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-26 16:05:43 | Norwood (Kelani Ganga) | 2.38 | 🟡 Alert | -0.010 |  |
| 2026-10-26 16:05:30 | Galgamuwa (Mee Oya) | 4.05 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-26 16:05:21 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.089 |  |
| 2026-10-26 16:05:21 | Holombuwa (Kelani Ganga) | 4.23 | 🟠 Minor Flood | -0.609 |  |
| 2026-10-26 16:05:17 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-26 16:05:17 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-10-26 16:05:10 | Nawalapitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.137 |  |
| 2026-10-26 16:05:03 | Panadugama (Nilwala Ganga) | 5.51 | 🟡 Alert | -0.272 |  |
| 2026-10-26 16:04:39 | Thawalama (Gin Ganga) | 3.66 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-26 16:04:39 | Moragaswewa (Deduru Oya) | 4.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 16:04:37 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-26 16:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-10-26 16:04:16 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 163.636 | 🔺 Rising |
| 2026-10-26 16:04:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:03:54 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 163.636 | 🔺 Rising |
| 2026-10-26 16:03:21 | Glencourse (Kelani Ganga) | 14.68 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-10-26 16:03:07 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-10-26 16:03:04 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 16:03:02 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-26 16:02:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:02:18 | Deraniyagala (Kelani Ganga) | 2.64 | 🟢 Normal | -0.396 |  |
| 2026-10-26 16:02:14 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 16:02:11 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 16:01:55 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:01:14 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:01:09 | Giriulla (Maha Oya) | 4.10 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-10-26 16:01:03 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-26 16:00:53 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.109 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 16:06:25 | Rathnapura (Kalu Ganga) | 8.07 | 🟠 Minor Flood | 0.105 | 🔺 Rising |
| 2026-10-26 16:05:21 | Holombuwa (Kelani Ganga) | 4.23 | 🟠 Minor Flood | -0.609 |  |
| 2026-10-26 16:09:24 | Kithulgala (Kelani Ganga) | 3.03 | 🟡 Alert | 0.127 | 🔺 Rising |
| 2026-10-26 16:10:01 | Magura (Kalu Ganga) | 4.38 | 🟡 Alert | 0.123 | 🔺 Rising |
| 2026-10-26 16:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | 0.110 | 🔺 Rising |
| 2026-10-26 16:03:07 | Dunamale (Aththanagalu Oya) | 3.90 | 🟡 Alert | 0.107 | 🔺 Rising |
| 2026-10-26 16:08:10 | Peradeniya (Mahaweli Ganga) | 5.62 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-10-26 16:05:43 | Norwood (Kelani Ganga) | 2.38 | 🟡 Alert | -0.010 |  |
| 2026-10-26 16:35:53 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.272 |  |
| 2026-10-26 16:04:16 | Moraketiya (Walawe Ganga) | 2.15 | 🟢 Normal | 163.636 | 🔺 Rising |
| 2026-10-26 16:03:21 | Glencourse (Kelani Ganga) | 14.68 | 🟢 Normal | 0.381 | 🔺 Rising |
| 2026-10-26 16:04:37 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-26 16:01:09 | Giriulla (Maha Oya) | 4.10 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-10-26 16:05:17 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-10-26 16:04:39 | Thawalama (Gin Ganga) | 3.66 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-26 16:05:30 | Galgamuwa (Mee Oya) | 4.05 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-26 16:03:04 | Ellagawa (Kalu Ganga) | 9.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 16:09:47 | Badalgama (Maha Oya) | 4.29 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-26 16:01:03 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-26 16:05:48 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-26 16:02:14 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 16:04:39 | Moragaswewa (Deduru Oya) | 4.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-26 16:08:13 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 16:02:11 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 16:06:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:02:19 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:06:29 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:02:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 16:05:17 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-10-26 16:01:55 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:01:14 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:04:14 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-26 16:03:02 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-10-26 16:06:36 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.032 |  |
| 2026-10-26 16:14:06 | Urawa (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.046 |  |
| 2026-10-26 16:05:21 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.089 |  |
| 2026-10-26 16:00:53 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.109 |  |
| 2026-10-26 16:05:10 | Nawalapitiya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.137 |  |
| 2026-10-26 16:02:18 | Deraniyagala (Kelani Ganga) | 2.64 | 🟢 Normal | -0.396 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)