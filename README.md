# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_03:46:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,885 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 03:46:57 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:46:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-03-01 03:36:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:36:10 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:22:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:13:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:10:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:09:14 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-01 03:08:58 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:33 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:22 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:18 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:12 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:19 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-01 03:06:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:00 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:26 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-03-01 03:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:19 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:12 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-03-01 03:02:23 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:02:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 03:02:09 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.003 |  |
| 2026-03-01 03:02:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:01:36 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:01:33 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.159 |  |
| 2026-03-01 03:01:10 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-03-01 02:59:52 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 00:16:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-02-28 18:00:50 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-01 01:42:15 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-03-01 03:02:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 03:02:09 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.003 |  |
| 2026-03-01 01:01:54 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:36:33 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:08:58 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:02:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:12 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:46:57 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:04:16 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 00:08:53 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:10:06 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:26 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:12 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-01 02:03:54 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:22 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:03:19 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:06:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:22:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:01:36 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:13:20 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-28 18:17:10 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:33 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-01 01:34:47 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:02:23 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 03:07:18 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 02:08:52 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-01 03:09:14 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-03-01 02:02:32 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | -0.010 |  |
| 2026-03-01 03:03:25 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.012 |  |
| 2026-03-01 03:46:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.018 |  |
| 2026-03-01 03:06:19 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-03-01 03:03:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.032 |  |
| 2026-03-01 03:01:33 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)