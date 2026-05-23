# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_09:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 09:12:41 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.025 |  |
| 2026-05-23 09:12:00 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.017 |  |
| 2026-05-23 09:10:43 | Rathnapura (Kalu Ganga) | 6.20 | 🟡 Alert | -0.062 |  |
| 2026-05-23 09:08:55 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.018 |  |
| 2026-05-23 09:08:30 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.048 |  |
| 2026-05-23 09:07:59 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.208 |  |
| 2026-05-23 09:07:54 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.072 |  |
| 2026-05-23 09:06:55 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-05-23 09:06:00 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:05:31 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | -0.032 |  |
| 2026-05-23 09:05:28 | Putupaula (Kalu Ganga) | 3.00 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-23 09:04:47 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:47 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.069 |  |
| 2026-05-23 09:04:34 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 09:04:21 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-23 09:04:19 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:04:18 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | -0.031 |  |
| 2026-05-23 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:07 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:05 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:03:49 | Hanwella (Kelani Ganga) | 6.94 | 🟢 Normal | -0.100 |  |
| 2026-05-23 09:03:49 | Dunamale (Aththanagalu Oya) | 5.14 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-23 09:03:46 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.062 |  |
| 2026-05-23 09:03:25 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-05-23 09:03:13 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-23 09:02:42 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-23 09:02:40 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 09:01:31 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:01:30 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:01:17 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:01:17 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 09:01:14 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.191 |  |
| 2026-05-23 09:00:43 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:00:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-05-23 09:00:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:00:25 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.050 |  |
| 2026-05-23 09:00:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 08:40:36 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 08:38:50 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.069 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 09:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 09:03:49 | Dunamale (Aththanagalu Oya) | 5.14 | 🟠 Minor Flood | -0.010 |  |
| 2026-05-23 09:04:21 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-05-23 09:05:28 | Putupaula (Kalu Ganga) | 3.00 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-05-23 09:04:18 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | -0.031 |  |
| 2026-05-23 09:10:43 | Rathnapura (Kalu Ganga) | 6.20 | 🟡 Alert | -0.062 |  |
| 2026-05-23 09:01:17 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 09:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 09:01:30 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:00:43 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:06:00 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:01:31 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:00:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:47 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:05 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:00:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:07 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:02:40 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-23 09:04:34 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:04:19 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:01:17 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-05-23 09:00:33 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.011 |  |
| 2026-05-23 09:02:42 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-23 09:12:00 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.017 |  |
| 2026-05-23 09:08:55 | Baddegama (Gin Ganga) | 2.57 | 🟢 Normal | -0.018 |  |
| 2026-05-23 09:03:13 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.021 |  |
| 2026-05-23 09:03:25 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.021 |  |
| 2026-05-23 09:12:41 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.025 |  |
| 2026-05-23 09:06:55 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-05-23 09:05:31 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | -0.032 |  |
| 2026-05-23 09:08:30 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.048 |  |
| 2026-05-23 09:00:25 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.050 |  |
| 2026-05-23 09:03:46 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.062 |  |
| 2026-05-23 09:04:47 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.069 |  |
| 2026-05-23 09:07:54 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.072 |  |
| 2026-05-23 09:03:49 | Hanwella (Kelani Ganga) | 6.94 | 🟢 Normal | -0.100 |  |
| 2026-05-23 09:01:14 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.191 |  |
| 2026-05-23 09:07:59 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)