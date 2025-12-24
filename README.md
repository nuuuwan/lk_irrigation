# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_18:32:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,813 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 18:32:02 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2025-12-24 18:24:26 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-24 18:17:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:11:09 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 18:10:38 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:02 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:06:51 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:06:36 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.052 |  |
| 2025-12-24 18:05:27 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:05:01 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2025-12-24 18:04:42 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:17 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:13 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2025-12-24 18:03:54 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2025-12-24 18:03:43 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.074 |  |
| 2025-12-24 18:03:39 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:15 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:12 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:10 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 18:02:57 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:37 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 18:02:29 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:20 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:02:02 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 18:01:58 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:51 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-24 18:01:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 18:01:19 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:14 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:11 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2025-12-24 18:00:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 18:04:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2025-12-24 18:01:51 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-24 18:03:39 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 18:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-24 18:11:09 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 18:03:10 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 17:18:56 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-24 18:24:26 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-24 18:02:02 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 18:02:37 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:11 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:29 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:58 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:19 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:13 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:17:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:57 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:00:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:14 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 17:00:26 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:17 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:39 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:42 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:06:51 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:10:38 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:01:49 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:02 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:02:20 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:54 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.019 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:15 | Glencourse (Kelani Ganga) | 8.77 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:03:12 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2025-12-24 18:01:02 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.021 |  |
| 2025-12-24 18:32:02 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 18:06:36 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.052 |  |
| 2025-12-24 18:05:01 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2025-12-24 18:03:43 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)