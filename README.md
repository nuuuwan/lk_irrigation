# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_23:08:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,257 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 23:08:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2025-12-12 23:07:33 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.019 |  |
| 2025-12-12 23:06:15 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:06:03 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.067 |  |
| 2025-12-12 23:05:48 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 23:05:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-12 23:04:43 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.248 |  |
| 2025-12-12 23:04:37 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 23:04:03 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:03:59 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:55 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:51 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-12 23:03:37 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2025-12-12 23:03:34 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2025-12-12 23:03:31 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:30 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:25 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-12 23:02:57 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:33 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:32 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2025-12-12 23:02:30 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:29 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:25 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:12 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 23:01:49 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2025-12-12 23:01:28 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:01:14 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:00:55 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.402 |  |
| 2025-12-12 22:57:27 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.248 |  |
| 2025-12-12 22:55:31 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.248 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 22:00:51 | Horowpothana (Yan Oya) | 6.36 | 🟡 Alert | -0.021 |  |
| 2025-12-12 23:08:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2025-12-12 23:05:26 | Magura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-12 23:03:25 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-12 23:05:48 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-12 23:02:12 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-12 23:04:37 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 23:02:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:57 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:30 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:29 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:02:12 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:01:14 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:01:49 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:30 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:33 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:02:25 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:31 | Badalgama (Maha Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:59 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:03:55 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-12 22:03:31 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-12 23:01:28 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:04:03 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:06:15 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-12 23:03:34 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2025-12-12 23:03:51 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2025-12-12 23:07:33 | Panadugama (Nilwala Ganga) | 3.61 | 🟢 Normal | -0.019 |  |
| 2025-12-12 22:01:27 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-12 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2025-12-12 23:02:32 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.031 |  |
| 2025-12-12 23:03:37 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.049 |  |
| 2025-12-12 23:06:03 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | -0.067 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-12 23:04:43 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.248 |  |
| 2025-12-12 23:00:55 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.402 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)