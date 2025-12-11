# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_21:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 21:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-11 21:15:13 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2025-12-11 21:11:40 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.033 |  |
| 2025-12-11 21:11:02 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.009 |  |
| 2025-12-11 21:09:09 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:36 | Thaldena (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-11 21:07:05 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:06:52 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.006 |  |
| 2025-12-11 21:05:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:04:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.107 |  |
| 2025-12-11 21:04:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:04:12 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2025-12-11 21:04:11 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:04:05 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-11 21:03:40 | Nakkala (Kumbukkan Oya) | 2.12 | 🟢 Normal | 0.638 | 🔺 Rising |
| 2025-12-11 21:03:36 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | -0.103 |  |
| 2025-12-11 21:03:35 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2025-12-11 21:03:31 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:03:16 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2025-12-11 21:02:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-11 21:02:56 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:02:37 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 21:02:24 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:02:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-11 21:02:00 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:01:38 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:01:32 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:01:23 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:01:21 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:00:24 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.082 |  |
| 2025-12-11 21:00:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 21:03:40 | Nakkala (Kumbukkan Oya) | 2.12 | 🟢 Normal | 0.638 | 🔺 Rising |
| 2025-12-11 21:04:12 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2025-12-11 21:03:35 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2025-12-11 21:03:16 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 21:07:36 | Thaldena (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-11 21:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-11 21:02:37 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 21:02:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-11 20:10:18 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-11 21:01:23 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:00:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:05:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 21:01:21 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:02:00 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:02:24 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:09:09 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:15:13 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:01:38 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:07:05 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:06:52 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 21:06:12 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.006 |  |
| 2025-12-11 21:11:02 | Horowpothana (Yan Oya) | 4.20 | 🟢 Normal | -0.009 |  |
| 2025-12-11 21:04:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:03:31 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:02:56 | Hanwella (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:04:11 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-11 20:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-11 21:04:05 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.011 |  |
| 2025-12-11 21:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-11 21:11:40 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.033 |  |
| 2025-12-11 21:02:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.063 |  |
| 2025-12-11 21:00:24 | Siyambalanduwa (Heda Oya) | 1.72 | 🟢 Normal | -0.082 |  |
| 2025-12-11 21:03:36 | Padiyathalawa (Maduru Oya) | 3.50 | 🟢 Normal | -0.103 |  |
| 2025-12-11 21:04:27 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)