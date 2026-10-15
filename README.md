# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_04:05:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 04:05:21 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-10-16 04:05:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2026-10-16 04:04:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:04:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-16 04:04:20 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2026-10-16 04:04:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:03:49 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.115 |  |
| 2026-10-16 04:03:49 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:03:31 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-16 04:03:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:02:20 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.106 |  |
| 2026-10-16 04:02:19 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-10-16 04:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-10-16 04:02:03 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.82 | 🟡 Alert | -0.010 |  |
| 2026-10-16 04:01:40 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.061 |  |
| 2026-10-16 04:01:19 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:00:47 | Moraketiya (Walawe Ganga) | 2.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-16 04:00:41 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-10-16 03:51:06 | Thawalama (Gin Ganga) | 3.55 | 🟢 Normal | -0.125 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 03:05:31 | Panadugama (Nilwala Ganga) | 6.66 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-10-16 03:04:29 | Thalgahagoda (Nilwala Ganga) | 1.92 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-16 04:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.82 | 🟡 Alert | -0.010 |  |
| 2026-10-16 03:02:47 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | -0.020 |  |
| 2026-10-16 03:05:40 | Pitabeddara (Nilwala Ganga) | 4.40 | 🟡 Alert | -0.081 |  |
| 2026-10-16 03:06:02 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-16 04:04:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 03:06:38 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-16 04:00:47 | Moraketiya (Walawe Ganga) | 2.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 03:06:29 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:03:29 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:01:19 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:02:03 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:04:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:03:49 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 04:04:15 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:01:55 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-16 03:15:19 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-10-16 04:03:31 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-16 04:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.012 |  |
| 2026-10-16 03:04:07 | Putupaula (Kalu Ganga) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-10-16 03:04:58 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | -0.020 |  |
| 2026-10-16 03:02:38 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-16 04:02:13 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-10-16 04:02:19 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-10-16 04:05:21 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-10-16 04:05:15 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2026-10-16 03:01:30 | Giriulla (Maha Oya) | 2.21 | 🟢 Normal | -0.031 |  |
| 2026-10-16 03:07:58 | Hanwella (Kelani Ganga) | 3.81 | 🟢 Normal | -0.036 |  |
| 2026-10-16 03:04:14 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.043 |  |
| 2026-10-16 04:04:20 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.049 |  |
| 2026-10-16 04:01:40 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | -0.061 |  |
| 2026-10-16 04:02:20 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.106 |  |
| 2026-10-16 04:03:49 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.115 |  |
| 2026-10-16 03:04:55 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-10-16 03:51:06 | Thawalama (Gin Ganga) | 3.55 | 🟢 Normal | -0.125 |  |

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)