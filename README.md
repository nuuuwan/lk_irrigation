# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_15:09:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,116 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 15:09:40 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:08:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-15 15:07:27 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-15 15:06:47 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:06:28 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-15 15:06:25 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:05:57 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 15:05:20 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:04:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-03-15 15:04:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-15 15:04:27 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.154 |  |
| 2026-03-15 15:04:14 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-03-15 15:04:11 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:04:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 15:03:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-15 15:03:52 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:03:28 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.114 |  |
| 2026-03-15 15:03:07 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:03:06 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:03:05 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-03-15 15:02:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-03-15 15:02:28 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-03-15 15:02:19 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-15 15:01:55 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 15:01:52 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:01:43 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-15 15:01:24 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-03-15 15:01:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:01:19 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:08 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.037 |  |
| 2026-03-15 15:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:00:49 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-03-15 15:00:33 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:00:28 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 15:00:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:47:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:28:38 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-15 14:27:06 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 15:04:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-15 15:01:43 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-15 15:03:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-15 15:08:20 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-15 15:06:28 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-15 15:00:28 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-15 15:04:07 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 15:05:57 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-15 15:01:55 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-15 15:00:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:05:20 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:47:40 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:02:28 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:24 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 14:05:34 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:04:11 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:07 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:06:47 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:06:25 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:03:06 | Moraketiya (Walawe Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:00:33 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:03:52 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:09:40 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:19 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 15:01:52 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:03:07 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:01:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-03-15 15:01:24 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.011 |  |
| 2026-03-15 15:04:14 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-03-15 15:07:27 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.019 |  |
| 2026-03-15 15:03:05 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-03-15 15:02:19 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-15 15:02:34 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-03-15 15:04:39 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2026-03-15 15:02:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-03-15 15:01:08 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.037 |  |
| 2026-03-15 15:00:49 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | -0.071 |  |
| 2026-03-15 15:03:28 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.114 |  |
| 2026-03-15 15:04:27 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.154 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)