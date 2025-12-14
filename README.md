# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--15_02:49:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **18,173 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 02:49:40 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:10:17 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:09:21 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.061 |  |
| 2025-12-15 02:08:46 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.085 |  |
| 2025-12-15 02:06:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 02:06:02 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-15 02:05:34 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:05:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:04:30 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:03:52 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-15 02:03:49 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:03:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2025-12-15 02:03:35 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-15 02:03:32 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.005 |  |
| 2025-12-15 02:03:03 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.031 |  |
| 2025-12-15 02:03:00 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 02:02:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:02:33 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.091 |  |
| 2025-12-15 02:02:22 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:02:19 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 02:02:06 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:01:55 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:27 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.025 |  |
| 2025-12-15 02:01:24 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-15 02:01:16 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.020 |  |
| 2025-12-15 02:00:35 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-15 02:01:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-15 01:11:59 | Rathnapura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-15 02:03:52 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-15 01:03:44 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-15 02:06:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 02:02:19 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 02:03:00 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-15 01:01:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:05:18 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:09 | Galgamuwa (Mee Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:03:49 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:04:30 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:13:08 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:02:34 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:05:34 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:49:40 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2025-12-15 01:01:16 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-14 18:01:24 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:10:17 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:00:35 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-15 02:03:32 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.005 |  |
| 2025-12-15 01:35:23 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.006 |  |
| 2025-12-15 01:19:48 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-15 02:06:02 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.009 |  |
| 2025-12-15 00:01:20 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-14 18:05:18 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:55 | Moragaswewa (Deduru Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-15 02:01:24 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-15 01:42:47 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.013 |  |
| 2025-12-15 02:01:16 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.020 |  |
| 2025-12-15 02:01:27 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.025 |  |
| 2025-12-15 02:03:35 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-15 02:03:03 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.031 |  |
| 2025-12-15 02:03:40 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2025-12-15 02:09:21 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.061 |  |
| 2025-12-15 02:08:46 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.085 |  |
| 2025-12-15 00:03:22 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.090 |  |
| 2025-12-15 02:02:33 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)