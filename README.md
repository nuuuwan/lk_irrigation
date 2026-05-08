# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_10:42:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,085 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 10:42:41 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:19:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-08 10:12:05 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-08 10:07:54 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-08 10:07:00 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.167 |  |
| 2026-05-08 10:06:27 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:06:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-05-08 10:06:26 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.123 |  |
| 2026-05-08 10:05:59 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.157 |  |
| 2026-05-08 10:05:54 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.147 |  |
| 2026-05-08 10:05:48 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.038 |  |
| 2026-05-08 10:04:42 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 10:04:37 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-05-08 10:04:33 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-08 10:04:22 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-08 10:04:10 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | -0.119 |  |
| 2026-05-08 10:03:54 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:03:53 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.195 |  |
| 2026-05-08 10:03:25 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:03:24 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.049 |  |
| 2026-05-08 10:03:23 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-08 10:03:19 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:03:08 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-05-08 10:02:26 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 10:02:15 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:02:05 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | -0.074 |  |
| 2026-05-08 10:01:59 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-05-08 10:01:43 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.050 |  |
| 2026-05-08 10:01:36 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.046 |  |
| 2026-05-08 10:01:35 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:01:32 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-08 10:01:32 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:01:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-05-08 10:01:16 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.067 |  |
| 2026-05-08 10:01:14 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-08 10:00:59 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-05-08 10:00:58 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 10:00:55 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 10:07:54 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-08 10:04:22 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-08 10:04:42 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 10:01:14 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-05-08 10:02:26 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-08 10:00:58 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 10:12:05 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-08 10:19:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-08 10:00:55 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:03:54 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:42:41 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:01:32 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:06:27 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-08 10:03:23 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-08 10:01:32 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-08 10:01:59 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-05-08 10:04:33 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-05-08 10:04:37 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-05-08 10:01:35 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:02:15 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:03:25 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:03:19 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-05-08 10:01:24 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | -0.021 |  |
| 2026-05-08 10:06:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-05-08 10:05:48 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.038 |  |
| 2026-05-08 10:00:59 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.040 |  |
| 2026-05-08 10:01:36 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.046 |  |
| 2026-05-08 10:03:24 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | -0.049 |  |
| 2026-05-08 10:01:43 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.050 |  |
| 2026-05-08 10:01:16 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.067 |  |
| 2026-05-08 10:02:05 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | -0.074 |  |
| 2026-05-08 10:03:08 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-05-08 10:04:10 | Hanwella (Kelani Ganga) | 2.41 | 🟢 Normal | -0.119 |  |
| 2026-05-08 10:06:26 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.123 |  |
| 2026-05-08 10:05:54 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.147 |  |
| 2026-05-08 10:05:59 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.157 |  |
| 2026-05-08 10:07:00 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.167 |  |
| 2026-05-08 10:03:53 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)