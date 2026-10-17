# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_08:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 08:10:24 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.063 |  |
| 2026-10-17 08:09:55 | Pitabeddara (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.069 |  |
| 2026-10-17 08:08:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:08:12 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.038 |  |
| 2026-10-17 08:08:04 | Panadugama (Nilwala Ganga) | 6.24 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-10-17 08:08:04 | Thanthirimale (Malwathu Oya) | 2.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 08:07:55 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-10-17 08:07:40 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:06:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:06:31 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:06:02 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:05:34 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:04:15 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.025 |  |
| 2026-10-17 08:04:14 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:04:09 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:04:09 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.041 |  |
| 2026-10-17 08:04:06 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.074 |  |
| 2026-10-17 08:03:35 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.109 |  |
| 2026-10-17 08:03:33 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 08:03:22 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.099 |  |
| 2026-10-17 08:03:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.043 |  |
| 2026-10-17 08:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | -0.010 |  |
| 2026-10-17 08:03:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:03:04 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.337 |  |
| 2026-10-17 08:02:49 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-10-17 08:02:38 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-10-17 08:02:32 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:02:26 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.070 |  |
| 2026-10-17 08:01:51 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.119 |  |
| 2026-10-17 08:01:43 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | -0.023 |  |
| 2026-10-17 08:01:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:01:41 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-10-17 08:01:36 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:01:30 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.121 |  |
| 2026-10-17 08:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:01:22 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:00:41 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:00:40 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.027 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 08:08:04 | Panadugama (Nilwala Ganga) | 6.24 | 🟠 Minor Flood | 0.042 | 🔺 Rising |
| 2026-10-17 08:03:33 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 08:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | -0.010 |  |
| 2026-10-17 08:02:38 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.390 | 🔺 Rising |
| 2026-10-17 08:00:40 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-10-17 08:08:04 | Thanthirimale (Malwathu Oya) | 2.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 08:07:40 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:02:32 | Ellagawa (Kalu Ganga) | 7.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:05:34 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 08:01:36 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:08:44 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:04:14 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:06:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:03:08 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:00:41 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-17 08:04:09 | Hanwella (Kelani Ganga) | 3.79 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:01:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-17 08:06:02 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:06:31 | Badalgama (Maha Oya) | 3.39 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:01:22 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-10-17 08:01:41 | Galgamuwa (Mee Oya) | 1.73 | 🟢 Normal | -0.021 |  |
| 2026-10-17 08:07:55 | Putupaula (Kalu Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-10-17 08:01:43 | Moragaswewa (Deduru Oya) | 1.63 | 🟢 Normal | -0.023 |  |
| 2026-10-17 08:04:15 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.025 |  |
| 2026-10-17 08:02:49 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.029 |  |
| 2026-10-17 08:08:12 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.038 |  |
| 2026-10-17 08:04:09 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.041 |  |
| 2026-10-17 08:03:17 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.043 |  |
| 2026-10-17 08:10:24 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.063 |  |
| 2026-10-17 08:09:55 | Pitabeddara (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.069 |  |
| 2026-10-17 08:02:26 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.070 |  |
| 2026-10-17 08:04:06 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.074 |  |
| 2026-10-17 07:22:38 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.078 |  |
| 2026-10-17 08:03:22 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.099 |  |
| 2026-10-17 08:03:35 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.109 |  |
| 2026-10-17 08:01:51 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.119 |  |
| 2026-10-17 08:01:30 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.121 |  |
| 2026-10-17 08:03:04 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)