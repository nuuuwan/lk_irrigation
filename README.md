# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_17:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,983 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 17:21:30 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-12 17:10:05 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | -0.077 |  |
| 2026-11-12 17:09:41 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.099 |  |
| 2026-11-12 17:09:35 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 17:08:46 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.037 |  |
| 2026-11-12 17:08:05 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-12 17:07:24 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-12 17:06:58 | Pitabeddara (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-12 17:06:36 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.060 |  |
| 2026-11-12 17:06:35 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.135 | 🔺 Rising |
| 2026-11-12 17:06:28 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-12 17:06:21 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:05:51 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-12 17:05:50 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-12 17:05:40 | Thanamalwila (Kirindi Oya) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-11-12 17:05:36 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.029 |  |
| 2026-11-12 17:05:36 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.041 |  |
| 2026-11-12 17:05:35 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-12 17:05:29 | Peradeniya (Mahaweli Ganga) | 4.63 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 17:05:27 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-12 17:04:39 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:04:32 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:04:28 | Thaldena (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-12 17:04:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.079 |  |
| 2026-11-12 17:03:44 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:03:32 | Wellawaya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-11-12 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 17:03:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 17:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 17:02:46 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-12 17:02:23 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.071 |  |
| 2026-11-12 17:02:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.076 |  |
| 2026-11-12 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | -0.010 |  |
| 2026-11-12 17:02:16 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-11-12 17:01:33 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.074 |  |
| 2026-11-12 17:01:09 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 17:01:08 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-12 17:00:22 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 17:06:35 | Panadugama (Nilwala Ganga) | 6.04 | 🟠 Minor Flood | 0.135 | 🔺 Rising |
| 2026-11-12 17:21:30 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-12 17:08:05 | Baddegama (Gin Ganga) | 4.12 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-12 17:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | -0.010 |  |
| 2026-11-12 17:05:36 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | -0.029 |  |
| 2026-11-12 17:08:46 | Dunamale (Aththanagalu Oya) | 4.10 | 🟡 Alert | -0.037 |  |
| 2026-11-12 17:10:05 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | -0.077 |  |
| 2026-11-12 17:06:58 | Pitabeddara (Nilwala Ganga) | 3.22 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-12 17:04:28 | Thaldena (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-11-12 17:06:28 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-12 17:05:51 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-11-12 17:05:29 | Peradeniya (Mahaweli Ganga) | 4.63 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 17:02:46 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-12 17:03:17 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-12 17:05:27 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-12 17:01:09 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-12 17:05:35 | Rathnapura (Kalu Ganga) | 5.05 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-12 17:01:08 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-12 17:09:35 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 17:07:24 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-12 17:03:24 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 17:00:22 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:04:39 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:06:21 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:04:32 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:03:44 | Kuda Oya (Kirindi Oya) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-11-12 17:03:18 | Galgamuwa (Mee Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-11-12 17:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.013 |  |
| 2026-11-12 17:05:50 | Katharagama (Menik Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-11-12 17:05:40 | Thanamalwila (Kirindi Oya) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-11-12 17:03:32 | Wellawaya (Kirindi Oya) | 2.16 | 🟢 Normal | -0.030 |  |
| 2026-11-12 17:05:36 | Moragaswewa (Deduru Oya) | 2.86 | 🟢 Normal | -0.041 |  |
| 2026-11-12 17:06:36 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.060 |  |
| 2026-11-12 17:02:23 | Hanwella (Kelani Ganga) | 4.96 | 🟢 Normal | -0.071 |  |
| 2026-11-12 17:01:33 | Giriulla (Maha Oya) | 2.50 | 🟢 Normal | -0.074 |  |
| 2026-11-12 17:02:22 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.076 |  |
| 2026-11-12 17:04:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.079 |  |
| 2026-11-12 17:09:41 | Glencourse (Kelani Ganga) | 12.20 | 🟢 Normal | -0.099 |  |
| 2026-11-12 17:00:30 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)