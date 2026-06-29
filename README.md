# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_12:19:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 12:19:20 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.015 |  |
| 2026-06-29 12:18:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-29 12:16:40 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-29 12:12:15 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:09:04 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-06-29 12:08:55 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-06-29 12:08:50 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:08:13 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.163 |  |
| 2026-06-29 12:07:29 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:07:26 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:07:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-29 12:07:18 | Rathnapura (Kalu Ganga) | 4.99 | 🟢 Normal | 1.041 | 🔺 Rising |
| 2026-06-29 12:06:47 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 12:05:57 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-29 12:05:39 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-29 12:05:37 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-29 12:05:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:04:52 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 12:04:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-29 12:04:12 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-06-29 12:04:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:04:00 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:03:47 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-29 12:03:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-29 12:03:39 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:03:28 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-29 12:03:25 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.023 |  |
| 2026-06-29 12:02:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:42 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 12:02:10 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:10 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-29 12:02:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:03 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:47 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:46 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 12:00:44 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-06-29 12:00:38 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 12:00:34 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:00:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:00:08 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 12:07:18 | Rathnapura (Kalu Ganga) | 4.99 | 🟢 Normal | 1.041 | 🔺 Rising |
| 2026-06-29 12:08:55 | Glencourse (Kelani Ganga) | 10.78 | 🟢 Normal | 0.290 | 🔺 Rising |
| 2026-06-29 12:09:04 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-06-29 12:05:37 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-29 12:00:44 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-06-29 12:04:12 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-06-29 12:02:42 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-06-29 12:04:17 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-29 12:16:40 | Panadugama (Nilwala Ganga) | 4.14 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-06-29 12:05:57 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-29 12:07:24 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-29 12:02:10 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-06-29 12:03:39 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-29 12:04:52 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 12:03:28 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-29 12:18:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.36 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-29 12:01:07 | Nawalapitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 12:06:47 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 12:03:47 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-29 12:00:08 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 12:02:10 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:03 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:08:50 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:04:03 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:05:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:47 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:45 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:00:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:02:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:07:29 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:04:00 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:12:15 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:01:46 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 12:05:39 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.009 |  |
| 2026-06-29 12:00:38 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-06-29 12:19:20 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.015 |  |
| 2026-06-29 12:03:25 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.023 |  |
| 2026-06-29 12:08:13 | Thawalama (Gin Ganga) | 2.69 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)