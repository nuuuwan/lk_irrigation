# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--01_14:17:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **86,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 14:17:32 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-03-01 14:12:48 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.045 |  |
| 2026-03-01 14:11:02 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:09:55 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.085 |  |
| 2026-03-01 14:08:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:07:55 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:07:31 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:07:27 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:06:32 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:06:23 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-01 14:06:14 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:53 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:04:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 14:04:09 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-01 14:03:53 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:03:49 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-03-01 14:03:42 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:03:35 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-03-01 14:03:16 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:03:05 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.048 |  |
| 2026-03-01 14:03:01 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:02:36 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:19 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:17 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:11 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:08 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:01:52 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:01:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-01 14:01:40 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.213 |  |
| 2026-03-01 14:01:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:00:59 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:00:44 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 13:41:31 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.085 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-01 14:01:46 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-03-01 14:04:09 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-01 14:04:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-01 14:06:23 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-01 14:03:01 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:03:53 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:07:31 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-01 14:01:52 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:06:14 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:15 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:11 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:00:44 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:08 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:03:42 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:07:55 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:11:02 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:08:47 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:20 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:17 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:04:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:05:53 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:06:32 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:02:36 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:01:25 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-01 14:17:32 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-03-01 13:02:38 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:03:16 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:02:19 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:00:59 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-03-01 14:03:49 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-03-01 14:03:35 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.021 |  |
| 2026-03-01 14:12:48 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.045 |  |
| 2026-03-01 14:03:05 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.048 |  |
| 2026-03-01 14:09:55 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.085 |  |
| 2026-03-01 14:01:40 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)