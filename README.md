# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_15:16:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 15:16:36 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.092 |  |
| 2026-05-08 15:11:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:10:22 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-05-08 15:08:56 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.049 |  |
| 2026-05-08 15:08:16 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:07:36 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2026-05-08 15:07:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-05-08 15:07:06 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.047 |  |
| 2026-05-08 15:06:53 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-05-08 15:06:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 15:06:24 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-05-08 15:06:06 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:05:15 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-08 15:04:49 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.089 |  |
| 2026-05-08 15:04:40 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:04:25 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -3.789 |  |
| 2026-05-08 15:04:06 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -3.789 |  |
| 2026-05-08 15:04:03 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.043 |  |
| 2026-05-08 15:03:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-08 15:03:35 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.068 |  |
| 2026-05-08 15:03:31 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 15:03:18 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-05-08 15:03:16 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.102 |  |
| 2026-05-08 15:03:10 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.061 |  |
| 2026-05-08 15:03:09 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-08 15:02:35 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-08 15:02:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:02:12 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.025 |  |
| 2026-05-08 15:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:01:40 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.023 |  |
| 2026-05-08 15:01:40 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:01:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-08 15:01:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:01:06 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.060 |  |
| 2026-05-08 15:01:04 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:01:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:00:36 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 15:00:30 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:00:14 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-08 14:57:06 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 15:06:24 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-05-08 15:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.282 | 🔺 Rising |
| 2026-05-08 15:03:09 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-08 15:06:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 15:05:15 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-08 15:03:46 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-08 15:00:36 | Thanthirimale (Malwathu Oya) | 1.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 15:03:31 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 15:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:00:30 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:02:35 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:11:08 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:06:06 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:04:40 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:01:04 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:08:16 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-08 15:02:22 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:01:40 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:01:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-08 15:01:17 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-05-08 15:06:53 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.011 |  |
| 2026-05-08 15:00:14 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-08 15:01:40 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.023 |  |
| 2026-05-08 15:02:12 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.025 |  |
| 2026-05-08 15:10:22 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-05-08 15:07:36 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2026-05-08 15:03:18 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.039 |  |
| 2026-05-08 14:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.039 |  |
| 2026-05-08 15:07:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.039 |  |
| 2026-05-08 15:04:03 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.043 |  |
| 2026-05-08 15:07:06 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.047 |  |
| 2026-05-08 15:08:56 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.049 |  |
| 2026-05-08 15:01:06 | Ellagawa (Kalu Ganga) | 5.42 | 🟢 Normal | -0.060 |  |
| 2026-05-08 15:03:10 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.061 |  |
| 2026-05-08 15:03:35 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.068 |  |
| 2026-05-08 15:04:49 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.089 |  |
| 2026-05-08 15:16:36 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | -0.092 |  |
| 2026-05-08 15:03:16 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.102 |  |
| 2026-05-08 15:04:25 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -3.789 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)