# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_22:09:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,767 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 22:09:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 22:07:56 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:07:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-16 22:07:14 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-16 22:05:18 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 22:05:15 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:04:56 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:04:46 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-16 22:04:25 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-05-16 22:04:03 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:03:37 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.084 |  |
| 2026-05-16 22:03:35 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-05-16 22:03:30 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 22:03:29 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-05-16 22:02:44 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 22:02:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:24 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.139 |  |
| 2026-05-16 22:02:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:20 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:13 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:01:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-16 22:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-16 22:01:41 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:01:40 | Dunamale (Aththanagalu Oya) | 3.53 | 🟡 Alert | -0.086 |  |
| 2026-05-16 22:01:36 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 22:01:36 | Moragaswewa (Deduru Oya) | 2.55 | 🟢 Normal | -0.079 |  |
| 2026-05-16 22:01:12 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.047 |  |
| 2026-05-16 22:01:09 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.050 |  |
| 2026-05-16 22:01:07 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:00:17 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:00:11 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 22:09:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.94 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-16 22:01:40 | Dunamale (Aththanagalu Oya) | 3.53 | 🟡 Alert | -0.086 |  |
| 2026-05-16 21:03:54 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 6.000 | 🔺 Rising |
| 2026-05-16 22:01:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-16 22:07:44 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-16 21:08:09 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-16 22:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-16 22:03:30 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-16 22:01:36 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 22:02:44 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-16 22:05:18 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 22:01:07 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:05:15 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:24 | Ellagawa (Kalu Ganga) | 8.07 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:04:56 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:00:17 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:27 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-16 21:05:04 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:07:56 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:02:20 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-16 22:01:41 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:04:03 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:00:11 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:02:13 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-16 22:04:25 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | -0.011 |  |
| 2026-05-16 22:07:14 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-05-16 22:03:35 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-05-16 22:03:29 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | -0.030 |  |
| 2026-05-16 22:04:46 | Deraniyagala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-16 21:10:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.036 |  |
| 2026-05-16 22:01:12 | Rathnapura (Kalu Ganga) | 4.05 | 🟢 Normal | -0.047 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-16 22:01:09 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.050 |  |
| 2026-05-16 22:01:36 | Moragaswewa (Deduru Oya) | 2.55 | 🟢 Normal | -0.079 |  |
| 2026-05-16 22:03:37 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.084 |  |
| 2026-05-16 22:02:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)