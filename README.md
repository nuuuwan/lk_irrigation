# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_18:31:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,093 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 18:31:48 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.013 |  |
| 2026-04-23 18:22:44 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 18:16:38 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-04-23 18:12:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-23 18:09:53 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:09:37 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-04-23 18:09:29 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 18:08:07 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:07:29 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | 0.869 | 🔺 Rising |
| 2026-04-23 18:07:05 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-23 18:06:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-23 18:05:56 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 18:05:44 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:05:33 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-23 18:05:32 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:04:58 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:04:04 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-23 18:03:53 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-23 18:03:36 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 18:03:34 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:25 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:03:01 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:02:54 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-04-23 18:02:35 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-04-23 18:01:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-23 18:01:32 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.056 |  |
| 2026-04-23 18:01:14 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:00:55 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.335 |  |
| 2026-04-23 18:00:45 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:00:39 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-04-23 18:00:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.032 |  |
| 2026-04-23 18:00:14 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-23 18:00:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 18:00:55 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.335 |  |
| 2026-04-23 18:07:29 | Thanamalwila (Kirindi Oya) | 2.38 | 🟢 Normal | 0.869 | 🔺 Rising |
| 2026-04-23 18:00:39 | Moraketiya (Walawe Ganga) | 2.25 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-04-23 18:04:04 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-23 18:00:14 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-23 18:01:39 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-04-23 18:12:22 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-23 18:07:05 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-23 18:05:33 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-23 18:01:14 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-23 18:09:29 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 18:02:35 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-23 18:22:44 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-23 18:05:56 | Giriulla (Maha Oya) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 18:03:36 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:01 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:09:53 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:05:32 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:00:45 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:34 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:25 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:08:07 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:06:45 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-04-23 18:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:05:44 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:02:54 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.011 |  |
| 2026-04-23 18:31:48 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.013 |  |
| 2026-04-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-04-23 18:03:53 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-04-23 18:00:39 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.032 |  |
| 2026-04-23 18:09:37 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.038 |  |
| 2026-04-23 18:16:38 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.051 |  |
| 2026-04-23 18:01:32 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.056 |  |
| 2026-04-23 18:00:09 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)