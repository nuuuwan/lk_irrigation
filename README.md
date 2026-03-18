# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--18_17:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **100,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 17:12:00 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:10:33 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:10:28 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:08:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:08:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:07:19 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:06:32 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-18 17:06:22 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-18 17:05:55 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.114 |  |
| 2026-03-18 17:04:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-18 17:04:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:28 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-18 17:04:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:03 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:03:48 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.048 |  |
| 2026-03-18 17:03:33 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:03:30 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-18 17:03:28 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:03:13 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 17:02:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:02:52 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:02:51 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 17:02:44 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:02:41 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:02:20 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-18 17:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 17:01:58 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 17:01:37 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.104 |  |
| 2026-03-18 17:01:37 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:01:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -324.000 |  |
| 2026-03-18 17:01:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -324.000 |  |
| 2026-03-18 17:01:14 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.083 |  |
| 2026-03-18 17:01:13 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-03-18 17:01:11 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:00:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.042 |  |
| 2026-03-18 17:00:34 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-03-18 16:59:20 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.057 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-18 17:03:30 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-18 17:04:28 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-03-18 17:01:58 | Manampitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 17:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-18 16:59:20 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-18 17:04:58 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-18 17:06:22 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-03-18 17:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-18 17:03:13 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-18 17:02:52 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:02:51 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:07:19 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-18 17:01:37 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 16:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:12:00 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:03 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:08:15 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:10:28 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:06 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:03:28 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:03:33 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:04:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:08:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:02:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-18 16:06:11 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:01:11 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:10:33 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:02:44 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-18 17:06:32 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-18 17:02:20 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-18 17:01:13 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-03-18 17:00:34 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-03-18 17:00:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.042 |  |
| 2026-03-18 17:03:48 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.048 |  |
| 2026-03-18 17:01:14 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.083 |  |
| 2026-03-18 17:01:37 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.104 |  |
| 2026-03-18 17:05:55 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.114 |  |
| 2026-03-18 17:01:21 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -324.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)