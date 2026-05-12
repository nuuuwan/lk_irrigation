# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_15:07:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,888 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 15:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:07:01 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 15:06:54 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-05-12 15:06:16 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.087 |  |
| 2026-05-12 15:06:02 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:05:41 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-05-12 15:05:05 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:05:03 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 15:04:23 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 15:04:12 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-12 15:04:09 | Katharagama (Menik Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:04:04 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.032 |  |
| 2026-05-12 15:03:52 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-05-12 15:03:16 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-12 15:03:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-12 15:03:08 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-05-12 15:03:02 | Galgamuwa (Mee Oya) | 1.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 15:03:00 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:02:49 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 15:01:51 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:01:48 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.089 |  |
| 2026-05-12 15:01:47 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:01:27 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:24 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:01:22 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 15:01:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:07 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-12 15:01:07 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.053 |  |
| 2026-05-12 15:00:57 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.030 |  |
| 2026-05-12 15:00:56 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 1.972 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 15:00:56 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 1.972 | 🔺 Rising |
| 2026-05-12 15:01:07 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-05-12 14:14:20 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-12 15:03:02 | Galgamuwa (Mee Oya) | 1.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-12 14:05:20 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-12 15:07:01 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 15:05:03 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-12 15:04:23 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 15:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 15:01:51 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 14:05:53 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:02:49 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:05:05 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:01:47 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:01:24 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:10:59 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-05-12 15:06:54 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-05-12 15:03:10 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-05-12 15:04:12 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-12 15:03:16 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-12 14:11:42 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.017 |  |
| 2026-05-12 14:09:25 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.018 |  |
| 2026-05-12 15:04:09 | Katharagama (Menik Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:06:02 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:27 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:22 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:01:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:03:00 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.020 |  |
| 2026-05-12 15:05:41 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-05-12 15:03:52 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.029 |  |
| 2026-05-12 15:02:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-05-12 15:00:57 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.030 |  |
| 2026-05-12 15:04:04 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.032 |  |
| 2026-05-12 15:03:08 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-05-12 15:01:07 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.053 |  |
| 2026-05-12 15:06:16 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | -0.087 |  |
| 2026-05-12 15:01:48 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | -0.089 |  |
| 2026-05-12 14:10:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)