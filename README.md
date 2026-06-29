# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--30_03:12:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **193,094 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 03:12:51 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-30 03:12:07 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.042 |  |
| 2026-06-30 03:08:44 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.069 |  |
| 2026-06-30 03:08:09 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 03:07:37 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-06-30 03:07:18 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.191 |  |
| 2026-06-30 03:07:14 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | -0.029 |  |
| 2026-06-30 03:06:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:06:23 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 03:06:20 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-06-30 03:06:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.249 |  |
| 2026-06-30 03:05:55 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.128 |  |
| 2026-06-30 03:05:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.057 |  |
| 2026-06-30 03:05:42 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:35 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:19 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | -0.215 |  |
| 2026-06-30 03:05:13 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:12 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-30 03:05:01 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-30 03:04:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -1.068 |  |
| 2026-06-30 03:03:51 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-06-30 03:03:41 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-06-30 03:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.068 |  |
| 2026-06-30 03:03:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:03:18 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:03:05 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 03:02:41 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:21 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-30 03:02:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:01:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:00:56 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:00:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 02:57:47 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-30 03:12:51 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-30 03:00:42 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-30 03:06:23 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-30 03:08:09 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-30 02:11:12 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-30 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 03:03:05 | Ellagawa (Kalu Ganga) | 7.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-30 03:05:12 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:20 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:41 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:01:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:01:22 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:00:56 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:03:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:06:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:42 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:02:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:35 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:13 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-30 03:05:01 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-06-30 03:07:37 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-06-30 03:02:21 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-06-30 03:03:51 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-06-30 03:06:20 | Baddegama (Gin Ganga) | 2.93 | 🟢 Normal | -0.021 |  |
| 2026-06-30 03:07:14 | Panadugama (Nilwala Ganga) | 4.09 | 🟢 Normal | -0.029 |  |
| 2026-06-30 03:03:41 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-06-30 03:12:07 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.042 |  |
| 2026-06-30 03:05:50 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.057 |  |
| 2026-06-30 03:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.068 |  |
| 2026-06-30 03:08:44 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.069 |  |
| 2026-06-30 03:05:55 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | -0.128 |  |
| 2026-06-30 03:07:18 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.191 |  |
| 2026-06-30 03:05:19 | Rathnapura (Kalu Ganga) | 4.84 | 🟢 Normal | -0.215 |  |
| 2026-06-30 03:06:08 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.249 |  |
| 2026-06-30 03:04:06 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -1.068 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)