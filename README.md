# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_14:05:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,131 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 14:05:02 | Panadugama (Nilwala Ganga) | 5.29 | 🟡 Alert | -0.041 |  |
| 2026-10-30 14:04:57 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:04:09 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:04:03 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-30 14:03:42 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:35 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:02:57 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.021 |  |
| 2026-10-30 14:02:51 | Putupaula (Kalu Ganga) | 3.29 | 🟡 Alert | -0.020 |  |
| 2026-10-30 14:02:50 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:02:41 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:02:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 14:02:13 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:02:05 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 14:01:38 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 14:01:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:01:18 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-30 14:01:12 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.207 |  |
| 2026-10-30 14:01:08 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 14:01:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.012 |  |
| 2026-10-30 14:00:53 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:00:37 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:00:35 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:00:22 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 14:00:02 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:29:24 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 14:00:22 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 13:12:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | -0.051 |  |
| 2026-10-30 14:02:51 | Putupaula (Kalu Ganga) | 3.29 | 🟡 Alert | -0.020 |  |
| 2026-10-30 14:05:02 | Panadugama (Nilwala Ganga) | 5.29 | 🟡 Alert | -0.041 |  |
| 2026-10-30 14:03:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-30 14:01:08 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 14:02:05 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 14:01:38 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-30 14:02:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 14:04:03 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:00:50 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:01:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:00:37 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:00:02 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:20:09 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:08:26 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:42 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-30 13:09:14 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:02:41 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:37 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:03:35 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:02:50 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 14:04:57 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:03:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:05:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:00:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:02:13 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:04:09 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-30 14:00:53 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:01:18 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:05:31 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-30 13:03:47 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-10-30 14:01:03 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.012 |  |
| 2026-10-30 14:01:18 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-30 13:02:58 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-10-30 14:02:57 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.021 |  |
| 2026-10-30 13:07:24 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.030 |  |
| 2026-10-30 13:04:13 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.072 |  |
| 2026-10-30 14:01:12 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)