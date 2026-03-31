# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_10:08:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 10:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.058 |  |
| 2026-03-31 10:08:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-03-31 10:08:05 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.037 |  |
| 2026-03-31 10:07:43 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -1.000 |  |
| 2026-03-31 10:07:07 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -1.000 |  |
| 2026-03-31 10:06:33 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.106 |  |
| 2026-03-31 10:05:40 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:24 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:19 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-31 10:05:19 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:02 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-03-31 10:04:43 | Baddegama (Gin Ganga) | 0.68 | 🟢 Normal | -0.033 |  |
| 2026-03-31 10:04:07 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-31 10:04:02 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:04:00 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:04:00 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:03:51 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 10:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-31 10:02:51 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.041 |  |
| 2026-03-31 10:02:29 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:29 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-31 10:02:27 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:23 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:07 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-31 10:02:01 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:46 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-31 10:01:35 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:27 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:23 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 10:01:18 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.119 |  |
| 2026-03-31 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:10 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.062 |  |
| 2026-03-31 10:01:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:00:45 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 09:32:37 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-31 09:21:27 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-31 09:20:42 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 10:03:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-31 10:04:07 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-31 10:02:29 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-31 09:01:34 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 10:01:23 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 10:03:51 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 10:02:01 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:24 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:04:02 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:04:00 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:35 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:01:27 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:40 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:23 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 09:32:37 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-03-31 09:21:27 | Panadugama (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:51 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:29 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:27 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:04:00 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:05:19 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:00:45 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:07 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 10:02:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-31 10:05:02 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.012 |  |
| 2026-03-31 10:05:19 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.019 |  |
| 2026-03-31 10:08:07 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-03-31 10:01:46 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-03-31 10:04:43 | Baddegama (Gin Ganga) | 0.68 | 🟢 Normal | -0.033 |  |
| 2026-03-31 10:08:05 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.037 |  |
| 2026-03-31 10:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.041 |  |
| 2026-03-31 10:08:25 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.058 |  |
| 2026-03-31 10:01:10 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.062 |  |
| 2026-03-31 10:06:33 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.106 |  |
| 2026-03-31 10:01:18 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.119 |  |
| 2026-03-31 10:07:43 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | -1.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)