# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--05_14:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **64,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 14:14:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.027 |  |
| 2026-02-05 14:13:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-05 14:12:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-05 14:10:01 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:09:47 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-02-05 14:09:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-02-05 14:07:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:05:23 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:05:17 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:04:09 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.095 |  |
| 2026-02-05 14:04:05 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:55 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 14:03:49 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:40 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:32 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-02-05 14:03:25 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:16 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:59 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.042 |  |
| 2026-02-05 14:02:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-05 14:02:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 14:02:27 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-02-05 14:02:24 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-02-05 14:02:21 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-05 14:02:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:59 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:42 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:15 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:00:52 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-05 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.084 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-05 14:02:24 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-02-05 14:02:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-05 06:07:34 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-05 14:00:52 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-05 14:03:55 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-05 14:02:31 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-05 14:01:42 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:15 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:21 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:33 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:04:05 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:07:08 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:05:23 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:16 | Dunamale (Aththanagalu Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:49 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:02:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:25 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:03:40 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:10:01 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-05 14:01:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-05 14:13:38 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-05 14:09:33 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-02-05 14:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-05 14:02:27 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-02-05 12:01:29 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.012 |  |
| 2026-02-05 14:09:47 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-02-05 14:12:29 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-02-05 14:03:32 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.026 |  |
| 2026-02-05 14:14:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.027 |  |
| 2026-02-05 14:02:59 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.042 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-05 14:00:11 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.084 |  |
| 2026-02-05 14:04:09 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.095 |  |
| 2026-02-03 22:06:20⌛ | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)