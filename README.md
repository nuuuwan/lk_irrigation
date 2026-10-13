# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_13:24:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 13:24:50 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-10-13 13:20:29 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.008 |  |
| 2026-10-13 13:12:06 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:11:25 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.083 |  |
| 2026-10-13 13:10:50 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:09:44 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.017 |  |
| 2026-10-13 13:07:55 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-10-13 13:07:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | -0.028 |  |
| 2026-10-13 13:07:12 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:07:09 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -1.385 |  |
| 2026-10-13 13:07:08 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:06:46 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:06:43 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -1.385 |  |
| 2026-10-13 13:06:13 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.126 |  |
| 2026-10-13 13:05:44 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.049 |  |
| 2026-10-13 13:05:27 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.053 |  |
| 2026-10-13 13:05:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2026-10-13 13:05:04 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-13 13:04:01 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:04:00 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:03:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.099 |  |
| 2026-10-13 13:03:39 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:03:38 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-13 13:03:23 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 13:02:54 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.684 | 🔺 Rising |
| 2026-10-13 13:02:52 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.020 |  |
| 2026-10-13 13:02:44 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-13 13:02:44 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.050 |  |
| 2026-10-13 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.062 |  |
| 2026-10-13 13:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:01:47 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:46 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:41 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.054 |  |
| 2026-10-13 13:01:26 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 13:03:23 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 13:07:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | -0.028 |  |
| 2026-10-13 13:01:41 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.054 |  |
| 2026-10-13 13:02:54 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.684 | 🔺 Rising |
| 2026-10-13 13:05:04 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-13 13:03:38 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-13 13:00:08 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 13:01:47 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:46 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:07:12 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:10:50 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:26 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:07:08 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:00:43 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:03:39 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:04:01 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:12:06 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:20:29 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.008 |  |
| 2026-10-13 13:06:46 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:02:08 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:04:00 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-13 13:24:50 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.016 |  |
| 2026-10-13 13:09:44 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.017 |  |
| 2026-10-13 13:00:32 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-10-13 13:02:44 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-13 13:02:52 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.020 |  |
| 2026-10-13 13:05:44 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.049 |  |
| 2026-10-13 13:02:44 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.050 |  |
| 2026-10-13 13:05:27 | Ellagawa (Kalu Ganga) | 7.10 | 🟢 Normal | -0.053 |  |
| 2026-10-13 13:02:35 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | -0.062 |  |
| 2026-10-13 13:11:25 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.083 |  |
| 2026-10-13 13:07:55 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.088 |  |
| 2026-10-13 13:05:05 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.097 |  |
| 2026-10-13 13:03:41 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.099 |  |
| 2026-10-13 13:06:13 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | -0.126 |  |
| 2026-10-13 13:07:09 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -1.385 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)