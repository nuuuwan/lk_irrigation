# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_04:06:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,715 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 04:06:15 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 04:06:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:05:42 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:03:48 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:02:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:01:49 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:48 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:01:40 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:32 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2025-12-29 04:01:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-29 04:01:11 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 04:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:03 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.060 |  |
| 2025-12-29 04:01:03 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2025-12-29 04:00:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:47 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:51:00 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.026 |  |
| 2025-12-29 03:44:41 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:44:04 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:21:18 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:13:58 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:11:15 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:11:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.012 |  |
| 2025-12-29 03:08:53 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -3.273 |  |
| 2025-12-29 03:08:31 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -3.273 |  |
| 2025-12-29 03:08:25 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 03:08:24 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 02:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-29 02:04:51 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-29 04:01:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-29 04:06:15 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 03:04:45 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 04:01:11 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 04:04:05 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:49 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:44:41 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:02:04 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:40 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-29 02:11:45 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-29 01:11:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:02:55 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:01:24 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:07:18 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:03:08 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:11:15 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:21:18 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:06:00 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:47 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-29 03:13:58 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:00:53 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:01:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-29 04:03:48 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:05:42 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:01:52 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:01:48 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2025-12-29 03:05:51 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-29 04:01:32 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.012 |  |
| 2025-12-29 03:51:00 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.026 |  |
| 2025-12-29 04:01:03 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2025-12-29 04:01:03 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.060 |  |
| 2025-12-29 03:08:53 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -3.273 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)