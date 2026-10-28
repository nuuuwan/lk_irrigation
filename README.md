# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_21:12:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,600 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 21:12:01 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:10:54 | Urawa (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.100 |  |
| 2026-10-28 21:07:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-28 21:06:22 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 21:06:17 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-28 21:05:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:05:38 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:05:33 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:05:01 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | -0.055 |  |
| 2026-10-28 21:04:57 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:04:17 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.049 |  |
| 2026-10-28 21:04:16 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-28 21:04:15 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.097 |  |
| 2026-10-28 21:04:06 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:03:53 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:03:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:03:35 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-28 21:03:35 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:03:12 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:03:08 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:03:05 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 21:03:01 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-10-28 21:02:41 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:02:22 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:02:12 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 21:02:07 | Pitabeddara (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.049 |  |
| 2026-10-28 21:02:06 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.134 |  |
| 2026-10-28 21:01:57 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 21:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 21:01:08 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.069 |  |
| 2026-10-28 21:00:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:00:19 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-28 21:00:12 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.042 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 21:03:35 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-28 21:03:08 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:03:35 | Panadugama (Nilwala Ganga) | 6.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 21:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 21:01:57 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-28 20:03:01 | Ellagawa (Kalu Ganga) | 10.38 | 🟡 Alert | -0.020 |  |
| 2026-10-28 21:05:01 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | -0.055 |  |
| 2026-10-28 21:01:08 | Magura (Kalu Ganga) | 4.25 | 🟡 Alert | -0.069 |  |
| 2026-10-28 21:06:17 | Glencourse (Kelani Ganga) | 11.66 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-28 21:04:16 | Peradeniya (Mahaweli Ganga) | 3.17 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-28 21:00:19 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-28 21:06:22 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-28 21:01:46 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-28 21:02:12 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 21:03:05 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 21:05:38 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:00:20 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:12:01 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:05:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:02:22 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:03:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:03:53 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:04:57 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-28 21:05:33 | Thawalama (Gin Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:03:12 | Holombuwa (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-10-28 21:04:06 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:02:41 | Hanwella (Kelani Ganga) | 4.19 | 🟢 Normal | -0.020 |  |
| 2026-10-28 21:03:01 | Giriulla (Maha Oya) | 2.07 | 🟢 Normal | -0.021 |  |
| 2026-10-28 21:07:54 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-10-28 21:00:12 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.042 |  |
| 2026-10-28 21:04:17 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.049 |  |
| 2026-10-28 21:02:07 | Pitabeddara (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.049 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-28 21:04:15 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.097 |  |
| 2026-10-28 21:10:54 | Urawa (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.100 |  |
| 2026-10-28 21:02:06 | Moragaswewa (Deduru Oya) | 2.66 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)