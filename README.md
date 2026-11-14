# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_16:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 16:02:58 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:43 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2026-11-14 16:02:37 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:33 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:02:33 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:02:31 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 16:02:30 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:20 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.101 |  |
| 2026-11-14 16:01:56 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:01:49 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.029 |  |
| 2026-11-14 16:01:46 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.031 |  |
| 2026-11-14 16:01:38 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:13 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:09 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:01:01 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:55 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:00:36 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:18 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:15 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 16:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-11-14 15:14:16 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:13:02 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 15:09:35 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 16:01:46 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.031 |  |
| 2026-11-14 15:05:09 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-14 16:00:15 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-14 15:07:59 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-14 16:02:31 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 15:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 16:02:58 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:13 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:02:33 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:01 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:01:38 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:30 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:18 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:37 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:36 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:03:06 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-14 15:09:40 | Urawa (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:02:20 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-11-14 16:00:55 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:01:44 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:02:14 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-11-14 16:01:56 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-11-14 15:05:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:02:33 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:01:09 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-11-14 16:02:33 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:07:35 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-14 15:02:15 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | -0.021 |  |
| 2026-11-14 16:00:10 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | -0.021 |  |
| 2026-11-14 15:01:01 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.024 |  |
| 2026-11-14 16:01:49 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.029 |  |
| 2026-11-14 15:03:21 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.041 |  |
| 2026-11-14 15:03:55 | Putupaula (Kalu Ganga) | 1.34 | 🟢 Normal | -0.045 |  |
| 2026-11-14 16:02:43 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:05:53 | Baddegama (Gin Ganga) | 3.41 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:04:56 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.051 |  |
| 2026-11-14 15:01:19 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.071 |  |
| 2026-11-14 16:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)