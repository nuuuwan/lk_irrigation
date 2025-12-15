# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_10:27:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 10:27:50 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:22:53 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:16:53 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-15 10:15:20 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:11:59 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.025 |  |
| 2025-12-15 10:10:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-15 10:06:51 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:06:31 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2025-12-15 10:06:19 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:22 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:05:19 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:12 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:03 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.050 |  |
| 2025-12-15 10:04:44 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-15 10:04:35 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:03:49 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:03:44 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.013 |  |
| 2025-12-15 10:03:36 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:03:34 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.051 |  |
| 2025-12-15 10:03:29 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-15 10:03:22 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2025-12-15 10:03:13 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2025-12-15 10:02:58 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:48 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 10:02:46 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:02:34 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | -0.034 |  |
| 2025-12-15 10:02:33 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:23 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:02:20 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-15 10:02:06 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-15 10:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:01:41 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:01:06 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:00:54 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-15 10:00:51 | Horowpothana (Yan Oya) | 4.04 | 🟢 Normal | -0.030 |  |
| 2025-12-15 10:00:48 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:00:38 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:00:12 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 10:02:17 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-15 10:00:54 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-15 10:00:12 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-15 10:10:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-15 10:02:48 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-15 10:01:41 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:27:50 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:30 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:03:36 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:15:20 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:06:51 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:12 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:01:06 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:33 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:58 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:19 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:00:48 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:06:19 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:22:53 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:02:20 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:00:38 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:05:22 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:02:46 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:01:06 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:02:23 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:04:35 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:16:53 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-15 10:03:44 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.013 |  |
| 2025-12-15 10:04:44 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.019 |  |
| 2025-12-15 10:02:06 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2025-12-15 10:03:29 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-15 10:06:31 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2025-12-15 10:11:59 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.025 |  |
| 2025-12-15 10:00:51 | Horowpothana (Yan Oya) | 4.04 | 🟢 Normal | -0.030 |  |
| 2025-12-15 10:03:22 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.030 |  |
| 2025-12-15 10:02:34 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | -0.034 |  |
| 2025-12-15 10:03:13 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | -0.040 |  |
| 2025-12-15 10:05:03 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.050 |  |
| 2025-12-15 10:03:34 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)