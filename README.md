# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_04:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,199 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 04:18:04 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:18:03 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:18:02 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:14:53 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:13:09 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:11:03 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.005 |  |
| 2026-02-07 04:09:19 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 04:07:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-07 04:07:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:07:02 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-07 04:06:24 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:06:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.037 |  |
| 2026-02-07 04:06:10 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:05:33 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:04:50 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-02-07 04:04:23 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.003 |  |
| 2026-02-07 04:04:20 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.015 |  |
| 2026-02-07 04:03:38 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:03:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:03:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:03:08 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:02:37 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:02:33 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.090 |  |
| 2026-02-07 04:02:20 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.037 |  |
| 2026-02-07 04:01:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:01:56 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 04:01:46 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:01:21 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-02-07 04:01:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:01:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:00:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 03:27:49 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 03:12:27 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.430 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-07 04:07:02 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-07 04:07:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-02-07 03:02:33 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-07 04:09:19 | Baddegama (Gin Ganga) | 1.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 04:01:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:03:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:04:57 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:18:04 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:03:08 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:06:24 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:00:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:14:53 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:07:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:01:21 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:02:37 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-06 18:03:13 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:05:33 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:13:09 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:03:38 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 04:04:23 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.003 |  |
| 2026-02-07 04:11:03 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.005 |  |
| 2026-02-07 04:03:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:06:10 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:01:01 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:02:48 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:01:46 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 04:04:20 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.015 |  |
| 2026-02-07 03:11:26 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-07 04:01:56 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 03:27:49 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-02-07 04:06:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.037 |  |
| 2026-02-06 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.039 |  |
| 2026-02-07 04:04:50 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-02-07 04:01:21 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-02-07 04:02:33 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | -0.090 |  |
| 2026-02-07 03:02:57 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)