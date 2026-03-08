# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_12:22:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,525 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 12:22:29 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-03-08 12:11:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.018 |  |
| 2026-03-08 12:08:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:08:23 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-03-08 12:08:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:07:06 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-08 12:06:04 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.019 |  |
| 2026-03-08 12:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-03-08 12:05:13 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:07 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:02 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-08 12:04:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:44 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:33 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:31 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-08 12:04:13 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-08 12:04:10 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-08 12:04:07 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-08 12:03:40 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:03:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-03-08 12:03:15 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.035 |  |
| 2026-03-08 12:03:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:03:10 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 12:02:49 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:40 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:39 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:28 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:08 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 12:01:59 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-08 12:01:33 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:01:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-08 12:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 12:00:47 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.072 |  |
| 2026-03-08 12:00:41 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:00:40 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-08 12:00:27 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:00:23 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 12:04:10 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-08 12:03:10 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-08 12:04:31 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-08 12:01:59 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-08 12:04:13 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-08 12:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-08 12:00:40 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-08 12:00:23 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 12:02:08 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 12:02:49 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:03:11 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:08:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:33 | Giriulla (Maha Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:13 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:04:44 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:08:40 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:40 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:00:27 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:03:40 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:01:33 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:39 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:02:28 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:05:07 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:00:41 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-08 11:07:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-08 12:22:29 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.008 |  |
| 2026-03-08 12:07:06 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-03-08 12:05:02 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-08 12:04:07 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-08 12:01:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.011 |  |
| 2026-03-08 12:11:17 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.018 |  |
| 2026-03-08 12:08:23 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-03-08 12:06:04 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.019 |  |
| 2026-03-08 12:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-03-08 12:03:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-03-08 12:03:15 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | -0.035 |  |
| 2026-03-08 12:00:47 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)