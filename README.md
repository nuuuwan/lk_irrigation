# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_22:05:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,290 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 22:05:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-05 22:05:40 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.145 |  |
| 2026-07-05 22:05:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:05:39 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:05:25 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-07-05 22:05:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 22:05:00 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:04:36 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:04:24 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-07-05 22:03:48 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-07-05 22:03:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:48 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:02:43 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.373 |  |
| 2026-07-05 22:02:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-07-05 22:02:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:21 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-07-05 22:02:20 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.060 |  |
| 2026-07-05 22:02:16 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:01:59 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.040 |  |
| 2026-07-05 22:01:34 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 11.036 | 🔺 Rising |
| 2026-07-05 22:01:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-07-05 22:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:00:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:59:17 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 11.036 | 🔺 Rising |
| 2026-07-05 21:58:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:21:06 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 22:01:34 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 11.036 | 🔺 Rising |
| 2026-07-05 22:05:46 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-05 21:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 22:05:00 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:00:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:03:11 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:43 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:01:44 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:01:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:05:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:08:11 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:08:25 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:03:23 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:04:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:05:39 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:03:06 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:58:08 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-05 21:01:51 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:16 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 22:02:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:00:44 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:02:48 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-05 22:02:21 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-07-05 22:04:24 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.012 |  |
| 2026-07-05 22:01:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.015 |  |
| 2026-07-05 22:05:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-07-05 22:02:29 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-07-05 22:05:25 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-07-05 21:02:54 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-07-05 22:03:48 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-07-05 22:01:59 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.040 |  |
| 2026-07-05 21:07:06 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.056 |  |
| 2026-07-05 22:02:20 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | -0.060 |  |
| 2026-07-05 22:05:40 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.145 |  |
| 2026-07-05 22:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.373 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)