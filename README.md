# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_09:11:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 09:11:21 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:09:36 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:08:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.187 |  |
| 2026-03-25 09:08:24 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:08:21 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:08:05 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 09:06:56 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:06:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-03-25 09:06:27 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:30 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:05:19 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:10 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:04:19 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:04:06 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 09:03:37 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:03:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-25 09:03:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-25 09:03:14 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:03:01 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:23 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-03-25 09:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:04 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:01:58 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-03-25 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:01:42 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:32 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:27 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-25 09:01:25 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:22 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:00:59 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:00:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 09:03:17 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-25 09:01:27 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-25 09:00:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-25 09:08:05 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 08:07:03 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 09:04:06 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 09:01:32 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:00:59 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:23 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:25 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:31 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:11:21 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:06:56 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:04:19 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:08:21 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:05 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:42 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:03:01 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:19 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:06:27 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:01:22 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:11 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:10 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:08:24 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:09:36 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:03:14 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 09:05:30 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:02:04 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:03:37 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-03-25 09:03:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-03-25 09:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.030 |  |
| 2026-03-25 09:01:58 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-03-25 09:06:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.050 |  |
| 2026-03-25 09:08:42 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)