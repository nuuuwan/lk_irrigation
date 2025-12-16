# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_09:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 09:12:18 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:10:39 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-16 09:10:27 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2025-12-16 09:08:58 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.065 |  |
| 2025-12-16 09:08:51 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 09:07:42 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:07:21 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:07:20 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:06:08 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.019 |  |
| 2025-12-16 09:05:49 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.025 |  |
| 2025-12-16 09:05:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:04:31 | Pitabeddara (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.726 |  |
| 2025-12-16 09:04:23 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:04:13 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:52 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:03:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:46 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:43 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:38 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-16 09:03:29 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:21 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 09:02:58 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:02:47 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:02:45 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:40 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | -0.069 |  |
| 2025-12-16 09:02:18 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:03 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.020 |  |
| 2025-12-16 09:01:46 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:01:35 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-16 09:01:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-16 09:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:00:51 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:00:43 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:00:23 | Horowpothana (Yan Oya) | 4.62 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2025-12-16 09:00:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:21:51 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.016 |  |
| 2025-12-16 08:19:59 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:16:56 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 09:00:23 | Horowpothana (Yan Oya) | 4.62 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2025-12-16 09:01:35 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-16 09:03:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 09:03:38 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-16 09:08:51 | Galgamuwa (Mee Oya) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-16 09:02:05 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:04:23 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:01:46 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-16 08:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:29 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:43 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:45 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:07:42 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:00:52 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:00:10 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:07:20 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:03:21 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:12:18 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:04:13 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:07:21 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:18 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-16 09:10:27 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.009 |  |
| 2025-12-16 09:00:43 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:03:52 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:02:58 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:02:47 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-16 09:05:11 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-16 08:21:51 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.016 |  |
| 2025-12-16 09:06:08 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.019 |  |
| 2025-12-16 09:02:03 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.020 |  |
| 2025-12-16 09:10:39 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-16 09:01:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-16 09:05:49 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.025 |  |
| 2025-12-16 08:00:52 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2025-12-16 09:08:58 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.065 |  |
| 2025-12-16 09:02:40 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | -0.069 |  |
| 2025-12-16 09:04:31 | Pitabeddara (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.726 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)