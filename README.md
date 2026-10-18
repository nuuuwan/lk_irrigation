# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_19:19:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,525 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 19:19:16 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-10-18 19:18:02 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.010 |  |
| 2026-10-18 19:11:51 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.154 |  |
| 2026-10-18 19:11:26 | Norwood (Kelani Ganga) | 1.74 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-10-18 19:09:16 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-18 19:09:13 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 19:08:38 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | -0.028 |  |
| 2026-10-18 19:06:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:06:48 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-18 19:06:27 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-18 19:05:55 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 19:05:42 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.019 |  |
| 2026-10-18 19:05:41 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:05:40 | Rathnapura (Kalu Ganga) | 4.34 | 🟢 Normal | 0.941 | 🔺 Rising |
| 2026-10-18 19:05:23 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-10-18 19:04:57 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:04:54 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:04:03 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-18 19:03:37 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.051 |  |
| 2026-10-18 19:03:20 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.113 |  |
| 2026-10-18 19:03:17 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-18 19:03:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:03:09 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.051 |  |
| 2026-10-18 19:03:03 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.106 |  |
| 2026-10-18 19:03:03 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:02:51 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-10-18 19:02:43 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-10-18 19:02:37 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:02:24 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.070 |  |
| 2026-10-18 19:02:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 19:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-10-18 19:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | -0.030 |  |
| 2026-10-18 19:01:34 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-10-18 19:01:32 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 19:01:07 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:00:36 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:00:30 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 19:01:32 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 19:11:26 | Norwood (Kelani Ganga) | 1.74 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-10-18 19:18:02 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.010 |  |
| 2026-10-18 19:05:40 | Rathnapura (Kalu Ganga) | 4.34 | 🟢 Normal | 0.941 | 🔺 Rising |
| 2026-10-18 19:05:23 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-10-18 19:04:03 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-18 19:09:13 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-18 19:06:27 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-10-18 19:06:48 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-18 19:02:10 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 19:05:55 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 19:03:03 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:00:30 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:01:07 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:03:10 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:04:57 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:06:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 19:19:16 | Magura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.008 |  |
| 2026-10-18 19:09:16 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-18 19:05:41 | Thawalama (Gin Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:04:54 | Dunamale (Aththanagalu Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:02:37 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-10-18 19:05:42 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.019 |  |
| 2026-10-18 19:02:43 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-10-18 19:01:34 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-10-18 19:03:17 | Moragaswewa (Deduru Oya) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-10-18 19:08:38 | Baddegama (Gin Ganga) | 3.09 | 🟢 Normal | -0.028 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 19:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | -0.030 |  |
| 2026-10-18 19:02:51 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 19:03:37 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.051 |  |
| 2026-10-18 19:03:09 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.051 |  |
| 2026-10-18 19:02:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.061 |  |
| 2026-10-18 19:02:24 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.070 |  |
| 2026-10-18 19:03:03 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | -0.106 |  |
| 2026-10-18 19:03:20 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.113 |  |
| 2026-10-18 19:11:51 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)