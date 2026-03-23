# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_12:19:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,160 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 12:19:57 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:15:26 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |
| 2026-03-23 12:09:40 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:07:05 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.068 |  |
| 2026-03-23 12:05:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:04:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-03-23 12:04:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:03:53 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:03:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:03:27 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:03:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:59 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-03-23 12:02:54 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:51 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:39 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 12:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:02:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:26 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:12 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:08 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:01:49 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-23 12:01:44 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-03-23 12:01:41 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:01:35 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.084 |  |
| 2026-03-23 12:01:34 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.098 |  |
| 2026-03-23 12:01:33 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:31 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:29 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:28 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 12:01:23 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:06 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:00:23 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:00:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-23 11:29:56 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 12:00:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-23 12:01:49 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-23 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:02:38 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:03:27 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-23 12:02:39 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-23 12:01:28 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 12:02:08 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:12 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:34 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:31 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:05:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:51 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:03:53 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:29 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:09:40 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:33 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 11:07:31 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:44 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:26 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:54 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:02:26 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:06 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:19:57 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:01:23 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:03:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:00:23 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-23 12:03:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:04:11 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:01:41 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-23 12:02:59 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-03-23 12:15:26 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.034 |  |
| 2026-03-23 12:01:44 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.041 |  |
| 2026-03-23 11:17:44 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.042 |  |
| 2026-03-23 12:04:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-03-23 12:07:05 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.068 |  |
| 2026-03-23 12:01:35 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.084 |  |
| 2026-03-23 12:01:33 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)