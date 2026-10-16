# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_22:07:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 22:07:33 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | -0.112 |  |
| 2026-10-16 22:06:48 | Thawalama (Gin Ganga) | 3.53 | 🟢 Normal | -0.042 |  |
| 2026-10-16 22:06:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 22:06:05 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-10-16 22:04:30 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-16 22:04:17 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:03:56 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-10-16 22:03:53 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-16 22:03:50 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-16 22:03:40 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-16 22:03:39 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-16 22:03:36 | Moragaswewa (Deduru Oya) | 2.09 | 🟢 Normal | -0.041 |  |
| 2026-10-16 22:03:29 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:03:26 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-16 22:03:25 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.129 |  |
| 2026-10-16 22:03:13 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.169 |  |
| 2026-10-16 22:03:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:02:42 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 22:02:13 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 22:02:00 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-16 22:01:44 | Pitabeddara (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 22:01:23 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-16 22:00:49 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.081 |  |
| 2026-10-16 22:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-10-16 22:00:25 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 21:05:44 | Panadugama (Nilwala Ganga) | 6.39 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 22:01:23 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | -0.023 |  |
| 2026-10-16 22:03:26 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-16 21:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.000 |  |
| 2026-10-16 22:02:00 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-16 22:03:53 | Rathnapura (Kalu Ganga) | 4.14 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-16 22:04:30 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-16 21:04:33 | Urawa (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-16 21:06:36 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-16 22:03:40 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-16 22:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 22:02:13 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 22:01:44 | Pitabeddara (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-16 21:00:50 | Moraketiya (Walawe Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 22:03:50 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 22:06:19 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-16 22:03:29 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:06:05 | Ellagawa (Kalu Ganga) | 7.40 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:14:04 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:02:42 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:04:17 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 22:03:00 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 21:03:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-10-16 21:03:27 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 22:00:48 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-10-16 22:03:39 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-16 21:13:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.025 |  |
| 2026-10-16 22:03:56 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.029 |  |
| 2026-10-16 22:00:25 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.040 |  |
| 2026-10-16 22:03:36 | Moragaswewa (Deduru Oya) | 2.09 | 🟢 Normal | -0.041 |  |
| 2026-10-16 22:06:48 | Thawalama (Gin Ganga) | 3.53 | 🟢 Normal | -0.042 |  |
| 2026-10-16 22:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.055 |  |
| 2026-10-16 22:00:49 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.081 |  |
| 2026-10-16 22:07:33 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | -0.112 |  |
| 2026-10-16 22:03:25 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.129 |  |
| 2026-10-16 22:03:13 | Deraniyagala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)