# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_22:20:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 22:20:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.023 |  |
| 2026-02-11 22:09:31 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-11 22:08:14 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:07:31 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.100 |  |
| 2026-02-11 22:07:17 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-02-11 22:07:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:06:06 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-11 22:05:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-02-11 22:05:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:05:31 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-02-11 22:05:28 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 22:05:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.038 |  |
| 2026-02-11 22:05:17 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:05:04 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.041 |  |
| 2026-02-11 22:04:58 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:04:53 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:03:35 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:03:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:03:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:45 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-02-11 22:02:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:23 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:09 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:09 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:02 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:01:48 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:36 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:32 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:06 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:00:51 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-11 22:00:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:00:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 22:07:17 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-02-11 22:00:51 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-11 22:06:06 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-11 22:05:28 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 22:09:31 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-11 22:00:12 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:04:58 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-11 21:02:16 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:48 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:00:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:32 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:23 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:36 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:32 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:03:35 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:05:39 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:09 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:04:53 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:03:10 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:07:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:02:09 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:08:14 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:02:02 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:03:18 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:05:17 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:04:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:01:06 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-11 22:02:45 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | -0.011 |  |
| 2026-02-11 22:20:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.023 |  |
| 2026-02-11 22:05:31 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2026-02-11 22:05:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-02-11 22:05:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.038 |  |
| 2026-02-11 22:05:04 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | -0.041 |  |
| 2026-02-11 22:07:31 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)