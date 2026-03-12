# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_10:16:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 10:16:32 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-12 10:12:00 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:09:14 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:08:26 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-03-12 10:08:24 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:07:40 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:07:18 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:06:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:06:45 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.129 |  |
| 2026-03-12 10:06:09 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:05:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-12 10:05:40 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.084 |  |
| 2026-03-12 10:04:57 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:04:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:04:47 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 10:04:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-12 10:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-03-12 10:04:16 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 10:04:12 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:03:52 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:03:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:03:44 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.059 |  |
| 2026-03-12 10:03:25 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-12 10:03:14 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-03-12 10:03:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:47 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:44 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:20 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:12 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.324 |  |
| 2026-03-12 10:02:06 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:01:53 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:36 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:10 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-03-12 10:00:48 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:00:36 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.505 | 🔺 Rising |
| 2026-03-12 10:00:34 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 10:00:36 | Weraganthota (Mahaweli Ganga) | -2.46 | 🟢 Normal | 0.505 | 🔺 Rising |
| 2026-03-12 09:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-03-12 10:04:45 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-03-12 10:04:16 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-12 10:16:32 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-12 10:04:47 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 10:04:57 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:02:06 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:03:52 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 10:02:47 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:44 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:53 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:49 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:04:12 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:43 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:12:00 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:09:14 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:07:40 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:08:24 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:06:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:01:36 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:03:45 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:03:05 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:07:18 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:00:48 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:00:34 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:04:50 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:02:20 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:03:25 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-12 10:01:10 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | -0.010 |  |
| 2026-03-12 10:03:14 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-03-12 10:05:47 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.030 |  |
| 2026-03-12 10:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-03-12 10:08:26 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.055 |  |
| 2026-03-12 10:03:44 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.059 |  |
| 2026-03-12 10:05:40 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.084 |  |
| 2026-03-12 10:06:45 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.129 |  |
| 2026-03-12 10:02:12 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)