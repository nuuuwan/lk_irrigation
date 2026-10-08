# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_20:08:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,556 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 20:08:32 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-08 20:08:01 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-08 20:08:00 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:07:46 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 20:07:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-08 20:07:06 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-08 20:06:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 20:06:36 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-08 20:06:30 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-08 20:06:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-08 20:05:54 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-08 20:05:43 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 20:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-10-08 20:04:59 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:04:39 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.043 |  |
| 2026-10-08 20:04:32 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 20:04:13 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-08 20:04:09 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 20:04:00 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-08 20:03:47 | Holombuwa (Kelani Ganga) | 4.50 | 🟠 Minor Flood | 0.288 | 🔺 Rising |
| 2026-10-08 20:03:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:03:39 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.020 |  |
| 2026-10-08 20:03:32 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-10-08 20:02:58 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-08 20:02:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 20:02:43 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 20:02:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-08 20:02:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:02:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:02:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-08 20:01:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:01:54 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-08 20:01:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 20:01:11 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-08 20:00:53 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-08 19:36:29 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 20:03:47 | Holombuwa (Kelani Ganga) | 4.50 | 🟠 Minor Flood | 0.288 | 🔺 Rising |
| 2026-10-08 19:10:42 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.999 | 🔺 Rising |
| 2026-10-08 20:04:13 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-10-08 20:01:54 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-10-08 20:02:39 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-08 20:07:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-08 20:06:36 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-08 20:00:53 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-08 20:02:14 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-10-08 20:06:30 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-08 20:06:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-08 20:04:00 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-08 20:01:11 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-08 20:05:54 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-08 20:08:01 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-08 20:02:43 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-08 20:04:09 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 20:05:43 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-08 20:06:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-08 20:02:58 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-08 20:02:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 20:01:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 20:04:32 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 20:07:46 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:01:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:04:59 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:07:01 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:02:30 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:02:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 18:02:32 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:08:00 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:03:41 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 20:08:32 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.019 |  |
| 2026-10-08 20:03:39 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.020 |  |
| 2026-10-08 20:07:06 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-10-08 20:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.039 |  |
| 2026-10-08 20:03:32 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | -0.042 |  |
| 2026-10-08 20:04:39 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.043 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)