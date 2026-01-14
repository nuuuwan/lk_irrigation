# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_15:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 15:09:42 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:09:07 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:07:43 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.029 |  |
| 2026-01-14 15:06:55 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:26 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 15:06:24 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:05 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:05:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-14 15:05:39 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:05:28 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-14 15:05:12 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-01-14 15:04:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:04:35 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-01-14 15:04:24 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:04:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:03:43 | Thanthirimale (Malwathu Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-01-14 15:03:43 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-01-14 15:03:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:03:29 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:03:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-01-14 15:03:24 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.054 |  |
| 2026-01-14 15:03:19 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-14 15:03:12 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:02:52 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.024 |  |
| 2026-01-14 15:02:47 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:02:45 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:02:26 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:02:24 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-14 15:02:12 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:02:04 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:52 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:01:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:30 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:01:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:00:41 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-01-14 15:00:16 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.097 |  |
| 2026-01-14 15:00:07 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-14 14:41:41 | Horowpothana (Yan Oya) | 3.04 | 🟢 Normal | -0.097 |  |
| 2026-01-14 14:28:18 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 15:03:19 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-01-14 15:05:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-14 15:02:24 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-14 15:06:25 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-14 15:00:07 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:02:04 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:23 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:05:39 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:05 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:55 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:04:02 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:24 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:02:45 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:01:47 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:09:42 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:06:26 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:09:07 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:04:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-14 15:00:41 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-01-14 15:05:12 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-01-14 15:03:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:04:24 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:02:26 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:01:52 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:01:30 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-14 15:03:43 | Thanthirimale (Malwathu Oya) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-01-14 15:02:47 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:03:12 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-01-14 15:04:35 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-01-14 15:02:52 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.024 |  |
| 2026-01-14 15:07:43 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | -0.029 |  |
| 2026-01-14 15:03:27 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-01-14 15:03:24 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.054 |  |
| 2026-01-14 15:05:28 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-14 15:03:43 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-01-14 15:00:16 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)