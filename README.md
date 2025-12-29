# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_07:19:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 07:19:54 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:50 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:13:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:12:05 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2025-12-29 07:12:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:10:12 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-29 07:08:46 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:08:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.027 |  |
| 2025-12-29 07:08:15 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.018 |  |
| 2025-12-29 07:08:08 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:53 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:39 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:34 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.643 |  |
| 2025-12-29 07:07:24 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:05:44 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2025-12-29 07:05:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:05:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:05:11 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:05:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:04:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:04:46 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.643 |  |
| 2025-12-29 07:04:36 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.002 |  |
| 2025-12-29 07:04:18 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.088 |  |
| 2025-12-29 07:04:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2025-12-29 07:03:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-29 07:03:00 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:32 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:30 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:13 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:04 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 07:01:29 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:01:11 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2025-12-29 07:01:11 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.033 |  |
| 2025-12-29 07:01:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-29 07:00:48 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:34:50 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:33:48 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.031 |  |
| 2025-12-29 06:33:47 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 07:03:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-29 07:01:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-29 07:02:04 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 07:05:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:01:13 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:00:48 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:32 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:28 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:50 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:15:38 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:01:29 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:39 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:12:01 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:13 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:08:08 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 06:18:21 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:03:00 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:13:11 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:53 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:19:54 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:07:24 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:05:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 07:04:36 | Thanthirimale (Malwathu Oya) | 1.63 | 🟢 Normal | -0.002 |  |
| 2025-12-29 07:10:12 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | -0.009 |  |
| 2025-12-29 07:05:44 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2025-12-29 07:04:54 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:05:16 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:02:30 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:05:11 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:08:46 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-29 07:08:15 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.018 |  |
| 2025-12-29 07:08:26 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.027 |  |
| 2025-12-29 07:12:05 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2025-12-29 07:01:11 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.033 |  |
| 2025-12-29 07:01:11 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2025-12-29 07:04:13 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.063 |  |
| 2025-12-29 07:04:18 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.088 |  |
| 2025-12-29 07:07:34 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.643 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)