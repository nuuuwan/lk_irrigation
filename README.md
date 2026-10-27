# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_16:16:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,514 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 16:16:48 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:16:34 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-27 16:15:50 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-27 16:10:11 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.061 |  |
| 2026-10-27 16:07:35 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.124 |  |
| 2026-10-27 16:06:03 | Badalgama (Maha Oya) | 4.41 | 🟢 Normal | -0.116 |  |
| 2026-10-27 16:06:03 | Thawalama (Gin Ganga) | 3.03 | 🟢 Normal | -0.067 |  |
| 2026-10-27 16:05:59 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:05:34 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | -0.114 |  |
| 2026-10-27 16:05:25 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.057 |  |
| 2026-10-27 16:05:11 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-10-27 16:05:01 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.049 |  |
| 2026-10-27 16:05:01 | Rathnapura (Kalu Ganga) | 8.02 | 🟠 Minor Flood | -0.081 |  |
| 2026-10-27 16:04:54 | Moragaswewa (Deduru Oya) | 4.88 | 🟡 Alert | -0.077 |  |
| 2026-10-27 16:04:36 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 16:04:34 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 16:04:23 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-10-27 16:04:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-27 16:04:18 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-10-27 16:03:56 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-10-27 16:03:56 | Hanwella (Kelani Ganga) | 5.63 | 🟢 Normal | -0.118 |  |
| 2026-10-27 16:03:51 | Putupaula (Kalu Ganga) | 3.38 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 16:03:48 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:03:41 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:03:39 | Ellagawa (Kalu Ganga) | 10.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 16:03:39 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 16:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 16:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:03:15 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-27 16:03:03 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:02:57 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:02:38 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:02:22 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:02:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-10-27 16:02:15 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:02:04 | Magura (Kalu Ganga) | 4.93 | 🟡 Alert | -0.090 |  |
| 2026-10-27 16:01:57 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.121 |  |
| 2026-10-27 16:01:38 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:01:31 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 16:01:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 16:03:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.60 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 16:15:50 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.017 | 🔺 Rising |
| 2026-10-27 16:03:39 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 16:04:34 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -0.029 |  |
| 2026-10-27 16:05:01 | Rathnapura (Kalu Ganga) | 8.02 | 🟠 Minor Flood | -0.081 |  |
| 2026-10-27 16:03:39 | Ellagawa (Kalu Ganga) | 10.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-27 16:04:36 | Thalgahagoda (Nilwala Ganga) | 1.63 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-10-27 16:03:51 | Putupaula (Kalu Ganga) | 3.38 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 16:04:54 | Moragaswewa (Deduru Oya) | 4.88 | 🟡 Alert | -0.077 |  |
| 2026-10-27 16:02:04 | Magura (Kalu Ganga) | 4.93 | 🟡 Alert | -0.090 |  |
| 2026-10-27 16:16:34 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-27 16:01:31 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 16:03:48 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:02:22 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:02:38 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:05:59 | Galgamuwa (Mee Oya) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:03:03 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:16:48 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 16:04:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-27 16:02:57 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:03:22 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:02:15 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:03:41 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:01:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-27 16:03:15 | Deraniyagala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-27 16:04:23 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-10-27 16:02:18 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.031 |  |
| 2026-10-27 16:03:56 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-10-27 16:04:18 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-10-27 16:05:01 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.049 |  |
| 2026-10-27 16:05:11 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.054 |  |
| 2026-10-27 16:05:25 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.057 |  |
| 2026-10-27 16:10:11 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.061 |  |
| 2026-10-27 16:06:03 | Thawalama (Gin Ganga) | 3.03 | 🟢 Normal | -0.067 |  |
| 2026-10-27 16:05:34 | Thanthirimale (Malwathu Oya) | 3.00 | 🟢 Normal | -0.114 |  |
| 2026-10-27 16:06:03 | Badalgama (Maha Oya) | 4.41 | 🟢 Normal | -0.116 |  |
| 2026-10-27 16:03:56 | Hanwella (Kelani Ganga) | 5.63 | 🟢 Normal | -0.118 |  |
| 2026-10-27 16:01:57 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.121 |  |
| 2026-10-27 16:07:35 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)