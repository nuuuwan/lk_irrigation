# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_05:23:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 05:23:18 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.000 |  |
| 2026-05-15 05:23:05 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.032 |  |
| 2026-05-15 05:22:53 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-15 05:12:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-15 05:12:17 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-05-15 05:11:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:11:18 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-05-15 05:09:20 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-05-15 05:09:20 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-05-15 05:09:00 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-15 05:08:49 | Dunamale (Aththanagalu Oya) | 4.65 | 🟠 Minor Flood | 0.058 | 🔺 Rising |
| 2026-05-15 05:08:40 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:07:57 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-05-15 05:07:40 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-05-15 05:06:35 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:06:28 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | -0.005 |  |
| 2026-05-15 05:05:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-05-15 05:05:39 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2026-05-15 05:05:22 | Baddegama (Gin Ganga) | 3.20 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2026-05-15 05:04:44 | Hanwella (Kelani Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:04:04 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 05:04:02 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:03:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:03:35 | Glencourse (Kelani Ganga) | 13.92 | 🟢 Normal | -0.226 |  |
| 2026-05-15 05:03:33 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:03:19 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-15 05:02:58 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.069 |  |
| 2026-05-15 05:02:57 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | -0.030 |  |
| 2026-05-15 05:02:51 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 05:02:49 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 05:01:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-15 05:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 05:01:47 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-05-15 05:01:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.130 |  |
| 2026-05-15 05:01:01 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.133 |  |
| 2026-05-15 05:00:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 04:51:59 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.130 |  |
| 2026-05-15 04:49:19 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 05:08:49 | Dunamale (Aththanagalu Oya) | 4.65 | 🟠 Minor Flood | 0.058 | 🔺 Rising |
| 2026-05-15 05:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.76 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-15 05:23:18 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.000 |  |
| 2026-05-15 05:05:39 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | 6.353 | 🔺 Rising |
| 2026-05-15 05:09:20 | Moragaswewa (Deduru Oya) | 2.90 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-05-15 05:11:18 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-05-15 05:22:53 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-15 05:09:00 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-15 05:12:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-15 05:04:04 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 05:02:49 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 05:02:51 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:00:37 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:03:33 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:04:44 | Hanwella (Kelani Ganga) | 6.20 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:08:40 | Ellagawa (Kalu Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:03:58 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:06:35 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:11:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-05-15 05:04:02 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-15 03:16:08 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | -0.005 |  |
| 2026-05-15 05:06:28 | Katharagama (Menik Ganga) | 0.85 | 🟢 Normal | -0.005 |  |
| 2026-05-15 05:07:40 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-05-15 05:01:52 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-05-15 05:03:19 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-15 05:12:17 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-05-15 05:05:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-05-15 05:02:57 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | -0.030 |  |
| 2026-05-15 05:23:05 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.032 |  |
| 2026-05-15 05:07:57 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-05-15 05:01:47 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-05-15 05:02:58 | Deraniyagala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.069 |  |
| 2026-05-15 05:09:20 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-15 05:01:12 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.130 |  |
| 2026-05-15 05:01:01 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.133 |  |
| 2026-05-15 05:03:35 | Glencourse (Kelani Ganga) | 13.92 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)