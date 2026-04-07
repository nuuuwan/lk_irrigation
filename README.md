# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_05:46:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,316 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 05:46:21 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:43:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 05:43:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:43:09 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:38:11 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.069 |  |
| 2026-04-07 05:34:35 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.008 |  |
| 2026-04-07 05:33:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-07 05:30:57 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:08:48 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-07 05:08:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:06:30 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:06:29 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:05:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 05:05:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.088 |  |
| 2026-04-07 05:05:15 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-07 05:05:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 05:04:42 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-07 05:04:40 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-04-07 05:04:24 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-07 05:04:21 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.035 |  |
| 2026-04-07 05:04:13 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-07 05:04:00 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:03:56 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 05:03:53 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 05:03:45 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.096 |  |
| 2026-04-07 05:03:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 3.144 | 🔺 Rising |
| 2026-04-07 05:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-07 05:02:17 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-07 05:01:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:34 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:17 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 05:01:16 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:00:59 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:00:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:00:43 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-07 04:59:41 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | 3.144 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 05:03:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 3.144 | 🔺 Rising |
| 2026-04-07 05:02:17 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-07 05:04:13 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-07 05:43:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-07 05:08:48 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-07 05:33:48 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-07 05:04:24 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-07 05:03:53 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-07 05:05:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 05:03:56 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-07 05:01:17 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 05:05:01 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 05:43:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:47 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:08:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:46:21 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:30:57 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:06:30 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:38:00 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:43:09 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:34 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:00:57 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-07 04:03:29 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:01:16 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-07 05:34:35 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.008 |  |
| 2026-04-07 05:04:42 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-07 05:00:43 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-07 04:03:25 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.011 |  |
| 2026-04-07 05:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-07 05:05:15 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-07 05:04:21 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.035 |  |
| 2026-04-07 05:04:40 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.039 |  |
| 2026-04-07 05:38:11 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.069 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-07 05:05:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.088 |  |
| 2026-04-07 05:03:45 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)