# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_18:15:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,208 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 18:15:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:14:14 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-01 18:07:46 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:07:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:06:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 18:06:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-01 18:06:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:09 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.100 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:04:54 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-01 18:04:40 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 18:04:30 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 18:04:26 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-01 18:04:18 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.023 |  |
| 2026-05-01 18:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:03:16 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 18:03:15 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.012 |  |
| 2026-05-01 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:02:56 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:02:50 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-05-01 18:02:50 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-01 18:02:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:35 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:23 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2026-05-01 18:02:07 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:01:42 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:01:42 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.050 |  |
| 2026-05-01 18:01:39 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:01:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:00:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.091 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 18:00:24 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:00:15 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.062 |  |
| 2026-05-01 18:00:12 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 18:06:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-01 18:02:50 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-01 18:04:30 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-01 17:03:21 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-01 18:04:26 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-01 18:04:40 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 18:03:16 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-01 18:04:54 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-01 18:06:32 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-01 18:00:12 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:01:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:07:46 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:00:24 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:37 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:37 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:03:25 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:23 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:06:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:15:11 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:01:42 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:35 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:02:56 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:02:07 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:07:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:01:39 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:14:14 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.011 |  |
| 2026-05-01 18:03:15 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.012 |  |
| 2026-05-01 18:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | -0.021 |  |
| 2026-05-01 18:02:50 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-05-01 18:04:18 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.023 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-01 18:01:42 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.050 |  |
| 2026-05-01 18:00:15 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.062 |  |
| 2026-05-01 18:00:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.091 |  |
| 2026-05-01 18:05:09 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)