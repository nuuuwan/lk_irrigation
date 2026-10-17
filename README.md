# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_07:22:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,157 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 07:22:38 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.078 |  |
| 2026-10-17 07:16:30 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-17 07:15:51 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.228 |  |
| 2026-10-17 07:15:00 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:13:02 | Thawalama (Gin Ganga) | 3.04 | 🟢 Normal | -0.052 |  |
| 2026-10-17 07:11:17 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-17 07:11:04 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | -0.016 |  |
| 2026-10-17 07:08:57 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | -0.018 |  |
| 2026-10-17 07:08:51 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 07:08:33 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 07:08:24 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.432 |  |
| 2026-10-17 07:07:52 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.015 | 🔺 Rising |
| 2026-10-17 07:07:42 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:07:31 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 07:07:15 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.157 |  |
| 2026-10-17 07:06:49 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.028 |  |
| 2026-10-17 07:06:49 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | -0.122 |  |
| 2026-10-17 07:05:50 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-17 07:05:33 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | -0.029 |  |
| 2026-10-17 07:05:28 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 07:04:13 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.81 | 🟡 Alert | -0.029 |  |
| 2026-10-17 07:04:05 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:03:59 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-10-17 07:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:03:43 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.070 |  |
| 2026-10-17 07:03:40 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:03:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:03:01 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 07:02:52 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:02:49 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.091 |  |
| 2026-10-17 07:02:21 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:02:12 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-10-17 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-17 07:01:10 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.416 |  |
| 2026-10-17 07:01:09 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:00:53 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:00:36 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:00:11 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.225 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 07:07:52 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.015 | 🔺 Rising |
| 2026-10-17 07:11:04 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | -0.016 |  |
| 2026-10-17 07:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.81 | 🟡 Alert | -0.029 |  |
| 2026-10-17 07:01:23 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-17 07:08:51 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-17 07:05:28 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 07:07:31 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-17 07:05:50 | Moraketiya (Walawe Ganga) | 1.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-17 07:08:33 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-17 07:11:17 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-17 07:16:30 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-17 07:03:01 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 07:03:03 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:04:13 | Galgamuwa (Mee Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:00:36 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:04:05 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 07:15:00 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:07:42 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.009 |  |
| 2026-10-17 07:03:40 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:02:52 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:01:09 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:02:21 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:00:53 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-17 07:08:57 | Moragaswewa (Deduru Oya) | 1.65 | 🟢 Normal | -0.018 |  |
| 2026-10-17 07:03:59 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.019 |  |
| 2026-10-17 07:06:49 | Badalgama (Maha Oya) | 3.41 | 🟢 Normal | -0.028 |  |
| 2026-10-17 07:05:33 | Dunamale (Aththanagalu Oya) | 3.26 | 🟢 Normal | -0.029 |  |
| 2026-10-17 07:02:12 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-10-17 07:13:02 | Thawalama (Gin Ganga) | 3.04 | 🟢 Normal | -0.052 |  |
| 2026-10-17 07:03:43 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.070 |  |
| 2026-10-17 07:22:38 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.078 |  |
| 2026-10-17 07:02:49 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.091 |  |
| 2026-10-17 07:06:49 | Glencourse (Kelani Ganga) | 11.58 | 🟢 Normal | -0.122 |  |
| 2026-10-17 07:07:15 | Rathnapura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.157 |  |
| 2026-10-17 07:00:11 | Pitabeddara (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.225 |  |
| 2026-10-17 07:15:51 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | -0.228 |  |
| 2026-10-17 07:01:10 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.416 |  |
| 2026-10-17 07:08:24 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.432 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)