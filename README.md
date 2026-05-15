# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_13:17:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 13:17:38 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:17:36 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-05-15 13:14:06 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:10:18 | Moragaswewa (Deduru Oya) | 3.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 13:10:13 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 13:09:53 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | -0.074 |  |
| 2026-05-15 13:09:44 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.048 |  |
| 2026-05-15 13:08:56 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-15 13:08:29 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:08:23 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.132 |  |
| 2026-05-15 13:08:23 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 13:08:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:08:12 | Katharagama (Menik Ganga) | 0.77 | 🟢 Normal | -0.065 |  |
| 2026-05-15 13:05:51 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:05:48 | Glencourse (Kelani Ganga) | 12.42 | 🟢 Normal | -0.190 |  |
| 2026-05-15 13:05:44 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.012 |  |
| 2026-05-15 13:05:25 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-05-15 13:05:22 | Badalgama (Maha Oya) | 4.38 | 🟢 Normal | -0.064 |  |
| 2026-05-15 13:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-05-15 13:04:48 | Galgamuwa (Mee Oya) | 3.85 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-15 13:04:16 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:03:26 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-15 13:03:01 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-05-15 13:02:57 | Hanwella (Kelani Ganga) | 5.74 | 🟢 Normal | -0.113 |  |
| 2026-05-15 13:02:53 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:02:49 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-05-15 13:02:29 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-05-15 13:02:10 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:02:09 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:01:57 | Giriulla (Maha Oya) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-05-15 13:01:26 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-05-15 13:01:08 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-15 13:01:05 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:01:05 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:00:39 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:00:28 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 13:08:23 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-15 13:05:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.99 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-05-15 13:03:01 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-05-15 13:09:44 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.048 |  |
| 2026-05-15 13:04:48 | Galgamuwa (Mee Oya) | 3.85 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-15 13:01:08 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-15 13:10:18 | Moragaswewa (Deduru Oya) | 3.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-15 12:00:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-15 13:00:28 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 13:10:13 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-15 13:00:22 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:00:49 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:01:05 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:08:18 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:05:51 | Ellagawa (Kalu Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:17:38 | Baddegama (Gin Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:08:29 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:14:06 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:04:16 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:02:10 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:00:39 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-15 13:01:05 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:02:09 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:02:53 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-15 13:01:26 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.011 |  |
| 2026-05-15 13:08:56 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-15 13:05:44 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.012 |  |
| 2026-05-15 13:03:26 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-15 13:02:49 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-05-15 13:02:29 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.032 |  |
| 2026-05-15 13:17:36 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.046 |  |
| 2026-05-15 13:05:25 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-05-15 13:01:57 | Giriulla (Maha Oya) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-05-15 13:05:22 | Badalgama (Maha Oya) | 4.38 | 🟢 Normal | -0.064 |  |
| 2026-05-15 13:08:12 | Katharagama (Menik Ganga) | 0.77 | 🟢 Normal | -0.065 |  |
| 2026-05-15 13:09:53 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | -0.074 |  |
| 2026-05-15 13:02:57 | Hanwella (Kelani Ganga) | 5.74 | 🟢 Normal | -0.113 |  |
| 2026-05-15 13:08:23 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.132 |  |
| 2026-05-15 13:05:48 | Glencourse (Kelani Ganga) | 12.42 | 🟢 Normal | -0.190 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)