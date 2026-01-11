# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_11:11:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 11:11:31 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:07:50 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-01-11 11:06:53 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-01-11 11:06:52 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:06:09 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:05:58 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-11 11:05:47 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:05:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-11 11:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-01-11 11:04:52 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-01-11 11:04:49 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:04:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-01-11 11:04:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-01-11 11:04:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:04:00 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:03:59 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-01-11 11:03:41 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-01-11 11:03:28 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:27 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:03:22 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.090 |  |
| 2026-01-11 11:03:15 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.138 |  |
| 2026-01-11 11:03:14 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:02:57 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 11:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:02:23 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:02:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:01:59 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:01:54 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:53 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-01-11 11:01:35 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 11:01:34 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:28 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:15 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:06 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 11:00:10 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:46:01 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 11:01:53 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-01-11 11:02:57 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-11 11:01:06 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 11:00:10 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:28 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:34 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:06:52 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:28 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:02:23 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:04:49 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:02:24 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:15 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:01:54 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:14 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:06:09 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:03:22 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-11 10:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:11:31 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:05:26 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-11 11:05:58 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-01-11 11:04:00 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:03:27 | Manampitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:04:02 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:02:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:03:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:01:59 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:05:47 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-01-11 11:06:53 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-01-11 11:04:52 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-01-11 11:03:41 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-01-11 11:01:35 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.020 |  |
| 2026-01-11 11:03:59 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.021 |  |
| 2026-01-11 11:07:50 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-01-11 11:04:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.031 |  |
| 2026-01-11 11:04:17 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-01-11 11:04:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.039 |  |
| 2026-01-11 11:03:16 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.090 |  |
| 2026-01-11 11:03:15 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)