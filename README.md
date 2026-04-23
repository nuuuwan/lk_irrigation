# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_10:24:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,768 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 10:24:45 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:20:08 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:20:08 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.102 |  |
| 2026-04-23 10:15:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.017 |  |
| 2026-04-23 10:13:57 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-23 10:13:29 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:07:57 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.293 |  |
| 2026-04-23 10:07:57 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-04-23 10:07:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.518 |  |
| 2026-04-23 10:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 10:07:13 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.103 |  |
| 2026-04-23 10:06:49 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.047 |  |
| 2026-04-23 10:06:15 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-04-23 10:04:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:04:15 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-23 10:03:56 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:03:50 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:03:05 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-23 10:02:53 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 10:02:49 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:02:48 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 10:02:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:02:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 10:02:31 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:02:20 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:02:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:52 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 10:01:45 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-04-23 10:01:41 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:01:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 10:01:36 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.062 |  |
| 2026-04-23 10:01:35 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-23 10:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:01:29 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:23 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-04-23 10:01:20 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-04-23 10:01:13 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:00:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-04-23 10:00:16 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 10:13:57 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-23 10:02:40 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 10:01:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 10:02:48 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 10:01:38 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-23 10:07:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 10:02:53 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 10:02:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:24:45 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:20:08 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:03:50 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:03:56 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:02:31 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:13 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:29 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:01:52 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:02:20 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 10:06:15 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-04-23 10:04:34 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:02:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:01:41 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:00:16 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:02:49 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-23 10:15:29 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.017 |  |
| 2026-04-23 10:04:15 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-04-23 10:01:35 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.021 |  |
| 2026-04-23 10:03:05 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-23 10:01:45 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.040 |  |
| 2026-04-23 10:07:57 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.040 |  |
| 2026-04-23 10:00:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.046 |  |
| 2026-04-23 10:06:49 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.047 |  |
| 2026-04-23 10:01:20 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-04-23 10:01:23 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-04-23 10:01:36 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.062 |  |
| 2026-04-23 10:20:08 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.102 |  |
| 2026-04-23 10:07:13 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.103 |  |
| 2026-04-23 10:07:57 | Glencourse (Kelani Ganga) | 9.21 | 🟢 Normal | -0.293 |  |
| 2026-04-23 10:07:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.518 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)