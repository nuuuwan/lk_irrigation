# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_17:24:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,174 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 17:24:27 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 17:16:57 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:09:16 | Thalgahagoda (Nilwala Ganga) | 1.69 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-11-10 17:09:09 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-10 17:09:03 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.105 |  |
| 2026-11-10 17:08:52 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:08:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 17:08:33 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-11-10 17:08:21 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-10 17:08:05 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.030 |  |
| 2026-11-10 17:07:57 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-10 17:07:38 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.061 |  |
| 2026-11-10 17:07:37 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 17:07:29 | Moragaswewa (Deduru Oya) | 4.01 | 🟢 Normal | -0.088 |  |
| 2026-11-10 17:06:54 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:05:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 17:05:15 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-11-10 17:04:54 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.065 |  |
| 2026-11-10 17:04:40 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-11-10 17:04:35 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:14 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:10 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:03:56 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:03:46 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | -0.041 |  |
| 2026-11-10 17:03:46 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 1.046 | 🔺 Rising |
| 2026-11-10 17:03:38 | Moraketiya (Walawe Ganga) | 3.03 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-10 17:03:33 | Dunamale (Aththanagalu Oya) | 4.55 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-10 17:03:23 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-10 17:03:21 | Hanwella (Kelani Ganga) | 4.76 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-11-10 17:03:19 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.775 | 🔺 Rising |
| 2026-11-10 17:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 17:03:00 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.038 |  |
| 2026-11-10 17:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.121 |  |
| 2026-11-10 17:02:47 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:02:36 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 17:02:20 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.061 |  |
| 2026-11-10 17:02:12 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.152 |  |
| 2026-11-10 17:01:52 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 17:01:46 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.035 |  |
| 2026-11-10 17:00:47 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 17:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 17:07:37 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 17:03:33 | Dunamale (Aththanagalu Oya) | 4.55 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-10 17:09:16 | Thalgahagoda (Nilwala Ganga) | 1.69 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-11-10 17:03:38 | Moraketiya (Walawe Ganga) | 3.03 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-10 17:03:46 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | -0.041 |  |
| 2026-11-10 17:09:03 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.105 |  |
| 2026-11-10 17:03:46 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 1.046 | 🔺 Rising |
| 2026-11-10 17:05:15 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-11-10 17:03:19 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.775 | 🔺 Rising |
| 2026-11-10 17:08:33 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-11-10 17:07:57 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-10 17:09:09 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-10 17:03:23 | Kuda Oya (Kirindi Oya) | 1.98 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-10 17:05:18 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 17:08:21 | Thawalama (Gin Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-10 17:02:36 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 17:01:52 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 17:08:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 17:02:47 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:14 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:16:57 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:35 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:06:54 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:08:52 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:10 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:03:56 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:40 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-11-10 17:00:47 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.017 |  |
| 2026-11-10 17:24:27 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 17:08:05 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.030 |  |
| 2026-11-10 17:01:46 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.035 |  |
| 2026-11-10 17:03:00 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.038 |  |
| 2026-11-10 17:02:20 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.061 |  |
| 2026-11-10 17:07:38 | Glencourse (Kelani Ganga) | 11.79 | 🟢 Normal | -0.061 |  |
| 2026-11-10 17:04:54 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.065 |  |
| 2026-11-10 17:07:29 | Moragaswewa (Deduru Oya) | 4.01 | 🟢 Normal | -0.088 |  |
| 2026-11-10 17:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.121 |  |
| 2026-11-10 17:02:12 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)