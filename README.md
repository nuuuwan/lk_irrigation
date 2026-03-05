# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--06_04:30:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **90,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 04:30:40 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:30:38 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:30:37 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:27:15 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.008 |  |
| 2026-03-06 04:15:51 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:15:42 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-06 04:13:51 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:13:29 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:10:59 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-03-06 04:10:42 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:10:24 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 04:08:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-06 04:06:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-03-06 04:06:23 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 04:05:56 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:49 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:41 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:06 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:04:48 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:03:54 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:03:05 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:02:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:02:19 | Norwood (Kelani Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-03-06 04:02:08 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:51 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:50 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.062 |  |
| 2026-03-06 04:01:34 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-03-06 04:01:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:14 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 04:01:14 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:06 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-03-06 04:00:55 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:00:31 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:44:57 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-06 04:10:59 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.492 | 🔺 Rising |
| 2026-03-06 04:06:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-03-05 18:00:12 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-03-06 03:19:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-06 04:01:06 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-03-06 04:15:42 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-06 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-06 04:06:23 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 04:10:24 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-06 04:01:14 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-06 03:02:05 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:03:05 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:51 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:49 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:41 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:01:37 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:01:17 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:30:40 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:00:55 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:02:08 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:01:14 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:06:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:10:42 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-06 03:03:23 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:00:31 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:56 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:02:58 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:05:06 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:08:37 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:03:54 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:04:48 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-05 18:00:43 | Thanthirimale (Malwathu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:13:51 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:15:51 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 04:27:15 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.008 |  |
| 2026-03-06 03:03:17 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-03-06 04:02:19 | Norwood (Kelani Ganga) | 0.30 | 🟢 Normal | -0.041 |  |
| 2026-03-06 04:01:50 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)