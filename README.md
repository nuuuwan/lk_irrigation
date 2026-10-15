# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_03:16:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 03:16:55 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-16 03:15:19 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-10-16 03:15:00 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-16 03:13:37 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:13:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:11:27 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-16 03:11:22 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 03:09:20 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:08:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:07:58 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | -0.036 |  |
| 2026-10-16 03:06:38 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 03:06:29 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 03:06:08 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:06:02 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-16 03:05:40 | Pitabeddara (Nilwala Ganga) | 4.40 | 🟡 Alert | -0.081 |  |
| 2026-10-16 03:05:39 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.057 |  |
| 2026-10-16 03:05:31 | Panadugama (Nilwala Ganga) | 6.66 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-10-16 03:05:28 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 03:04:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.020 |  |
| 2026-10-16 03:04:55 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-10-16 03:04:48 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-16 03:04:29 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 03:04:14 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.043 |  |
| 2026-10-16 03:04:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:04:07 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-16 03:04:03 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-10-16 03:03:32 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-10-16 03:03:15 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-16 03:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | 0.000 |  |
| 2026-10-16 03:02:47 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.020 |  |
| 2026-10-16 03:02:45 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:02:38 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-16 03:02:26 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.022 |  |
| 2026-10-16 03:02:13 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 03:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:01:54 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:01:30 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 03:05:31 | Panadugama (Nilwala Ganga) | 6.66 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-10-16 03:04:29 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 03:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | 0.000 |  |
| 2026-10-16 03:02:47 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.020 |  |
| 2026-10-16 03:05:40 | Pitabeddara (Nilwala Ganga) | 4.40 | 🟡 Alert | -0.081 |  |
| 2026-10-16 03:16:55 | Kithulgala (Kelani Ganga) | 2.24 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-16 03:04:48 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-16 03:06:02 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 03:11:22 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-16 03:06:38 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 03:02:13 | Moragaswewa (Deduru Oya) | 2.96 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 03:05:28 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-16 03:06:29 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:08:21 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:13:37 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:02:45 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:04:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:06:08 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:09:20 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:03:15 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-16 03:15:19 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-10-16 03:04:07 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-16 03:04:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.020 |  |
| 2026-10-16 03:02:38 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-16 03:04:03 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-10-16 03:03:32 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-10-16 03:02:26 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.022 |  |
| 2026-10-16 03:11:27 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.029 |  |
| 2026-10-16 03:01:30 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.031 |  |
| 2026-10-16 03:15:00 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.034 |  |
| 2026-10-16 03:07:58 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | -0.036 |  |
| 2026-10-16 03:04:14 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.043 |  |
| 2026-10-16 03:05:39 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.057 |  |
| 2026-10-16 03:04:55 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-10-16 02:00:47 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | -0.188 |  |

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)