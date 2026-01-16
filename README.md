# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--16_12:09:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,123 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 12:09:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:09:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:08:14 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-01-16 12:05:14 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-16 12:04:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:04:40 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-16 12:04:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.084 |  |
| 2026-01-16 12:03:54 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:42 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:42 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:37 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 12:03:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 12:03:31 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:28 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:19 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:12 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-16 12:03:05 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:02:46 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-16 12:02:44 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:02:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-16 12:02:31 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:02:30 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-01-16 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 12:02:15 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:02:08 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-16 12:01:45 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:29 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:16 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:00:54 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 12:00:47 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:00:23 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.057 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-16 12:03:12 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-16 12:02:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-16 11:04:18 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-16 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 12:03:37 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-16 12:04:40 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-16 12:03:35 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 12:00:54 | Weraganthota (Mahaweli Ganga) | -1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-16 12:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:54 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:00:47 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:45 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:42 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:31 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:42 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-16 11:13:34 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:28 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:09:14 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:19 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:04:37 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:04:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:09:52 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:03:05 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:02:15 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:01:29 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-16 12:02:31 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:02:44 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:01:16 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-16 11:01:06 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-01-16 12:02:08 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-01-16 12:02:30 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-01-16 12:02:46 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-01-16 12:08:14 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.020 |  |
| 2026-01-16 12:05:14 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | -0.030 |  |
| 2026-01-16 11:10:10 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.054 |  |
| 2026-01-16 12:00:23 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.057 |  |
| 2026-01-16 12:03:55 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)