# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_09:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 09:03:25 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:18 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.137 |  |
| 2026-11-12 09:02:59 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:50 | Thawalama (Gin Ganga) | 4.04 | 🟡 Alert | -0.290 |  |
| 2026-11-12 09:02:48 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:02:36 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-11-12 09:02:10 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:06 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:01:52 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-12 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:00:55 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:00:29 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 09:00:27 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.091 |  |
| 2026-11-12 09:00:13 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-11-12 08:26:10 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.072 |  |
| 2026-11-12 08:16:14 | Moragaswewa (Deduru Oya) | 3.51 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 08:09:10 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 08:12:47 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 08:11:20 | Moraketiya (Walawe Ganga) | 3.88 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-11-12 08:03:56 | Dunamale (Aththanagalu Oya) | 4.24 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-11-12 08:10:29 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:25 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.000 |  |
| 2026-11-12 08:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 08:04:17 | Rathnapura (Kalu Ganga) | 5.42 | 🟡 Alert | -0.030 |  |
| 2026-11-12 08:02:40 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.041 |  |
| 2026-11-12 08:02:38 | Peradeniya (Mahaweli Ganga) | 5.10 | 🟡 Alert | -0.107 |  |
| 2026-11-12 09:02:50 | Thawalama (Gin Ganga) | 4.04 | 🟡 Alert | -0.290 |  |
| 2026-11-12 09:00:29 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:02:59 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 08:01:45 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 08:04:21 | Badalgama (Maha Oya) | 4.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-12 09:02:06 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-12 08:03:43 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:02:48 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 08:02:50 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-12 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:00:13 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:10 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:36 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-11-12 08:16:14 | Moragaswewa (Deduru Oya) | 3.51 | 🟢 Normal | -0.040 |  |
| 2026-11-12 08:09:36 | Thaldena (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.042 |  |
| 2026-11-12 08:02:08 | Katharagama (Menik Ganga) | 0.71 | 🟢 Normal | -0.061 |  |
| 2026-11-12 08:26:10 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.072 |  |
| 2026-11-12 09:00:55 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:01:52 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-12 08:09:18 | Holombuwa (Kelani Ganga) | 1.94 | 🟢 Normal | -0.090 |  |
| 2026-11-12 09:00:27 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.091 |  |
| 2026-11-12 08:01:15 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.135 |  |
| 2026-11-12 09:03:18 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.137 |  |
| 2026-11-12 08:09:35 | Glencourse (Kelani Ganga) | 13.55 | 🟢 Normal | -0.160 |  |
| 2026-11-12 08:06:21 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.242 |  |
| 2026-11-12 08:04:18 | Thanamalwila (Kirindi Oya) | 2.85 | 🟢 Normal | -0.248 |  |
| 2026-11-12 08:07:03 | Kuda Oya (Kirindi Oya) | 2.83 | 🟢 Normal | -0.265 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)