# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_10:24:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 10:24:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:22:22 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.008 |  |
| 2026-03-08 10:15:43 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:14:22 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-08 10:14:04 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:11:00 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:10:47 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.043 |  |
| 2026-03-08 10:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:07:37 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:07:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.062 |  |
| 2026-03-08 10:06:51 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-08 10:06:12 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:05:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:05:19 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.049 |  |
| 2026-03-08 10:05:07 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-08 10:04:50 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:04:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-03-08 10:03:43 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-08 10:03:37 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:28 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:03:28 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:18 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:05 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:02:52 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:02:40 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-08 10:02:28 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.093 |  |
| 2026-03-08 10:02:23 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.124 |  |
| 2026-03-08 10:02:18 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:02:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.052 |  |
| 2026-03-08 10:01:38 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-03-08 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:26 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-08 10:01:14 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:11 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:06 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:00:50 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 10:00:43 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-03-08 10:00:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 10:00:43 | Weraganthota (Mahaweli Ganga) | -1.85 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-03-08 10:02:40 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-03-08 10:01:26 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-08 10:03:43 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-08 10:14:22 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-08 10:06:51 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-08 10:00:50 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 10:02:18 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:02:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:00:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:11:00 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:37 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:05:21 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:14:04 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:02:52 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:11 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:15:43 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:14 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:06:12 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:03:28 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:24:39 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:04:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:07:37 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:04:50 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:01:06 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 10:22:22 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.008 |  |
| 2026-03-08 10:05:07 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-08 10:03:28 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:07:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:03:05 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-03-08 10:03:57 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | -0.029 |  |
| 2026-03-08 10:01:38 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.031 |  |
| 2026-03-08 10:10:47 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.043 |  |
| 2026-03-08 10:05:19 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.049 |  |
| 2026-03-08 10:01:47 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.052 |  |
| 2026-03-08 10:07:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.062 |  |
| 2026-03-08 10:02:28 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.093 |  |
| 2026-03-08 10:02:23 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)