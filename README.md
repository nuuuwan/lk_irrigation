# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_14:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 14:15:18 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:11:52 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:11:50 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-30 14:10:32 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-03-30 14:10:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:09:02 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:08:19 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.048 |  |
| 2026-03-30 14:07:26 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:06:23 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:06:20 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:05:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-03-30 14:05:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:04:12 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-30 14:04:10 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 14:04:05 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:04:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:58 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.219 |  |
| 2026-03-30 14:03:55 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:46 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:44 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:43 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-30 14:03:40 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-30 14:03:21 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:03:15 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:02:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-30 14:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-30 14:02:38 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:11 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:51 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:40 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:00:59 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:00:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-30 14:00:49 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 13:59:14 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 14:00:53 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-30 14:03:43 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-30 14:02:50 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-30 14:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-30 14:04:10 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-30 14:04:04 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:51 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:32 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:05:47 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:51 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:55 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:00:59 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:15:18 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:46 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:04:05 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:06:20 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:11:52 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-30 13:59:14 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:51 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:11 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:10:12 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:38 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:03:44 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:07:26 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:00:49 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:09:02 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:01:40 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:02:11 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-30 14:11:50 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-03-30 14:10:32 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-03-30 14:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-03-30 14:03:40 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-03-30 14:04:12 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-03-30 14:03:15 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:06:23 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:03:21 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-03-30 14:05:55 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.030 |  |
| 2026-03-30 14:08:19 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.048 |  |
| 2026-03-30 14:03:58 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)