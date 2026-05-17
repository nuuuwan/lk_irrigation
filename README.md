# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_05:30:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,003 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 05:30:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 05:21:37 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.050 |  |
| 2026-05-17 05:18:55 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-17 05:17:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:09:59 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-05-17 05:09:04 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.018 |  |
| 2026-05-17 05:06:57 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.036 |  |
| 2026-05-17 05:06:40 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-17 05:06:25 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-05-17 05:06:16 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.072 |  |
| 2026-05-17 05:06:08 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:05:55 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.052 |  |
| 2026-05-17 05:05:25 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.020 |  |
| 2026-05-17 05:03:51 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:49 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.013 |  |
| 2026-05-17 05:03:45 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:29 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:13 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-17 05:03:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.214 |  |
| 2026-05-17 05:03:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-17 05:03:05 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-17 05:02:55 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:02:46 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:02:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:02:18 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:02:12 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:01:51 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -0.030 |  |
| 2026-05-17 05:01:28 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.219 |  |
| 2026-05-17 05:01:24 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:01:14 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:10 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:09 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 05:30:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-17 05:03:06 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-17 05:18:55 | Magura (Kalu Ganga) | 3.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-17 05:03:05 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-17 05:06:40 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 18:01:12 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 05:03:13 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-17 02:07:10 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.003 |  |
| 2026-05-17 05:02:46 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:02:44 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:36 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:02:55 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:51 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:14 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:17:44 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:10 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:06:08 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:24 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:45 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:01:09 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:03:29 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-17 05:09:59 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-05-17 05:02:12 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:02:18 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-17 03:08:26 | Putupaula (Kalu Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-05-17 05:03:49 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.013 |  |
| 2026-05-17 05:09:04 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.018 |  |
| 2026-05-17 05:05:25 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | -0.020 |  |
| 2026-05-17 05:06:25 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-05-17 05:01:51 | Ellagawa (Kalu Ganga) | 7.98 | 🟢 Normal | -0.030 |  |
| 2026-05-16 18:01:55 | Thanthirimale (Malwathu Oya) | 3.80 | 🟢 Normal | -0.030 |  |
| 2026-05-17 05:06:57 | Dunamale (Aththanagalu Oya) | 3.28 | 🟢 Normal | -0.036 |  |
| 2026-05-16 18:04:15 | Galgamuwa (Mee Oya) | 2.90 | 🟢 Normal | -0.048 |  |
| 2026-05-17 05:21:37 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.050 |  |
| 2026-05-17 05:05:55 | Glencourse (Kelani Ganga) | 11.15 | 🟢 Normal | -0.052 |  |
| 2026-05-17 05:06:16 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.072 |  |
| 2026-05-17 05:03:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.214 |  |
| 2026-05-17 05:01:28 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)