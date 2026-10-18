# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_23:30:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 23:30:52 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-18 23:17:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:14:22 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-18 23:13:11 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:10:23 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 23:09:40 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:07:06 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 23:07:04 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-18 23:06:40 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | -0.061 |  |
| 2026-10-18 23:06:06 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 23:06:04 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:06:03 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-18 23:05:11 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.051 |  |
| 2026-10-18 23:05:10 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.098 |  |
| 2026-10-18 23:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:04:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-10-18 23:03:30 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.493 | 🔺 Rising |
| 2026-10-18 23:03:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:03:07 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.080 |  |
| 2026-10-18 23:03:05 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:57 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-18 23:02:30 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-10-18 23:02:17 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:02:14 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-18 23:02:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-10-18 23:02:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-18 23:01:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.050 |  |
| 2026-10-18 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:01:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:00:42 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 23:07:06 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 23:10:23 | Panadugama (Nilwala Ganga) | 5.67 | 🟡 Alert | 0.000 |  |
| 2026-10-18 23:03:07 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.080 |  |
| 2026-10-18 23:03:30 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.493 | 🔺 Rising |
| 2026-10-18 23:06:03 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-18 23:02:14 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-18 23:30:52 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-18 23:06:06 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 23:14:22 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-18 23:02:17 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:23 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:17:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-18 22:11:41 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:01:16 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:13:11 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:03:21 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:02:03 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 23:09:40 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:03:05 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-18 23:02:57 | Moragaswewa (Deduru Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-10-18 22:13:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.60 | 🟢 Normal | -0.017 |  |
| 2026-10-18 23:07:04 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-10-18 23:04:44 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:06:04 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:01:33 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-10-18 23:02:54 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-10-18 23:02:09 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-10-18 23:00:42 | Moraketiya (Walawe Ganga) | 1.77 | 🟢 Normal | -0.025 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 23:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-18 21:03:08 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.043 |  |
| 2026-10-18 23:01:39 | Ellagawa (Kalu Ganga) | 7.32 | 🟢 Normal | -0.050 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 23:05:11 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.051 |  |
| 2026-10-18 23:06:40 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | -0.061 |  |
| 2026-10-18 23:04:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.070 |  |
| 2026-10-18 23:02:30 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.091 |  |
| 2026-10-18 23:05:10 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)