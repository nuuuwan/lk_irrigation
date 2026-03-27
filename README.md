# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_22:10:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 22:10:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-27 22:07:58 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-27 22:07:19 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:07:16 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:06:52 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-03-27 22:06:08 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:49 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:21 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:12 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 22:05:11 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:03:43 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.032 |  |
| 2026-03-27 22:03:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:56 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:45 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:36 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:34 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:34 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-03-27 22:02:32 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:30 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-27 22:02:23 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 22:02:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-27 22:02:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:01:53 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:01:36 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:01:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-27 22:00:57 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 22:00:47 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:00:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 22:06:52 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-03-27 22:00:57 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-27 22:02:23 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-27 22:05:12 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 22:02:23 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 22:10:47 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-27 22:02:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:49 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:30 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:00:17 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:00:47 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:01:51 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:06:08 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:07:16 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:07:19 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:45 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:18 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:34 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:11 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:03:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:36 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:25 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-27 21:04:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:32 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:05:21 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-27 21:05:20 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:01:36 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:00:28 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:02:56 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:01:53 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-27 22:07:58 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-27 22:02:22 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-27 22:02:34 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-03-27 22:01:22 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-27 22:03:43 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.032 |  |
| 2026-03-27 21:02:15 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.052 |  |
| 2026-03-27 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)