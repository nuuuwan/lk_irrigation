# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_04:38:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **153,077 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 04:38:05 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.013 |  |
| 2026-05-16 04:33:57 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:33:22 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-05-16 04:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.11 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-05-16 04:18:57 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-16 04:17:00 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:14:33 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-16 04:11:18 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:11:14 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.018 |  |
| 2026-05-16 04:08:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.071 |  |
| 2026-05-16 04:06:59 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:58 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:46 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:01 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:05:28 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:05:27 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.029 |  |
| 2026-05-16 04:05:26 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.029 |  |
| 2026-05-16 04:05:12 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-16 04:04:31 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.119 |  |
| 2026-05-16 04:04:20 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.041 |  |
| 2026-05-16 04:03:48 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.157 |  |
| 2026-05-16 04:03:43 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.021 |  |
| 2026-05-16 04:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:02:52 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.032 |  |
| 2026-05-16 04:02:48 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | -0.027 |  |
| 2026-05-16 04:02:38 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | -0.180 |  |
| 2026-05-16 04:02:09 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:01:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.013 |  |
| 2026-05-16 04:01:40 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.051 |  |
| 2026-05-16 04:01:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-05-16 04:01:33 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-16 04:01:16 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:01:15 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:00:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-16 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-16 04:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.11 | 🟠 Minor Flood | 0.024 | 🔺 Rising |
| 2026-05-16 04:02:48 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | -0.027 |  |
| 2026-05-16 04:05:12 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-16 03:08:28 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-16 04:18:57 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-16 04:03:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-16 03:01:47 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:01 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:17:00 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:05:28 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:59 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:01:15 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:02:09 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:33:57 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:01:16 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:06:46 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-05-16 04:00:55 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-16 04:38:05 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.013 |  |
| 2026-05-16 04:01:43 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.013 |  |
| 2026-05-16 04:11:14 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.018 |  |
| 2026-05-16 03:11:00 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.018 |  |
| 2026-05-16 04:14:33 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-05-16 04:01:33 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-05-16 04:03:43 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.021 |  |
| 2026-05-16 04:01:34 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-05-16 04:33:22 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.028 |  |
| 2026-05-16 04:05:27 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | -0.029 |  |
| 2026-05-16 04:05:26 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.029 |  |
| 2026-05-16 04:00:53 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-05-16 04:02:52 | Magura (Kalu Ganga) | 3.97 | 🟢 Normal | -0.032 |  |
| 2026-05-16 04:04:20 | Hanwella (Kelani Ganga) | 4.18 | 🟢 Normal | -0.041 |  |
| 2026-05-16 04:01:40 | Horowpothana (Yan Oya) | 2.81 | 🟢 Normal | -0.051 |  |
| 2026-05-16 04:08:38 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.071 |  |
| 2026-05-16 04:04:31 | Rathnapura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.119 |  |
| 2026-05-16 04:03:48 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.157 |  |
| 2026-05-16 04:02:38 | Moragaswewa (Deduru Oya) | 3.72 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)