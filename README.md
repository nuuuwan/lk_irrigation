# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_23:09:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,522 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 23:09:57 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.023 |  |
| 2026-03-14 23:09:55 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:09:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:07:53 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -2.500 |  |
| 2026-03-14 23:07:36 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:06:50 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-14 23:06:41 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -2.500 |  |
| 2026-03-14 23:06:37 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-03-14 23:06:16 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 23:05:56 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:05:55 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:05:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:04:50 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-03-14 23:04:23 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:04:21 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:03:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:03:51 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:03:49 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:03:17 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-03-14 23:02:58 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:54 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-14 23:02:54 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-03-14 23:02:31 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-14 23:02:21 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:19 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 23:02:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 23:02:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-14 23:01:47 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-03-14 23:01:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 23:01:20 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-14 23:01:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:01:12 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:44:46 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:43:20 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 23:02:54 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-03-14 23:01:20 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-03-14 23:02:54 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-14 23:02:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-14 22:01:17 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-14 23:06:16 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-14 22:01:16 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 23:01:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 23:02:19 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 23:02:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-03-14 23:02:20 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 22:02:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:01:12 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:01:12 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:03:54 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:21 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:02:31 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:04:23 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:05:56 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-14 23:09:29 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:05:55 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:07:36 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-03-14 23:04:21 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:05:16 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:09:55 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:03:49 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:03:51 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-03-14 23:06:37 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-03-14 23:06:50 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.019 |  |
| 2026-03-14 23:03:17 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2026-03-14 23:09:57 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.023 |  |
| 2026-03-14 22:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-03-14 23:02:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-03-14 23:01:47 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-03-14 23:04:50 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.032 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-14 23:07:53 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -2.500 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)