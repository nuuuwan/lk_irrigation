# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_17:29:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 17:29:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:10:13 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-02-13 17:07:41 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-13 17:07:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:07:18 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:07:00 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:06:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-13 17:06:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-02-13 17:06:05 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:05:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:05:22 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-02-13 17:05:19 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-02-13 17:04:57 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:04:50 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.037 |  |
| 2026-02-13 17:04:49 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-02-13 17:04:42 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.029 |  |
| 2026-02-13 17:04:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:04:09 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-02-13 17:04:06 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:56 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.039 |  |
| 2026-02-13 17:03:23 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:15 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:06 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:40 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:34 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:02:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:02:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-02-13 17:01:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:01:39 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:01:35 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:01:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:00:59 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 17:00:43 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:00:35 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 17:06:56 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-02-13 17:00:59 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 17:07:41 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-13 17:00:33 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 16:08:25 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 17:01:35 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:07:38 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:01:39 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:23 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:06 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:29:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:04:06 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:34 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:05:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:56 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:07:00 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:04:57 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:03:56 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:07:18 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:40 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:06:05 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:04:49 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-02-13 17:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:04:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:02:22 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:02:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:01:26 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-13 17:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.012 |  |
| 2026-02-13 17:04:42 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.029 |  |
| 2026-02-13 17:10:13 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.029 |  |
| 2026-02-13 17:00:43 | Weraganthota (Mahaweli Ganga) | -2.37 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:01:49 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:02:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-02-13 17:06:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-02-13 17:05:22 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | -0.032 |  |
| 2026-02-13 17:04:50 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.037 |  |
| 2026-02-13 17:05:19 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.039 |  |
| 2026-02-13 17:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.039 |  |
| 2026-02-13 17:04:09 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)