# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_05:15:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,450 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 05:15:59 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:10:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:09:38 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.055 |  |
| 2026-03-06 05:09:00 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.043 |  |
| 2026-03-06 05:08:33 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:08:08 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 05:07:08 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-03-06 05:06:48 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 05:06:20 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:05:58 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:05:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.125 |  |
| 2026-03-06 05:05:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:04:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:04:58 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:04:55 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.009 |  |
| 2026-03-06 05:04:31 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-03-06 05:03:43 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:03:27 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:03:20 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:02:53 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:02:28 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 05:02:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -1.510 |  |
| 2026-03-06 05:01:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:01:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -1.035 |  |
| 2026-03-06 05:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:00:36 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.082 |  |
| 2026-03-06 05:00:35 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-06 05:00:22 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:59:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -1.510 |  |
| 2026-03-06 04:38:47 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 04:06:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-03-05 18:00:12 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-06 05:00:35 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-06 04:15:42 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-06 05:06:48 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-06 05:08:08 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 05:02:28 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 05:01:43 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:15:59 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:03:27 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:01:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:01:17 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:08:33 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:00:55 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:06:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:05:58 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:03:43 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:00:22 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:09:38 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:05:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:10:00 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:02:53 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:04:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:00:43 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:01:59 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:06:20 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-06 05:04:55 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | -0.009 |  |
| 2026-03-06 05:03:20 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:01:27 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:04:58 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-06 05:04:31 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-03-06 04:02:19 | Norwood (Kelani Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-03-06 05:09:00 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.043 |  |
| 2026-03-06 05:09:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.055 |  |
| 2026-03-06 05:07:08 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.075 |  |
| 2026-03-06 05:00:36 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.082 |  |
| 2026-03-06 05:05:39 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.125 |  |
| 2026-03-06 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.21 | 🟢 Normal | -1.035 |  |
| 2026-03-06 05:02:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -1.510 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)