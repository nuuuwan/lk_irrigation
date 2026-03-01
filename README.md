# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_12:20:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 12:20:30 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:10:59 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 12:09:55 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:09:51 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:09:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:08:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.035 |  |
| 2026-03-01 12:08:18 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:07:30 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-01 12:06:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 12:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.049 |  |
| 2026-03-01 12:05:31 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:55 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:46 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:04:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:23 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:20 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-03-01 12:03:42 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:03:37 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 12:03:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-03-01 12:03:31 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:21 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-01 12:03:21 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:03:02 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:02:58 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:02:48 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.023 |  |
| 2026-03-01 12:02:21 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:56 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:01:53 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 12:01:53 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:51 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.110 |  |
| 2026-03-01 12:01:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:01:50 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:42 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-03-01 12:01:38 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.023 |  |
| 2026-03-01 12:01:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:03 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 12:03:21 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-03-01 12:06:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-01 12:03:37 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-01 12:10:59 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-01 12:01:53 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-01 12:01:56 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:03 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:30 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:05:31 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:02:21 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:02 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:09:35 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:23 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:20:30 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:20 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:50 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:31 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:09:55 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:08:18 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:04:55 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:53 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:02:58 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:01:22 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 12:03:47 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-03-01 12:03:21 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:01:53 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:01:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:03:42 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:04:46 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-01 12:03:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.011 |  |
| 2026-03-01 12:01:42 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-03-01 12:07:30 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-01 12:02:48 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.023 |  |
| 2026-03-01 12:01:38 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.023 |  |
| 2026-03-01 12:08:50 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.035 |  |
| 2026-03-01 12:06:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.049 |  |
| 2026-03-01 12:01:51 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)