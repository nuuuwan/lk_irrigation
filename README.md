# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_04:52:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 04:52:59 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.265 |  |
| 2026-04-12 04:50:43 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.265 |  |
| 2026-04-12 04:47:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:28:11 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.007 |  |
| 2026-04-12 04:23:02 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.007 |  |
| 2026-04-12 04:11:42 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:09:13 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.082 |  |
| 2026-04-12 04:07:10 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -11.368 |  |
| 2026-04-12 04:06:51 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -11.368 |  |
| 2026-04-12 04:06:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-12 04:06:00 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-04-12 04:05:36 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:05:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:05:03 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 04:04:38 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.071 |  |
| 2026-04-12 04:04:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-12 04:04:29 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:03:46 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.003 |  |
| 2026-04-12 04:03:33 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:03:26 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:03:22 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:57 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:45 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:39 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.079 |  |
| 2026-04-12 04:02:16 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:08 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.059 |  |
| 2026-04-12 04:01:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:50 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-12 04:01:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:42 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:18 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:13 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:59 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:56 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:47 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 03:10:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.311 | 🔺 Rising |
| 2026-04-12 03:17:22 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-12 04:05:03 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 04:00:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:47:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:04:29 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:16 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:05:36 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-11 18:03:33 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:02:57 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:56 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:03:22 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:05:05 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:03:33 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:55 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:01:18 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:59 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:00:47 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:11:42 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 04:03:46 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | -0.003 |  |
| 2026-04-12 04:28:11 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.007 |  |
| 2026-04-12 04:23:02 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.007 |  |
| 2026-04-12 04:03:26 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-11 18:00:38 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:13 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:01:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-04-12 04:06:00 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-04-12 04:04:29 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-12 04:01:50 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-04-12 04:06:15 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-04-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.040 |  |
| 2026-04-12 04:02:05 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.059 |  |
| 2026-04-12 04:04:38 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.071 |  |
| 2026-04-12 04:02:39 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.079 |  |
| 2026-04-12 04:09:13 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.082 |  |
| 2026-04-12 04:52:59 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | -0.265 |  |
| 2026-04-12 04:07:10 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -11.368 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)