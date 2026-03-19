# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_11:24:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,548 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 11:24:23 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:10:00 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:08:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-03-19 11:08:42 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-03-19 11:08:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.059 |  |
| 2026-03-19 11:08:24 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 11:08:18 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-03-19 11:08:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:06:00 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:56 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.048 |  |
| 2026-03-19 11:05:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-03-19 11:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.067 |  |
| 2026-03-19 11:05:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-19 11:05:09 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.057 |  |
| 2026-03-19 11:04:55 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:04:03 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:03:35 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:03:16 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.043 |  |
| 2026-03-19 11:03:03 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:02:54 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:53 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:02:51 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:30 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:25 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 11:02:23 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-19 11:02:13 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-19 11:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:34 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:30 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-03-19 11:01:23 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:17 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-19 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:06 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 11:01:01 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:00:13 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 10:58:58 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 11:02:23 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-19 11:05:36 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-03-19 11:01:30 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-03-19 11:02:13 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-19 11:01:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-19 11:08:24 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 11:02:25 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-19 11:01:06 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 11:02:53 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:03:35 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:03:03 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 11:00:13 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:51 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:24:23 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:30 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:02:54 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:34 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:10:00 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:04:55 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:04:03 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:17 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:20 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:06:00 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:01:01 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:08:00 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-19 11:05:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-19 11:08:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-03-19 11:08:18 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.029 |  |
| 2026-03-19 11:03:16 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.043 |  |
| 2026-03-19 11:05:56 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.048 |  |
| 2026-03-19 11:08:42 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-03-19 11:05:09 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.057 |  |
| 2026-03-19 11:08:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.059 |  |
| 2026-03-19 11:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)