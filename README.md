# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_17:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,467 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 17:26:53 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:20:19 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:16:43 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 17:15:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-19 17:13:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:11:41 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 17:10:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-02-19 17:07:56 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-19 17:06:44 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:36 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:05:29 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:28 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:09 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:05:05 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:57 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-02-19 17:04:46 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:35 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:31 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:04:25 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:03:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:03:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:03:40 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:03:20 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:02:24 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-02-19 17:02:21 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:02:14 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:02:10 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 17:02:04 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:02:02 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.051 |  |
| 2026-02-19 17:01:44 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 17:01:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2026-02-19 17:01:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:01:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:01:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:00:52 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:00:08 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 16:59:31 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-19 16:52:27 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-19 16:45:13 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 17:07:56 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-19 17:15:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-19 17:01:44 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 17:00:08 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 17:02:10 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 17:11:41 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-19 17:02:14 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:03:20 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:04:31 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:05:36 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:05:09 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 17:16:43 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 16:59:31 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:25 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:20:19 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:02:21 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:28 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:46 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:03:55 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:29 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:01:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:26:53 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:01:06 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:01:07 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:04:35 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:03:59 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:06:44 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:05:05 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:13:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:00:52 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 17:10:31 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-02-19 17:02:04 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:02:10 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:03:40 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.010 |  |
| 2026-02-19 17:04:57 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-02-19 17:02:24 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-02-19 17:02:02 | Manampitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.051 |  |
| 2026-02-19 17:01:08 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)