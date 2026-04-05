# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_21:12:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 21:12:14 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.038 |  |
| 2026-04-05 21:10:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-05 21:10:06 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:09:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 21:08:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.092 |  |
| 2026-04-05 21:07:04 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.009 |  |
| 2026-04-05 21:06:11 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.124 |  |
| 2026-04-05 21:06:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-05 21:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 21:05:43 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:05:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 21:05:04 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:05:03 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.042 |  |
| 2026-04-05 21:04:52 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-05 21:04:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.050 |  |
| 2026-04-05 21:03:48 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:03:37 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-04-05 21:03:29 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-04-05 21:03:02 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-04-05 21:02:53 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-04-05 21:02:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:25 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:58 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 21:01:51 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:48 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:48 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:38 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:24 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-04-05 21:01:06 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-04-05 21:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:00:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:59:07 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:53:47 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:29:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 21:01:58 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 21:05:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 21:05:47 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-05 21:00:10 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:38 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:09:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:27 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:05:04 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 20:59:07 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:48 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:03:48 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:25 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:10:06 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:23 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:48 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:05:43 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:02:26 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 21:01:51 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 19:18:54 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.008 |  |
| 2026-04-05 21:07:04 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.009 |  |
| 2026-04-05 21:04:52 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 21:03:29 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.012 |  |
| 2026-04-05 21:06:07 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-05 21:10:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-04-05 21:01:24 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-04-05 21:03:02 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-04-05 21:01:06 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.031 |  |
| 2026-04-05 21:02:53 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-04-05 21:12:14 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.038 |  |
| 2026-04-05 21:05:03 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.042 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 21:04:12 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.050 |  |
| 2026-04-05 21:03:37 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-04-05 21:08:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.081 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 21:08:04 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.092 |  |
| 2026-04-05 21:06:11 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)