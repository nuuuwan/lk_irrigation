# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_12:14:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **121,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 12:14:37 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -1.687 |  |
| 2026-04-10 12:10:11 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-10 12:08:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:08:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:08:13 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -1.687 |  |
| 2026-04-10 12:07:01 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:07:01 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:06:58 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:06:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.048 |  |
| 2026-04-10 12:05:49 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:19 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:16 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:04:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-10 12:04:50 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.038 |  |
| 2026-04-10 12:03:50 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:03:34 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 12:03:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-10 12:03:18 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-04-10 12:03:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-10 12:03:01 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:03:00 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:54 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-10 12:02:41 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:38 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:24 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 12:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 12:02:20 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:01:53 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:01:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-10 12:01:21 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-10 12:01:14 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 12:01:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.191 |  |
| 2026-04-10 12:00:57 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 12:03:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-10 12:01:14 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 12:03:34 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 12:03:00 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:08:34 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:15 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:23 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-10 11:01:03 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:06:58 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:03:01 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:20 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:03:50 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:41 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:49 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:00:57 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:08:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:34 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:07:01 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:07:01 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:16 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:05:19 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:02:38 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:01:53 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-10 12:10:11 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-04-10 12:01:42 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-10 12:02:54 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-04-10 11:00:47 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-10 12:03:20 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-10 12:01:21 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-10 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-04-10 12:02:24 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-04-10 12:04:50 | Manampitiya (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.038 |  |
| 2026-04-10 12:03:18 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.040 |  |
| 2026-04-10 12:04:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-10 12:06:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.048 |  |
| 2026-04-10 12:01:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.191 |  |
| 2026-04-10 12:14:37 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -1.687 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)