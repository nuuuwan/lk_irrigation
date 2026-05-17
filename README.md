# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_14:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 14:18:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:14:29 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.046 |  |
| 2026-05-17 14:13:48 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-05-17 14:12:17 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-05-17 14:12:04 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:10:35 | Thanthirimale (Malwathu Oya) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:09:47 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:09:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-17 14:07:56 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:07:45 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-05-17 14:06:51 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:06:47 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:06:37 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 14:06:10 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:05:49 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:05:45 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.019 |  |
| 2026-05-17 14:05:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 14:04:27 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-17 14:04:09 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:04:09 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-17 14:03:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:03:27 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.041 |  |
| 2026-05-17 14:03:16 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-05-17 14:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.041 |  |
| 2026-05-17 14:02:41 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:02:31 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.101 |  |
| 2026-05-17 14:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.012 |  |
| 2026-05-17 14:02:29 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-17 14:02:17 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:51 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:46 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.061 |  |
| 2026-05-17 14:01:46 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.044 |  |
| 2026-05-17 14:01:42 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:40 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-17 14:01:19 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:15 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.055 |  |
| 2026-05-17 14:00:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-17 14:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 14:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.012 |  |
| 2026-05-17 14:02:29 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-17 14:09:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-17 14:00:57 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-17 14:06:37 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 14:05:30 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 14:03:30 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:09:47 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:02:41 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:51 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:04:09 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:06:51 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:15 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:42 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:02:17 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:06:10 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:05:49 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:12:04 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:06:47 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:10:35 | Thanthirimale (Malwathu Oya) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:07:56 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:18:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:01:19 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-17 14:12:17 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-05-17 14:04:27 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-17 14:04:09 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-05-17 14:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-05-17 14:05:45 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | -0.019 |  |
| 2026-05-17 14:07:45 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-05-17 14:13:48 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-05-17 14:03:16 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-05-17 14:01:40 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-05-17 14:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.041 |  |
| 2026-05-17 14:03:27 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | -0.041 |  |
| 2026-05-17 14:01:46 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.044 |  |
| 2026-05-17 14:14:29 | Magura (Kalu Ganga) | 2.93 | 🟢 Normal | -0.046 |  |
| 2026-05-17 14:01:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.055 |  |
| 2026-05-17 14:01:46 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.061 |  |
| 2026-05-17 14:02:31 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)