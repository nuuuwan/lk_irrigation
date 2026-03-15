# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_23:10:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,417 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 23:10:58 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 23:07:38 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 23:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-03-15 23:06:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 23:06:11 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.044 |  |
| 2026-03-15 23:06:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:05:48 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:05:32 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:05:04 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-15 23:04:38 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:33 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-03-15 23:04:32 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:31 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:04:14 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:04:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:04:02 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-15 23:04:01 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.189 |  |
| 2026-03-15 23:03:59 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-15 23:03:39 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:03:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:03:13 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.614 | 🔺 Rising |
| 2026-03-15 23:02:52 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:02:42 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:02:32 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:53 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:51 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:43 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:34 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:01:29 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:01:19 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-15 23:01:05 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 22:27:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 23:03:13 | Peradeniya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.614 | 🔺 Rising |
| 2026-03-15 23:01:16 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-03-15 23:04:02 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-15 23:10:58 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-15 23:07:38 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 23:06:26 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 22:01:00 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:47 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:19 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:05:32 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:38 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:02:32 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:05:04 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:05 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:32 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:03:26 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:02:52 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:06:08 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:53 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:51 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:01:43 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-15 23:04:14 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:01:29 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:03:39 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-15 23:04:31 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:05:48 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:01:34 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:04:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:02:42 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-03-15 23:03:59 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-03-15 23:04:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-15 23:07:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.031 |  |
| 2026-03-15 23:04:33 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.038 |  |
| 2026-03-15 18:02:59 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.040 |  |
| 2026-03-15 23:06:11 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.044 |  |
| 2026-03-15 23:04:01 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)