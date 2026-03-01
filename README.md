# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_13:41:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 13:41:31 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:19:16 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:15:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:14:13 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:11:59 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-01 13:11:30 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:09:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:08:24 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.052 |  |
| 2026-03-01 13:07:20 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-01 13:07:19 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:07:08 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-03-01 13:06:59 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.009 |  |
| 2026-03-01 13:06:46 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:34 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:33 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-03-01 13:06:09 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:00 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:05:54 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-03-01 13:05:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 13:04:34 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:34 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -2.028 |  |
| 2026-03-01 13:04:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:08 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-01 13:04:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:00 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-01 13:03:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:33 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:17 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -2.028 |  |
| 2026-03-01 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-01 13:03:12 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:02:39 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.247 |  |
| 2026-03-01 13:02:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-01 13:02:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-01 13:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:01:11 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:00:36 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:00:31 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.046 |  |
| 2026-03-01 13:00:25 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 13:05:54 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-03-01 13:02:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-03-01 13:04:08 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-01 13:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-01 13:04:00 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-01 13:04:39 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 13:11:59 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-01 13:03:56 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:34 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:00:25 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:05:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:11:30 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:01:11 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:00 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:34 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:28 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:14:13 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:33 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:04:04 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:01:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:07:19 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:09 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:15:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:19:16 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:41:31 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:03:12 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:09:34 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:46 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:06:59 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.009 |  |
| 2026-03-01 13:02:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-01 13:07:08 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.018 |  |
| 2026-03-01 13:06:33 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-03-01 13:07:20 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-03-01 13:00:31 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.046 |  |
| 2026-03-01 13:08:24 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.052 |  |
| 2026-03-01 13:02:39 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.247 |  |
| 2026-03-01 13:04:28 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -2.028 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)