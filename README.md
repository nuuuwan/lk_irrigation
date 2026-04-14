# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_20:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 20:11:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:10:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:09:14 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-04-14 20:08:05 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.060 |  |
| 2026-04-14 20:07:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-04-14 20:06:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:06:16 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:06:10 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-04-14 20:06:08 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:05:30 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-04-14 20:05:27 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:04:34 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-14 20:04:31 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:04:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.021 |  |
| 2026-04-14 20:04:04 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-04-14 20:03:53 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 20:03:51 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 20:03:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-14 20:03:33 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-04-14 20:02:58 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.035 |  |
| 2026-04-14 20:02:57 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-14 20:02:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-14 20:02:16 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:15 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:12 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:50 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 20:01:34 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:09 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.043 |  |
| 2026-04-14 20:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:00:43 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-14 20:00:21 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 20:00:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 20:05:30 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-04-14 20:03:53 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 20:03:51 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 20:00:21 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 20:00:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:50 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:01:34 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:15 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:04:31 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:02:16 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:10:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:06:16 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:06:37 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:05:27 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:06:08 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:11:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 20:04:34 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-04-14 20:03:44 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-04-14 20:01:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-14 19:08:30 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-14 20:02:57 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-04-14 20:03:33 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-04-14 20:04:04 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.021 |  |
| 2026-04-14 20:04:05 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.021 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-14 20:06:10 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.023 |  |
| 2026-04-14 20:09:14 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-04-14 20:07:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-04-14 20:02:58 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.035 |  |
| 2026-04-14 20:00:43 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-14 20:01:09 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.043 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 20:08:05 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.060 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |
| 2026-04-14 20:02:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-14 19:02:10 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)