# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--22_19:35:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **104,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 19:35:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:33:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:33:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:33:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-22 19:26:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-22 19:15:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:09:27 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-22 19:08:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.038 |  |
| 2026-03-22 19:07:37 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:07:37 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:07:23 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-22 19:06:53 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.009 |  |
| 2026-03-22 19:06:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:06:07 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:05:41 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:05:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:05:18 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-22 19:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:04:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.162 |  |
| 2026-03-22 19:03:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 19:03:55 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-22 19:03:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:03:46 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:03:22 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:03:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:03:03 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 19:02:53 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:02:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.058 |  |
| 2026-03-22 19:02:25 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-03-22 19:02:17 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:02:12 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:01:34 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:01:26 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:01:18 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-22 19:01:13 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:00:49 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:00:32 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-03-22 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:00:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-22 19:33:39 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-22 19:07:23 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-22 19:01:18 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-22 19:00:11 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-22 19:03:55 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-22 19:03:03 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-22 19:09:27 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-22 19:03:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-22 19:26:49 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-22 19:01:34 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:15:53 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:00:49 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:00:06 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:05:41 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:01:13 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:03:46 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:05:12 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:06:07 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:06:15 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:07:37 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:03:50 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-22 18:01:37 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:01:26 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:02:17 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:35:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-03-22 19:06:53 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.009 |  |
| 2026-03-22 19:03:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:07:37 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:05:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:02:53 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:03:22 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:02:12 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-22 19:00:32 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-03-22 19:02:25 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-03-22 19:08:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.038 |  |
| 2026-03-22 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.051 |  |
| 2026-03-22 19:02:50 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.058 |  |
| 2026-03-22 19:04:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)