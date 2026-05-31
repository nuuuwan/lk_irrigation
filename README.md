# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_00:07:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 00:07:21 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:06:34 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:05:25 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:05:19 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.030 |  |
| 2026-06-01 00:05:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-06-01 00:04:48 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:44 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:43 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:04:39 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:35 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:03:58 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 00:03:36 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-06-01 00:03:03 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 32.000 | 🔺 Rising |
| 2026-06-01 00:03:02 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:55 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-01 00:02:52 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:41 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:02:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:04 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-01 00:02:00 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:00 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 32.000 | 🔺 Rising |
| 2026-06-01 00:01:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-01 00:01:38 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:01:27 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-05-31 23:33:10 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-05-31 23:20:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 00:03:03 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 32.000 | 🔺 Rising |
| 2026-06-01 00:02:04 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-01 00:01:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-01 00:02:55 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-01 00:03:58 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:01:38 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:33 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:43 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:52 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:00 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:06:10 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:06:26 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:03:02 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:04:43 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:07 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:04:35 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:05:02 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:17:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:41 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-05-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:07:21 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-31 23:03:44 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-31 22:16:28 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:02:36 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 00:01:27 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.005 |  |
| 2026-05-31 23:33:10 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.008 |  |
| 2026-06-01 00:04:48 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:05:25 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:39 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:01:54 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:02:23 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-01 00:04:44 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-31 23:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-05-31 23:03:32 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-06-01 00:05:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-06-01 00:03:36 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-06-01 00:05:19 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.030 |  |
| 2026-05-31 23:20:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)