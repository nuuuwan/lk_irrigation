# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_05:14:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 05:14:37 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.054 |  |
| 2026-06-24 05:13:19 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:12:38 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.042 |  |
| 2026-06-24 05:11:54 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-06-24 05:09:39 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:08:44 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-06-24 05:08:01 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-06-24 05:07:41 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:06:54 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-06-24 05:06:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-24 05:06:27 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:05:30 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.476 |  |
| 2026-06-24 05:05:29 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.039 |  |
| 2026-06-24 05:05:29 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:05:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:03:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-06-24 05:03:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:03:09 | Horowpothana (Yan Oya) | 5.38 | 🟢 Normal | 3.919 | 🔺 Rising |
| 2026-06-24 05:03:07 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:02:49 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.174 |  |
| 2026-06-24 05:02:26 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.100 |  |
| 2026-06-24 05:02:22 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.073 |  |
| 2026-06-24 05:02:21 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-24 05:02:18 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.040 |  |
| 2026-06-24 05:02:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.050 |  |
| 2026-06-24 05:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:30 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:08 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-24 05:01:00 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:00 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-24 05:00:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:59:12 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.476 |  |
| 2026-06-24 04:57:40 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:56:20 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.476 |  |
| 2026-06-24 04:55:21 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.476 |  |
| 2026-06-24 04:40:29 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 04:00:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | -0.020 |  |
| 2026-06-24 05:02:18 | Dunamale (Aththanagalu Oya) | 3.32 | 🟡 Alert | -0.040 |  |
| 2026-06-24 05:03:09 | Horowpothana (Yan Oya) | 5.38 | 🟢 Normal | 3.919 | 🔺 Rising |
| 2026-06-24 05:06:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-06-24 05:01:08 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-24 05:01:00 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-24 04:04:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 05:01:30 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:00:56 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:07:41 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:03:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:15 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:03:07 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:05:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 03:13:07 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:09:39 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:01:00 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:13:19 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-24 04:10:32 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:06:27 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 05:08:01 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-06-24 05:02:21 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 05:08:44 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.018 |  |
| 2026-06-24 04:05:32 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-06-24 05:05:29 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.039 |  |
| 2026-06-24 05:03:19 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-06-24 05:11:54 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.040 |  |
| 2026-06-24 05:12:38 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.042 |  |
| 2026-06-24 05:06:54 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.046 |  |
| 2026-06-24 05:02:10 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.050 |  |
| 2026-06-24 05:14:37 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.054 |  |
| 2026-06-24 05:02:22 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.073 |  |
| 2026-06-24 05:02:26 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.100 |  |
| 2026-06-24 05:02:49 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.174 |  |
| 2026-06-24 05:05:30 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.476 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)