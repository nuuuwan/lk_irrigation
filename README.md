# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_02:33:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 02:33:19 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-14 02:20:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-14 02:17:02 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.014 |  |
| 2026-11-14 02:11:32 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | -0.057 |  |
| 2026-11-14 02:08:51 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 02:06:43 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:06:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:05:33 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.047 |  |
| 2026-11-14 02:04:32 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.039 |  |
| 2026-11-14 02:03:41 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:03:38 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:03:19 | Kuda Oya (Kirindi Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-14 02:03:17 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:03:04 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-14 02:02:50 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-14 02:02:49 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:46 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:31 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:31 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.041 |  |
| 2026-11-14 02:02:31 | Baddegama (Gin Ganga) | 3.85 | 🟡 Alert | -0.031 |  |
| 2026-11-14 02:01:54 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:01:47 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:01:18 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:01:17 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 02:08:51 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 01:06:42 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.020 |  |
| 2026-11-14 02:02:31 | Baddegama (Gin Ganga) | 3.85 | 🟡 Alert | -0.031 |  |
| 2026-11-14 02:09:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.50 | 🟡 Alert | -0.057 |  |
| 2026-11-14 02:20:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-14 02:33:19 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 02:03:41 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:01:54 | Moragaswewa (Deduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:06:43 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:31 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:46 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:02:49 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:11:32 | Ellagawa (Kalu Ganga) | 6.98 | 🟢 Normal | 0.000 |  |
| 2026-11-14 01:02:16 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-14 02:06:03 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-14 00:14:27 | Urawa (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-14 01:31:10 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.007 |  |
| 2026-11-14 02:01:47 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:03:17 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:01:18 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:03:38 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | -0.010 |  |
| 2026-11-14 02:01:17 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-14 01:00:46 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.012 |  |
| 2026-11-14 02:17:02 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.014 |  |
| 2026-11-14 02:03:04 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-14 02:03:19 | Kuda Oya (Kirindi Oya) | 2.21 | 🟢 Normal | -0.020 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-14 00:01:56 | Pitabeddara (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-11-14 02:02:50 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-14 01:02:42 | Putupaula (Kalu Ganga) | 2.13 | 🟢 Normal | -0.031 |  |
| 2026-11-14 02:04:32 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.039 |  |
| 2026-11-14 02:02:31 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.041 |  |
| 2026-11-14 02:05:33 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.047 |  |
| 2026-11-14 01:01:31 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.048 |  |
| 2026-11-14 01:38:19 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.054 |  |
| 2026-11-14 01:21:12 | Moraketiya (Walawe Ganga) | 2.98 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)