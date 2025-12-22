# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_17:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,974 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 17:03:31 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 17:03:07 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.049 |  |
| 2025-12-22 17:03:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:48 | Horowpothana (Yan Oya) | 3.30 | 🟢 Normal | -0.050 |  |
| 2025-12-22 17:02:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -1.256 |  |
| 2025-12-22 17:02:30 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-22 17:02:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:27 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 17:02:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:12 | Thanthirimale (Malwathu Oya) | 4.43 | 🟢 Normal | -0.021 |  |
| 2025-12-22 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2025-12-22 17:02:09 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-22 17:02:05 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:05 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 17:01:42 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2025-12-22 17:01:42 | Galgamuwa (Mee Oya) | 0.97 | 🟢 Normal | -0.122 |  |
| 2025-12-22 17:01:40 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-22 17:01:34 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.013 |  |
| 2025-12-22 17:01:27 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 17:01:20 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:01:08 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -1.256 |  |
| 2025-12-22 17:00:47 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:17:07 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.013 |  |
| 2025-12-22 16:16:03 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -1.256 |  |
| 2025-12-22 16:15:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 16:09:18 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.011 |  |
| 2025-12-22 16:08:38 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:07:23 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | -0.122 |  |
| 2025-12-22 16:06:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-22 16:05:56 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:22 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 17:02:30 | Weraganthota (Mahaweli Ganga) | -1.03 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-22 16:15:23 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-22 17:02:05 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 17:03:31 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 17:02:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:05 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:24 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:02:30 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:05:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:02 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:00:47 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:01:51 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:03:04 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2025-12-22 17:01:20 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:39 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:33 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:02:16 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 16:04:04 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:08:38 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 17:01:27 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:02:38 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:00:22 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:03:36 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-22 17:02:27 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-22 16:01:27 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-22 17:01:40 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2025-12-22 17:01:42 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2025-12-22 17:01:34 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.013 |  |
| 2025-12-22 17:02:09 | Siyambalanduwa (Heda Oya) | 0.94 | 🟢 Normal | -0.020 |  |
| 2025-12-22 17:02:12 | Thanthirimale (Malwathu Oya) | 4.43 | 🟢 Normal | -0.021 |  |
| 2025-12-22 16:03:52 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.029 |  |
| 2025-12-22 16:01:40 | Manampitiya (Mahaweli Ganga) | 2.37 | 🟢 Normal | -0.031 |  |
| 2025-12-22 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2025-12-22 17:03:07 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.049 |  |
| 2025-12-22 17:02:48 | Horowpothana (Yan Oya) | 3.30 | 🟢 Normal | -0.050 |  |
| 2025-12-22 17:01:42 | Galgamuwa (Mee Oya) | 0.97 | 🟢 Normal | -0.122 |  |
| 2025-12-22 17:02:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -1.256 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)