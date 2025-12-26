# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_21:04:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,709 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 21:04:46 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 21:04:29 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:03:51 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.042 |  |
| 2025-12-26 21:03:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:03:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:58 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2025-12-26 21:02:54 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.080 |  |
| 2025-12-26 21:02:53 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:40 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-26 21:02:25 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2025-12-26 21:02:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:06 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:04 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:01:50 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.054 |  |
| 2025-12-26 21:01:45 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:01:44 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:01:27 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:01:07 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.107 |  |
| 2025-12-26 21:01:00 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:00:50 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2025-12-26 21:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:00:42 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:00:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:00:14 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:44:20 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.107 |  |
| 2025-12-26 20:19:21 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:11:22 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.012 |  |
| 2025-12-26 20:09:29 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:09:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:07:46 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 20:01:57 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.529 | 🔺 Rising |
| 2025-12-26 21:02:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-26 20:01:48 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2025-12-26 21:04:46 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 21:02:53 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:00:38 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:03:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:03:10 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:40 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:02:48 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:04 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:10 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:06 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:09:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 20:06:50 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:01:45 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:00:14 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:02:58 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 21:01:27 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:03:51 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:04:29 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.010 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:00:42 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:01:00 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:01:44 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-26 21:02:55 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2025-12-26 21:02:25 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2025-12-26 20:04:16 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2025-12-26 21:00:50 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2025-12-26 20:06:02 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.013 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-26 21:03:51 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.042 |  |
| 2025-12-26 21:01:50 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.054 |  |
| 2025-12-26 21:02:54 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.080 |  |
| 2025-12-26 21:01:07 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.107 |  |
| 2025-12-26 20:02:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.116 |  |
| 2025-12-26 20:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.397 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)