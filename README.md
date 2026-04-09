# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_18:08:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 18:08:44 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-09 18:08:37 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-04-09 18:08:16 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:06:51 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 18:06:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:05:59 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 18:05:31 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:49 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2026-04-09 18:04:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:03 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-04-09 18:03:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.070 |  |
| 2026-04-09 18:03:48 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:03:36 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-09 18:03:19 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:02:44 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-09 18:02:44 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-09 18:02:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:12 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:02:09 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:09 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:02:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:00 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-09 18:01:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:01:34 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 18:01:31 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:01:18 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:01:08 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-09 18:00:39 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:00:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:00:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:18:45 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 18:02:00 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-09 18:08:44 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-09 18:03:36 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-09 18:01:08 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 18:02:35 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-09 18:01:34 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 18:05:59 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 18:06:51 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 18:01:49 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:00:13 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:12 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:09 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:13:34 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:44 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:00:36 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:05:31 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:01:31 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:35 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:02:01 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:09:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:00:39 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:08:16 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:06:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:03:48 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:03:19 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-09 18:02:09 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:01:18 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-04-09 18:04:49 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.013 |  |
| 2026-04-09 18:04:03 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.019 |  |
| 2026-04-09 18:02:44 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-04-09 18:08:37 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.028 |  |
| 2026-04-09 18:03:53 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.070 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-09 17:04:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)