# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_10:18:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,141 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 10:18:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:18:15 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-13 10:14:42 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:14:16 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-03-13 10:13:13 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:11:04 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:10:57 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:09:07 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.133 |  |
| 2026-03-13 10:07:28 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.046 |  |
| 2026-03-13 10:07:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-13 10:05:39 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-13 10:05:28 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-13 10:05:22 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:57 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.090 |  |
| 2026-03-13 10:04:56 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:37 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:27 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:24 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.067 |  |
| 2026-03-13 10:04:19 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:04:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:03:47 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-13 10:03:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 10:03:12 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.029 |  |
| 2026-03-13 10:03:07 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-13 10:03:01 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-13 10:02:38 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:02:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.050 |  |
| 2026-03-13 10:02:31 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.079 |  |
| 2026-03-13 10:02:25 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-13 10:02:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:38 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:01:14 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:12 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 10:18:15 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-13 10:05:28 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-03-13 10:03:01 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-13 08:12:43 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 10:03:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-13 10:00:15 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:02:38 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:14:42 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:03:12 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:18:32 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:09 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:13:13 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:27 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:02:38 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:19 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:02:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:11:04 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:10:57 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:05:22 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:14 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:56 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:04:37 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 10:01:38 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:04:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:01:12 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-13 10:14:16 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-03-13 10:02:25 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-03-13 10:07:22 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-03-13 10:03:10 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.029 |  |
| 2026-03-13 10:05:39 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-13 10:03:07 | Hanwella (Kelani Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-13 10:07:28 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.046 |  |
| 2026-03-13 10:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.050 |  |
| 2026-03-13 10:03:47 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-13 10:04:24 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.067 |  |
| 2026-03-13 10:02:31 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.079 |  |
| 2026-03-13 10:04:57 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.090 |  |
| 2026-03-13 10:09:07 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)