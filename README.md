# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_18:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:11:25 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-19 18:10:13 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-19 18:07:55 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:07:36 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-19 18:07:12 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 18:06:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-19 18:05:17 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:04:53 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:04:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:04:13 | Manampitiya (Mahaweli Ganga) | 4.28 | 🟡 Alert | -0.076 |  |
| 2025-12-19 18:04:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 18:04:11 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-19 18:03:38 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:32 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-19 18:03:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:24 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:59 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 18:02:59 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-19 18:02:35 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:02:34 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:26 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.080 |  |
| 2025-12-19 18:02:20 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:01:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.053 |  |
| 2025-12-19 18:01:38 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-19 18:01:15 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:00:45 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-19 18:00:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:22 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:21 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2025-12-19 18:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 17:59:14 | Thaldena (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.042 |  |
| 2025-12-19 17:29:52 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-19 18:07:12 | Horowpothana (Yan Oya) | 6.28 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2025-12-19 18:04:13 | Manampitiya (Mahaweli Ganga) | 4.28 | 🟡 Alert | -0.076 |  |
| 2025-12-19 18:07:36 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2025-12-19 17:08:30 | Padiyathalawa (Maduru Oya) | 2.73 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-19 18:03:32 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-19 18:01:38 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-19 18:04:11 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-19 18:03:24 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 18:04:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-19 18:02:59 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 18:02:59 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:04:53 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:22 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:38 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:01:58 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:34 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:00:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:07:55 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:02:26 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-19 17:02:23 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:01:15 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:04:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:10:13 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-19 18:11:25 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-19 18:02:20 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:02:35 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:00:49 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:05:17 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2025-12-19 18:00:45 | Nakkala (Kumbukkan Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2025-12-19 18:06:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-19 17:59:14 | Thaldena (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.042 |  |
| 2025-12-19 18:00:21 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.042 |  |
| 2025-12-19 18:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.053 |  |
| 2025-12-19 18:02:24 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)