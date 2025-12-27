# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_17:02:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **29,430 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 17:02:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-27 17:02:02 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2025-12-27 17:01:53 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:50 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:35 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:02 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:00 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:00:26 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:51:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.014 |  |
| 2025-12-27 16:11:19 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:11:09 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -216.000 |  |
| 2025-12-27 16:11:08 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -216.000 |  |
| 2025-12-27 16:11:00 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:08:54 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.014 |  |
| 2025-12-27 16:07:20 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-27 16:06:45 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-27 16:05:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-27 16:05:45 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.005 |  |
| 2025-12-27 16:05:27 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:05:24 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:05:14 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:04:50 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:04:33 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:04:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-27 16:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:04:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 16:04:06 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 16:04:02 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:03:59 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 16:05:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-27 17:02:09 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-27 16:04:06 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-27 16:02:48 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 17:01:35 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 16:04:18 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 16:01:13 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:53 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:02:16 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:03:41 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:02:42 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:03:19 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:47 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:00:26 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:36 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:04:33 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:11:19 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:00:44 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:01:33 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-27 17:01:50 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 16:05:45 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.005 |  |
| 2025-12-27 16:07:20 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2025-12-27 16:05:14 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:05:24 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:05:27 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:04:50 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:01:40 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:00:54 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:04:02 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2025-12-27 16:00:35 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-27 17:01:16 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2025-12-27 17:01:02 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2025-12-27 16:51:37 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.014 |  |
| 2025-12-27 16:03:08 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | -0.032 |  |
| 2025-12-27 17:02:02 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.040 |  |
| 2025-12-27 16:11:09 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)