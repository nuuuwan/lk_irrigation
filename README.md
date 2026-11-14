# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_21:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,927 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 21:12:12 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | -0.027 |  |
| 2026-11-14 21:11:35 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.025 |  |
| 2026-11-14 21:08:05 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:07:01 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.038 |  |
| 2026-11-14 21:06:48 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:06:47 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:06:40 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-11-14 21:05:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:05:28 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:04:56 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-14 21:04:44 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:04:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.057 |  |
| 2026-11-14 21:04:34 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-14 21:04:30 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | -0.032 |  |
| 2026-11-14 21:04:22 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-11-14 21:04:12 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:04:02 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.039 |  |
| 2026-11-14 21:03:48 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.040 |  |
| 2026-11-14 21:03:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-11-14 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:03:10 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:03 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:59 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-14 21:02:56 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-14 21:02:50 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-14 21:02:39 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-14 21:02:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:11 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |
| 2026-11-14 21:02:01 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:01:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-14 21:01:32 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:22 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 21:00:22 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 21:04:30 | Panadugama (Nilwala Ganga) | 5.16 | 🟡 Alert | -0.032 |  |
| 2026-11-14 21:02:50 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-14 21:02:39 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-14 21:04:56 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-14 21:01:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 21:05:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:05:28 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:03:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:48 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:01:32 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:08:05 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:11 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:04:44 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:10 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:06:47 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:03:03 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:01 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:56 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:04:12 | Ellagawa (Kalu Ganga) | 5.87 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:06:40 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 21:04:22 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-11-14 21:03:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-11-14 21:04:34 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-14 21:02:59 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-14 21:11:35 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.025 |  |
| 2026-11-14 21:12:12 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | -0.027 |  |
| 2026-11-14 21:02:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-14 21:07:01 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.038 |  |
| 2026-11-14 21:04:02 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.039 |  |
| 2026-11-14 21:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | -0.040 |  |
| 2026-11-14 21:04:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.057 |  |
| 2026-11-14 21:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)