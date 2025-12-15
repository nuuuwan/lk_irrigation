# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_11:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,524 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 11:06:17 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 11:06:13 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:05:59 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:05:57 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:05:49 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:05:43 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:04:22 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:04:22 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 11:03:56 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.061 |  |
| 2025-12-15 11:03:45 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 11:03:37 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 11:03:34 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:33 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2025-12-15 11:03:33 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:03:28 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2025-12-15 11:03:25 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:18 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:03:04 | Weraganthota (Mahaweli Ganga) | -1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:02:54 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:02:38 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:02:37 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2025-12-15 11:02:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2025-12-15 11:02:24 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:02:03 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 11:01:35 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:01:31 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2025-12-15 11:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.080 |  |
| 2025-12-15 11:01:07 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:01:05 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:00:59 | Horowpothana (Yan Oya) | 4.01 | 🟢 Normal | -0.030 |  |
| 2025-12-15 11:00:45 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:00:39 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:00:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.015 |  |
| 2025-12-15 11:00:19 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:27:50 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:22:53 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:16:53 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-15 10:15:20 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:11:59 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2025-12-15 10:10:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.034 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 11:02:03 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 11:03:37 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-15 11:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-15 11:04:22 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-15 11:06:17 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-15 11:00:39 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:04:22 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 11:00:19 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:01:35 | Moragaswewa (Deduru Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:03:36 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:06:13 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:15:20 | Panadugama (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:45 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:01:05 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:25 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:05:43 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:34 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:01:07 | Thanthirimale (Malwathu Oya) | 4.24 | 🟢 Normal | 0.000 |  |
| 2025-12-15 10:22:53 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:02:38 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:00:45 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-15 11:03:33 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:02:24 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:03:04 | Weraganthota (Mahaweli Ganga) | -1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:05:49 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:02:54 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-15 11:03:18 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-15 10:16:53 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-15 11:01:31 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.012 |  |
| 2025-12-15 11:00:38 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.015 |  |
| 2025-12-15 11:03:28 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.020 |  |
| 2025-12-15 11:03:33 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2025-12-15 11:02:34 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2025-12-15 11:00:59 | Horowpothana (Yan Oya) | 4.01 | 🟢 Normal | -0.030 |  |
| 2025-12-15 11:02:37 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2025-12-15 10:02:34 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | -0.034 |  |
| 2025-12-15 11:03:56 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.061 |  |
| 2025-12-15 11:01:23 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)