# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_02:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 02:11:57 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:08:23 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2025-12-28 02:08:19 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2025-12-28 02:08:04 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2025-12-28 02:05:43 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2025-12-28 02:05:15 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:05:14 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 02:04:59 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:04:49 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:04:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2025-12-28 02:04:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-28 02:04:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:57 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-28 02:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:39 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:51 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:35 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:03 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:01 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.150 |  |
| 2025-12-28 02:01:41 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:01:36 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:01:23 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2025-12-28 02:01:04 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:32 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:10 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 02:08:23 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 45.000 | 🔺 Rising |
| 2025-12-28 02:04:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-28 01:31:18 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-28 02:05:14 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 01:15:36 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.003 |  |
| 2025-12-28 00:00:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 19:15:41 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:32 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:03 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:01:36 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:02:35 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:04:03 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-27 18:03:28 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:05:22 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:39 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:01:41 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:05:15 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:05:19 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:03:23 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:10 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:04:59 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:04:49 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:01:04 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:11:57 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-28 02:00:38 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-27 22:09:15 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:08:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 01:02:58 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-28 00:12:05 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.003 |  |
| 2025-12-28 02:03:57 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2025-12-27 18:01:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-28 01:01:23 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-28 02:04:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2025-12-28 02:08:04 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.012 |  |
| 2025-12-28 02:05:43 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.030 |  |
| 2025-12-28 02:01:23 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.040 |  |
| 2025-12-27 21:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-28 02:02:01 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)