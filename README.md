# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_17:14:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 17:14:31 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:08:22 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:07:59 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:07:46 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:07:23 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:06:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.018 |  |
| 2026-03-16 17:06:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:06:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-16 17:05:23 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:05:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:05:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-16 17:05:00 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-03-16 17:04:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.138 |  |
| 2026-03-16 17:04:22 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:04:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:04:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.016 |  |
| 2026-03-16 17:03:56 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:03:53 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:28 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:19 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-16 17:03:00 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:02:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-03-16 17:02:42 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:02:40 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-16 17:02:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 17:02:19 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-03-16 17:02:15 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:01:46 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:01:43 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-16 17:01:36 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.042 |  |
| 2026-03-16 17:01:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:29 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:16 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-03-16 16:27:16 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | -0.016 |  |
| 2026-03-16 16:24:59 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 16:23:16 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 17:02:40 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-03-16 17:03:19 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-16 16:09:37 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-16 17:01:43 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-16 17:06:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-16 17:02:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 17:07:46 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:16 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:29 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:04:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:04:22 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:08:22 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:14:31 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:29 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:02:42 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:01:46 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:07:59 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:07:23 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:28 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:00:55 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:05:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:05:23 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-16 16:07:47 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:00 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:53 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:01:02 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:02:15 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 17:03:56 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:02:19 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:06:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-03-16 17:05:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.011 |  |
| 2026-03-16 17:04:03 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.016 |  |
| 2026-03-16 17:06:52 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.018 |  |
| 2026-03-16 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-03-16 17:05:00 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-03-16 17:01:36 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.042 |  |
| 2026-03-16 17:02:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.101 |  |
| 2026-03-16 17:04:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)