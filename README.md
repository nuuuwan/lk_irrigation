# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--17_18:05:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **154,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 18:05:44 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-05-17 18:05:41 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:05:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.148 |  |
| 2026-05-17 18:05:32 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:05:09 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.059 |  |
| 2026-05-17 18:05:03 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.060 |  |
| 2026-05-17 18:04:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:04:07 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:56 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:53 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-17 18:03:48 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-17 18:03:46 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-17 18:03:36 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:03:20 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:03:12 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:03:12 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:02:57 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.089 |  |
| 2026-05-17 18:02:54 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:02:49 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 18:02:47 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.043 |  |
| 2026-05-17 18:02:46 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 18:02:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-17 18:01:38 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:01:15 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.091 |  |
| 2026-05-17 18:00:59 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:43 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.051 |  |
| 2026-05-17 18:00:41 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:00:15 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:11 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:23:09 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:15:35 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-17 17:14:39 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-17 18:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.55 | 🟠 Minor Flood | -0.041 |  |
| 2026-05-17 18:05:44 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-05-17 18:03:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-05-17 18:03:53 | Dunamale (Aththanagalu Oya) | 3.04 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-17 18:02:49 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-17 18:02:46 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-17 18:00:11 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:04:18 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:12 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:01:38 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:59 | Galgamuwa (Mee Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:15 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:52 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:46 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:03:56 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:59 | Putupaula (Kalu Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:02:54 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-17 17:08:55 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:00:41 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-17 18:05:32 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:05:41 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:04:07 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:03:12 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:03:20 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:02:40 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-05-17 18:01:25 | Thanthirimale (Malwathu Oya) | 3.62 | 🟢 Normal | -0.020 |  |
| 2026-05-17 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:03:36 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-05-17 17:03:41 | Moragaswewa (Deduru Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-17 18:03:48 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-05-17 18:02:47 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.043 |  |
| 2026-05-17 18:00:43 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.051 |  |
| 2026-05-17 18:05:09 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.059 |  |
| 2026-05-17 18:05:03 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.060 |  |
| 2026-05-17 18:02:57 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.089 |  |
| 2026-05-17 18:01:15 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.091 |  |
| 2026-05-17 18:05:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.148 |  |
| 2026-05-17 17:02:18 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)