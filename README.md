# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_06:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 06:11:07 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:08:00 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:07:43 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.137 |  |
| 2026-01-24 06:07:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:06:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-24 06:06:58 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 06:06:55 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 06:06:48 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:06:44 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:06:30 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-24 06:06:16 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-24 06:05:16 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 06:04:36 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:06 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:01 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:03:44 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-01-24 06:03:42 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:03:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:02:46 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-24 06:02:38 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.061 |  |
| 2026-01-24 06:02:32 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-01-24 06:02:31 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.022 |  |
| 2026-01-24 06:02:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:48 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:47 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:40 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:29 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.113 |  |
| 2026-01-24 06:01:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:00:55 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:00:46 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:00:38 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-24 05:35:44 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 05:27:18 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-24 05:21:18 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:18:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:17:37 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 06:06:30 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-24 05:08:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-24 06:00:38 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-24 06:05:16 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-24 06:06:55 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 06:06:58 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-24 04:02:59 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.002 |  |
| 2026-01-24 06:01:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:03:20 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:02:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:22 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 18:03:40 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:00:55 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:06:44 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:40 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:08:00 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:06 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:11:07 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:03:42 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:06:48 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:47 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:36 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:08 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:04:01 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:48 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:07:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:01:19 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 06:03:44 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.005 |  |
| 2026-01-24 06:06:16 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:10:41 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-24 06:02:46 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-23 18:01:34 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-24 06:02:32 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.013 |  |
| 2026-01-24 06:06:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-24 06:02:31 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.022 |  |
| 2026-01-24 06:02:38 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.061 |  |
| 2026-01-24 06:01:29 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.113 |  |
| 2026-01-24 06:07:43 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)