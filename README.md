# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_02:28:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,431 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 02:28:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:23:33 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.079 |  |
| 2026-04-05 02:12:12 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:06:44 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-04-05 02:06:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:06:33 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:06:27 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-04-05 02:06:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-05 02:04:28 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:04:24 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 02:04:14 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 02:03:39 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:03:18 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-04-05 02:03:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-05 02:02:33 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:02:32 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:02:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 02:02:01 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.160 |  |
| 2026-04-05 02:02:01 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-04-05 02:01:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:51 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:50 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 02:01:37 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.042 |  |
| 2026-04-05 02:01:29 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-04-05 02:01:23 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-05 02:01:17 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:00:26 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:00:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 01:29:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-04-05 02:06:18 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-04-05 02:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-05 02:00:15 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-05 02:01:50 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-05 02:04:14 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 02:04:24 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-05 01:01:05 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-05 02:01:17 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:00:26 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:51 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:02:32 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:01:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:28:06 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-04-05 00:01:47 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:03:39 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:02:33 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:02:34 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:06:37 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 02:12:12 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-05 01:01:54 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-04-05 02:03:08 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:04:28 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 02:01:23 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-04-05 02:06:44 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-04-05 02:02:11 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 02:01:29 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.022 |  |
| 2026-04-05 00:54:40 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-05 02:02:01 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-04-05 02:06:27 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.040 |  |
| 2026-04-05 02:03:18 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-04-05 02:01:37 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.042 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-05 02:23:33 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.079 |  |
| 2026-04-05 02:02:01 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)