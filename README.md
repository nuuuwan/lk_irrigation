# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_14:07:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 14:07:38 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-20 14:07:03 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-20 14:06:44 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:05:35 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.076 |  |
| 2025-12-20 14:04:47 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:04:39 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:04:33 | Weraganthota (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-20 14:04:32 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:04:29 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2025-12-20 14:04:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2025-12-20 14:03:49 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:45 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-20 14:03:42 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:21 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.100 |  |
| 2025-12-20 14:03:18 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:12 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2025-12-20 14:03:08 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:45 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:36 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:11 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:00 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:01:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:01:31 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:01:21 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:01:18 | Manampitiya (Mahaweli Ganga) | 3.53 | 🟡 Alert | -0.137 |  |
| 2025-12-20 14:01:08 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 14:00:56 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:00:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:00:17 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | 0.000 |  |
| 2025-12-20 14:00:14 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:28:58 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:14:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-20 13:12:48 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.012 |  |
| 2025-12-20 13:11:00 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 14:00:17 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | 0.000 |  |
| 2025-12-20 13:02:50 | Thanthirimale (Malwathu Oya) | 5.45 | 🟡 Alert | -0.033 |  |
| 2025-12-20 14:01:18 | Manampitiya (Mahaweli Ganga) | 3.53 | 🟡 Alert | -0.137 |  |
| 2025-12-20 14:04:33 | Weraganthota (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-20 13:04:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-20 14:03:45 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-20 14:07:03 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-20 13:14:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-20 14:01:08 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 14:03:42 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:49 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:04:32 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:06:44 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:18 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:00:56 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:30 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:36 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:40 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:01:53 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:00:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:04:49 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:08 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:11 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:45 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:00 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:04:47 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:07:38 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.009 |  |
| 2025-12-20 14:04:39 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:07:28 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:01:31 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:01:21 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:00:14 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-20 14:03:12 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2025-12-20 14:04:29 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.012 |  |
| 2025-12-20 14:04:11 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2025-12-20 14:05:35 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.076 |  |
| 2025-12-20 14:03:21 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)