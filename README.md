# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_21:10:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,318 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 21:10:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:09:04 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:08:28 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 21:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-05-01 21:06:52 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-01 21:06:30 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.051 |  |
| 2026-05-01 21:06:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.053 |  |
| 2026-05-01 21:05:45 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:05:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 21:05:15 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-05-01 21:05:06 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-05-01 21:04:46 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:57 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.040 |  |
| 2026-05-01 21:03:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.058 |  |
| 2026-05-01 21:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-01 21:02:52 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-01 21:02:49 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-05-01 21:02:48 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:37 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.030 |  |
| 2026-05-01 21:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:23 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:07 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:02:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-05-01 21:02:03 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:02:02 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:01:38 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 21:01:37 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:01:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 21:00:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:00:00 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 21:02:58 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-01 21:02:52 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-01 21:05:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 21:01:38 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-01 21:01:09 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-01 21:08:28 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 21:00:15 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:20 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:10:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:09:04 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:04:46 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:03:59 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:48 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:05:45 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:02:23 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-05-01 21:02:07 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:01:37 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:02:02 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 19:01:07 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:02:03 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-05-01 21:05:15 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.011 |  |
| 2026-05-01 21:00:00 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.018 |  |
| 2026-05-01 21:06:52 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-05-01 21:02:49 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | -0.022 |  |
| 2026-05-01 21:02:37 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.030 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 21:05:06 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-05-01 21:03:57 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.040 |  |
| 2026-05-01 21:02:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.043 |  |
| 2026-05-01 21:06:30 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.051 |  |
| 2026-05-01 21:06:08 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.053 |  |
| 2026-05-01 21:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)