# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_16:11:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,634 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 16:11:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:11:34 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-20 16:09:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-03-20 16:07:22 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-03-20 16:07:05 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:06:39 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-03-20 16:06:36 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.048 |  |
| 2026-03-20 16:06:34 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:05:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:05:40 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:05:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-20 16:05:24 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-03-20 16:04:28 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:13 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:09 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:08 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-20 16:03:50 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:03:38 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-03-20 16:03:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-03-20 16:03:26 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 16:03:03 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:02:57 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:02:53 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-03-20 16:02:51 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:02:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:02:42 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:02:37 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.055 |  |
| 2026-03-20 16:02:13 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-20 16:02:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 16:02:04 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.059 |  |
| 2026-03-20 16:02:00 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-03-20 16:01:39 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.100 |  |
| 2026-03-20 16:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:01:27 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.055 |  |
| 2026-03-20 16:01:21 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:01:03 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 16:00:54 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:00:24 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 16:04:08 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-03-20 16:05:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-20 16:11:34 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-03-20 16:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 16:01:03 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 16:02:09 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 16:02:51 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:01:21 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:28 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:00:24 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:09 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:05:54 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:04:13 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:06:34 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:03:26 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:02:44 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:05:40 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:02:57 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 16:07:05 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:00:54 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:11:35 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:03:03 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:03:50 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:02:42 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-20 16:02:00 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-03-20 16:09:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-03-20 16:07:22 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-03-20 16:02:13 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-20 16:06:39 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-03-20 16:03:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-03-20 16:03:38 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-03-20 16:02:53 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-03-20 16:05:24 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.038 |  |
| 2026-03-20 16:06:36 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.048 |  |
| 2026-03-20 16:02:37 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.055 |  |
| 2026-03-20 16:01:27 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.055 |  |
| 2026-03-20 16:02:04 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.059 |  |
| 2026-03-20 16:01:39 | Weraganthota (Mahaweli Ganga) | -2.68 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)