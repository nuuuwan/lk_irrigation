# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_03:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 03:17:22 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 03:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:09:38 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:09:18 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:07:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-04-12 03:07:26 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 03:06:33 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:05:34 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-04-12 03:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:04:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:54 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:53 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:16 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-04-12 03:03:07 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:04 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-04-12 03:02:57 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:53 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:43 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.071 |  |
| 2026-04-12 03:02:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-12 03:02:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 03:02:09 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.013 |  |
| 2026-04-12 03:02:02 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -1.938 |  |
| 2026-04-12 03:01:59 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-04-12 03:01:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:01:41 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:01:23 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-04-12 03:01:22 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.005 |  |
| 2026-04-12 03:01:11 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-12 03:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 03:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:17:22 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 02:07:08 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-12 03:01:11 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-12 03:02:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-12 03:07:26 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 03:02:23 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 03:01:53 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:00:13 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:53 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 02:02:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:38 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:11:00 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:43 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:01:09 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:57 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:53 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:02:26 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:04:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:09:38 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 01:36:45 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:03:07 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 03:01:22 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | -0.005 |  |
| 2026-04-12 03:06:33 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:01:41 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.010 |  |
| 2026-04-12 03:03:16 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-04-12 03:02:09 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | -0.013 |  |
| 2026-04-12 03:05:34 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-04-12 03:01:59 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-04-12 03:03:04 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-04-12 03:07:33 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-04-12 03:02:39 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.071 |  |
| 2026-04-12 03:01:23 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.081 |  |
| 2026-04-12 02:04:18 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -1.565 |  |
| 2026-04-12 03:02:02 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -1.938 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)