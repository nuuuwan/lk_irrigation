# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_05:28:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 05:28:16 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.192 |  |
| 2026-10-17 05:24:32 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.050 |  |
| 2026-10-17 05:19:21 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -4.909 |  |
| 2026-10-17 05:18:59 | Panadugama (Nilwala Ganga) | 6.26 | 🟠 Minor Flood | -4.909 |  |
| 2026-10-17 05:14:49 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.088 |  |
| 2026-10-17 05:14:25 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 05:12:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.000 |  |
| 2026-10-17 05:07:43 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 05:07:14 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | -0.044 |  |
| 2026-10-17 05:06:40 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.032 |  |
| 2026-10-17 05:06:38 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 05:05:21 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-17 05:05:14 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.125 |  |
| 2026-10-17 05:04:56 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-10-17 05:04:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-17 05:04:48 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.042 |  |
| 2026-10-17 05:04:14 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-17 05:04:12 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 05:04:11 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-17 05:04:11 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.020 |  |
| 2026-10-17 05:03:53 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.111 |  |
| 2026-10-17 05:03:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.069 |  |
| 2026-10-17 05:03:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-10-17 05:03:39 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | 0.039 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 05:00:27 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.103 | 🔺 Rising |
| 2026-10-17 05:19:21 | Panadugama (Nilwala Ganga) | 6.23 | 🟠 Minor Flood | -4.909 |  |
| 2026-10-17 05:12:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.000 |  |
| 2026-10-17 05:04:11 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.020 |  |
| 2026-10-17 05:05:21 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-16 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-17 05:03:39 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-17 05:01:42 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 05:02:34 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 05:02:49 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 05:14:25 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-16 18:01:05 | Thanthirimale (Malwathu Oya) | 1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 05:07:43 | Baddegama (Gin Ganga) | 3.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-17 05:01:59 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-17 05:06:38 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 05:04:12 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-17 04:35:18 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.007 |  |
| 2026-10-17 04:17:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-10-17 05:04:50 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-17 05:00:18 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-17 05:01:35 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-10-17 05:03:15 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2026-10-17 05:04:14 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-10-17 05:04:56 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-10-16 18:02:38 | Galgamuwa (Mee Oya) | 2.02 | 🟢 Normal | -0.023 |  |
| 2026-10-17 05:06:40 | Urawa (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.032 |  |
| 2026-10-17 05:00:12 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2026-10-17 05:04:48 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.042 |  |
| 2026-10-17 05:07:14 | Moragaswewa (Deduru Oya) | 1.72 | 🟢 Normal | -0.044 |  |
| 2026-10-17 05:01:05 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.049 |  |
| 2026-10-17 05:24:32 | Magura (Kalu Ganga) | 3.85 | 🟢 Normal | -0.050 |  |
| 2026-10-17 05:03:50 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-10-17 05:04:11 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.060 |  |
| 2026-10-17 05:03:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.069 |  |
| 2026-10-17 05:03:10 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.071 |  |
| 2026-10-17 05:14:49 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.088 |  |
| 2026-10-17 05:03:53 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.111 |  |
| 2026-10-17 05:05:14 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.125 |  |
| 2026-10-17 05:28:16 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)