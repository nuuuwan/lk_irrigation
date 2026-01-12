# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_21:09:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 21:09:24 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:08:59 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 21:07:48 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:07:43 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-12 21:07:37 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:07:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.037 |  |
| 2026-01-12 21:07:09 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:06:36 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-01-12 21:05:46 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:05:16 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 21:04:12 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 21:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:04:00 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:03:55 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-12 21:03:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:03:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-01-12 21:03:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:03:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-01-12 21:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 21:03:03 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 21:03:01 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-12 21:02:56 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 21:02:56 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 21:02:40 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:02:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:01:59 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:01:35 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.013 |  |
| 2026-01-12 21:01:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-12 21:01:21 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 21:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:01:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.105 |  |
| 2026-01-12 21:01:00 | Yaka Wewa (Ma Oya) | 1.54 | 🟢 Normal | -0.122 |  |
| 2026-01-12 21:00:43 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 20:22:18 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 20:17:58 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 20:17:01 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.013 |  |
| 2026-01-12 20:13:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 21:03:10 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-01-12 21:03:55 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-01-12 21:03:01 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-12 21:07:43 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-12 21:01:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-12 21:00:43 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-12 21:01:21 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 21:02:56 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 21:08:59 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 21:05:16 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 21:02:56 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 21:03:03 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 21:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:02:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:07:48 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:06:05 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:01:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:03:49 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:05:46 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:02:40 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:03:12 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:01:10 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:09:24 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-12 21:07:09 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:04:00 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-01-12 21:06:36 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:01:59 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:07:37 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-12 21:01:35 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.013 |  |
| 2026-01-12 21:04:12 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 21:07:33 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.037 |  |
| 2026-01-12 21:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-01-12 21:03:21 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-01-12 21:01:10 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.105 |  |
| 2026-01-12 21:01:00 | Yaka Wewa (Ma Oya) | 1.54 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)